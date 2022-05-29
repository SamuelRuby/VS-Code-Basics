from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image
from moviepy.video.fx.all import crop

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')

GIF_DIR = os.path.join(SAMPLE_OUTPUTS, 'gif')
os.makedirs(GIF_DIR, exist_ok=True)

output_path1 = os.path.join(SAMPLE_OUTPUTS, 'sample1.gif')
output_path2 = os.path.join(SAMPLE_OUTPUTS, 'sample2.gif')

#creating a gif clip
clip =VideoFileClip(source_path)
fps = clip.reader.fps
subclip = clip.subclip(10,20) #the time duration that you want
subclip = subclip.resize(width= 500) #resize without breaking the scale of the actual clip
subclip.write_gif(output_path1, fps = fps, program = 'ffmpeg') #dfault is imageio

#creating a cropped clip
w,h  = clip.size
subclip2 = clip.subclip(10,20) 
squared_cropped_clip= crop(subclip2, width = 320, height = 320, x_center=w/2, y_center= h/2)
clip =VideoFileClip(source_path)

squared_cropped_clip.write_gif(output_path2, fps=fps, program = 'ffmpeg')
