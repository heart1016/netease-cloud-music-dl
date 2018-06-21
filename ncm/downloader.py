# -*- coding: utf-8 -*-

import os
import re
import requests

from ncm import config
from ncm.api import CloudApi
from ncm.file_util import add_metadata_to_song
from ncm.file_util import resize_img


def download_song_by_id(song_id, download_folder, sub_folder=True):
    # get song info
    api = CloudApi()
    song = api.get_song(song_id)
    download_song_by_song(song, download_folder, sub_folder)


def download_song_by_song(song, download_folder, sub_folder=True):
    # get song info
    api = CloudApi()
    song_id = song['id']
    song_name = format_string(song['name'])
    if song_name is None:
        print('no song_name')
    artist_name = format_string(song['artists'][0]['name'])
    if artist_name is None:
        print('no artist_name')
    album_name = format_string(song['album']['name'])
    if album_name is None:
        print('no album_name')
        album_name = ""

    # update song file name by config
    song_file_name = '{}.mp3'.format(song_name)
    switcher_song = {
        1: song_file_name,
        2: '{} - {}.mp3'.format(artist_name, song_name),
        3: '{} - {}.mp3'.format(song_name, artist_name)
    }
    song_file_name = switcher_song.get(config.SONG_NAME_TYPE, song_file_name)

    lrc_file_name = '{}.lrc'.format(song_name)
    switcher_song = {
        1: lrc_file_name,
        2: '{} - {}.lrc'.format(artist_name, song_name),
        3: '{} - {}.lrc'.format(song_name, artist_name)
    }
    lrc_file_name = switcher_song.get(config.SONG_NAME_TYPE, lrc_file_name)
    # update song folder name by config, if support sub folder
    if sub_folder:
        switcher_folder = {
            1: download_folder,
            2: os.path.join(download_folder, artist_name),
            3: os.path.join(download_folder, artist_name, album_name),
        }
        song_download_folder = switcher_folder.get(config.SONG_FOLDER_TYPE, download_folder)
    else:
        song_download_folder = download_folder

    # download song
    song_url = api.get_song_url(song_id)
    if song_url is None:
        print('Song <<{}>> is not available due to copyright issue!'.format(song_name))
        return
    is_already_download = download_file(song_url, song_file_name, song_download_folder)
    if is_already_download:
        print('Mp3 file already download:', song_file_name)
        return


    #download_lrc
    lrc = api.get_lrc(song_id)
    if 'no lrc' in lrc:
        print(lrc_file_name, 'is no')
    else:
        lrc = lrc.encode('utf-8')
        if not os.path.exists(song_download_folder):
            os.makedirs(song_download_folder)
        file_path = os.path.join(song_download_folder, lrc_file_name)
        with open(file_path, 'ab+') as f:
            f.write(lrc)

    #download_tran lrc
    lrc = api.get_lrc_tran(song_id)
    if 'no tran lrc' in lrc:
        print(lrc_file_name, 'tran is no')
    else:
        lrc = lrc.encode('utf-8')
        if not os.path.exists(song_download_folder):
            os.makedirs(song_download_folder)
        file_path = os.path.join(song_download_folder, lrc_file_name)
        with open(file_path, 'ab+') as f:
            f.write(lrc)

    # download cover
    cover_url = song['album']['blurPicUrl']
    if cover_url is None:
        print('no cover_url')
    else:
        cover_file_name = 'cover_{}.jpg'.format(song_id)
        download_file(cover_url, cover_file_name, song_download_folder)

        # resize cover
        resize_img(os.path.join(song_download_folder, cover_file_name))

        # add metadata for song
        song_file_path = os.path.join(song_download_folder, song_file_name)
        cover_file_path = os.path.join(song_download_folder, cover_file_name)
        add_metadata_to_song(song_file_path, cover_file_path, song)

        # delete cover file
        os.remove(cover_file_path)

"""
    # downloa lrc
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + format(song_id) + '&lv=1&kv=1&tv=-1'
    lyric = requests.get(lrc_url)
    json_obj = lyric.text
    j = json.loads(json_obj)
    lrc = j['lrc']['lyric']
    #pat = re.compile(r'\[.*\]')
    #lrc = re.sub(pat, "", lrc)
    #lrc = lrc.strip()
    print(lrc)
"""
'''
    tlrc = api.get_lrc_zh(song_id)
    if 'no lrc' in tlrc:
        print(lrc_file_name, 'is no zh')
    else:
        tlrc = tlrc.encode('utf-8')
        if not os.path.exists(song_download_folder):
            os.makedirs(song_download_folder)
        file_path = os.path.join(song_download_folder, lrc_file_name)
        with open(file_path, 'wb') as f:
            f.write(tlrc)

'''
def download_file(file_url, file_name, folder):

    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, file_name)

    response = requests.get(file_url, stream=True)
    length = int(response.headers.get('Content-Length'))
    if length is None:
        print('continue length ...')
        response = requests.get(file_url, stream=True)
        length = int(response.headers.get('Content-Length'))

    # TODO need to improve whether the file exists
    if os.path.exists(file_path) and os.path.getsize(file_path) > length:
        return True

    progress = ProgressBar(file_name, length)

    with open(file_path, 'wb') as file:
        for buffer in response.iter_content(chunk_size=1024):
            if buffer:
                file.write(buffer)
                progress.refresh(len(buffer))
    return False



class ProgressBar(object):

    def __init__(self, file_name, total):
        super().__init__()
        self.file_name = file_name
        self.count = 0
        self.prev_count = 0
        self.total = total
        self.end_str = '\r'

    def __get_info(self):
        return 'Progress: {:6.2f}%, {:8.2f}MB, [{:.100}]'\
            .format(self.count/self.total*100, self.total/1024/1024, self.file_name)

    def refresh(self, count):
        self.count += count
        # Update progress if down size > 10k
        if (self.count - self.prev_count) > 10240:
            self.prev_count = self.count
            print(self.__get_info(), end=self.end_str)
        # Finish downloading
        if self.count >= self.total:
            self.end_str = '\n'
            print(self.__get_info(), end=self.end_str)


def format_string(string):
    """
    Replace illegal character with ' '
    """
    if string is None:
        return string
    else:
        return re.sub(r'[\\/:*?"<>|]', ' ', string)
