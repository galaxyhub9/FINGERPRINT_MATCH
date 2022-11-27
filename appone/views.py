from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from appone.models import FileUpload
import cv2
import os
# Create your views here.

def index(req): 
    file =' '  
    a=None 
    for dot in os.listdir('static/dots'):
            os.remove(os.path.join(r'static/dots/',dot))
    print('removed dot files')
    if req.method == 'POST':           
        finger1= req.FILES.get('fingerprint1')         
        images = req.FILES.getlist('fingerprint2')
        print('finger1---------------',req.FILES.get('fingerprint1'))
        for image in images:   
            FileUpload(fingerprint1=finger1,fingerprint2=image).save() 
        return HttpResponseRedirect('match')
        
    return render(req,'appone/index.html')
                      

def match(req):
    deleted = FileUpload.objects.all()
    objectlen=len(deleted)
    filename=None
    if objectlen == 0:
        dots=''
        value=''
        file=''
        allfiles=[]
        finger1=''
        matchp=''
        score=''
        # 'objectlen':objectlen
    else:        
        score = 0
        kp1, kp2, mp = None, None, None
        matchp = []
        value= "perecentage".upper()
        score = 0      
        i = 0 
        current_data = FileUpload.objects.last()
        fp1 = str(current_data.fingerprint1)         
        sample= cv2.imread(os.path.join(r'media',fp1)) 
        firstimg = FileUpload.objects.first() 
        fpf = firstimg.fingerprint1
        split = str(fpf).split("/")
        finger1 = split[1]       

        for file in os.listdir('media/file2'):   
            print(file)
            fp_image = cv2.imread(os.path.join(r'media/file2/', file))    
            sift = cv2.SIFT_create()
            keypoints_1, descriptor_1 = sift.detectAndCompute(sample, None)
            keypoints_2, descriptor_2 = sift.detectAndCompute(fp_image, None)
            matches = cv2.FlannBasedMatcher({
                'algorithm': 1, 'trees': 10}, {}).knnMatch(descriptor_1,descriptor_2, k=2)
            match_point = []
            for p, q in matches:
                if p.distance < 0.1*q.distance:
                    match_point.append(p)
            keypoints = 0
            if len(keypoints_1) < len(keypoints_2):
                keypoints = len(keypoints_1)
            else:
                keypoints = len(keypoints_2)
                
            a =len(match_point)/keypoints*100
            matchp.append(round(a,2))
            print(a)             
            if len(match_point)/keypoints * 100 > score:
                    score = len(match_point)/keypoints*100   
                    filename = file
                    kp1, kp2, mp = keypoints_1, keypoints_2, match_point
                
            result= cv2.drawMatches(sample,kp1,fp_image,kp2,mp,None)
            result = cv2.resize(result,None,fx=1,fy=1)
            cv2.imwrite('static/dots/match{}.jpg'.format(i),result)            
            print('images of dot uploaded',i)
            i=i+1
                
        
        print('filename:{}'.format(filename))
        print('match:{}%'.format(score))            
            
                
            
        allfiles=[]    
        for i in os.listdir('media/file2'):
            allfiles.append(i)
                        
        if score == float(100):
            value="IT'S A COMPLETE 100% MATCH"
            file = '{}'.format(filename)
        else:
            value="IT'S A MATCH WITH {}%".format(round(score,2))           
            file = '{}'.format(filename)
                
        for two in os.listdir('media/file2'):
            os.remove(os.path.join(r'media/file2/',two))
        print('removed files in 2')
            
        for one in os.listdir('media/file1'):
            os.remove(os.path.join(r'media/file1/',one))
        print('removed files in 1')
            
        dots=[]
        for dot in os.listdir('static/dots'):
            dots.append(os.path.join('static/dots/',dot))
            print(dots)
        
    
        deleted.delete()
        
    return render(req,'appone/match.html',{'dots':dots,'value':value,
                                           'file':file,'allfiles':allfiles,
                                           'finger1':finger1,'matchp':matchp,
                                           'score':score,'objectlen':objectlen})

    
   