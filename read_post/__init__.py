import shutil
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dist_dir = os.path.join(BASE_DIR, 'templates', 'dist')
static_dir = os.path.join(BASE_DIR, 'templates', 'dist', 'static')

if os.path.isdir(os.path.join(BASE_DIR, 'templates')) and \
        os.path.isdir(os.path.join(dist_dir)) and \
        os.path.isdir(os.path.join(static_dir)) and \
        os.path.isfile(os.path.join(static_dir, 'index.html')):
    shutil.copy(os.path.join(static_dir, 'index.html'), os.path.join(dist_dir, 'index.html'))
else:
    print("index 파일경로가 잘못되었습니다.")
