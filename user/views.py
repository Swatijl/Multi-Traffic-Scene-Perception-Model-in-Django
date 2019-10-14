import os

import PIL
import cv2
from PIL import Image
from django.db.models import Count

from .check import comp
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from Multi_Traffic_Scene_Perception.settings import BASE_DIR
from user.forms import RegisterForms, UploadForm
from user.models import RegisterModel, Upload_Model, CheckTraffic


def index(request):
    if request.method=="POST":

        usid=request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            check = RegisterModel.objects.get(userid=usid,password=pswd)
            request.session['userid']=check.id
            return redirect('homepage')
        except:
            pass

    return render(request,'user/index.html')


def register(request):
    if request.method=="POST":
        forms=RegisterForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
        forms=RegisterForms()
    return render(request,'user/register.html',{'form':forms})


def homepage(request):

    if request.method=="POST":
        cur = request.FILES['testcur']
        fs = FileSystemStorage()
        filename = fs.save(cur.name, cur)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, 'assets/media/' + filename)
        res = comp(pat)
        obj = Upload_Model.objects.get(id=res)
        trwthr = obj.wheather
        tarea = obj.area
        tdict = obj.distric
        CheckTraffic.objects.create(wetr=trwthr, are=tarea, img=tdict, traf=obj,file_path=pat)
        return redirect('gryscale', res)
    return render(request,'user/homepage.html')

def user_uplolad_page(request):
    uid = request.session['userid']
    objec = RegisterModel.objects.get(id=uid)
    if request.method=="POST":
        forms=UploadForm(request.POST, request.FILES)
        if forms.is_valid():
            ff = forms.save(commit=False)
            ff.usid = objec
            ff.save()
            return redirect('user_uplolad_page')
    else:
        forms=UploadForm()
    return render(request,'user/user_uplolad_page.html',{'form':forms})

def gryscale(request,pk):
    message = ''
    if pk == '0':
        obj = None
        message = 'There is no matching currencies'
    else:
        obj = Upload_Model.objects.get(id=pk)
        ast=obj.images.url
        pat=os.path.join(BASE_DIR,'assets/'+ast)
        ss=str(pat)
        img = cv2.imread(pat)
        cv2.imshow("img", img)
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        labimage = os.path.join(BASE_DIR, 'assets/static/image/lab.png')
        cv2.imwrite(labimage, lab)
        l, a, b = cv2.split(lab)
        lchannel = os.path.join(BASE_DIR, 'assets/static/image/l.png')
        cv2.imwrite(lchannel, l)
        achannel = os.path.join(BASE_DIR, 'assets/static/image/a.png')
        cv2.imwrite(achannel, a)
        bchannel = os.path.join(BASE_DIR, 'assets/static/image/b.png')
        cv2.imwrite(bchannel, b)
        # -----Splitting the LAB image to different channels-------------------------
        clahe = cv2.createCLAHE(clipLimit=9.0, tileGridSize=(8, 8))
        cl = clahe.apply(l)
        claheouput = os.path.join(BASE_DIR, 'assets/static/image/clahe.png')
        cv2.imwrite(claheouput, cl)
        # -----Merge the CLAHE enhanced L-channel with the a and b channel-----------
        limg = cv2.merge((cl, a, b))
        limageinput = os.path.join(BASE_DIR, 'assets/static/image/limage.png')
        cv2.imwrite(limageinput, limg)
        final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        finaloutput = os.path.join(BASE_DIR, 'assets/static/image/final.png')
        cv2.imwrite(finaloutput, final)
    return render(request,'user/gryscale.html',{'obj':obj,'message':message,'pk':pk})

def viewlist(request,pk):
    message=''
    if pk=='0':
        obj=None
        message='There is no matching currencies'
    else:
        obj=Upload_Model.objects.get(id=pk)
    return render(request,'user/viewlist.html',{'obj':obj,'message':message})

def traffic_images(request):
    det = Upload_Model.objects.all()
    return render(request,'user/traffic_images.html',{'form':det})

def categoryanalysis_chart(request,chart_type):
    chart = CheckTraffic.objects.values('wetr').annotate(dcount=Count('wetr'))
    return render(request,'user/chart.html',{'objects':chart,'chart_type':chart_type})