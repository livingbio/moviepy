# coding: utf-8

from moviepy.editor import *


def example_video1():

    nice_yo = TextClip(txt="Nice Yo", bg_color='white', fontsize=100)
    nice_yo = nice_yo.set_position(lambda t: (1 + t*90, 'center'))

    color = ColorClip(col=(33, 0, 0), size=(800,450))

    return CompositeVideoClip([color, nice_yo]).set_duration(6)


def main():
    video = example_video1()
    video.write_videofile(fps=10, filename="a.mp4")
    import os
    os.system("open a.mp4")


if __name__ == "__main__":
    main()
