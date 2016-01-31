import pafy
url = 'https://www.youtube.com/watch?v=JOX-krmWf8Q'
video = pafy.new(url)
for s in video.streams:
	print s.url
