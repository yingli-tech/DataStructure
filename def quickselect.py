def quickselect(array, kth_lowest_value, left_index, right_index):
    """
    在数组中快速选择第 k 小的元素（基于零的索引）
    
    参数:
        array: 待搜索的列表
        kth_lowest_value: 要查找的第 k 小的元素的索引（从 0 开始）
        left_index: 当前子数组的左边界
        right_index: 当前子数组的右边界
    """
    # 基准情形：子数组只剩一个元素
    if right_index - left_index <= 0:
        return array[left_index]
    
    # 分区操作并返回轴的位置
    pivot_position = partition(array, left_index, right_index)
    
    if kth_lowest_value < pivot_position:
        # 在左半部分递归查找
        return quickselect(array, kth_lowest_value, left_index, pivot_position - 1)
    elif kth_lowest_value > pivot_position:
        # 在右半部分递归查找
        return quickselect(array, kth_lowest_value, pivot_position + 1, right_index)
    else:
        # 找到目标元素
        return array[pivot_position]

def partition(array, left_pointer, right_pointer):
    """
    分区函数（Lomuto 分区方案）
    """
    pivot_index = right_pointer
    pivot_value = array[pivot_index]
    right_pointer -= 1
    
    while True:
        while array[left_pointer] < pivot_value:
            left_pointer += 1
        while array[right_pointer] > pivot_value:
            right_pointer -= 1
        
        if left_pointer >= right_pointer:
            break
        else:
            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]
    
    # 将轴值交换到正确位置
    array[left_pointer], array[pivot_index] = array[pivot_index], array[left_pointer]
    return left_pointer

# 示例用法
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
k = 7  # 查找第 5 小的元素（索引 4，因为从 0 开始）
result = quickselect(arr, k, 0, len(arr) - 1)
print(f"第 {k + 1} 小的元素是: {result}") 