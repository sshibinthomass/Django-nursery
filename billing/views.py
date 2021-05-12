from django.shortcuts import render,redirect
import csv,re

# Create your views here.

def find_val(val):
    val=val.split(',')
    lst=[]
    l1=[]
    plantNum=[]
    plantQua=[]
    plantNam=[]
    allplant=[]
    SNo=[]
    count=1
    for i in val:
        a=re.split('-',i)
        plantNum.append(int(a[0]))
        SNo.append(count)
        count+=1
        try:
            plantQua.append(int(a[1]))
        except:
            plantQua.append(1)
    lst.append(SNo)
    lst.append(plantNum)
    tot=sum(plantQua)
    with open('Plant.csv.','r') as file:
        reader=csv.reader(file)
        for i in reader:
            try:
                index=int(i[0])
            except:
                index=0
            allplant.append(i[1])
    for i in lst[0]:
        l1.append(allplant[i])
    lst.append(l1)
    lst.append(plantQua)
    return zip(lst[0],lst[1],lst[2],lst[3]), tot


def plantfinder(request):
    return render(request,'plantfinder.html')

def plantlist(request):
    val=request.POST['plantnumb']
    lst,l2=find_val(val)
    return render(request,'plantlist.html',{'plantID':lst,'l2':l2})