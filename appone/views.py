from django.shortcuts import render,redirect
# from django.http import HttpResponse,HttpResponseRedirect
from appone.models import FileUpload
from appone.forms import FileUploadForm
import cv2
import os
# Create your views here.
def index(req):    
    if req.method == 'POST':
        upload_form = FileUploadForm(req.POST,req.FILES,auto_id='%s')
        if upload_form.is_valid():
            upload_form.save()
            current_data = FileUpload.objects.filter(username=req.POST.get('username')).first()
            print(current_data.username)                          
            fp1 = str(current_data.fingerprint1)
            fp2 = str(current_data.fingerprint2)
            sample= cv2.imread(os.path.join(r'media',fp2))            
                   
            score = 0
            kp1,kp2,mp = None,None, None
            fp_image = cv2.imread(os.path.join(r'media',fp1))
        

            sift = cv2.SIFT_create()                              # scale invariant feature transform (allows to extract key points from individual images)
            keypoints_1,descriptor_1 = sift.detectAndCompute(sample,None)
            keypoints_2,descriptor_2 = sift.detectAndCompute(fp_image,None)
            matches =  cv2.FlannBasedMatcher({'algorithm':1,'trees':10},{}).knnMatch(descriptor_1,descriptor_2,k=2)
                    
            match_point =[]
            for p,q in matches:
                if p.distance < 0.1*q.distance:
                    match_point.append(p)
            keypoints =  0
            if len(keypoints_1)<len(keypoints_2):
                keypoints = len(keypoints_1)
            else:
                keypoints = len(keypoints_2)
                    
            if len(match_point)/keypoints *100 > score:
                score = len(match_point)/keypoints*100
                kp1,kp2,mp = keypoints_1,keypoints_2,match_point
            print('match:{}%'.format(score))
            result = cv2.drawMatches(sample,kp1,fp_image,kp2,mp,None)
            result = cv2.resize(result,None,fx=1,fy=1)
            cv2.imwrite('static/images/match.jpg',result)
            cv2.imread('static/images/match.jpg')  
            
                      
            if score == float(100):
                value="{} YEAH IT'S COMPLETE 100% MATCH :-) ".format(current_data.username).upper()
            else:
                value="{} IT'S A MATCH WITH {}%".format(current_data.username,round(score,2)).upper()            

    else:    
        value= "your match perecentage"  
        score = 0  
        upload_form= FileUploadForm(auto_id='%s') 
    return render(req,'appone/index.html',{'form':upload_form,'value':value})
  
        