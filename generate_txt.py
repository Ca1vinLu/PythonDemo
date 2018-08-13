import os


def create_file(file_name_prefix, length):
    if length == 1:
        for i in range(ord('a'), ord('z') + 1):
            try:
                file = open(folder_name + file_name_prefix + chr(i) + '.txt', 'w+')
                file.write('hello')
                file.close()
            except Exception as e:
                print(e)
    elif length > 1:
        for i in range(ord('a'), ord('z') + 1):
            create_file(file_name_prefix + chr(i), length - 1)


folder_name = 'C:\\PythonProject\\PythonDemo\\files\\'
# print('请输入路径：')
# folder_name = input()
folder = os.path.exists(folder_name)
if not folder:
    os.mkdir(folder_name)
create_file('', 3)
