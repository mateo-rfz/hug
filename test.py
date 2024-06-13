import youtube_dl

def download_soundcloud_track(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# لینک آهنگ SoundCloud را در اینجا وارد کنید
track_url = 'https://soundcloud.com/aslistream/romania?in=javad-ahmadi-507941826/sets/mehrad-hidden-shayea-album'
download_soundcloud_track(track_url)
