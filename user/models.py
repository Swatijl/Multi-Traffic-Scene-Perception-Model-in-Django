from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    firstname=models.CharField(max_length=300)
    lastname=models.CharField(max_length=200)
    userid=models.CharField(max_length=200)
    password=models.IntegerField()
    mblenum=models.BigIntegerField()
    email=models.EmailField(max_length=400)
    gender=models.CharField(max_length=200)

class Upload_Model(models.Model):
    usid=models.ForeignKey(RegisterModel)
    wheather=models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    images = models.FileField(upload_to='train/')
    state = models.CharField(max_length=200)
    distric = models.CharField(max_length=200)


class CheckTraffic(models.Model):
    wetr = models.CharField(max_length=200)
    are = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    traf = models.ForeignKey(Upload_Model)
    file_path=models.CharField(max_length=200)
