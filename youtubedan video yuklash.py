from pytube import YouTube
YouTube ('https://www.youtube.com/watch?v=MRqGDFJ-Djs') .streams.first() .download()
yt = YouTube ('https://youtu.be/MRqGDFJ-Djs?si=R08TD7YRHFWtDmtl')
yt.streams
filter (progressive=True, file_extension='mp4')
order_by('resolution')
desc()
first()
download()
