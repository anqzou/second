import pandas as pd
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import os
import pymysql

# Image data 
Image_clean_file="./PT Vision/clean"
Image_dirty_file="./PT Vision/polluted"
# Load training data
Image_training=[]

#图像正则化
def normalization (image,width,height):
    image_copy = np.copy(image)
    image_normalize = cv.resize(image_copy,(width,height))
    return image_normalize

#热编码1
def file(label):
    classify = [0,1]
    if label =="clean_list":
        classify = [1,0]
    return classify

#热编码2
file1={'clean_list':[1,0],'dirty_list':[0,1]}

#图片整理
def standard_list1():
    Image_clean_file="c:/Users/azou/Downloads/PT Vision/clean"
    Image_dirty_file="c:/Users/azou/Downloads/PT Vision/polluted"
    clean_list=os.listdir(Image_clean_file)
    dirty_list=os.listdir(Image_dirty_file)
    dic={'clean_list':Image_clean_file,'dirty_list':Image_dirty_file}
    dic1={'clean_list':clean_list,'dirty_list':dirty_list}
    standard_list=[]
    for n in ['clean_list','dirty_list']:
        label = n
        for i in range(0,len(dic1[n]),1):
            img=plt.imread(dic[n]+"/"+ dic1[n][i])
           # plt.imshow(normalization(img,300,300))
            standard_list.append([normalization(img,300,300),file1[label]])
            print(file1[label])
           # plt.show()
    return standard_list

#图像处理
def image_processing(standard_list,ii):
    img = standard_list[ii][0]
    imgcrop =img[30:210,20:300]
    gray=cv.cvtColor(imgcrop,cv.COLOR_RGB2GRAY)
    filtered=cv.medianBlur(gray,9)
    shuangbian=cv.bilateralFilter(gray,0,100,0)
    thre1 = cv.threshold(shuangbian,70,130,cv.THRESH_BINARY)
    # plt.imshow(thre1,cmap='gray')
    return thre1

#α参数
def a(thre1):
    pic=thre1[1]
    pic1=pic[80:150,130:230]
    np.sum(pic1)
    a= (np.sum(pic[80:160,50:230])-np.sum(pic1))/np.sum(pic1)
    return a
    
#db connect
def connect_to_db(host,user,password,database):
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=database,
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

#add_data
def add_data(host,user,password,database,a,time):
    connection = connect_to_db(host,user,password,database)
    error = False
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute('insert into test_2(a,time) values(%s,%s)',(a,time))
                connection.commit()
    except:
        connection.rollback()
        error = True
    finally:
        pass