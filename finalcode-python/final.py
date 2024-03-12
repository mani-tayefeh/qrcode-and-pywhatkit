from colorama import Fore
import pyqrcode as qq
from tqdm import tqdm
from time import sleep
import pywhatkit as ww
import random
import pyfiglet


txt=pyfiglet.figlet_format("Final code",font="slant")

print(txt)

print("\n============================================================")


name = str(input("\nEnter your name please : "))

family = str(input("\nEnter your family-name please : "))

age = int(input("\nEnter your age please : "))

if age >= 18:
    pass
else: 
    print(Fore.RED,"\n⚠your name is suitable to continue⚠",Fore.RESET)
    exit()

pascode = random.randint(1000, 9999)

print(Fore.GREEN, f"\nYour pascode is: {pascode}", Fore.RESET)

pasword = input(f"\nOK MR/MISS {family}\n Enter password: ")

if pasword != str(pascode): 
    print(Fore.RED, "\n🔴 Password is incorrect 🔴", Fore.RESET)
    exit()
else:
    print("\n============================================================")
    pass

qrcode = input("\nEnter the text inside the QR Code : ")

whatkit = input("\nEnter your address of the file : ")



image=whatkit

save = qq.create(qrcode)

for char in tqdm(range(100), colour="GREEN" , ncols=70):
    sleep(0.02)

if char and ww:
    pass


save.svg(f"{name}-{family}-QRcode.svg",scale=8)

ww.image_to_ascii_art(image,f'{name}-{family}-txt')

print(Fore.GREEN,f"\n✅your QRCode code has been saved with the name {name}-{family}-QRcode and your txt file has been saved with the name {name}-{family}-txt✅\n",Fore.GREEN)
