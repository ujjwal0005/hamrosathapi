from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import User,DoctorProfile


@receiver(post_save,sender=User)
def create_doc_profile(sender,instance,created,*args, **kwargs):
    if created: 
        if instance.is_doctor:
            DoctorProfile.objects.create(user=instance)
