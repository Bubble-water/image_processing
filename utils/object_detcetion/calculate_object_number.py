import os
import sys
import json
import pandas as pd
import seaborn as sns
from pylab import arange
import xml.dom.minidom
import matplotlib.pyplot as plt


def calculate_object_number_xml(xml_path):
    """
    xml_path:xml的路径
    """
    object_dict = {}
    for file_name in os.listdir(xml_path):
        if not file_name.endswith("xml"):
            continue
        xmlfile_path = os.path.join(xml_path,file_name)
        DomTree = xml.dom.minidom.parse(xmlfile_path)
        annotation = DomTree.documentElement
        objectlist = annotation.getElementsByTagName('object')
        for objects in objectlist:
            namelist = objects.getElementsByTagName('name')
            objectname = namelist[0].childNodes[0].data
            if objectname in object_dict:
                object_dict[objectname] += 1
            else:
                object_dict[objectname] = 1
    return object_dict


def calculate_object_number_json(json_path):
    """
    json_path:annotations.json的路径
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family']='sans-serif'
    plt.rcParams['figure.figsize'] = (10.0, 10.0)
    with open(json_path) as f:
        json_file = json.load(f)
    """
    print('标签类别:')
    print('类别数量：',len(json_file['categories']))
    print(json_file['categories'])
    print('训练集图片数量：',len(json_file['images']))
    print('训练集标签数量：',len(json_file['annotations']))
    """
    """
    total=[]
    for img in json_file['images']:
        hw=(img['height'],img['width'])
        total.append(hw)
    unique=set(total)
    for k in unique:
        print('长宽为(%d,%d)的图片数量为：'%k,total.count(k))
    """
    ##创建类别标签字典
    category_dic=dict([(i['id'],i['name']) for i in json_file['categories']])
    # print("category_dic:",category_dic)
    counts_label=dict([(i['name'],0) for i in json_file['categories']])
    for i in json_file['annotations']:
        counts_label[category_dic[i['category_id']]]+=1
    # print("counts_label:",counts_label)
    return counts_label

def statistics_classes2plot(object_dict,save_name,title,mark=0):
    if not os.path.exists("./images_picture"):#在当前路径下面新建个images文件夹，为了保存统计柱形图图片
        os.mkdir("./images_picture")
    x_label = list()
    y_value = list()
    for key,value in object_dict.items():
        x_label.append(key)
        y_value.append(value)
    if mark==0:#是否需要按照类别数量从大到小进行排列，0为需要，其他数为不需要要
        temp = sorted(range(len(y_value)), key=lambda k: y_value[k],reverse=True)
        y_value.sort(reverse=True)
        x_label1 = []
        for i in temp:
            x_label1.append(x_label[i])
        x_label = x_label1
    width =0.4
    plt.figure(figsize=(20, 8), dpi=80) # (20, 8)宽20，高8，dpi设置图片清晰度， 让图片更加清晰
    plt.xticks(arange(len(x_label)), x_label,fontsize=20,rotation=45)
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
    plt.savefig('images_picture/%s.png'%save_name, format='png')

if __name__ == "__main__":
    # xml_path = sys.argv[1]
    """
    xml_path = "E:\\BaiduNetdiskDownload\\test_data\\ruifeng_mac1\\yolo\\mydigit\\Annotations"
    object_dict = calculate_object_number_xml(xml_path)
    print("object_dict:",object_dict)
    save_name = "xml"
    title = "xml_object"
    statistics_classes2plot(object_dict,save_name,title)
    """
    json_path = "D:\\download\\chongqing1_round1_train1_20191223\\chongqing1_round1_train1_20191223\\annotations.json"
    counts_label = calculate_object_number_json(json_path)
    print("counts_label:",counts_label)
    save_name = "json"
    title = "json_object"
    statistics_classes2plot(counts_label,save_name,title)