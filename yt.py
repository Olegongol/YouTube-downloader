import yt_dlp
#from pydub import AudioSegment

goi = input('Link here: ').strip()  
pupka = input('choice format, 1 for video 2 for audio ')

audio_opts = {
    "format" : "bestaudio/best",
    "outtmpl" : "E:/gg/%(title)s.%(ext)s",
    #"postprocessors": [{
    #    "key": "FFmpegExtractAudio",
    #    "preferredcodec": "mp3",
    #    "preferredquality": "192",
    #}]
}

ydl_opts = {
    "format" : "best",
    "outtmpl" : "E:/gg/%(title)s.%(ext)s",
    #"postprocessors": [{
    #    "key": "FFmpegExtractAudio",
    #    "preferredcodec": "mp4",
    #    "preferredquality": "192",
    #}]
}

if pupka == '1' :
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(goi)

elif pupka == "2":
    with yt_dlp.YoutubeDL(audio_opts) as ydl:
        ydl.download(goi)

else :
    print('Долбаёб, по людски написано 1 или 2')