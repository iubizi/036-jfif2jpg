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
            
        file_name = name + '.jpg' # 转换为jpg

        try:
            os.rename(file, file_name) # 改名
        except: # 出现重名问题
            file_name = name + '.new.jpg' # 转换为jpg
            os.rename(file, file_name) # 改名
            
        print(file_name) # 打印名称
            


input() # 看看结果
