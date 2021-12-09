# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 02:48:23 2021

@author: cpslab Jerry Shih
"""
import os
import random
# from PIL import Image
import argparse
import time
from rembg.bg import remove
import numpy as np
import io
from PIL import Image,ImageFile,ImageDraw,ImageFilter
from rembg.bg import remove
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"
def readlabel(labeltxt):
    d = {}
    with open(labeltxt) as f:
        for line in f:
           (key, val) = line.split()
           d[int(key)] = val
    return d

def get_key(dict,value):
    return [k for k,v in dict.items() if v == value]

def remove_background(path):
    
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    f = np.fromfile(path)
    result = remove(f)
    img = Image.open(io.BytesIO(result)).convert("RGBA")
    # img.save(output_path)
    return img

def remove_white(img):
    newImage = []
    for item in img.getdata():
        if item[:3] == (255, 255, 255):
            newImage.append((255, 255, 255, 0))
        else:
            newImage.append(item)
    
    img.putdata(newImage)
    return img
    

if __name__ == '__main__':
    #args = parse_args()    
    # print('Called with args:')
    # print(args)
    
    
    #label = args.label
    
    # save_data_file = "C:/Users/cpslab/Desktop/my_img_label_tool/data"
    save_data_file = "./data"
    data_txt_file = "/txt/"
    data_img_file = "/img/"
    label_file = "./object/"
    BG_path  = "./background"
    
    # label = "white"
    
    dic = readlabel("labels.txt")
    
       
    
    label_list = os.listdir(label_file)
    # obj_list=os.listdir(Obj_path)
    bg_list=os.listdir(BG_path)
    
    #_obj_list = random.sample(obj_list,args.obj_num)  #隨機物件
    _bg_list  = random.sample(bg_list ,10)  #隨機背景
    
    count = 0
    # for obj in _obj_list:
    #     for bg in _bg_list:
    for labels in label_list:
        Obj_path = "./object/"+labels
        obj_list=os.listdir(Obj_path)
        key_label = get_key(dic,labels) 
        for obj in obj_list:
            for bg in _bg_list:
            # try:
                # obj_img = cv2.imread(obj)
                # bg_img  = cv2.imread(bg)
                obj_img = remove_background(Obj_path+"/"+obj)
                
                bg_img = Image.open(BG_path+"/"+bg)
                bg_img = bg_img.resize((1024, 720))
                zoom_factor = 1 # 除與1不變 除與2為原圖一半
                
                #===============去背==================
                # bg_img = remove_background(bg_img)

                #=====================================
                
                bg_img = bg_img.convert("RGBA")
                
                obj_w,obj_h = obj_img.size
                # print("物件長寬:",obj_img.size)
                bg_w,bg_h   =  bg_img.size
                # print("背景長寬:",bg_img.size)
                
                con_img_w = int(bg_w/zoom_factor)
                con_img_h = int(bg_h/zoom_factor)  
                
                re_obj_w = round(obj_w/random.uniform(0.2,1))
                re_obj_h = round(obj_h/random.uniform(0.2,1))
                
                if re_obj_w > con_img_w:
                    re_obj_w = con_img_w
                if re_obj_h > con_img_h:
                    re_obj_h = con_img_h
                
                
                
                icon = obj_img.resize((
                    re_obj_w,re_obj_h),Image.ANTIALIAS)
                
                
                # icon = remove_white(icon)
                
                # icon.show(icon)
                # if re_obj_w < (con_img_w-re_obj_w):
                #     w_rand_start = round((re_obj_w)/2)
                #     w_rand_end = round((con_img_w-re_obj_w)/2)
                # else:
                #     w_rand_end = round((re_obj_w)/2)
                #     w_rand_start = round((con_img_w-re_obj_w)/2)
                    
                # if re_obj_h < (con_img_h-re_obj_h):
                #     h_rand_start = round((re_obj_h)/2)
                #     h_rand_end = round((con_img_h-re_obj_h)/2)
                # else:
                #     h_rand_end = round((re_obj_h)/2)
                #     h_rand_start = round((con_img_h-re_obj_h)/2)
                    
                # coor_x = random.randint(w_rand_start,w_rand_end)
                # coor_y = random.randint(h_rand_start,h_rand_end)
                
                coor_x = random.randint(0,round((con_img_w-re_obj_w)))
                coor_y = random.randint(0,round((con_img_w-re_obj_h)))
                
                coordinate = (coor_x,coor_y)
                # xmin = coor_x - re_obj_w/2
                # ymin = coor_y - re_obj_h/2
                # xmax = coor_x + re_obj_w/2
                # ymax = coor_y + re_obj_h/2
                xmin = coor_x 
                ymin = coor_y
                xmax = coor_x + re_obj_w
                ymax = coor_y + re_obj_h
                
                
                #===pil 貼上======
                #新建一個透明的底圖
                resultPicture = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
                #把照片貼到底圖
                
                
                resultPicture.paste(bg_img,(0,0))
                resultPicture.paste(icon,coordinate,icon)
                
                #++++++++++++++++test
                # img1 = ImageDraw.Draw(resultPicture)  
                # img1.rectangle(((xmin,ymin),(xmax,ymax)),fill=None,outline=(255,0,0))
                # resultPicture.show()
                #++++++++++++++++
                
                
                # key_label = key_label[0]
                #===============================================
                ms = time.time()
                ms = int(ms)
                save_img =save_data_file+ data_img_file + str(key_label[0])+"_"+str(ms)+".png"
                resultPicture.save(save_img)
                
                with open(save_data_file+data_txt_file+str(key_label[0])+"_"+str(ms)+".txt", 'a') as f:
                    f.write( str(key_label[0]) + ' ' +
                              str(xmin) + ' ' +
                              str(ymin) + ' ' +
                              str(xmax) + ' ' +
                              str(ymax) + ' \n' )
                count = count + 1
    print("generate "+str(count)+" images")
            # except:
            #     continue
