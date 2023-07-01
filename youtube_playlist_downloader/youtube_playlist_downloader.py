from pytube import Playlist,YouTube
import sys
import os

link = sys.argv[1]
p = Playlist(link)
title1 = p.title.encode('utf-8').decode('utf-8')
os.makedirs(title1)
e_file = f'./{title1}/e_file.txt'

for url in p.video_urls:
    try:
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download(f'./{title1}/')
    except:
        with open(e_file,'w') as ef:
            ef.write(url)