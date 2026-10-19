import yt_dlp

import os

link = input('Вставте сылку:')

ydl_opts = {
    'outtmpl':'temp.mp4',
    'format':'mp4'
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print('Все готово')

hz = input('Удалять ролик:')

if hz == 'Да':
    if os.path.exists('temp.mp4'):
        os.remove('temp.mp4')
        print('Видео удаленно)')
else:
    print('Хорошо ')