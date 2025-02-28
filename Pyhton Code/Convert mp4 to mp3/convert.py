
from moviepy.editor import *

def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

VIDEO_FILE_PATH = "/home/asif/Project/python-code/convert-mp4-to-mp3/Yeh Jism Hai Toh Kya [Slowed+Reverb] Ali Azmat.mp4"
AUDIO_FILE_PATH = "/home/asif/Project/python-code/convert-mp4-to-mp3/Yeh Jism Hai Toh Kya.mp3"

MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
