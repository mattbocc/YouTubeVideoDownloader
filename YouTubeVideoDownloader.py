from pytube import YouTube
from sys import argv

#If you dont want to use command line use the line below instead
#videoLink = "" 

videoLink = argv[1]
details = YouTube(videoLink)


#for downloading MP4
downloadVideo = details.streams.get_highest_resolution()
downloadVideo.download('/Users/matth/Videos/ScriptDownloads/Videos')

#for downloading MP3
downloadAudio = details.streams.get_audio_only()
downloadAudio.download('/Users/matth/Videos/ScriptDownloads/Audios')