from gettext import install
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import os
import function as fu
import datetime
from time import sleep
import pymysql.cursors


def main():
    # Load training data
    Image_training=[]
    #standard images list
    standard_list=fu.standard_list1()
    #for ii in range(0,len(standard_list)-1,1):
        #treated images
    for ii in range(0,len(standard_list)-1,1):
        ther1=fu.image_processing(standard_list,ii)
        #a parameters
        a1=fu.a(ther1)
        #connect to db
        host='pvg03s1dtpdb001.cb2.pvg03.tzla.net'
        user='dtpadmin'
        password='T*5t4J&KCrDqabFb'
        database='zaqtest'
        fu.connect_to_db(host,user,password,database)
        time=datetime.datetime.now()
        fu.add_data(host,user,password,database,a1,time)
    sleep(10)
if __name__=="__main__":
    main()


