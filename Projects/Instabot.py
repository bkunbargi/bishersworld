import urllib.request as req
from InstagramAPI import ImageUtils,InstagramAPI
from PIL import Image

#InstagramAPI = InstagramAPI('culver_loons','jibneh82')
#InstagramAPI.login()


def image_aspect_change(image_loc):
    width,height = ImageUtils.getImageSize(image_loc)
    if width > height:
        new_height = int(width/1.91)
    else:
        new_height = int((5*width)/4)
    my_pic = Image.open(image_loc)
    my_pic = my_pic.resize((width,new_height),Image.ANTIALIAS)
    my_pic.save(image_loc)


def image_handle(r,photo_url, photo):
    '''nested helper function for image resizing and posting'''
    req.urlretrieve(photo_url, photo)
    image_aspect_change(photo)
    r.uploadPhoto(photo)

def local_image(r,photo,photo_loc):
    base = Image.open(photo).convert('RGB').save("Projects/image_name.jpg")
    image_aspect_change(photo_loc)
    r.uploadPhoto(photo_loc)

def run_insta(imagfunc,photo,photo_loc):
    global InstagramAPI
    InstagramAPI = InstagramAPI('culver_loons','jibneh82')
    InstagramAPI.login()
    imagfunc(InstagramAPI,photo,photo_loc)
