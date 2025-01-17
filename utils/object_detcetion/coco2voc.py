# @TIME  :2019/7/21 15:34
# @File  :coco2xml.py
"""从coco instance.json生成voc--xml文件"""
 
"""
首先得下载编译cocoapi
pip install cython
git clone https://github.com/cocodataset/cocoapi.git
cd coco/PythonAPI
make
"""
 
import sys
bag_path = "../cocoapi-master/PythonAPI/"
if not bag_path in sys.path:
    sys.path.append(bag_path)
 
from pycocotools.coco import COCO
import os
import shutil
from tqdm import tqdm
import skimage.io as io
import matplotlib.pyplot as plt
import cv2
from PIL import Image, ImageDraw
 
# the path you want to save your results for coco to voc
savepath = "../result/"#保存生成文件路径
img_dir = savepath + 'images/'#保存生成jpg文件路径
anno_dir = savepath + 'Annotations/'#保存生成xml文件路径
# datasets_list=['train2014', 'val2014']
datasets_list = ['train2017']#coco数据集里面图片
 
# Store annotations and train2014/val2014/... in this folder
dataDir = '../../coco/coco2017/'#coco数据集整体文件，里面包含annotations和图片文件夹
#path = os.path.abspath(dataDir)
#print(path)
 
headstr = """\
<annotation>
    <folder>VOC</folder>
    <filename>%s</filename>
    <source>
        <database>My Database</database>
        <annotation>COCO</annotation>
        <image>flickr</image>
        <flickrid>NULL</flickrid>
    </source>
    <owner>
        <flickrid>NULL</flickrid>
        <name>company</name>
    </owner>
    <size>
        <width>%d</width>
        <height>%d</height>
        <depth>%d</depth>
    </size>
    <segmented>0</segmented>
"""
objstr = """\
    <object>
        <name>%s</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>%d</xmin>
            <ymin>%d</ymin>
            <xmax>%d</xmax>
            <ymax>%d</ymax>
        </bndbox>
    </object>
"""
 
tailstr = '''\
</annotation>
'''
 
 
# if the dir is not exists,make it,else delete it
def mkr(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)
 
 
mkr(img_dir)
mkr(anno_dir)
 
 
def id2name(coco):
    classes = dict()
    for cls in coco.dataset['categories']:
        classes[cls['id']] = cls['name']
    return classes
 
 
def write_xml(anno_path, head, objs, tail):
    f = open(anno_path, "w")
    f.write(head)
    for obj in objs:
        f.write(objstr % (obj[0], obj[1], obj[2], obj[3], obj[4]))
    f.write(tail)
 
 
def save_annotations_and_imgs(coco, dataset, filename, objs):
    # eg:COCO_train2014_000000196610.jpg-->COCO_train2014_000000196610.xml
    anno_path = anno_dir + filename[:-3] + 'xml'
    img_path = dataDir + dataset + '/' + filename
    #print(img_path)
    dst_imgpath = img_dir + filename
 
    img = cv2.imread(img_path)
    if (img.shape[2] == 1):
        #print(filename + " not a RGB image")
        return
    shutil.copy(img_path, dst_imgpath)
 
    head = headstr % (filename, img.shape[1], img.shape[0], img.shape[2])
    tail = tailstr
    write_xml(anno_path, head, objs, tail)
 
 
def showimg(coco, dataset, img, classes, cls_id, show=True):
    global dataDir
    I = Image.open('%s/%s/%s' % (dataDir, dataset, img['file_name']))
    # 通过id，得到注释的信息
    annIds = coco.getAnnIds(imgIds=img['id'], catIds=cls_id, iscrowd=None)
    # print(annIds)
    anns = coco.loadAnns(annIds)
    # print(anns)
    # coco.showAnns(anns)
    objs = []
    for ann in anns:
        class_name = classes[ann['category_id']]
        if 'bbox' in ann:
            bbox = ann['bbox']
            xmin = int(bbox[0])
            ymin = int(bbox[1])
            xmax = int(bbox[2] + bbox[0])
            ymax = int(bbox[3] + bbox[1])
            obj = [class_name, xmin, ymin, xmax, ymax]
            objs.append(obj)
            draw = ImageDraw.Draw(I)
            draw.rectangle([xmin, ymin, xmax, ymax])
    if show:
        plt.figure()
        plt.axis('off')
        plt.imshow(I)
        plt.show()
 
    return objs
 
 
for dataset in datasets_list:
    # ./COCO/annotations/instances_train2014.json
    annFile = '{}/annotations/instances_{}.json'.format(dataDir, dataset)
 
    # COCO API for initializing annotated data
    coco = COCO(annFile)
    '''
    COCO 对象创建完毕后会输出如下信息:
    loading annotations into memory...
    Done (t=0.81s)
    creating index...
    index created!
    至此, json 脚本解析完毕, 并且将图片和对应的标注数据关联起来.
    '''
    # show all classes in coco
    classes = id2name(coco)
 
    classes_names = []
    for key, value in classes.items():
        classes_names.append(value)
 
    classes_ids = coco.getCatIds(catNms=classes_names)
    img_ids_totoal =[]
    for cls in classes_names:
        # Get ID number of this class
        cls_id = coco.getCatIds(catNms=[cls])
        img_ids = coco.getImgIds(catIds=cls_id)
        for img_id in img_ids:
            img_ids_totoal.append(img_id)
    print(len(img_ids_totoal))
    tem=set(img_ids_totoal)
    temp = list(tem)
    temp.sort()
    print(len(tem))
    print(len(temp))
    for imgId in tqdm(temp):
        img = coco.loadImgs(imgId)[0]
        filename = img['file_name']
        # print(filename)
        objs = showimg(coco, dataset, img, classes, classes_ids, show=False)
        # print(objs)
        save_annotations_and_imgs(coco, dataset, filename, objs)