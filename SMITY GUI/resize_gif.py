#https://gist.github.com/skywodd/8b68bd9c7af048afcedcea3fb1807966

from PIL import Image, ImageSequence
import pathlib


def resize_gif(w,h):
    location = pathlib.Path(__file__).parent.absolute()
    # Output (max) size
    size = 257, 261


    # Open source
    im = Image.open('%s\\Home page\\home page gif2.gif'%(location))

    # Get sequence iterator
    frames = ImageSequence.Iterator(im)

    # Wrap on-the-fly thumbnail generator
    def thumbnails(frames):
        for frame in frames:
            thumbnail = frame.copy()
            thumbnail.thumbnail(257, 261, Image.ANTIALIAS)
            yield thumbnail

    frames = thumbnails(frames)

    # Save output
    om = next(frames) # Handle first frame separately
    om.info = im.info # Copy sequence info
    om.save("out.gif", save_all=True, append_images=list(frames))

resize_gif(w,h)