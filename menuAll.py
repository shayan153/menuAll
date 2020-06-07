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
{5}----Covid19 statistics----{5}
{6}-----Temperatures-----{6}
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
    elif m=='5':
        Covid19_statistics()
    elif m=='6':
        Temperatures()
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
  ca a   a    ll l   p  l  r  s           a    l    l
ca      aaa   ll l p    lr      s    l   aaa   l \  l
ca     a   a  ll l      l         s  l  a   a  l  \ l
 ca a a     a ll l      l      sss   l a     a l   \l 

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
        else:
            again()
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
    clearScr()
    m=color_random[8]+'''
b     ii lllllll   cccccc    oo    ii  NN     N
b     ii   l      c        o    o  ii  N N    N
bbbb  ii   l     c        o      o ii  N  N   N
b   b ii   l     c        o      o ii  N   N  N
b   b ii   l      c        o    o  ii  N    N N
bbbbb ii   l        ccccc    oo    ii  N     NN
'''
    print(m)
    def bit():
        Url='https://api.coinbase.com/v2/prices/spot?currency=USD'
        r=requests.get(Url)
        p=float(r.json()['data']['amount'])
        print(color_random[4]+'Bitcoin price is %s dollars '%p)
    bit()
    menu()
def Covid19_statistics():
    clearScr()
    print(color_random[2]+'''
   !! attention attention!!
Dear friend, this program gives statistics from the first day of covid19 until today, and it is updated every day
''')
    p=input(color_random[3]+'enter name country: ')
    url=('https://api.covid19api.com/total/dayone/country/%s'%p)
    r=requests.get(url)
    print(r.text)
    menu()
def Temperatures():
    clearScr()
    def Temperature():
        ls1=input(color_random[2]+'''
Click 'F' to convert Fahrenheit to Celsius and 'C'to convert Celsius to Fahrenheit and 'B' to return
== ''')
        if ls1.upper()=='C':
            og=float(input('enter C°: '))
            s=(9/5*og+32)
            print(s,'F°')
            Temperature()
        elif ls1.upper()=='F':
            f=float(input('enter F°: '))
            v=(f-32)
            b=5/9
            j=b*v
            print(j,'C°')
            Temperature()
        elif ls1.upper()=='B':
            print('Ok come back')
            menu()
        else:
            print('Error!!,You made a mistake and tried again')
            Temperature()
    Temperature()
menu()
