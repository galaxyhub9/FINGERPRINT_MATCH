
from django.db import models

# Create your models here.
class FileUpload(models.Model):
    username = models.CharField(max_length=100)
    fingerprint1 = models.FileField(upload_to='file1',verbose_name = 'fingerprint1')
    fingerprint2 = models.FileField(upload_to='file2',verbose_name = 'fingerprint2')
    
    def __str__(self):
        return f'{self.username}|{self.fingerprint1}'