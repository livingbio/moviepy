# coding: utf-8
import cProfile
import os
import pstats
from moviepy.editor import *


def example_video1():

    nice_yo = TextClip(txt="Nice Yo", bg_color='white', fontsize=100)
    nice_yo = nice_yo.set_position(lambda t: (1 + t*90, 'center'))

    color = ColorClip(col=(33, 0, 0), size=(1280, 720))

    return CompositeVideoClip([color, nice_yo]).set_duration(5)


def main():
    video = example_video1()
    video.write_videofile(fps=30, filename="a.mp4")


if __name__ == "__main__":
    cProfile.run('main()', './profiling')
    p = pstats.Stats('./profiling')
    p.sort_stats('time').print_stats(20)

    os.system("open a.mp4")
