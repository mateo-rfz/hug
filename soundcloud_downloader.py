import yt_dlp
import url_finder

class soundcloud_download:
    def __init__(self) :
        pass
    def downloader(url) :
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
            content_url = url_finder.Finder()
            download_path = ()
            download_soundcloud_content(content_url, download_path)
        return 1
