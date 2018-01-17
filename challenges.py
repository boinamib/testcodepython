#!/usr/bin/env python
def helloWord(data):
    print "Hello"+" "+ data

def alphabet_position(text):
    alphadic = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9", "j": "10", "k": "11", "l": "12", "m": "13", "n": "14", "o": "15", "p": "16", "q": "17", "r": "18", "s": "19", "t": "20", "u": "21", "v": "22", "w": "23", "x": "24", "y": "25", "z": "26"}
    alphalist = []
    text = text.lower()
    for i in text:
        if i.isalpha():
            alphalist.append(alphadic[i])
    res = " ".join(alphalist)
    return res

def is_isogram(data):
    char ="abcdefghijklmnopqrstuvwxyz"
    data = data.lower()
    count = 0
    for c in char:
        if c in data:
            count = data.count(c)
            if count > 1:
                return "False"
    return "True"

def accum(data):
    accumlist = []
    accumlist1 = []
    for c in data:
        accumlist.append(c.upper())
    for c in range(len(accumlist)):
        cc = accumlist[c]+c*accumlist[c].lower()
        accumlist1.append(cc)

    print accumlist
    print accumlist1
    print "-".join(accumlist1)

def high_and_low(data):
    data = data.split()
    data1 = []
    for n in data:
        n = int(n)
        data1.append(n)
    print data1
    high = max(data1)
    low = min(data1)

    return str(high)+" "+ str(low)

def dig_pow(data, data1):
    data3 = []
    somme = 0
    data2 = str(data)
    for i in data2:
        data3.append(i)
    print data3
    for i in range(len(data3)):
        somme += int(data3[i])**(data1+i)
    print somme
    print data
    if somme % data == 0:
        return somme / data
    else:
        return -1

def get_sum(a,b):
    #good luck!
    r = []
    sm =0

    if a == b:
       return a
    elif a > b:
        r = range(b, a+1)
    else:
        r = range(a, b+1)
    for s in r:
        sm+=s
    return sm

def calculate_years(p,i,t,d):
    y = 0
    s = 0
    if p == d:
        return 0
    while p < d:
         #s= p + ((p*i)-(p*i*t))
         s = p*(1+i-i*t)
         print p
         p = s
         y+=1
    return y

def dont_give_me_five(start, end):
    tab = []
    tab = range(start, end+1)
    for i in tab:
        if "5" in str(i):
            tab.remove(i)
    print tab
    return len(tab)

def duplicate_count(text):
    tab = []
    c = 0
    text = text.upper()
    for i in text:
        if i not in tab and text.count(i) > 1:
            c += 1
            tab.append(i)
    return c

def valide_pin(pin):
    tab = " ".join(pin).split()
    if len(tab) == 4 or len(tab) == 6:
        for i in tab:
            if (i.isalpha()) or (i.isdigit() == False):
                return "False"
        else:
                return "True"
    else:
        return "False"

def find_missing_letter(chars):
    alphabet =["a", "b", "c", "d", "e","f", "g", "h", "i", "j", "k","l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    chars1 = []
    for c in chars:
        chars1.append(c.lower())
    letter = ""
    start = chars1[0]
    end = chars1[-1]
    for i in range(alphabet.index(start), alphabet.index(end)):
        if alphabet[i] not in chars1:
            letter = alphabet[i]
    if chars[0].istitle():
        return letter.upper()
    else:
        return letter

def findSmallestInt(arr):
        return min(arr)

def unique_in_order(iterable):
        unique = []
        tmp = " ".join(iterable).split()
        unique.append(tmp[0])
        for i in range(len(tmp)):
            while i < len(tmp):
                if tmp[i+1] != tmp[i]:
                    unique.append(tmp[i+1])
        return unique

def create_phone_number(n):
    n.insert(0, "(")
    n.insert(4, ")")
    n.insert(5, " ")
    n.insert(9, "-")
    r= ""
    for i in n:
        r+=str(i)
    print r






if __name__=="__main__":
    #helloWord("Hiyam et Ishak")
    #print alphabet_position("Ali Va A l'Ecole")
    #print is_isogram("Dermatoglyphics")
    #accum("baba")
    #print high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")
    #print(dig_pow(46288, 3))
    #print get_sum(0,1)
    #print calculate_years(1000,0.05,0.18,1000)
    #print dont_give_me_five(-20, -5)
    #print duplicate_count("indivisibility115589AabB")
    #print valide_pin("-1.234")
    #print find_missing_letter(["a", "b", "c", "d", "f"])
    #print findSmallestInt([2,5,8,9])
    #print unique_in_order("AAABBBCCDAABB")
    create_phone_number([1,2,3,4,5,6,7,8,9])
