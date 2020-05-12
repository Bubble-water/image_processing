import os
import sys
import matplotlib.pyplot as plt
from pylab import *


def statistics(path,save_name="train",title="title",mark=0):
    if not os.path.exists("./images"):#在当前路径下面新建个images文件夹，为了保存统计柱形图图片
        os.mkdir("./images")
    x_label = list()
    y_value = list()
    for first_path in os.listdir(path):
        x_label.append(first_path)
        second_path = os.path.join(path,first_path)
        y_value.append(len(os.listdir(second_path)))
    if mark==0:#是否需要按照类别数量从大到小进行排列，0为需要，其他数为不需要要
        temp = sorted(range(len(y_value)), key=lambda k: y_value[k],reverse=True)
        y_value.sort(reverse=True)
        x_label1 = []
        for i in temp:
            x_label1.append(x_label[i])
        x_label = x_label1
    width =0.4
    plt.figure(figsize=(20, 8), dpi=80) # (20, 8)宽20，高8，dpi设置图片清晰度， 让图片更加清晰
    plt.xticks(arange(len(x_label)), x_label,fontsize=13,rotation=45)
    plt.bar(arange(len(x_label)),y_value,width,color='b')
    x1 = arange(len(x_label))
    for a,b in zip(x1,y_value):
        plt.text(a,b+0.05,'%d'% b,ha='center',va= 'bottom',fontsize=20)
    plt.title(title,color='r',fontsize=20)
    plt.xlabel('class',color='r',fontsize=20)
    plt.ylabel('value',color='r',fontsize=20)
    plt.yticks(fontsize=15)#y刻度值数字显示大小
    plt.ylim(0,max(y_value)+20)#y轴范围
    plt.tight_layout()
    plt.savefig('images/%s.png'%save_name, format='png')
    # plt.show()

if __name__ == "__main__":
    path = sys.argv[1]##需要统计图片的路径，其文件夹第二层就是要分类图像的类别文件夹
    save_name = sys.argv[2]#统计可视化的图片名称，自己起个名字
    title = sys.argv[3]#图的title
    mark = sys.argv[4]#是否需要按照类别数量从大到小进行排列，0为需要，其他数为不需要要
    statistics(path,save_name,title,int(mark))