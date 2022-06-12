from django.db import models

class News(models.Model):
    image = models.ImageField(upload_to='News',null=True,blank=True)
    title = models.TextField()
    description = models.TextField()
    time = models.CharField(max_length=15)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return f"{self.id} | {self.title[:20]}"

class Murojat(models.Model):
    manzil = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    theme = models.TextField()
    file = models.FileField(upload_to='Files',null=True,blank=True)
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

class Yuridik(models.Model):
    manzil = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    faks = models.CharField(max_length=15,null=True,blank=True)
    theme = models.TextField()
    file = models.FileField(upload_to='Files',null=True,blank=True)
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
