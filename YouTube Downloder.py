from pytube import YouTube
url = input('Enter Url - ') 
print("Download Start Please Wait....")
yt = YouTube(str(url))
yt.streams.first().download()
print('Download Complete  ---> ',  yt.title)
