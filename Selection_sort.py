def Selection_Sort(list):
    for i in range(len(list)-1):
        smallest = i
        for j in range(i+1,len(list)):
            if list[j] < list[smallest]:
                smallest = j
                list[i],list[smallest] = list[smallest],list[i]

list = eval(input("Enter a list:"))

Selection_Sort(list)
print('List after sorting is : ', end='')
print(list)


