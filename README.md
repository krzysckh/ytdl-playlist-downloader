# ytdl-playlist-downloader
youtube-dl playlist downloading script

#how to use it?
1. install dependencies
  - on linux
    - install python3
      - ```sudo apt-get install python3```
    - install youtube-dl
      - ```sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl```
      - ```sudo chmod a+rx /usr/local/bin/youtube-dl```
      - ```youtube-dl -U```
  - on windows
    - install python3 and youtube-dl with a package manager or how you like it idk
2. clone the repo
  - ```git clone https://github.com/krzysckh/ytdl-playlist-downloader```
  - ```cd ytdl-playlist-downloader```
3. create a file with songs
  - name the file however you want and format it like this:
  ```testfile.txt```
  ```
  LOOK MUM NO COMPUTER - MODERN GAS
  C418 - STAL
  MC Virgins - Anime Thighs
  ```
4. run the program
  - on linux
    - ```python3 ytdl-downloader.py```
  - on windows
    - ```python ytdl-downloader.py```
5. the script will prompt you for name of file with songs and number of songs
6. wait
7. profit?

