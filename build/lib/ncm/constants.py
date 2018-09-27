# -*- coding: utf-8 -*-

from fake_useragent import UserAgent
# Encrypt key
modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
nonce = '0CoJUm6Qyw8W8jud'
pub_key = '010001'

ua = UserAgent()
uu = ua.ie
headers = {
     'User-Agent': uu,
     'Cookie': '_iuqxldmzr_=32; _ntes_nnid=60003a034a46215d8b87083095855b14,1512963119212; _ntes_nuid=60003a034a46215d8b87083095855b14; __utma=94650624.895259998.1512963120.1512963120.1512963120.2; _ngd_tid=93P0wkNfYlo2SjTHSRlLIbA4ItEcA1Aa; vjuids=-254930f27.1605299a1a8.0.b2d3add6c1ef1; mail_psc_fingerprint=94f00f4191536786591a1d4493ec6301; NTES_CMT_USER_INFO=44638978%7C%E5%AF%82%E5%AF%9E%E5%A5%94%E8%B7%9124%7Chttp%3A%2F%2Ftp3.sinaimg.cn%2F2700694134%2F180%2F5652748345%2F1%7Cfalse%7CeWp5MTAxNjIxMTVAMTYzLmNvbQ%3D%3D; nts_mail_user=yjy10162115@163.com:-1:1; usertrack=ezq0plpn99kdmolfJu5zAg==; __utmz=187553192.1524910080.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=187553192.440712774.1524910080.1524910080.1526029821.2; __f_=1528771235067; P_INFO=yjy10162115@163.com|1529400897|0|urs|00&10|bej&1529400852&mail163#bej&null#10#0#0|136469&0|urs&mail163|yjy10162115@163.com; vjlast=1513214288.1530690381.11; vinfo_n_f_l_n3=cd9302ab3767a9f8.1.9.1515566972672.1530690446669.1532311994938; WM_TID=mEyz9Z8S00fwdm4W3opJt4KRqgFnPSO0; __remember_me=true; MUSIC_U=b933008465161a75a92a944594509228d4d2a3fed043be591ace733e17a21f8e7c8d0964386d1f4979bd24827be7363576b1ee8f31d0a3b8; __csrf=f233404e93ebda3b0f67c59f320a7ed4; playerid=12616091; WM_NI=J2Fb%2FzYsiZ5DjCAsyrWV2ByZYv6BiBT8oALeDdZtfMeInmPbQOLxBO%2FjSAjROjYvUs7RsFojoSvzAuWnAqeavxkujRuRwP%2BTmIlTUkFFezKMqN%2FxAPwyak8rKjVVmYFDM1U%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed2c525b4f1aad0f368a9aa8782f64fbae8fdd2c1628bbcb689cf3d81b79ad0f12af0fea7c3b92a8aee8a83ae729bada7bbb850aa9d8f94fc7a958afea3fc529baafaa3ec4a98e8a1a2cf6f88bc9695e547a797a28ed36a93918499c145edb69da2e95a8db69797d879f58ebda7ee62ad8dba9bc47f95b28f92e86bb6a8a596e95ab78eb9b1aa60af97a4b5d861869aab9bca47b392e199c45cb5a7af8cbb7a89b69ab7f053869c83d2d837e2a3; JSESSIONID-WYYY=MKj88I%5CJjoPUPlR0yV4G%2FNy3z%2FvaQhuBwvwy7waJnVWwS1UUwMJJYrpk5By3a%2Bq4%2FF06QUjJb7RT1eaf%2Faww7qJmcN7t1%2Fa2utK62Y1M3v8Kbzyv9WT4W%5CM%2BVNPPtoUhROTBuzSnqowOaqRChJmi914eqqyizGFodBre8isKR0mFNsWM%3A1533618388909',
     'Accept': '*/*',
     'Host': 'music.163.com',
     'Referer': 'http://music.163.com',
     'Connection': 'close'
}

#proxies={"http":"http://127.0.0.1:8118"}
song_download_url = 'http://music.163.com/weapi/song/enhance/player/url?csrf_token='


def get_song_url(song_id):
    return 'http://music.163.com/api/song/detail/?ids=[{}]'.format(song_id)


def get_album_url(album_id):
    return 'http://music.163.com/api/album/{}/'.format(album_id)


def get_artist_url(artist_id):
    return 'http://music.163.com/api/artist/{}'.format(artist_id)


def get_playlist_url(playlist_id):
    return 'http://music.163.com/api/playlist/detail?id={}'.format(playlist_id)

def get_lrc_url(lrc_id):
    return 'http://music.163.com/api/song/lyric?' + 'id=' + format(lrc_id) + '&lv=1&kv=1&tv=-1'

