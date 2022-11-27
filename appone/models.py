
from django.db import models
from datetime import datetime

# Create your models here.
class FileUpload(models.Model):

    date_uploaded = models.DateTimeField(auto_now=datetime.now)
    fingerprint1 = models.FileField(upload_to='file1',verbose_name = 'fingerprint1')
    fingerprint2 = models.FileField(upload_to='file2',verbose_name = 'fingerprint2')
    
    def __str__(self):
        return f'{self.date_uploaded}'
    
