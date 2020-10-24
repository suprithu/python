
from gtts import gTTS
import os
from os import system, name
import sys
from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

	
mytext = 'welcome to this session. Please login with new account'
language = 'hi'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system("mpg321 welcome.mp3")

_ = system('clear')


username1 = raw_input("please enter your username : ")
password1 = raw_input("please enter your password : ")
mytext0 = 'welcom again' + username1 + "now you are logged in with your new account and password"
language= 'hi'

myobj0 = gTTS(text=mytext0, lang=language, slow=False)

myobj0.save("username.mp3")

os.system("mpg321 username.mp3")

_ = system('clear')

accno = random_with_N_digits(12)
print ("Your account number is: ")
print accno

mytext = ' Hellow '+  username1   +'Note this is number '+ str(accno) +'you wnat to login with this number for verficiation. Not with your user name. But the password will remain same'
language = 'hi'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("account.mp3")

os.system("mpg321 account.mp3")

_ = system('clear')

print("Hellow " + username1 + " you are now logged in with a password and your account number is " + accno  )
