# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:35:57 2019
@author: Melo705
"""
import pandas as pd
import numpy as np
#Read data
Raw_data=pd.read_excel(r'C:\Users\201810\Desktop\机器学习数据集\1.xls',sheet_name='Sheet1',index_col=None)
Raw_data=Raw_data.values#取值，且转化为二维数组
data=np.array(Raw_data)#二维数组(矩阵) 这里的np.array()是为了下面使用numpy包，转化为nummpy数据标准 ,并不改变维度
(m,n)=Raw_data.shape #矩阵的行数m列数n，返回一个元组
 
def entropy(vector,segnment): #自定义一个求解信息熵的函数，vector为向量，segment分段数值
    x_min=np.min(vector)
    x_max=np.max(vector)
    x_dis=np.abs(x_max-x_min)
    x_lower=x_min
    seg=1.0/segnment
    ternal=x_dis*seg
    list1=[]
    List1=[]
    #
    for i in range(len(vector)):
        if vector[i]>=x_lower+ternal:
            list1.append(vector[i])
    len_list1=len(list1)
    List1.append(len_list1)
    #
    for j in range(1,segnment):
        list1=[]
        for i in range(len(vector)):
            if vector[i]>=x_lower+j*ternal and vector[i]<x_lower+(j+1)*ternal:
                list1.append(vector[i])
        len_list1=len(list1)
        List1.append(len_list1)
    #
    list1=[]
    for i in range(len(vector)):
        if vector[i]>=x_lower+(segnment-1)*ternal :
            list1.append(vector[i])
    len_list1=len(list1)
    List1.append(len_list1)
    List1=List1/np.sum(List1) 
    
    y=0
    Y=[]
    for i in range(segnment):
        if List1[i]==0:
            y=0
            Y.append(y)
        else:
            y=-List1[i]*np.log2(List1[i]);
            Y.append(y)
    result=np.sum(Y) 
    return result
 
#数据预处理
data_feature=np.zeros(shape=(6,n)) #特征二维数组(矩阵)的初始化 np.zeros(shape=(行，列))
for i in range(n):
    data_ave=np.mean(data[:,i])
    data_std=np.std(data[:,i],ddof=1)
    for j in range(1,m-1): #基于拉伊达准则的数据异常值处理
        if np.abs(data[j,i])>3*data_std:
            data[j,i]=0.5*(data[j-1][i]+data[j+1][i])
        else:
           continue
    data_ave=np.mean(data[:,i]) #均值
    data_std=np.std(data[:,i]) #标准差
    data_max=np.max(data[:,i]) #最大值
    data_min=np.min(data[:,i]) #最小值
    data_energy=np.sum(np.abs(data[:,i])) #能量：数据绝对值之和表示能量
    data_normal = (data[:,i]-data_min) / (data_max-data_min)#数据归一化(0,1)
    segnment=int(0.5*m);
    data_etropy=entropy(data_normal,segnment)#信息熵
    data_feature[:,i]=[data_ave,data_std,data_max,data_min,data_energy,data_etropy]#特征二维数组
 
#写入数据
data_f = pd.DataFrame(data_feature)#写入数据
data_f.columns = ['Ax','Ay','Az','Gx','Gy','Gz','Mx','My','Mz']#列标题
data_f.index = ['ave','std','max','min','energy','entropy']#行标题
writer = pd.ExcelWriter(r'C:\Users\201810\Desktop\机器学习数据集\f1.xls')#写入路径
data_f.to_excel(writer,'data_feature',float_format='%.2f') # data_feature为sheet名，float_format 数值精度
writer.save()#保存
       
     
            