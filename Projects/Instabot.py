import urllib.request as req
from InstagramAPI import ImageUtils,InstagramAPI
from PIL import Image


global InstagramAPI
InstagramAPI = InstagramAPI('culver_loons','jibneh82')
InstagramAPI.login()


def image_aspect_change(image_loc):
    width,height = ImageUtils.getImageSize(image_loc)
    if width > height:
        new_height = int(width/1.91)
    else:
        new_height = int((5*width)/4)
    my_pic = Image.open(image_loc)
    my_pic = my_pic.resize((width,new_height),Image.ANTIALIAS)
    my_pic.save(image_loc)


def final_image_step(photo,caption):
    base = Image.open(photo).convert('RGB').save("Projects/image_name.jpg")
    image_aspect_change(photo)
    InstagramAPI.uploadPhoto(photo,caption)


def image_handle(photo_url, photo_loc, caption = None):
    #nested helper function for image resizing and posting
    req.urlretrieve(photo_url, photo_loc)
    base = Image.open(photo_loc).convert('RGB').save("Projects/image_name.jpg")
    image_aspect_change(photo_loc)
    InstagramAPI.uploadPhoto(photo_loc,caption)
    #final_image_step(photo,caption)

def local_image(photo,photo_loc,caption = None):
    base = Image.open(photo).convert('RGB').save("Projects/image_name.jpg")
    image_aspect_change(photo_loc)
    InstagramAPI.uploadPhoto(photo_loc,caption)
    #final_image_step(photo_loc,caption)



def run_insta(imagefunc,photo,photo_loc,caption):
    #base = Image.open(photo).convert('RGB').save("Projects/image_name.jpg")
    #image_aspect_change(photo_loc)
    #InstagramAPI.uploadPhoto(photo_loc,caption)
    imagefunc(photo,photo_loc,caption)
