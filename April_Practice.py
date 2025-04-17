#Sortlist
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
# print("---")
# thislist = [100, 50, 65, 82, 23]
# thislist.sort() #sort nay la sap xep 
# print(thislist)
# print("---")
# x = 1
# while x < 100:
#    print(x)
#    x = x*2
# print("---")
# x = 1
# i = 0
# while x < 100:
#    if i == 5:
#        break
#    print(i, x)
#    x = x*2
#    i += 1
# print("---")
# i = 0
# while i < 10:
#     if i % 3 != 0:
#         print(i)
#         i += 1
#         continue
#     i += 1
from time import sleep
n = 10
while n>=0:
    if n== 5:
        print('Place your reservation soon! 5 minutes remaining')
    elif n== 2:
        print("Don't lose your seats! 2 minutes remaining")
    elif n== 0:
        print("User timed out")
    else:
        print(n)
    sleep(1)
    n = n-1

from time import sleep

print("Get ready...")
sleep(1)  # waits 2 seconds
print("Go!")