import csv
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
from itertools import islice
import moviepy.editor as mymovie
from moviepy.editor import *
import random
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe"})
# specify the URL of the archive here
url = "https://www.pexels.com/search/videos/programming/?orientation=portrait"
video_links = []

#reading quotes from quotes.txt file
array =[]

def read_file():
    with open('quotes\quotedata.txt', 'r') as f:
        reader = csv.reader(f)
        content = f.readlines()
        #print(content)
       
    for i in range(0, len(content) -1, 2):
        str = content[i] + " " + content[i+1]
        i = i +1
        array.append(str)

#getting all video links
def getting_links():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.maximize_window()
    time.sleep(2)
    browser.get(url)
    time.sleep(5)

    vids = input("How many videos you want to download? ")

    soup = BeautifulSoup(browser.page_source, 'lxml')
    links = soup.findAll("source")
    for link in islice(links, int(vids)):
        video_links.append(link.get("src"))
    return video_links

#download all videos

def downloading_videos(video_links):
    songs = input("Number of songs present right now? ")
    i=1
    for link in video_links:
   # iterate through all links in video_links
    # and download them one by one
        fn = link.split('/')[-1]  
        file_name = fn.split("?")[0]
        print ("Downloading video: %s"%file_name)

        #create response object2
        r = requests.get(link, stream = True)
 
        #download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 1024*1024):
                if chunk:
                    f.write(chunk)
    
        print ("%s downloaded!"%file_name)

        #editing the video
        list = random.choice(range(1, int(songs)))
        clip = mymovie.VideoFileClip(file_name)
        clip_duration = clip.duration
        audioclip = mymovie.AudioFileClip(f"songs/songs{list}.mp3").set_duration(clip_duration)
        new_audioclip = mymovie.CompositeAudioClip([audioclip])
        finalclip = clip.set_audio(new_audioclip)
        #adding quote on video
        index = random.choice(range(0, len(array)-1))
        print("adding quote: " + array[index])
        txt_clip = TextClip(array[index],font='Amiri-regular', fontsize = 30, color = 'white', kerning=-2, interline=-1, size =clip.size, method='caption').set_position('top')
        txt_clip = txt_clip.set_duration(clip.duration)

        newfinalclip = CompositeVideoClip([finalclip, txt_clip])
        newfinalclip.write_videofile(f"videos/vid{i}.mp4", fps=60)
        print("%s has been edited!\n"%file_name)
        i+=1



if __name__ == "__main__":
    read_file()
  #getting all video links
    video_links = getting_links()

  #download all videos
    downloading_videos(video_links)