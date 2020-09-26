# Testing  put varous files into one file even url into this
import os
#import pdb
import glob
import pathlib
import requests

# Generate necessary files.

tempfile_temp = pathlib.Path("temp/")
tempfile_m3u = pathlib.Path("m3u/")
tempfile_url_list = pathlib.Path("url_list.txt")

if tempfile_temp.exists():
    pass
else:
    print("The folder 'temp' was created")
    os.makedirs("temp/")

if tempfile_m3u.exists():
    pass
else:
    print("The folder 'm3u' was created please put your m3u files inside and run again this program.")
    os.makedirs("m3u/")

if tempfile_url_list.exists():
    pass
else:
    os.system("echo 'https://pastebin.com/raw/HV5LwnLb' >> url_list.txt")


# Clean duplicates url in url_list.txt

lines_seen = set()  # holds lines already seen
with open("url_list2.txt", "w") as output_file:
    for each_line in open("url_list.txt", "r"):
        if each_line not in lines_seen:  # check if line is not duplicate
            output_file.write(each_line)
            lines_seen.add(each_line)
old_list = "url_list2.txt"
new_list = "url_list.txt"
os.remove("url_list.txt")
os.rename(old_list, new_list)

# Reading the url's into "url_list.txt"
with open("url_list.txt", 'r') as f:
    for line in f:
        m3u = requests.get(line)
        
        if '.m3u' in line:
            os.system(f'wget -N -P m3u/ {line}')
        elif '.m3u8' in line:
            os.system(f'wget -N -P m3u/ {line}')
        elif m3u.status_code != 200:
            line.strip()
            print("Borrado url desactiva")   
        else:
            m3url = m3u.text
            with open("temp/temp.txt", 'a') as outfile:
                outfile.write(m3url)
                outfile.write("\n")


# Reading m3u files.

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

# Put in one file every temp file.

url_ok_1 = open("temp/temp.txt", encoding = "ISO-8859-1").read()

with open("Final_List.txt", 'a') as file:
    file.write(url_ok_1)


# Delete files into folder "temp_m3u"

tempath = 'temp/*'
r = glob.glob(tempath)
for i in r:
    os.remove(i)
    # pass


# Clean duplicates in final list

lines_seen = set()  # holds lines already seen
with open("Final_List2.txt", "w") as output_file:
    for each_line in open("Final_List.txt", "r"):
        if each_line not in lines_seen:  # check if line is not duplicate
            output_file.write(each_line)
            lines_seen.add(each_line)


# Rename final file
old_file_name = "Final_List2.txt"
new_file_name = "complete_List.m3u"
os.remove("Final_List.txt")

os.rename(old_file_name, new_file_name)

os.system(f'./iptv-check {new_file_name}')

os.remove("complete_List.m3u")