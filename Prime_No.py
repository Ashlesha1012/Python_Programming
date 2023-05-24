
# for Number in range (1, 101):
#     count = 0
#     for i in range(2, (Number//2 + 1)):
#         if(Number % i == 0):
#             count = count + 1
#             break

#     if (count == 0 and Number != 1):
#         print(" %d" %Number, end = '  ')

def Prime(first,last):
    for number in range(first,last+1):
        if number>1:
            for i in range(2,(number//2)+1):
                if number % i == 0:
                    break
            else:
                print(number,end=" ")
Prime(1,100)