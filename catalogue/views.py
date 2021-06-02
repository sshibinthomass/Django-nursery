from django.shortcuts import render
import csv
# Create your views here.

SNO=[]
priceOrg=[]
price=[]
NameO=[]
NameC=[]
plants=[]
risk=[]
BillNameArr=[]
BillQuaArr=[]
BillSnoArr=[]
BillPriceArr=[]
sumQua=0
sumPrice=0


CSNO=[]
CNameO=[]
CNameC=[]
CPrice=[]
CDiscount=[]
CRisk=[]
CVisible=[]
Index=[]


catagory=[
    "Every Plant",
    "Cactus",
    "Succulents",
     "Ground Cover/Sedum",
     "Hanging",
     "Aloe",
     "Haworthia",
     "Others",
     "Indoor"
    ]

states=[
"All States-H",
"Tamil Nadu-H",
"Andhra Pradesh-H",
"Assam-M",
"Bihar-L",
"Chhattisgarh-L",
"Goa-M",
"Gujarat-L",
"Haryana-M",
"Himachal Pradesh-L",
"Jharkhand-L",
"Karnataka-H",
"Kerala-H",
"Madhya Pradesh-L",
"Maharashtra-M",
"Meghalaya-L",
"Odisha-L",
"Punjab-M",
"Rajasthan-L",
"Telangana-M",
"Uttarakhand-L",
"Uttar Pradesh-L",
"West Bengal-M",
"Chandigarh-L",
"Delhi-H",
"Dadra, Nagar Haveli,Daman & Diu-L",
"Puducherry-H"]
stateName=[]
stateID=[]
for i in states:
    stateName.append(i.split('-')[0])
    stateID.append(i.split('-')[1])


def list(val):
    with open('Detailsplant.csv','r') as file:
        reader=csv.reader(file)
        SNO.clear()
        price.clear()
        NameO.clear()
        NameC.clear()
        risk.clear()
        priceOrg.clear()
        for i in reader:
            try:
                if(val=="H"):
                    if(int(i[0]) not in SNO and i[4]=='TRUE'):
                        SNO.append(int(i[0]))
                        NameO.append(i[1])
                        NameC.append(i[2])
                        price.append(int(i[3])-int(i[5]))
                        risk.append(i[6])
                        priceOrg.append(int(i[3]))
                if(val=="M"):
                    if(int(i[0]) not in SNO and i[4]=='TRUE' and (i[6][0]=="M" or i[6][0]=="L")):
                        SNO.append(int(i[0]))
                        NameO.append(i[1])
                        NameC.append(i[2])
                        price.append(int(i[3])-int(i[5]))
                        risk.append(i[6])
                        priceOrg.append(int(i[3]))
                if(val=="L"):
                    if(int(i[0]) not in SNO and i[4]=='TRUE' and i[6][0]=="L"):
                        SNO.append(int(i[0]))
                        NameO.append(i[1])
                        NameC.append(i[2])
                        price.append(int(i[3])-int(i[5]))
                        risk.append(i[6])
                        priceOrg.append(int(i[3]))
            except:
                pass
    return zip(SNO,NameO,NameC,price,risk,priceOrg)

def bill(val,qua):
    with open('Detailsplant.csv','r') as file:
        reader=csv.reader(file)
        for i in reader:
            try:
                if(i[1] not in BillNameArr and int(i[0])==val):
                    BillSnoArr.append(int(i[0]))
                    BillNameArr.append(i[1])
                    BillQuaArr.append(int(qua))
                    BillPriceArr.append(int(qua)*(int(i[3])-int(i[5])))     
                else:
                    for j in range(len(BillNameArr)):
                        if(BillNameArr[j]==i[1] and int(i[0])==val):
                            BillQuaArr[j]=int(qua)
                            BillPriceArr[j]=int(qua)*(int(i[3])-int(i[5]))
            except:
                pass

def clear():
    try:
        BillNameArr.clear()
        BillQuaArr.clear()
        BillSnoArr.clear()
        BillPriceArr.clear()
    except:
        pass

def Remove(val):
    try:
        val-=1
        BillNameArr.pop(val)
        BillQuaArr.pop(val)
        BillSnoArr.pop(val)
        BillPriceArr.pop(val)
    except:
        pass

save={
    "risk":"H",
    "state":"Tamil Nadu",
    "type":"Every Plant"
}

def catalogue(request):
    plants=list(save["risk"])
    try:
        if request.method=="POST":
            try:
                val=request.POST["button1"]
                if val=="Clear cart":
                    clear()
                elif("Remove" in val):
                    Remove(int(val.split('.')[0]))
                else:
                    num=int(val.split('.')[0])
                    qua=request.POST["quantity"]
                    bill(num,qua)
            except:
                pass
            try:
                state_sel=(request.POST["state_sel"])
                cat_sel=(request.POST["cat_sel"])
                if(state_sel!="Select State"):
                    save["state"]=state_sel[:-2]
                    state_sel=state_sel[-1]
                if(cat_sel!="Select type"):
                    save["type"]=cat_sel
                if(state_sel=="L" or state_sel=="M" or state_sel=="H"):
                    save["risk"]=state_sel
                    plants=list(state_sel)
            except:
                pass
            try:
                cat_sel=(request.POST["cat_sel"])
            except:
                pass
    except:
        pass


    val=zip(BillSnoArr,BillNameArr,BillQuaArr,BillPriceArr)
    state=zip(states,stateName)
    sumQua=sum(BillQuaArr)
    sumPrice=sum(BillPriceArr)
    return render(request, 'catalogue.html',{'save':save,'plants':plants,'bill':val,'sumQua':sumQua,'sumPrice':sumPrice,'state':state,'catagory':catagory})


def adddata():
    data_list=[]
    for i in range(len(CSNO)):
        l1=[]
        l1.append(CSNO[i])
        l1.append(CNameO[i])
        l1.append(CNameC[i])
        l1.append(CPrice[i])
        l1.append(CVisible[i])
        l1.append(CDiscount[i])
        l1.append(CRisk[i])
        data_list.append(l1)
    with open('Detailsplant.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(data_list)


def writeData(VSNO,VNameO,VNameC,VPrice,VDiscount,VRisk,VVisible):
    CNameO[VSNO]=VNameO
    CNameC[VSNO]=VNameC
    CPrice[VSNO]=VPrice
    CVisible[VSNO]=VVisible
    CDiscount[VSNO]=VDiscount
    CRisk[VSNO]=VRisk
    adddata()


def changeLst():
    with open('Detailsplant.csv','r') as file:
        reader=csv.reader(file)
        for i in reader:
            try:
                if(int(i[0]) not in CSNO):
                    CSNO.append(int(i[0]))
                    CNameO.append(i[1])
                    CNameC.append(i[2])
                    CPrice.append(i[3])
                    CDiscount.append(i[5])
                    CRisk.append(i[6])
                    CVisible.append(i[4])
            except:
                pass
    return zip(CSNO,CNameO,CNameC,CPrice,CDiscount,CRisk,CVisible)


def changeVal(request):
    if request.method=="POST":
        try:
            if(request.POST["btn1"]=="add"):
                ASNO=int(request.POST["ASNO"])
                if(ASNO not in CSNO):
                    CSNO.append(len(CSNO)+1)
                    CNameO.append(request.POST["ANameO"])
                    CNameC.append(request.POST["ANameC"])
                    CPrice.append(int(request.POST["APrice"]))
                    CDiscount.append(int(request.POST["ADiscount"]))
                    CRisk.append(request.POST["ARisk"])
                    CVisible.append(request.POST["AVisible"])
                    adddata()
        except:
            pass
        try:
            VSNO=int(request.POST["btn"])-1
            VNameO=request.POST["VNameO"]
            VNameC=request.POST["VNameC"]
            VPrice=request.POST["VPrice"]
            VDiscount=request.POST["VDiscount"]
            VRisk=request.POST["VRisk"]
            VVisible=request.POST["VVisible"]
            writeData(VSNO,VNameO,VNameC,VPrice,VDiscount,VRisk,VVisible)
        except:
            pass

    plants=changeLst()
    return render(request, 'changeVal.html',{'plants':plants})