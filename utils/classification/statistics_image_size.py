import os
import sys
import cv2

def statistics_size(path):
    image_size_list = []
    for first_path in os.listdir(path):
        second_path = os.path.join(path,first_path)
        if len(os.listdir(second_path))>0:
            for imgae in os.listdir(second_path):
                image_path = os.path.join(second_path,imgae)
                img = cv2.imread(image_path)
                try:
                    size = img.shape[1],img.shape[0]
                    if size in image_size_list:
                        continue
                    else:
                        image_size_list.append(size)
                except:
                    print("folder in folder！")#文件夹里套文件夹错误
                    print("desktop.ini！")#分类图片里面夹杂desktop.ini文件
                    print("image_path:",image_path)
        else:
            continue
    if len(image_size_list)>1:
        print("error!!!!!!!!!!!!!!!!")
        print("image_size_list:",image_size_list)
    else:
        print("the size is same.............")
        print("image_size_list:",image_size_list)
if __name__ == "__main__":
    path = sys.argv[1]#需要统计图片尺寸的路径，其文件夹第二层就是要分类图像的类别文件夹
    statistics_size(path)