import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join (BASE_DIR, 'images')

#if not os.path.exists(files_dir):
 #   print ('This is not a valid path')

#this makes all directories reagrdless of whether or not they exist
os.makedirs(files_dir, exist_ok = True)

my_images = range (0, 12)

for i in my_images: 
    fname = f'{i}.jpg'
    file_path = os.path.join(files_dir, fname)
    if os.path.exists (file_path):
        #to skip the images, not overwrite them
        print(f'skipped {fname}')   
        #to not skip the images
        # print(f'skipped fname')    
        continue
    with open(file_path, 'w') as f:
        f.write ('Hello world')
