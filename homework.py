"""#4 A Print the number of vowels used in the sentence and D Print the number of consonants used in the sentence.
Sent = input("Enter Sentence: ")
ccount = 0
vcount = 0
vowel = "AaEeIiOoUuYy"

for i in Sent:
    if i in vowel and i.isalpha():
        ccount += 1
    else:
        continue
    if i not in vowel and i.isalpha():
        vcount += 1
print(ccount)
print(vcount)
#4 B Print the sum of the digits used in the sentence.
Sent = input("Enter Sentence: ")
count = 0
for i in Sent:
    if i.isdigit():
        count += int(i)
print(count)

#4 C Print the number of capital letters used in the sentence.
Sent = input("Enter Sentence: ")
count = 0
for i in Sent:
    if i.isupper():
        count += 1
print(count)

#5 Enter words n times, print the longest word entered.

Sent = input("Enter Sentence: ")
word = Sent.split()
length_word = ""
count = 0
for i in word:
    if len(i) > count:
        length_word = i
        count = len(i)
print(length_word)

#6 Enter either a word or a number n times. Print the numbers that end with an even digit.
Sent = input("Enter Sentence: ")
woint = Sent.split()
count = 0
for i in woint:
    if i.isdigit() and int(i)%2==0:
        count = int(i)
        print(count)
    else:
        continue

#1 Enter the numbers n and m. Print the sum of the numbers between n and m.
n = int(input( "Enter number: "))
m = int(input( "Enter number: "))
msum = 0
if n > m:
    n,m = m,n
for i in range(n,m):
    msum += i
print(msum)

#2 Enter the numbers n and m. Print the sum of even numbers between n and m.
n = int(input( "Enter number: "))
m = int(input( "Enter number: "))
msum = 0
if n > m:
    n,m = m,n
for i in range(n,m):
    if i%2==0:
        msum += i
print(msum)

#Polindrom 
mstr = input("Enter sentence: ")
count = ""
kam = mstr.split()
for m in kam:
    if m[::] == m[::-1] and (m.isalpha() or m.isdigit()):
        count = m
        print(count)

"""
word = "sergeI"
k = ""
for i in range(len(word)):
    if 97 >= ord(word[i]) >= 62:
        k += chr(ord(word[i]) + 32)
    else:
        k = word
print(k)
