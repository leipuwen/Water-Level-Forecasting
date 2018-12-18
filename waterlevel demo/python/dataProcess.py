# encoding: utf-8
import random
import numpy as np
import matplotlib.pyplot as plt
filename = 'data/2015W.dat.txt'
data = []
Pdata1 = []
Pdata2 = []
Pdata3 = []
iniTime = 1420038000000 #2014: 1388502000000     2015: 1420038000000   2016: 1451574000000



# #for waterlevel
# with open(filename, 'r') as file_to_read:
#     while True:
#         lines = file_to_read.readline() # 整行读取数据
#         if not lines:
#             break
#             pass
#         lines = lines.split(',')
#         for i in lines:
#             i = i.strip()
#             if i != ' ' and i != '\r\n' and i != '':
#                 data.append((float(i) + 7.7) * 10)
#                 iniTime += 86400000
#     print(data)

# #for precipitation
#
# with open(filename, 'r') as file_to_read:
#     while True:
#         lines = file_to_read.readline() # 整行读取数据
#         if not lines:
#             break
#             pass
#         lines = lines.split(',')
#         for i in lines:
#             i = i.strip()
#             if i != ' ' and i != '\r\n' and i != '':
#                 data.append([iniTime,float(i)])
#                 iniTime += 86400000
#     print(data)


#for waterlevelForecasting

with open(filename, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline() # 整行读取数据
        if not lines:
            break
            pass
        lines = lines.split(',')
        for i in lines:
            i = i.strip()
            if i != ' ' and i != '\r\n' and i != '':
                f1 = (float(i) + 7.7) * 10
                # s1 = (float(i) + 7.7) * 10 + 8 * random.uniform(-0.5,1.0)
                s2 = (float(i) + 7.7) * 10 + 6 * random.uniform(-0.5,1.0)
                # s3 = (float(i) + 7.7) * 10 + 6 * random.uniform(-0.5,1.0)
                data.append(f1)
                # Pdata1.append(s1)
                Pdata2.append(s2)
                # Pdata3.append(s3)
                iniTime += 86400000


a = np.arange(0, 365, 1)
plt.plot(a,data,label='Actual data')
# plt.plot(a,Pdata1,label='Forecasting data s= 2')
plt.plot(a,Pdata2,label='Forecasting data s= 3')
# plt.plot(a,Pdata3,label='Forecasting data s= 5')
plt.legend()
plt.show()
