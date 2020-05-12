# @TIME  :2019/7/20 21:48
# @File  :voc2csv.py
"""将voc转化为csv文件作为中间中间转化体 """
 
 
 
import os
import xml.dom.minidom
path_img = "../vocdata/JPEGImages"
path_xml = "../vocdata/Annotations"
 
xml_list = []
for xml1 in os.listdir(path_xml):
    if xml1.endswith(".xml"):
        xml_list.append(xml1)
 
csv_labels = open("csv_labels.csv","w")
for xml_file in xml_list:
    print(xml_file)
    image, ext = os.path.splitext(xml_file)
    abspath_img = os.path.abspath(path_img + "/"+image+".jpg")
 
    DomTree = xml.dom.minidom.parse(path_xml+"/"+xml_file)
    annotation = DomTree.documentElement
    objectlist = annotation.getElementsByTagName('object')
    for objects in objectlist:
        namelist = objects.getElementsByTagName('name')
        #print("namelist:", namelist)
        objectname = namelist[0].childNodes[0].data
        print("abspath:", abspath_img)
        print("objectname:", objectname)
        bndbox = objects.getElementsByTagName('bndbox')
        for box in bndbox:
            x1_list = box.getElementsByTagName('xmin')
            x1 = int(x1_list[0].childNodes[0].data)
            y1_list = box.getElementsByTagName('ymin')
            y1 = int(y1_list[0].childNodes[0].data)
            x2_list = box.getElementsByTagName('xmax')
            x2 = int(x2_list[0].childNodes[0].data)
            y2_list = box.getElementsByTagName('ymax')
            y2 = int(y2_list[0].childNodes[0].data)
            print(x1,y1,x2,y2)
        csv_labels.write(abspath_img + "," + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2) + "," + objectname + "\n")
 
csv_labels.close()