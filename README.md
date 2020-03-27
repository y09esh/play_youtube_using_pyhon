# play_youtube_using_pyhon

vlc is the original package from pylib website. if you already have installed using "pip install python-vlc", then 

change line 163 from "dll = ctypes.CDLL(libname)" to "dll = ctypes.CDLL('./'+libname)"
