import os
from colorama import *
from logo import logo
from selections import selections
import time

def removeColor():
    print(Style.RESET_ALL);

numbers = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
  
    logo()

    selections()

while True:
    show_menu()
    yourSelection = input("Tanlovingiz: ")

    if yourSelection == '1':
        number = input("Akkount qo'shish uchun nomerni kiriting: ")
        smsCode = input("Borgan sms kodni kiriting: ")
        
        if smsCode.isdigit():
            numbers.append(number)
            print("Tabriklayman akkount qo'shildi")
        else:
            print(Fore.RED + "Xato: Kiritilgan sms kod")
            removeColor()
    
    elif yourSelection == '2':
        if len(numbers) == 0: 
            print(Fore.RED + "Siz nomer qo'shmagansiz")
            removeColor()
        else:
            print("Akkountlar ro'yxati:")
            for num in numbers:
                print(num)
    
    elif yourSelection == '3':
        count = input("Kanalga nechta obunachi qo'shay? ")
        if count.isdigit():
           count = int(count)
           if count <= len(numbers):
              channelName = str(input("Kanal havolasini kiriting: "))
              if "https://t.me/" in channelName:
                  print("Obuna bo'lish boshlandi!");
              else:
                  print(Fore.RED + "Kanal havolasi noto'g'ri !")
                  removeColor();
           else:
               print(Fore.RED + "Nomerlar yetarli emas !")
               removeColor();
        else: 
            print(Fore.RED + "Raqam kiritmadingiz !")
            removeColor();
    
    elif yourSelection == '4':
        count = input("Botga nechta start bosay? ")
        if count.isdigit():
           count = int(count)
           if count > len(numbers):
              channelName = str(input("Referral havolani kiriting: "))
              if "https://t.me/" in channelName:
                  print("Start bosish boshlandi!");
              else:
                  print(Fore.RED + "Bot ref. havolasi noto'g'ri !")
                  removeColor();
           else:
               print(Fore.RED + "Nomerlar yetarli emas !")
               removeColor();
        else: 
            print(Fore.RED + "Raqam kiritmadingiz !")
            removeColor();
    
    elif yourSelection == '5':
        count = input("So'rovnomaga nechta ovoz beray? ")
        if count.isdigit():
           count = int(count)
           if count > len(numbers):
              channelName = str(input("So'rovnoma havolasini kiriting: "))
              if "https://t.me/" in channelName:
                  print("Ovoz berish boshlandi!");
              else:
                  print(Fore.RED + "So'rovnoma havolasi noto'g'ri !")
                  removeColor();
           else:
               print(Fore.RED + "Nomerlar yetarli emas !")
               removeColor();
        else: 
            print(Fore.RED + "Raqam kiritmadingiz !")
            removeColor();
    
    elif yourSelection == '6':
        if len(numbers) != 0:
            print("Raqamlaringiz tekshirilmoqda ...")
            print("2 daqiqa kutishingiz talab qilinadi !")
            time.sleep(120)
            print(Fore.GREEN + "Hamma akkountingiz spamdan ozod ekan !")
            removeColor();
        else: print("Sizda nomer yo'q");

    elif yourSelection == '7':
            if len(numbers) != 0:
                print("O'chib ketgan raqamlar tozalanmoqda ...")
                print("30 soniya kutishingiz talab qilinadi !")
                time.sleep(30)
                print(Fore.GREEN + "Hamma o'chib ketgan raqamlar tozalandi !")
                removeColor();
            else: print("Sizda nomer yo'q")
    
    elif yourSelection == '8':
       exitAccount = int(input("Chiqmoqchi bo'lgan nomeringizni yozing ..."))
       if exitAccount in numbers:
           numbers.remove(exitAccount)
           print(Fore.GREEN + "Akkountdan muvaffaqiyatli chiqib ketdim")
           
    elif yourSelection == '9':
        if len(numbers) != 0:
            print("Tekshirilmoqda ...")
            time.sleep(4)
            print(Fore.RED + "Afsuski bironta ham akkountingiz premium yutmadi")
            removeColor()
        else: print("Sizda nomer yo'q")
    
    elif yourSelection == '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        exit(True);
    
    else: print("Bunday tanlov yo'q")

    input("Davom etish uchun Enter tugmasini bosing...")

