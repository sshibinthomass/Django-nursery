from django.shortcuts import render
import csv
# Create your views here.

def list():
    SNO=[]
    price=[]
    NameO=[]
    NameC=[]
    plants=[]
    with open('Detailsplant.csv','r') as file:
        reader=csv.reader(file)
        for i in reader:
            if i[4]=='TRUE':
                SNO.append(int(i[0]))
                NameO.append(i[1])
                NameC.append(i[2])
                price.append(int(i[3])-int(i[5]))
    return zip(SNO,NameO,NameC,price)

def catalogue(request):
    if request.method=="POST":
        print("hi")
    plants=list()
    return render(request, 'catalogue.html',{'plants':plants})
