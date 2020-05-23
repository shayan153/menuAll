'''
import
'''
import os
import sys
import re
import random
import whois

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
re=('''
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
lotafan yk gozine entekhab kon:
{1}-----menucalPersian-----{1}
{2}-----menuGame-----{2}
{99}-----EXIT-----{99}
 : ''')
    if m=='1':
        menucalPersian()
    elif m=='2':
        menuGame()
    elif m=='99':
        print('by by :)')
    else:
        print('''
!!!ERORR!!!
dost aziz lotfan az gozineh ha entekhab kon''')
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
khob hala mikhay che amaliaty angam bedy??
baray jam bezan----{'+'}
baray tafrigh bezan-----{'-'}
baray zarb bezan---{'*'}
baray taghsim bezan----------{'/'}
baray back  ham bezan -----{'99'}
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
lotfan az gozine ha entekhab kon
gozineha:
zarb:+
taghsim:/
jam:+
tafrigh:- ''')
        again()
    def again():
        m=input(color_random[4]+'''
aya dost darid baz hesab konid
age are bezan 'Y'
age na bezan 'N'
== ''')
        if m.upper()=='Y':
            hesab()
        elif m.upper()=='N':
            print('mamnoon az entekhabeton va beomiddidar :)')
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
age mikhay dobareh bazi kony bezan 'Y' age na bezan 'N' mamnon = ''')
            if sm.upper()=='Y':
                clearScr()
                game()
            elif sm.upper()=='N':
                print (color_random[2]+'by by :) ')
                menu()
            else:
                again()
        sh=input(color_random[1]+'''
age amadey bazy hasti bezan 'Y' age na bezan 'N'
== ''')
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
menu()
