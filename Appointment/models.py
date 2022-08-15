from statistics import mode
from account.models import User
from django.db import models

# Create your models here.
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='doctor_appointment')
    starttime = models.TimeField()
    endtime = models.TimeField()
    date = models.DateField()
    doctor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='appointment')
    is_cancelled = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}-{self.starttime}'

# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_comment')
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='blog_comment')
#     comment = models.TextField(null=True,blank=True)
#     is_verified = models.BooleanField(default=True)

#     def __str__(self):
#         return f'{self.user}-{self.blog}'
