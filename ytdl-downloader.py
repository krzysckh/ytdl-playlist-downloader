import os
fname = ""
nofsongs = ""
while fname == "":
    fname = input("filename with song names (every song in new line): ")
while nofsongs == "":
    nofsongs = input("and how many songs?: ")

nofsongs = int(nofsongs)
f = open(fname, 'r')

songs = f.read()

print("LIST TO DOWNLOAD: ")
print(songs)

songsInList = songs.split("\n")

i = 0;
while i < nofsongs:
    print("downloading " + songsInList[i])
    os.system('youtube-dl "ytsearch1:' + songsInList[i] + '" --extract-audio --audio-format mp3')
    i += 1
