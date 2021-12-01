import string
import random



lowercase=string.ascii_lowercase
uppercase=string.ascii_uppercase
digits =string.digits
symbols = string.punctuation





def genpassword(l,h,d,s):

    password = ""
    l=int(l)
    h=int(h)
    d=int(d)
    s=int(s)

    if l<1 or h<1 or d<1 or s<1:
        return "1 is the minimum number for all fields"
    try:

        for i in range(0,h):
            password=password+random.choice(uppercase)

        for i in range(0,l):
            password=password+random.choice(lowercase)

        for i in range(0,d):
            password=password+random.choice(digits)

        for i in range(0,s):
            password=password+random.choice(symbols)

        return(password)
    except:
        return("Something went wrong")




