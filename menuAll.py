'''
import
'''
import os
import sys
import random
import requests
import json

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'
color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
random.shuffle(color_random)
def clearScr():
    os.system('clear')
clearScr()
re=(color_random[8]+'''
sw          swEEEEE ll   cs cs        MM   MM EEEEE
 sw        sw E     ll cs      OOOOO  M M M M E
  sw  sw  sw  EEE   ll cs     O     O M  M  M EEE
   swswswsw   E     ll cs     O     O M     M E
    sw  sw    EEEEE ll   cs cs O O O  M     M EEEEE


 MM   MM EEEEE N    N U   U    A     ll ll
 M M M M E     N N  N U   U   A A    ll ll
 M  M  M EEE   N  N N U   U  AAAAA   ll ll
 M     M E     N   NN U   U A     A  ll ll
 M     M EEEEE N    N  UUU A       A ll ll
 ''')
print(re)
def menu():
    m=input(color_random[6]+'''
Please select an option:
{1}-----menucalPersian-----{1}
{2}-----menuGame-----{2}
{3}----IPchecker----{3}
{4}----Bitcoin price----{4}
{99}-----EXIT-----{99}
 : ''')
    if m=='1':
        menucalPersian()
    elif m=='2':
        menuGame()
    elif m=='3':
        ipchecker()
    elif m=='4':
        Bitcoin_price()
    elif m=='99':
        print('by by :)')
    else:
        print('''
!!!ERORR!!!
Dear friend, please select only from the options''')
        menu()
def menucalPersian():
    def clearScr():
        os.system('clear')
    clearScr()
    logo=color_random[2]+''' 
                   p           sss   o    
  ca a   a    l  l   p  l  r  s           a    l    l
ca      aaa   l  l p    lr      s    l   aaa   l \  l
ca     a   a  l  l      l         s  l  a   a  l  \ l
 ca a a     a l  l      l      sss   l a     a l   \l 

'''

    print(logo)
    def hesab():
        l=input(color_random[9]+'''
So what do you want to do now???
Gather for----{'+'}
To subtract-----{'-'}
To multiply---{'*'}
Click to split----------{'/'}
Click on me to return-----{'99'}
== ''')
        if l=='+':
            number1=float(input('Enter Number ='))
            number2=float(input('Enter Number ='))
            print(number1+number2)
        elif l=='-':
            number1=float(input('Enter Number ='))
            number2=float(input('Enter Number ='))
            print(number1-number2)
        elif l=='*':
            number1=float(input('Enter Number ='))
            number2=float(input('Enter Number ='))
            print(number1*number2)
        elif l=='/':
            number1=float(input('Enter Number ='))
            number2=float(input('Enter Number ='))
            print(number1/number2)
        elif l=='99':
            print('back')
        else:
            print(color_random[5]+'''
!!!ERORR!!!
Dear friend, please select only from the options
options:
multiply=*
split=/
gather=+
subtract=-
: ''')
        again()
    def again():
        m=input(color_random[4]+'''
If you want to count again, click 'Y', if you don't want to, click 'N'
== ''')
        if m.upper()=='Y':
            hesab()
        elif m.upper()=='N':
            print('by by ;)')
            menu()
        else:
            again()
    hesab()
def menuGame():
    clearScr()
    loGo=color_random[9]+'''

 G G G       A      MM     MM   EEEEEE
G           A A     M M   M M   E
G  G G     A   A    M  M M  M   EEEE
G     G   AAAAAAA   M   M   M   E
 G G G   A       A  M       M   EEEEEE
'''
    print(loGo)
    def game():
        def again():
            sm=input(color_random[0]+'''
If you want to play again, click 'Y', if you don't want to play 'N' : ''')
            if sm.upper()=='Y':
                clearScr()
                game()
            elif sm.upper()=='N':
                print (color_random[2]+'by by :) ')
                menu()
            else:
                again()
        sh=input(color_random[1]+'''
Click 'Y' to start the game and 'N' to return :  ''')
        if sh.upper()=='Y':
            sequence =[random.choice(['''
 -----
|     |
|  1  |
 -----''',
 '''
 -----
|     |
|  2  |
 -----''',
 '''
 -----
|     |
|  3  |
 ----''',
 '''
 -----
|     |
|  4  |
 -----''',
 '''
 -----
|     |
|  5  |
 -----''',
 '''
 -----
|     |
|  6  |
 -----'''])]
            for _ in range(1):

                selection = random.choice(sequence)
                print(selection)

                again()

        elif sh.upper()=='N':
            print(color_random[3]+'by by :) ')
            menu()
    game()
def ipchecker():
    clearScr()
    kk=(color_random[5]+'''
 o lPPP   ccccc l     eeeee  ccccc k  k  eeee  r  rr
   l   P c      l     e     c      k k   e     r r
 i lPPP  c      lmmm  eee   c      kk    ee e  rr
 i l     c      l   m e     c      k k   e     r
 i l      ccccc l   m eeee   ccccc k  k  eeee  r
 ''')
    print(kk)
    ee=input(color_random[7]+'''
To check, tap 'IP'
to return 'B'
: ''')
    if ee.upper()=='IP':
        er=input('enter ip : ')
        respons=requests.get('http://ip-api.com/json/%s' % er)
        json_date=respons.json()
        print(json.dumps(json_date,indent = 4,sort_keys=False))
        menu()
    elif ee.upper()=='B':
        menu()
    else:
        print('!!ERORR!! , Dear friend, just use the options')
        ipchecker()
def Bitcoin_price():
    def bit():
        clearScr()
        Url='https://api.coinbase.com/v2/prices/spot?currency=USD'
        r=requests.get(Url)
        p=float(r.json()['data']['amount'])
        print(color_random[4]+'Bitcoin price is %s dollars '%p)
        m=input(color_random[6]+'''
If you want me to give you a sms, hit the price of bitcoin 'O' if you don't want to hit 'E'
== ''')
        if m.upper()=='O':
            Url='https://api.coinbase.com/v2/prices/spot?currency=USD'
            n=input('enter number: ')
            url='https://api.kavenegar.com/v1/65443736634F786E634646324A637173726934454F3037484C75366F515A4B314A7869594F5270565063633D/sms/send.json'
            payload={'receptor':n,'message':'Bitcoin price is %s dollars' % p}
            respons=requests.post(url,payload)
        elif m.upper()=='E':
            print('by by ;) ')
        else:
            print('!!erorr!!,You made a mistake, try again')
            bit()
    bit()
menu()
