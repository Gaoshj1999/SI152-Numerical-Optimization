# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 00:14:11 2020

@author: duola
"""
"""
本程序实现了测试数据到在ampl中运行模型所需数据格式的转化，并以excel格式输出
"""
file=open("1.txt", "r") 
data=file.readline().split(" ") # 读取文件
print(data)
requests=int(data[1].strip("Orders="))
riders=int(data[2].strip("Vehicles="))
trip=[]#可行的request搭配，原key
triplen=0
rider=[]#每个rider有那些可以接受的trip
cost=[]
exist=[]#request是否在trip当中
requestintrip=[]#含requestj的订单
tripbyriders=[]#能负责trip的rider编号(原key-1)
for i in range(riders):
    rider.append([])
    cost.append([])
for i in range(requests):
    exist.append([])
for i in range(requests):
    requestintrip.append([])
for line in file.readlines():
    temptriplen=triplen
    line=line.strip("\n")
    line=line.split("\t")  #去掉列表中每一个元素的换行符
    line1=line[1].split(",")
    if len(line1)==1:
        if int(line1[0]) not in trip:
            trip.append(int(line1[0]))
            triplen+=1
    elif len(line1)==2:
        if (int(line1[0]),int(line1[1])) not in trip:
            trip.append((int(line1[0]),int(line1[1])))
            triplen+=1 
    line2=int(line[2])
    rider[line2-1].append(len(trip)-1)#rider(key)号有order(key)号订单
    line3=float(line[3])
    cost[line2-1].append(line3)
    #也即均是-1的
    if triplen>temptriplen:
        tripbyriders.append([line2-1])
    else:
        tripbyriders[triplen-1].append(line2-1)
for i in range(len(trip)):
    if type(trip[i])==int:
        requestintrip[trip[i]-1].append(i)
    else:
        requestintrip[trip[i][0]-1].append(i)
        requestintrip[trip[i][1]-1].append(i)
for i in range(len(exist)):
    for j in range(len(trip)):
        exist[i].append(0)
for j in range(len(trip)):
    if type(trip[j])==int:
        exist[trip[j]-1][j]=1
    if type(trip[j])==tuple:
        exist[trip[j][0]-1][j]=1
        exist[trip[j][1]-1][j]=1

"""
import xlwt
count=0
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("riderstrip")
for i in range(len(rider)):
    sheet.write(count,0,"trip[rider["+str(i+1)+"]]")
    for j in range(len(rider[i])):
        sheet.write(count,j+1,"trip"+str(rider[i][j]+1)) # row, column, value
    count+=1
workbook.save('riderstrip.xls')
"""
"""
import xlwt
count=0
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("riderstrip")
for i in range(len(rider)):
    sheet.write(count,0,"set trip[rider"+str(i+1)+"]:=")
    for j in range(len(rider[i])):
        if j==len(rider[i])-1:
            sheet.write(count,j+1,"trip"+str(rider[i][j]+1)+";")
        else:
            sheet.write(count,j+1,"trip"+str(rider[i][j]+1))# row, column, value
    count+=1
workbook.save('riderstrip.xls')
"""
"""
import xlwt
count=0
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("cost")
for i in range(len(rider)):
    sheet.write(count,1,"rider["+str(i+1)+"]")
    count+=1
    for j in range(len(rider[i])):
        sheet.write(count+j,0,"trip"+str(rider[i][j]+1)) # row, column, value
        sheet.write(count+j,1,cost[i][j])
    count+=len(rider[i])
workbook.save('cost.xls')
"""
"""
import xlwt
count=0
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("cost")
sheet.write(count,0,"param cost :=")
for i in range(len(rider)):
    sheet.write(count,1,"[rider"+str(i+1)+",*]:=")
    count+=1
    for j in range(len(rider[i])):
        sheet.write(count+j,0,"trip"+str(rider[i][j]+1)) # row, column, value
        sheet.write(count+j,1,cost[i][j])
    count+=len(rider[i])
workbook.save('cost.xls')
"""
"""
import xlwt
count=0
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("exist")
for j in range(len(trip)):
    sheet.write(count,j+1,"trip"+str(j+1)) # row, column, value    
count+=1
for i in range(requests):
    sheet.write(count,0,"request["+str(i+1)+"]")
    for j in range(len(trip)):   
        sheet.write(count,j+1,exist[i][j])
    count+=1
workbook.save('exist.xls')
"""
"""
import xlwt
count=0
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("exist")
sheet.write(0,0,"param:")
for j in range(len(trip)):
    if j==len(trip)-1:
        sheet.write(count,j+1,"trip"+str(j+1)+":=") # row, column, value    
    else:
        sheet.write(count,j+1,"trip"+str(j+1)) # row, column, value  
count+=1
for i in range(requests):
    sheet.write(count,0,"request"+str(i+1))
    for j in range(len(trip)):   
        sheet.write(count,j+1,exist[i][j])
    count+=1
workbook.save('exists.xls')
"""
"""
import xlwt
count=0
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Trip")
sheet.write(count,0,"Trip") # row, column, value    
for i in range(len(trip)):
    sheet.write(count,i+1,"trip"+str(i+1))
workbook.save('Trip.xls')
"""
"""
import xlwt
count=0
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("rider")
sheet.write(0,count,"rider") # row, column, value    
for i in range(len(rider)):
    sheet.write(i+1,count,"rider"+str(i+1))
workbook.save('rider.xls')
"""
"""
import xlwt
count=0
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("request")
sheet.write(count,0,"request") # row, column, value    
for i in range(requests):
    sheet.write(count,i+1,"request"+str(i+1))
workbook.save('request.xls')
"""
"""
import xlwt
count=0
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("tripandrequest")
for i in range(len(trip)):
    sheet.write(count,0,"trip["+str(i+1)+"]:")
    if type(trip[i])==int:
        sheet.write(count,1,"request"+str(trip[i]))
    else:
        for j in range(len(trip[i])):
            sheet.write(count,j+1,"request"+str(trip[i][j])) # row, column, value
    count+=1
workbook.save('request in trip.xls')
"""