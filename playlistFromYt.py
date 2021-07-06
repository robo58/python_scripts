from __future__ import unicode_literals
import youtube_dl
import sys
import argparse


def downloadPlaylistFromYt(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
        'prefer_ffmpeg': True,
        'keepvideo': False
    }
    
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.cache.remove()
            ydl.download([url])
        except youtube_dl.DownloadError as error:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A program that downloads mp3s from yt playlist')
    parser.add_argument("-url", help="Prints the supplied argument.")
    args = parser.parse_args()
    print(args.url)
    downloadPlaylistFromYt(args.url)
