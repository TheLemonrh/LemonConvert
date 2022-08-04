# Install packages

pip install pytube

# Script

from pytube import YouTube

yt = YouTube("LINK")
yt = yt.get('FORMAT', 'QUALITÄT')
yt.download('PATH')
