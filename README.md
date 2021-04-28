# play_youtube__videos_using_python

vlc is the original package from pylib website. if you already have installed using "pip install python-vlc", then 

change line 163 from "dll = ctypes.CDLL(libname)" to "dll = ctypes.CDLL('./'+libname)"

dont forget to change url of video if it changes for live ones
