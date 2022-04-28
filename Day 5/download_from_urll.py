import os
import requests
import shutil
from download_util import download_file

THIS_FILE_PATH = os.path.abspath (__file__)
BASE_DIR= os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join (BASE_DIR, 'downloads')
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

downloaded_img_path = os.path.join(DOWNLOADS_DIR, '1.jpg')
url = 'https://t3.ftcdn.net/jpg/01/22/93/96/360_F_122939679_d0EwmFrZpa2u6hyWvwU8TiANPvqUhTCA.jpg'

# a smallish item
r = requests.get (url, stream = True)
r.raise_for_status() #if it's not a 200 status, it will run an error
with open(downloaded_img_path, 'wb') as f:
    f.write(r.content)
    #f.write(r.raw) - looks for a byte like object

#dl_filename = os.path.basename (url)
#new_dl_path = os.path.join(DOWNLOADS_DIR, dl_filename)
#with requests.get(url, stream =True) as r:
 #   with open (new_dl_path, 'wb') as file_obj: 
  #      shutil.copyfileobj(r.raw, file_obj)

download_file(url, DOWNLOADS_DIR)