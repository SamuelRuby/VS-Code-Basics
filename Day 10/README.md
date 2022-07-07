VIDEO TO THUMBNAILS TO GIF WITH MOVIEPY

**CHALLENGE:
- Creating thumbnails from any image useful for automating your thumbnails from any image

- Processing Videos, Audio using Python in a package called Moviepy. 

- Create thumbnails from videos, mix audio, composite video, create intros, and more. All with Moviepy, ffmpeg, and ImageMagick


MOVIEPy is supercharged with 2 other packages: imagemagick and ffmpeg

**We're going to be using Moviepy to do the following:

- Create thumbnails from videos

- Image Collection to Video

- Generate a GIF animation

- Combine Audio Samples in a Video

- Overlay Text, Image, or Video

**Requirements:

- Python 3.6+

- Pipenv (or another virtual environment)

- moviepy==1.0.2 (or greater)

- ffmpeg & imagemagick installed 



**Installations:

**FFmpeg: https://www.ffmpeg.org/download.html

Moviepy and ffmpeg work well together. ffmpeg can do most/all of this on it's own but lacks Python bindings. Thus, moviepy is used!

**macOS:

Use homebrew: https://brew.sh/

cmd: brew update && brew install ffmpeg


**Windows/Linux: 

Use the executable: https://www.ffmpeg.org/download.html



***ImageMagick. https://imagemagick.org/script/download.php

To add text, you must install ImageMagic.

**macOS:

Use homebrew: https://brew.sh/

cmd: brew update && brew install imagemagick

**Linux:

Download here: https://imagemagick.org/script/download.php

**Windows:

Use the binary or exe: https://imagemagick.org/script/download.php#windows


***Base Project
1. Start project
We're using pipenv and Moviepy:https://zulko.github.io/moviepy/

cd path/to/your/project/folder/

pipenv install --python 3.8 moviepy
pipenv shell
mkdir data
mkdir data/samples
mkdir data/samples/inputs
mkdir data/samples/outputs

2. Create conf.py
import os
ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)
DATA_DIR = os.path.join(BASE_DIR, "data")
SAMPLE_DIR = os.path.join(DATA_DIR, "samples")
SAMPLE_INPUTS = os.path.join(SAMPLE_DIR, "inputs")
SAMPLE_OUTPUTS = os.path.join(SAMPLE_DIR, 'outputs')


3. 

-Make/download a sample audio of your choice
-Make/download a sample video of your choice


Once downloaded, move these files to your project's data/samples/inputs directory.