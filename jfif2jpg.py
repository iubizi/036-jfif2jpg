import os

files = os.listdir()
# print(files)

for file in files:
    
    suffix = file.split('.')[-1] # 提取后缀
    if suffix == 'jfif' or suffix == 'JFIF':
        
        name_list = file.split('.')[:-1]
        name = ''
        for i in name_list:
            name += i # 还原名字
            
        name = name + '.jpg' # 转换为jpg
        os.rename(file, name) # 改名
        print(name) # 打印名称


