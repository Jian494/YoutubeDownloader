from pytube import YouTube , Playlist
import os
from tqdm import tqdm
from multiprocessing import Process
import sys
import time
import os
import ffmpeg
import re

def mp4():    
    videoname = YouTube(url).title
    video = YouTube(url).streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first().download(filename="video")        
    music = YouTube(url).streams.filter(audio_codec="mp4a.40.2").desc().first().download(filename="audio")                    
    video1 = ffmpeg.input("video.mp4")    
    music2 = ffmpeg.input("audio.mp4")    
    if "/" in videoname:
        cname2 = videoname.replace("/"," ")
        merged = ffmpeg.concat(video1,music2, v=1 , a =1).output(cname2+".mp4")
        merged.run(cmd='ffmpeg', capture_stdout=False, capture_stderr=False, input=None, quiet=True, overwrite_output=True)
    else:
        merged = ffmpeg.concat(video1,music2, v=1 , a =1).output(videoname+".mp4")
        merged.run(cmd='ffmpeg', capture_stdout=False, capture_stderr=False, input=None, quiet=True, overwrite_output=True)   
    os.system("rm -r -f video.mp4 audio.mp4")        

def vbar(count):
    size = YouTube(url).streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first().filesize
    b = tqdm(range(size),desc="Processing...")
    if 0 < size < 2200000:
        for i in range(int(size/5)):
            b.update(5)
            time.sleep(count)
        print(YouTube(url).title+" DONE" +"\n")
    elif  55000000 < size < 400000000:
        for i in range(int(size/30)):
            b.update(30)
            time.sleep(count)
        print(YouTube(url).title+" DONE" +"\n")
    elif  2200000 < size < 55000000:
        for i in range(int(size/17)):
            b.update(17)
            time.sleep(count)
        print(YouTube(url).title+" DONE" +"\n")

def mbar(count):
    size = YouTube(url).streams.filter(audio_codec="mp4a.40.2").desc().first().filesize
    b = tqdm(range(size),desc="Processing...")
    for i in range(int(size/500)):
        b.update(500)
        time.sleep(count)
    time.sleep(1)
    print(YouTube(url).title+" DONE" +"\n")

def mp3():
    music = YouTube(url).streams.filter(audio_codec="mp4a.40.2").desc().first().download(filename="naudio")                            
    rname= YouTube(url).title.replace("/","")                                              
    os.rename("naudio.mp4",rname+".mp3")      

if __name__=='__main__':
    print("__   _______ ____                      _                 _           ")
    print("\ \ / /_   _|  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __ ")
    print(" \ V /  | | | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|")
    print("  | |   | | | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   ")
    print("  |_|   |_| |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   ")
    print("\n")
    while True:
        print("\n"+"Output Format"+"\n"+"==================="+"\n"+"1) mp4"+"\n"+"2) mp3"+"\n"+"\n")
        a = input("Choice --> ")
        if a == "1":
            url = input("Url --> ")
            if "&list=" not in url:  
                p1 = Process(target = mp4)
                p1.start()
                p2 = Process(target = vbar(0.0000001))
                p2.start()
                p1.join()
                p2.join()
            if "&list=" in url:  
                name1 = Playlist(url)        
                name1._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
                try:
                    print((name1.title()))
                except:
                    pass
                print("Total videos " + str(len(name1.video_urls))+"\n")
                print("Start Progressing...")
                for url in name1.video_urls:  
                    name2 = YouTube(url)         
                    print(name2.title)    
                    p1 = Process(target = mp4)
                    p1.start()
                    p2 = Process(target = vbar(1))
                    p2.start()
                    p1.join()
                    p2.join()                                               
        if a == "2":
            url = input("Url --> ")
            if "&list=" not in url:    
                p1 = Process(target = mp3)
                p1.start()
                p2 = Process(target = mbar(0.0000001))
                p2.start()
                p1.join()
                p2.join()
            if "&list=" in url:     
                name1 = Playlist(url)                  
                name1._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
                try:
                    print((name1.title()))
                except:
                    pass
                print("Total videos " + str(len(name1.video_urls))+"\n")     
                for url in name1.video_urls:                  
                    name2 = YouTube(url)         
                    print(name2.title)     
                    p1 = Process(target = mp3)
                    p1.start()
                    p2 = Process(target = mbar(0.0000001))
                    p2.start()
                    p1.join()
                    p2.join()
