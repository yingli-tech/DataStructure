def insertion_sort(array):
    for index in range(1, len(array)):

        position=index
        temp_value=array[index]
        while position > 0 and array[position -1] > temp_value:
            array[position]=array[position -1]
            position=position -1
        array[position]=temp_value
    return array

list = [65,550,45,35,100,15,10]
print(insertion_sort(list))