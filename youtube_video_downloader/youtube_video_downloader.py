from pytube import YouTube  # pip install pytube
import sys

def youtube_video(link,s_file):
    video = YouTube(link)
    video.streams.get_highest_resolution().download(s_file)


link = sys.argv[1]
s_file = "./"  # Here mension the path where to save video

youtube_video(link,s_file)
