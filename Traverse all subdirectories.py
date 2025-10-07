import os

def find_directories(directory):
    # 遍历给定目录下的文件和子目录
    for filename in os.listdir(directory):
        # 构造完整的路径
        full_path = os.path.join(directory, filename)
        # 检查是否是目录，并且排除 "." 和 ".."
        if os.path.isdir(full_path) and filename not in [".", ".."]:
            print(full_path)
            # 递归调用，遍历子目录
            find_directories(full_path)

# 以当前目录为参数，调用 find_directories
find_directories(".")