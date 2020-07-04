import os


# 将文件夹名字中的 ". " 替换为 "_". 例如："01. Folder1" --> "01_Folder1"
def rename_folder(path):
    file_list = os.listdir(path)
    # print(path)

    count = 0  # 记录有几个文件发生替换
    for i, name in enumerate(file_list):
        sub_path = path + "/" + name
        if os.path.isdir(sub_path):
            new_path = sub_path.replace(". ", "_", 1)
            if new_path != sub_path:
                count = count + 1
                print("    ---- rename dir: \t" + sub_path + "\t --> " + new_path)
                os.rename(sub_path, new_path)
            rename_folder(new_path)
        else:
            continue

    if count > 0:
        print(path + ": 替换" + str(count) + "/" + str(len(file_list)) + "\n")


rename_folder("D:/01_Software")
