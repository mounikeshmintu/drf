from django.db import models
from django.conf import settings
# Create your models here.
def upload(instance,filename):
    return ("update/{user}/{image}").format(user=instance.user,filename=filename)
class status(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to="upload",null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content
