#1
def msum(*num):
    c = 0
    for i in num:
        c += i
    return c
print(msum(12,13,45,67,4,5,6))

#2
def malpha(*m):
    c = 0
    for i in list(m):
        if type(i) == type(str()):
            c += 1
    return c
print(malpha(1,2,3,4,"ghgd","gdhd"))


#3
def mid(*num):
    c = 0
    k = 0
    for i in num:
        c += 1
        k += i
    return k/c
print(mid(12,13,134,56,34,23,45,78))


#4
def math_oper(m,n,s):
    if s == "+":
        return m + n
    elif s == "-":
        return m - n
    elif s == "*":
        return m * n
    else:
        return m / n
print(math_oper(12,13,"/"))



#5
#upper
def upper(word):
    mword = ""
    for i in range(len(word)):
        if 129 >= ord(word[i]) >= 97:
            mword += chr(ord(word[i]) - 32)
        else:
            mword += word[i]
    return mword
print(upper(input("Enter word")))


#6
def lower(word):
    mword = ""
    for i in range(len(word)):
        if 97 >= ord(word[i]) >= 65:
            mword += chr(ord(word[i]) + 32)
        else:
            mword += word[i]
    return mword
print(lower(input("Enter word: ")))

#7
def title(word):

    mword = ""
    spaces = True
    for i in range(len(word)):
        if spaces and 129 >= ord(word[i]) >= 97:
            mword += chr(ord(word[i]) - 32) 
            spaces = False
        else:
            mword += word[i]
            if word[i] == " ":
                spaces = True
    return mword
print(title(input("Enter word: ")))


#8
def reverse(word):
    return word[::-1]
print(reverse(input("Enter word: ")))

#9
def arg(word,dig1,dig2):
    pass

#10def long_word(ml):
    km = ml.split()
    m = ""
    for i in km:
        if len(i) > len(m):
            m = i
    return m
print(long_word(input("Enter word: ")))

#11
def most(word):
    m = 0
    k = ""
    for i in word:
        if word.count(i) > m:
            m = word.count(i)
            k = i  
    return k,m
print(most(input("Enter word: ")))

#12
def long_most(word):
    km = word.split()
    m = ""
    k = ""
    s = 0
    for i in km:
        if len(i) > len(km):
            m = i
    for i in m:
        if m.count(i) > s:
            s = m.count(i)
            k = i
    return k,s
print(long_most(input("Enter word: ")))

#13
def find_el(word,num):
    return word[num],word[-num]
print(find_el(input("Enter word: "),3))

#15
def polindrom(num):
    count = 0
    num1 = num
    ml = []
    while num > 0:
        num = num//10
        count += 1
    for i in range(0,count):
        a = num1 // 10**i
        ml.append(a%10)
    for i in range(len(ml)//2):
        if ml[i] == ml[-(i+1)]:
            continue
        else:
            return "no polindrom"
    return "Polindrom"
print(polindrom(1222))

#16
def polindrom2(num):
    count = 0
    num1 = num
    ml = []
    while num > 0:
        num = num//10
        count += 1
    for i in range(0,count):
        a = num1 // 10**i
        ml.append(a%10)
    for i in range(len(ml)//2):
        if ml[i] != ml[-(i+1)]:
            ml[i] = ml[-(i+1)]
    return ml[:]
print(polindrom2(1))


#17
def num(dig):
    count = 0
    num1 = dig
    ml = []
    while dig > 0:
        dig = dig//10
        count += 1
    for i in range(0,count):
        a = num1 // 10**i
        ml.append(a%10)
    return ml[0]*ml[-1]
print(num(6234))

#18
def string(ml):
    count = 0
    if len(ml) == 0:
        return None
    for i in ml:
        if type(i) == type(str()):
            count += 1
    return count
mk = [1,2,3,4,5,"djfjf","sjfke"]
print(string(mk))

#19
def mmax(num):
    count = 0
    for i in num:
        if type(i) == type(int()):
            if int(i) > count:
                count = i
    return count
ml = [1,3,44,5,6,72,8,"jjdfjd","efkfjke","kskd"]
print(mmax(ml))

#20
def even(ml):
    mk = []
    for i in ml:
        if type(i) == type(int()):
          if i//100 == 0 and i%2 == 0:
                mk.append(i)
    return mk
ms = [111,21,312,423,532,662,22,55,66,88,"hejhjd",'edjndkj']
print(even(ms))

#21
def mid(ml):
    count = 0
    l = 0
    for i in ml:
        if type(i) == type(int()):
            count += i
            l += 1
    return count /l
mk = [1,2,3,4,5,89,"efkjfje","d","ef"]
print(mid(mk)) 

#22
def string_len(ml):
    count = 0
    mk = []
    for i in ml:
        mk.append(len(i))
    return mk
ms = ["aasd","dwfek","kjfke","dwnkk","knnf"]
print(string_len(ms))

#23
def decraes(ml):
    ms = []
    mw = []
    for i in ml:
        if type(i) == type(int()):
            ms.append(i)
        else:
            mw.append(i)
    ms.sort(reverse=True)
    return ms + mw
mk = [1,2,3,44,5,66,7,"dmnmcd","edfkjfjk","dekkdk"]
print(decraes(mk))

#24
def des_ord(ml):
    ms = []
    md = []
    km = []
    for i in ml:
        if type(i) == type(str()):
            ms.append(i)
        else:
            md.append(i)

    ms.sort(key = len)
    km.extend(ms)
    km.sort(reverse = True,key = len)
    return km+md
mk = [1,2,3,4,"djhfhhjf","jhrjkf","jkjf","djkjd"]
print(des_ord(mk))

#25
def string_list(ml):
    vowel = "aeiyou"
    count = 0
    k = 0
    for i in ml:
        for j in i:
            if j in vowel:
                count += 1
            if count > k:
                k = count
                return i
mg = ["Smdm","jfr","frfraaaa","shjqwekj"]
print(string_list(mg))

#26
def sentence(sen):
    max_word_count = 0
    sentence_with_most_words = ""

    for sentence in sen: 
        words = sentence.split()  # Split the sentence into words
        word_count = len(words)
        
        if word_count > max_word_count:
            max_word_count = word_count
            sentence_with_most_words = sentence
    
    return sentence_with_most_words

print(sentence(["ajshd wdkjjkd dekj", "dghehgaadwd dnedndwdwdwd dkk", "shg fe dgh dh deh"]))

#27

def big_dig(tmp):
    mp = ""
    sm = ""
    for i in tmp:
        if i.isdigit():
            sm += i
        elif sm:
            mp += sm + ","
            sm = ""
    if sm:
        mp += sm + ","
    mp = mp.strip(",")
    lp = mp.split(",")
    m = 0
    for i in lp:
        if int(i) > m:
            m = int(i)
    
    return m
print(big_dig("1223karen 12332, fnkr3456,nrmn2345"))

#28
def man(ml):
    m = 0
    k = {}
    for i in ml:
        for j in i.items():
            if i["age"] > m:
                m = i["age"]
                k = i
    return k
print(man([{"age":21,"name":"Jon"},{"age":23,"name":"Karen"},{"age":43,"name":"Mane"}]))


#29
def student(ml):
    km = []
    lm = []
    for i in ml:
        km.append(list(i.items()))
    km.sort()
    for j in km:
        lm.append(dict(j))

    return lm

print(student([{"point":85,"name":"Karen","the study":"paid"},
               {"point":72,"name":"Marine","the study":"free of charge"},
               {"point":98,"name":"Sergey","the study":"free of charge"}]))
#30
def university(ml):
    km = []
    for i in ml:
        if i["name"]:
            km.append(len(i["name"]))
    km.sort()
    length_word = km[-1]
    for univers in ml :
        if len(univers["name"]) == length_word:
            return univers
        
print(university([{"name":"NPUA Gb","god ":"1967"},
               {"name":"ASUE GB"},
               {"name":"Asue"}]))


