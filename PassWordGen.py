import random
import string
print("WELCOME TO PASSWORD GENERATOR")

length=int(input("Enter password length:"))
letters=(input("Include letters(yes or no):")).upper
numbers=(input("Include numbers(yes or no):")).upper
special_char=(input("Include special charachters(yes or no):")).upper
letters_lst=list(string.ascii_letters)
numbers_lst=["1",'2','3','4','5','6','7','8','9','0']
special_char_lst=['!','@','#','$','%','^','&','*']
all=[letters,numbers,special_char]
all_str=["letter","num","char"]
perm=[]
password=[]
for i in range(len(all)):
    if all[i] =='YES':
        perm.append(all_str[i])



print(perm)
for i in range(length):
    select=random.choice(perm)
    if select=="num":
        a=random.randint(0,9)
        password.append(numbers_lst[a])
    if select=='char':
        a=random.randint(0,len(special_char_lst)-1)
        password.append(special_char_lst[a])
    if select=='letter':
        a=random.randint(0,len(letters_lst)-1)
        password.append(letters_lst[a])
print(''.join(password))
