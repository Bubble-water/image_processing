import os
import sys
import cv2


def resize_image(path,width,height,save_path):
    """
    将path路径下面的图片
    """
    for first_path in os.listdir(path):
        second_path_save = os.path.join(save_path,first_path)
        if not os.path.exists(second_path_save):
            os.mkdir(second_path_save)
        second_path = os.path.join(path,first_path)
        if len(os.listdir(second_path))>0:
            for imgae in os.listdir(second_path):
                image_path = os.path.join(second_path,imgae)
                image_path_save = os.path.join(second_path_save,imgae)
                try:
                    img = cv2.imread(image_path)
                    img = cv2.resize(img, (width,height), interpolation=cv2.INTER_AREA)#调用cv2的cv2.INTER_AREA rezie方法
                    cv2.imwrite(image_path_save,img)
                except:
                    print("folder in folder！")#文件夹里套文件夹错误
                    print("desktop.ini！")#分类图片里面夹杂desktop.ini文件
                    print("image_path:",image_path)
        else:
            continue
    print("finished!!!!!!!")
if __name__ == "__main__":
    path = sys.argv[1]#需要resize图片的路径，其文件夹第二层就是要分类图像的类别文件夹
    width = sys.argv[2]#resize的宽
    height = sys.argv[3]#resize的高
    save_path = sys.argv[4]#resize图片保存的路径，save_path文件夹必须存在
    resize_image(path,int(width),int(height),save_path)