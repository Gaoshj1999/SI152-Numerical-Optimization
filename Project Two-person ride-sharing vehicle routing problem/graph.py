# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:39:59 2020

@author: duola
"""
'''
1.假设城市为网状，任意相邻点间距离相等
2.不允许先接一单再接一单，这视为两单
'''
'''
本程序实现了网图模拟现实地图，并可通过输入车辆乘客和对应目的地，输出不同车辆
对应的可行单以及相应花费。
'''
class node:
    def __init__(self,cid,sid,did):
        self.cid=cid
        self.sid=sid
        self.did=did
    def changecar(self,cid):
        self.cid=cid
    def changestart(self,sid):
        self.sid=sid
    def changedestination(self,did):
        self.did=did
def create(n,m):#n为车数,m为人数
    car=[]
    people=[]
    for i in range(n):
        x=eval(input("请输入车"+str(i+1)+"号横坐标:"))
        y=eval(input("请输入车"+str(i+1)+"号纵坐标:"))
        car.append((x,y))
    for i in range(m):
        x1=eval(input("请输入顾客"+str(i+1)+"号起点横坐标:"))
        y1=eval(input("请输入顾客"+str(i+1)+"号起点纵坐标:"))
        x2=eval(input("请输入顾客"+str(i+1)+"号终点横坐标:"))
        y2=eval(input("请输入顾客"+str(i+1)+"号终点横坐标:"))
        people.append((x1,y1,x2,y2))
    return car,people    
def limitwaittime():
    time=eval(input("请输入最长等待时间:"))
    return time
def limitextratime():
    time=eval(input("请输入最长额外时间:"))
    return time    
class graph:
    def __init__(self,height,width):
        self.height=height
        self.width=width
        self.matrix=[]
        for i in range(height):
            tempmatrix=[]
            for j in range(width):
                tempmatrix.append(node(0,0,0))
            self.matrix.append(tempmatrix)
        self.car=[]#(x,y)为地址
        self.people=[]#(x1,y1,x2,y2),其中(x1,y1)为出发点,(x2,y2)为终点
        self.trip=[]#(cid,pid,cost)or(cid,(p1id,p2id),cost)
    def gcreate(self,n,m):
        car,people=create(n,m)
        for i in range(len(car)):
            self.matrix[car[i][0]][car[i][1]].cid=i+1
            self.car.append((car[i][0],car[i][1]))
            #注意这里car的key存的是真实cid-1
        for i in range(len(people)):
            self.matrix[people[i][0]][people[i][1]].sid=i+1
            self.matrix[people[i][2]][people[i][3]].did=i+1
            self.people.append((people[i][0],people[i][1],people[i][2],people[i][3]))
            #注意这里people的key存的是真实sid-1,did-1
    def carnumber(self):
        return len(self.car)
    def peoplenumber(self):
        return len(self.people)
    def distance(self,carid,peopleid):#总行程的距离
        d=abs(self.car[carid-1][0]-self.people[peopleid-1][0])\
        +abs(self.car[carid-1][1]-self.people[peopleid-1][1])\
        +abs(self.people[peopleid-1][0]-self.people[peopleid-1][2])\
        +abs(self.people[peopleid-1][1]-self.people[peopleid-1][3])
        return d
    def time(self,carid,peopleid):#车与人之间的距离
        t=abs(self.car[carid-1][0]-self.people[peopleid-1][0])\
        +abs(self.car[carid-1][1]-self.people[peopleid-1][1])
        return t
    def extratime(self,p1id,p2id):#人与人之间的距离
        t=abs(self.people[p1id-1][0]-self.people[p2id-1][0])\
        +abs(self.people[p1id-1][1]-self.people[p2id-1][1])
        return t
    def traveltime(self,p1id,d2id):#人与目的地之间的距离
        t=abs(self.people[p1id-1][0]-self.people[d2id-1][2])\
        +abs(self.people[p1id-1][1]-self.people[d2id-1][3])
        return t
    def travelextratime(self,d1id,d2id):
        t=abs(self.people[d1id-1][2]-self.people[d2id-1][2])\
        +abs(self.people[d1id-1][3]-self.people[d2id-1][3])
        return t
    def createtrip(self):#c是顾客最长等待时间,时间正比于路程
    #m是最长额外时间
        c=limitwaittime()
        m=limitextratime()
        for i in range(len(self.car)):
            permittrip=[]
            length=0
            for j in range(len(self.people)):
                if self.time(i+1,j+1)<=c:
                    permittrip.append(j+1)
                    self.trip.append((i+1,j+1,self.distance(i+1,j+1)))
            length=len(permittrip)
            for j in range(length):
                for k in range(length-j-1):
                    cost1=float("inf")
                    c1=0
                    cost2=float("inf")
                    c2=0
                    if self.time(i+1,permittrip[j])+self.extratime(permittrip[j],permittrip[j+k+1])<=c:
                        if self.traveltime(permittrip[j+k+1],permittrip[j])+self.travelextratime(permittrip[j],permittrip[j+k+1])\
                            <=self.traveltime(permittrip[j+k+1],permittrip[j+k+1])+self.travelextratime(permittrip[j+k+1],permittrip[j]):
                            cost1=self.time(i+1,permittrip[j])+self.extratime(permittrip[j],permittrip[j+k+1])\
                                +self.traveltime(permittrip[j+k+1],permittrip[j])+self.travelextratime(permittrip[j],permittrip[j+k+1])
                        else:
                            cost1=self.time(i+1,permittrip[j])+self.extratime(permittrip[j],permittrip[j+k+1])\
                                +self.traveltime(permittrip[j+k+1],permittrip[j+k+1])+self.travelextratime(permittrip[j+k+1],permittrip[j])
                            c1=1
                    if self.time(i+1,permittrip[j+k+1])+self.extratime(permittrip[j+k+1],permittrip[j])<=c:
                        if self.traveltime(permittrip[j],permittrip[j+k+1])+self.travelextratime(permittrip[j+k+1],permittrip[j])\
                            <=self.traveltime(permittrip[j],permittrip[j])+self.travelextratime(permittrip[j],permittrip[j+k+1]):
                            cost2=self.time(i+1,permittrip[j+k+1])+self.extratime(permittrip[j+k+1],permittrip[j])\
                                +self.traveltime(permittrip[j],permittrip[j+k+1])+self.travelextratime(permittrip[j+k+1],permittrip[j])
                        else:
                            cost2=self.time(i+1,permittrip[j+k+1])+self.extratime(permittrip[j+k+1],permittrip[j])\
                                +self.traveltime(permittrip[j],permittrip[j])+self.travelextratime(permittrip[j],permittrip[j+k+1])
                            c2=1
                    if cost1<=cost2:
                        if c1==0:
                            if cost1-self.distance(i+1,permittrip[j+k+1])<=m and self.time(i+1,permittrip[j])+self.extratime(permittrip[j],permittrip[j+k+1])\
                                +self.traveltime(permittrip[j+k+1],permittrip[j])-self.distance(i+1,permittrip[j])<=m:
                                self.trip.append((i+1,(permittrip[j],permittrip[j+k+1]),cost1))
                        elif c1==1:
                            if cost1-self.distance(i+1,permittrip[j])<=m and self.time(i+1,permittrip[j])+self.extratime(permittrip[j],permittrip[j+k+1])\
                                +self.traveltime(permittrip[j+k+1],permittrip[j+k+1])-self.distance(i+1,permittrip[j+k+1])<=m:
                                self.trip.append((i+1,(permittrip[j],permittrip[j+k+1]),cost1))
                    else:
                        if c2==0:
                            if cost2-self.distance(i+1,permittrip[j])<=m and self.time(i+1,permittrip[j+k+1])+self.extratime(permittrip[j+k+1],permittrip[j])\
                                +self.traveltime(permittrip[j],permittrip[j+k+1])-self.distance(i+1,permittrip[j+k+1])<=m:
                                self.trip.append((i+1,(permittrip[j],permittrip[j+k+1]),cost2))
                        elif c2==1:
                            if cost2-self.distance(i+1,permittrip[j+k+1])<=m and self.time(i+1,permittrip[j+k+1])+self.extratime(permittrip[j+k+1],permittrip[j])\
                                +self.traveltime(permittrip[j],permittrip[j])-self.distance(i+1,permittrip[j])<=m:
                                self.trip.append((i+1,(permittrip[j],permittrip[j+k+1]),cost2))
                     
graph1=graph(5,5)
graph1.gcreate(2,3)#(car,people)
graph1.createtrip()
print(graph1.trip)