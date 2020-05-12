# image_processing
image processing for classification and object detection
文件夹结构：
```
|-- README.md
`-- utils
    |-- classification
    |   |-- image_resize.py
    |   |-- statistics_classes2plot.py
    |   `-- statistics_image_size.py
    `-- object_detcetion
        |-- calculate_object_number.py
        `-- processing_crop_image.py
```
## classification
### image_resize.py
将文件夹里面的图片归一化到统一尺寸
### statistics_classes2plot.py
统计分类图像的类别文件夹里面每类图片总数目，并将统计结果化成柱状图
### statistics_image_size.py
统计分类图像的类别文件夹里面所有图片尺寸分布
## object_detcetion
### calculate_object_number.py
统计目标检测数据集里面每类数目、大小分布和图片尺寸等
### processing_crop_image
图像滑窗按窗口大小、stride大小、是否padding进行切割保存每一个窗口大小图片
