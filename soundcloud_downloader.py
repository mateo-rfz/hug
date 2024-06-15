import yt_dlp
import url_finder

"""
creat class for this file and use on main file 
"""
def download_soundcloud_content(content_url, download_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': download_path + '/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([content_url])

if __name__ == "__main__":
    content_url = input("Enter the SoundCloud URL (single track or playlist): ")
    download_path = input("Enter the path where you want to save the content: ")
    download_soundcloud_content(content_url, download_path)
