class SortableArray:
    def __init__(self, array):
       # 使数据存储在 变量名.array 属性中，这是整个类的初始化
        self.array = array

    def partition(self, left_pointer, right_pointer):
        # 总是取最右的值作为轴
        pivot_position = right_pointer
        pivot = self.array[pivot_position]
        # 将右指针指向轴左边的一格
        right_pointer -= 1
        count_left = 0
        count_right = 0
        while True:
            while self.array[left_pointer] < pivot:
                left_pointer += 1
                count_left += 1
                print("currently the count_left is ", count_left)
            while self.array[right_pointer] > pivot:
                right_pointer -= 1
                count_right += 1
                print("currently the count_right is ", count_right)
            if left_pointer >= right_pointer:
                break
            else:
                self.swap(left_pointer, right_pointer)
                print("the count_left is ", count_left)
                print("the count_right is ", count_right)


        # 最后将左指针的值与轴交换
        self.swap(left_pointer, pivot_position)
        # 返回左指针的位置（用于快速排序）
        return left_pointer

    def swap(self, pointer_1, pointer_2):
        # 交换两个指针位置的值
        self.array[pointer_1], self.array[pointer_2] = self.array[pointer_2], self.array[pointer_1]

    def quicksort(self, left_index, right_index):
    # 基准情形：分出的子数组长度为0或1
        if right_index - left_index <= 0:
            return
    
    # 将数组分成两部分，并返回分隔所用的轴的索引
        pivot_position = self.partition(left_index, right_index)
    
    # 对轴左侧的部分递归调用quicksort
        self.quicksort(left_index, pivot_position - 1)
    
    # 对轴右侧的部分递归调用quicksort
        self.quicksort(pivot_position + 1, right_index)

# 1. 创建 SortableArray 实例，初始化数组
arr = [0, 5, 45, 11, 25, 100,65, 85, 2, 1, 7,6, 3]
sortable_array = SortableArray(arr)
sortable_array.quicksort(0, len(sortable_array.array) - 1)
print("分区后的数组:", sortable_array.array)  