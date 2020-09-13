import requests
import os


# Option to show
print("Validator of m3u lists")
print("Choice an option:")
print(" (1)-Read folder with m3u files.")
print(" (2)-Put a m3u URL to validate.")
option = input()

file = ("tv.m3u")
with open(file, 'r') as m3u:
    list = m3u.read()

if option == "1":
    os.system(f'./iptv-check {file}')
    #print(list)


if option == "2":
    print("Put URL: ")
    link = input()
    f = requests.get(link)
    os.system(f'./iptv-check {link}')
    # print(f.text)

# M3U list.
#


# Open list m3u file


# c = s[s.index("http"):s.index(".m3u8")+len(".m3u8")]
#response = requests.get(c)


# print(response)
