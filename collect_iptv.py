# Testing  put varous files into one file even url into this
import os
#import pdb 
import glob
import requests

os.makedirs("temp/")

#Reading the url's into "url_list.txt"
with open("url_list.txt", 'r') as f:
    for line in f:
        m3u = requests.get(line)

        if '.m3u' in line:
            os.system(f'wget -N -P m3u/ {line}')
        elif '.m3u8' in line:
            os.system(f'wget -N -P m3u/ {line}')   
        else:
            m3url = m3u.text
            with open("temp/temp.txt", 'a') as outfile:
                outfile.write(m3url)


#Reading m3u files.

m3u_files = glob.glob("m3u/*.m3u")

with open("temp/temp.txt", 'ab') as outfile:
    for f in m3u_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

m3u8_files = glob.glob("m3u/*.m3u8")

with open("temp/temp.txt", 'ab') as outfile:
    for f in m3u8_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())            

#Put in one file every temp file.

url_ok_1 = open("temp/temp.txt").read()

with open("Final_List.txt", 'a') as file:
    file.write(url_ok_1)

#Delete files into folder "temp_m3u"
tempath = 'temp/*'
r = glob.glob(tempath)
for i in r:
   os.remove(i)

#Rename final file

old_file_name = "Final_List.txt"
new_file_name = "Final_List.m3u"

os.rename(old_file_name, new_file_name)
