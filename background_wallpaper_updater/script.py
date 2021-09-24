import ctypes
import time
import requests
import os

# save image
def saveImage(url):
    image_name = 'wallpaper.jpg'
    r = requests.get(url)
    with open(image_name, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)
    return

# get random url from unsplash
def getUrl():
    key = os.environ.get("UNSPLASH_ACCESS_KEY")
    payload = {'collections':'1263731'}
    url = 'https://api.unsplash.com/photos/random'
    headers = {'Authorization':'Client-ID '+ key}
    r = requests.get(url, headers=headers, params=payload) 
    response =  r.json() 
    return response['urls']['raw']



# set background
def setBackground():
    path = os.environ.get("WALLPAPER_PATH")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)


def getNewUnsplashBackground():
    url = getUrl()
    saveImage(url)
    setBackground()

def startScheduler():
    while True:
        getNewUnsplashBackground()
        time.sleep(1 * 60)


startScheduler()
