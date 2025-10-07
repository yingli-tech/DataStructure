def insert_sort(list):
    length = len(list)
    for index in range(1, length):
        temp = list[index]   # store the current element
        position = index - 1
        while position >= 0 and list[position] > temp:
            list[position+1]= list[position]
            position -= 1
        list[position+1] = temp  # Please note that this variable has been minused by 1 in the while loop after finishing the movement. So we need to add 1 to compensate it
        print(list)
    return list
list = [65,550,45,35,100,15,10]
print(insert_sort(list))

