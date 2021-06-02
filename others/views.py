from django.shortcuts import render
import csv
import io
from django.http import FileResponse
# Create your views here.


arr=[]
SNO=[]
price=[]
NameO=[]
NameC=[]
plants=[]


def some_view(request):
    if request.method=='POST':
        val=int(request.POST["send1"])-1
        if val == 0:
        # Create a file-like buffer to receive PDF data.
            buffer = io.BytesIO()

            # Create the PDF object, using the buffer as its "file."
            p = canvas.Canvas(buffer)

            # Draw things on the PDF. Here's where the PDF generation happens.
            # See the ReportLab documentation for the full list of functionality.
            p.drawString(100, 100, "Hello world.")

            # Close the PDF object cleanly, and we're done.
            p.showPage()
            p.save()
            print("lo")
            # FileResponse sets the Content-Disposition header so that browsers
            # present the option to save the file.
            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
    else:
        return render(request,'home.html')




def list(SNO,price,NameO,NameC,plants):
    with open('Detailsplant.csv','r') as file:
        reader=csv.reader(file)
        for i in reader:
            if i[4]=='TRUE':
                SNO.append(int(i[0]))
                NameO.append(i[1])
                NameC.append(i[2])
                price.append(int(i[3])-int(i[5]))
list(SNO,price,NameO,NameC,plants)

def home(request):
    if request.method=='POST':
        val=int(request.POST["send1"])-1
        if val == 0:
            print("ell")
            some_view(request)
        if val == 1:
            arr.append(NameO[val])
        if val == 2:
            print(arr)
    return render(request,'home.html')

