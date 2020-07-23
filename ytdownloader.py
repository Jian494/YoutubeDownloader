from pytube import YouTube , Playlist
import os
import ffmpeg

os.system("clear" or "cls")

print("__   _______ ____                      _                 _           ")
print("\ \ / /_   _|  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __ ")
print(" \ V /  | | | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|")
print("  | |   | | | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   ")
print("  |_|   |_| |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   ")
print("\n")

while True:
    print("URL Format"+"\n"+"==================="+"\n"+"1) Single"+"\n"+"2) Playlist"+"\n"+"\n")
    a = input("Choice --> ")
    if a == "1":
        print("\n")
        url = input("URL --> ")
        print("\n"+"Youtube Name: " + YouTube(url).title+"\n")
        print("\n"+"Output Format"+"\n"+"==================="+"\n"+"1) mp4"+"\n"+"2) mp3"+"\n"+"\n")
        a = input("Choice --> ")
        if a == "1":
            print("Start Progressing...")
            video = YouTube(url).streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first().download(filename="video")
            music = YouTube(url).streams.filter(audio_codec="mp4a.40.2").desc().first().download(filename="audio")            
            video1 = ffmpeg.input("video.mp4")
            music2 = ffmpeg.input("audio.mp4")
            merged = ffmpeg.concat(video1,music2, v=1 , a =1).output(YouTube(url).title+".mp4").run()
            os.remove("video.mp4","audio.mp4")
            print("DONE")
            cont = input("Another one? Y/N --> ")
            if cont == "Y":
                continue
            elif cont == "N":
                break
            else:
                print("Invalid Input"+"\n")
                break
        if a == "2":
            print("Start Progressing...")
            music = YouTube(url).streams.filter(audio_codec="mp4a.40.2").desc().first().download(filename="audio")
            os.rename("audio.mp4",YouTube(url).title+".mp3")
            print("DONE"+"\n")
            cont = input("Another one? Y/N --> ")
            if cont == "Y":
                continue
            elif cont == "N":
                break
            else:
                print("Invalid Input"+"\n")
                break
        else:
            print("Invalid Input"+"\n")
            continue
    if a == "2":        
        playlist = Playlist(input("URL -->> "))
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        print("Total videos " + str(len(playlist.video_urls))+"\n")
        print((playlist.title()))
        for url in playlist.video_urls:
            print(YouTube(url).title)  
            print(url+"\n")     
        print("Start Progressing...")
        playlist.download_all()
        cont = input("Another one? Y/N --> ")
        if cont == "Y":
            continue
        elif cont == "N":
            break
        else:
            print("Invalid Input"+"\n")
            break
    else:
        print("Invalid Input"+"\n")
        continue
