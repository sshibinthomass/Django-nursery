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
    for i in val:
        a=re.split('-',i)
        plantNum.append(int(a[0]))
        try:
            plantQua.append(int(a[1]))
        except:
            plantQua.append(1)
    lst.append(plantNum)
    lst.append(plantQua)
    with open('C:/Users/shibi/Downloads/Plant.csv','r') as file:
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
    return zip(lst[0],lst[1],lst[2])



def plantfinder(request):
    return render(request,'plantfinder.html')

def plantlist(request):
    val=request.POST['plantnumb']
    lst=find_val(val)
    return render(request,'plantlist.html',{'plantID':lst})