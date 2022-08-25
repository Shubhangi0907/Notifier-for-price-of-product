import requests
import bs4
import time
import tkinter
import sys
from tkinter import messagebox

while (True):
    pixel = requests.get("https://www.flipkart.com/asus-tuf-gaming-a17-ryzen-7-octa-core-4800h-16-gb-512-gb-ssd-windows-10-home-4-graphics-nvidia-geforce-rtx-3050-144-hz-fa766ic-hx005t-fa766ic-hx005w-laptop/p/itm05769934382c7?pid=COMG5QHNU3DSZGEY&lid=LSTCOMG5QHNU3DSZGEYG2ALG4&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_2&otracker=hp_omu_Best%2Bof%2BElectronics_6_3.dealCard.OMU_SG7UU0MTI0RX_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_6_NA_view-all_3&fm=neo%2Fmerchandising&iid=en_%2BsNpYUhQSqKRLyq%2FXfCqVNH3wZnUldEBvZexlahOKyCnn1qJmWszS3JIZ9o5xieo4k%2Fh7RYhHI01uQhHGFyP%2FA%3D%3D&ppt=hp&ppn=homepage&ssid=qnm6fr53g00000001661402280091")
    soup = bs4.BeautifulSoup(pixel.text,'lxml')
    price = soup.find("",{"class":'_30jeq3 _16Jk6d'})
    prices = []
    prices.append(price.text)
    print(prices)
    actual_price = prices[0]
    actual_price = actual_price[1:3]+actual_price[4:7]
    print(actual_price)
    price = int(actual_price)
    time.sleep(10)
    if price<75000:
        print("Buy Buy Buy")
        tkinter.messagebox.showinfo(title = "hello",message = "buy buy buy")
    elif price>75000:
        print("Not Buy")
        tkinter.messagebox.showinfo(title = "hello",message = "buy not buy not buy")