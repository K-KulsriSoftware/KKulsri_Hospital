from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# class Profile(models.Model):
    # BLOOD_GROUP = (
    #     ("A", "A"),
    #     ("B", "B"),
    #     ("O", "O"),
    # )
    # GENDER = (
    #     ("MEN", "ชาย"),
    #     ("WOMEN", "หญิง"),
    #     ("OTHER", "อื่นๆ"),
    # )
    # BLOOD_RH = (
    #     ("P", "+"),
    #     ("M", "-"),
    # )
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # patient_name_title = models.CharField(max_length=30, blank=True)
    # patient_name = models.CharField(max_length=50, blank=True)
    # patient_surname = models.CharField(max_length=50, blank=True)
    # birth_date = models.DateField(null=True, blank=True)
    # patient_img = models.ImageField( upload_to='picture/', default='picture/none/no-img.jpg')
    # id_card_number = models.CharField(max_length=13, blank=True)
    # gender = models.CharField( max_length=3, choices=GENDER, default="MAN",)
    # blood_group_abo = models.CharField(max_length=3, choices=BLOOD_GROUP, default="O",)
    # blood_group_rh = models.CharField(max_length=2, choices=BLOOD_RH, default="P",)
    # race = models.CharField(max_length=50, blank=True)
    # nationallity = models.CharField(max_length=50, blank=True)
    # Religion = models.CharField(max_length=50, blank=True)
    # Status = models.CharField(max_length=50, blank=True)
    # pateint_address = models.CharField(max_length=200, blank=True)
    # occupy = models.CharField(max_length=100, blank=True)
    # telphone_number = models.CharField(max_length=11, blank=True)
    # father_name = models.CharField(max_length=100, blank=True)
    # mother_name = models.CharField(max_length=100, blank=True)
    # emergency_name = models.CharField(max_length=100, blank=True)
    # emergency_phone = models.CharField(max_length=11, blank=True)
    # emergency_addr = models.CharField(max_length=200, blank=True)
    # email = models.EmailField(max_length=50, blank=True)
    # congenital_disease = models.CharField(max_length=200, blank=True)
    # order_ids
    # submit = models.CharField(max_length=200, blank=True)

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
