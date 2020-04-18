import cv2

def processing_crop_image(img, window_size, stride,rate,path,padding=None,resize=None):
    """
    0--------->y
    |
    |
    |
    x
    """
    if (rate[0] != 1) and (rate[1] != 1):
        pass
    else:
        pass
    height, width = img.shape[:2]
    if (height < window_size[1]) or (width < window_size[0]):
        print("error:the window_size over the image!!!")
        return 
    elif (height < stride[1]) or (width < stride[0]):
        print("error:the stride over the image!!!")
        return
    elif (window_size[0] < stride[0]) or (window_size[1] < stride[1]):
        print("error:the stride over the window_size!!!")
        return
    else:
        w0 = (width-window_size[0])%(stride[0])
        h0 = (height-window_size[1])%(stride[1])
        w = (width-window_size[0])//(stride[0]) + 1
        h = (height-window_size[1])//(stride[1]) + 1
        count = 0
        print("!!!!!!!!!!!!!!!")
        print(w,h)
        print(w0,h0)
        if ((w0 == 0) and (h0 == 0)):
            for i in range(w):
                for j in range(h):
                    start_y = j*stride[1]
                    end_y= window_size[1]+start_y
                    start_x = i * stride[0]
                    end_x = window_size[0]+start_x
                    crop_image = img[start_y:end_y,start_x:end_x]
                    cv2.imwrite(path+str(count)+".jpg",crop_image)
                    count += 1
        elif ((w0 == 0) and (h0 != 0)):
            for i in range(w):
                for j in range(h):
                    start_y = j*stride[1]
                    end_y= window_size[1]+start_y
                    start_x = i * stride[0]
                    end_x = window_size[0]+start_x
                    crop_image = img[start_y:end_y,start_x:end_x]
                    cv2.imwrite(path+str(count)+".jpg",crop_image)
                    count += 1
            for j in range(w):
                start_y = height-window_size[1] 
                end_y= height
                start_x = j * stride[0]
                end_x = window_size[0] + start_x
                crop_image = img[start_y:end_y,start_x:end_x]
                cv2.imwrite(path+str(count)+".jpg",crop_image)
                count += 1
        elif ((w0 != 0) and (h0 == 0)):
            for i in range(w):
                for j in range(h):
                    start_y = j*stride[1]
                    end_y= window_size[1]+start_y
                    start_x = i * stride[0]
                    end_x = window_size[0]+start_x
                    crop_image = img[start_y:end_y,start_x:end_x]
                    cv2.imwrite(path+str(count)+".jpg",crop_image)
                    count += 1
            for i in range(h):
                start_y = i * stride[1]
                end_y= window_size[1] + start_y
                start_x = width - window_size[0]
                end_x = width
                crop_image = img[start_y:end_y,start_x:end_x]
                cv2.imwrite(path+str(count)+".jpg",crop_image)
                count += 1
        else:
            for i in range(w):
                for j in range(h):
                    start_y = j*stride[1]
                    end_y= window_size[1]+start_y
                    start_x = i * stride[0]
                    end_x = window_size[0]+start_x
                    crop_image = img[start_y:end_y,start_x:end_x]
                    cv2.imwrite(path+str(count)+".jpg",crop_image)
                    count += 1
            for i in range(h):
                start_y = i * stride[1]
                end_y= window_size[1] + start_y
                start_x = width - window_size[0]
                end_x = width
                crop_image = img[start_y:end_y,start_y:end_y]
                cv2.imwrite(path+str(count)+".jpg",crop_image)
                count += 1
            for j in range(w):
                start_y = height-window_size[1] 
                end_y= height
                start_x = j * stride[0]
                end_x = window_size[0] + start_x
                crop_image = img[start_y:end_y,start_x:end_x]
                cv2.imwrite(path+str(count)+".jpg",crop_image)
                count += 1
            crop_image = img[height-window_size[1]:height,width-window_size[0]:width]
            cv2.imwrite(path+str(count)+".jpg",crop_image)
            count += 1

if __name__ == "__main__":
    """
    path = "./save1/"
    image_path = "E:\\BaiduNetdiskDownload\\test_data\\ruifeng_mac4\\3014\\crop_erro\\20200415133201\\1.jpg"
    img = cv2.imread(image_path)
    # print(img.shape)
    window_size=[2049,5300]
    stride=[2048,5300]
    rate = [1,1]
    processing_crop_image(img, window_size, stride,rate,path)
    """
    import os
    import cv2
    save_path = "E:\\BaiduNetdiskDownload\\test_data\\ruifeng_mac4\\3014\\train"
    target_image_path = "E:\\BaiduNetdiskDownload\\test_data\\ruifeng_mac4\\3014\\zheng-0411"
    window_size=[1664,1664]
    stride=[608,608]
    rate = [1,1]
    for first_folder in os.listdir(target_image_path):
        first_folder_path = os.path.join(target_image_path,first_folder)
        for image in os.listdir(first_folder_path):
            image_path = os.path.join(first_folder_path,image)
            img = cv2.imread(image_path)
            save_name = image.split(".")[0]
            save_path_name = save_path+"/"+first_folder+"_"+save_name+"_"
            print("save_path_name:",save_path_name)
            processing_crop_image(img, window_size, stride,rate,save_path_name)
    print("finished!!!!!!")