def select_sort(list):
    lowestNumberIndex = 0
    sorted_until_length = len(list)-1
    for j in range(sorted_until_length):
        a = list[j]
        lowestNumberIndex = j #initialize the lowestNumberIndex to the current index 
        for i in range(sorted_until_length - j):
            if list[i+1+j] < a:
                lowestNumberIndex = i + j +1
                a = list [i+1+j]          
        if lowestNumberIndex != j:
            print("this value of j is:",j)
            print("the value of lowestNumberIndex is:",lowestNumberIndex)
            list[j],list[lowestNumberIndex] = list[lowestNumberIndex],list[j],
        print("the temporary list is:",list)
list = [65,55,45,200,100,15,10]
list2 = [36,55,38,69,37,10,15,10,45,200,100,15,10]
select_sort(list2)
print(list2)
