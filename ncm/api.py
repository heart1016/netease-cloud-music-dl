# -*- coding: utf-8 -*-

import requests
import time
import http
import urllib3

from ncm.encrypt import encrypted_request
from ncm.constants import headers
from ncm.constants import song_download_url
from ncm.constants import get_song_url
from ncm.constants import get_album_url
from ncm.constants import get_artist_url
from ncm.constants import get_playlist_url
from ncm.constants import get_lrc_url



class CloudApi(object):

	def __init__(self, timeout=30):
		try:
			super().__init__()
			self.session = requests.session()
			self.session.headers.update(headers)
			self.timeout = timeout
		except:
			print('__init__ sleep 10 seconds')
			time.sleep(10)
			super().__init__()
			self.session = requests.session()
			self.session.headers.update(headers)
			self.timeout = timeout

	def get_request(self, url):
		try:
			response = self.session.get(url, timeout=self.timeout)
			result = response.json()
			if result['code'] != 200:
				print('Return {} when try to get {}'.format(result, url))
			else:
				return result
		except:
			print('get_request sleep 10 seconds')
			time.sleep(10)
			response = self.session.get(url, timeout=self.timeout)
			result = response.json()
			if result['code'] != 200:
				print('Return {} when try to get {}'.format(result, url))
			else:
				return result

	def post_request(self, url, params):
		try:
			data = encrypted_request(params)
			response = self.session.post(url, data=data, timeout=self.timeout)
			result = response.json()
			if result['code'] != 200:
				print('Return {} when try to post {} => {}'.format(result, params, url))
			else:
				return result
		except:
			print('post_request sleep 10 seconds')
			time.sleep(10)
			data = encrypted_request(params)
			response = self.session.post(url, data=data, timeout=self.timeout)
			result = response.json()
			if result['code'] != 200:
				print('Return {} when try to post {} => {}'.format(result, params, url))
			else:
				return result

	def get_song(self, song_id):
		try:
			url = get_song_url(song_id)
			result = self.get_request(url)
			return result['songs'][0]
		except:
			print('get_song sleep 10 seconds')
			time.sleep(10)
			url = get_song_url(song_id)
			result = self.get_request(url)
			return result['songs'][0]

	def get_album_songs(self, album_id):
		try:
			url = get_album_url(album_id)
			result = self.get_request(url)
			return result['album']['songs']
		except:
			print('get_album_songs sleep 10 seconds')
			time.sleep(10)
			url = get_album_url(album_id)
			result = self.get_request(url)
			return result['album']['songs']

	def get_song_url(self, song_id, bit_rate=320000):
		try:
			url = song_download_url
			csrf = ''
			params = {'ids': [song_id], 'br': bit_rate, 'csrf_token': csrf}
			result = self.post_request(url, params)
			song_url = result['data'][0]['url']
			return song_url
		except:
			print('get_song_url sleep 10 seconds')
			time.sleep(10)
			url = song_download_url
			csrf = ''
			params = {'ids': [song_id], 'br': bit_rate, 'csrf_token': csrf}
			result = self.post_request(url, params)
			song_url = result['data'][0]['url']
			return song_url

	def get_hot_songs(self, artist_id):
		try:
			url = get_artist_url(artist_id)
			result = self.get_request(url)
			return result['hotSongs']
		except:
			print('get_hot_songs sleep 10 seconds')
			time.sleep(10)
			url = get_artist_url(artist_id)
			result = self.get_request(url)
			return result['hotSongs']

	def get_playlist_songs(self, playlist_id):
		try:
			url = get_playlist_url(playlist_id)
			result = self.get_request(url)
			return result['result']['tracks'], result['result']['name']
		except:
			print('get_playlist_songs sleep 10 seconds')
			time.sleep(10)
			url = get_playlist_url(playlist_id)
			result = self.get_request(url)
			return result['result']['tracks'], result['result']['name']

	def get_lrc(self, lrc_id):
		try:
			url = get_lrc_url(lrc_id)
			lyric = self.get_request(url)
			if 'nolyric' in lyric or 'uncollected' in lyric or lyric['lrc']['lyric'] is None:
				return "no lrc"
			else:
				return lyric['lrc']['lyric']
		except:
			print('get_lrc_sleep sleep 10 seconds')
			time.sleep(10)
			url = get_lrc_url(lrc_id)
			lyric = self.get_request(url)
			if 'nolyric' in lyric or 'uncollected' in lyric or lyric['lrc']['lyric'] is None:
				return "no lrc"
			else:
				return lyric['lrc']['lyric']


	def get_lrc_tran(self, lrc_id):
		try:
			url = get_lrc_url(lrc_id)
			lyric = self.get_request(url)
			if 'nolyric' in lyric or 'uncollected' in lyric or lyric['tlyric']['lyric'] is None:
				return "no tran lrc"
			else:
				return lyric['tlyric']['lyric']
		except:
			print('get_lrc_sleep sleep 10 seconds')
			time.sleep(10)
			url = get_lrc_url(lrc_id)
			lyric = self.get_request(url)
			if 'nolyric' in lyric or 'uncollected' in lyric or lyric['tlyric']['lyric'] is None:
				return "no tran lrc"
			else:
				return lyric['tlyric']['lyric']
'''
def get_lrc_zh(self, lrc_id):
	url = get_lrc_url(lrc_id)
	try:
		tlyric = self.get_request(url)
	except (http.client.RemoteDisconnected, urllib3.exceptions.ProtocolError, requests.exceptions.ConnectionError):
		print('sleep 10 second')
		time.sleep(10)
		if 'tlyric' not in tlyric or tlyric['tlyric']['lyric'] is None:
			return "no lrc"
		else:
			return tlyric['tlyric']['lyric']
'''
