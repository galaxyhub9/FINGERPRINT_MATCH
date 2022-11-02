from dataclasses import fields
from appone.models import FileUpload
from django import forms

class FileUploadForm(forms.ModelForm):
    fingerprint1 = forms.FileField(label_suffix='', label='Click to upload file one' )
    fingerprint2 = forms.FileField(label_suffix='', label='Click to upload file two')
  
    
    class Meta():        
        model= FileUpload
        fields=('username','fingerprint1','fingerprint2')
        
        labels={
            'username':''
        }
        widgets ={
          'username':forms.TextInput(attrs={'id':'user','placeholder':'enter username'}),
        
        }
        
