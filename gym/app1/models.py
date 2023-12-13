from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
# Create your models here.


# گزینه های انتخاب جنسیت
class Gender(models.TextChoices):
    FEMALE = 'FM','Female'
    MALE = 'ML','Male'

#گزینه های انتخاب زمان آسیب دیدن ورزشکارmanager_customuser
class damagedwhen (models.TextChoices):
    RECENT_MONTHS = 'RM',' ماه های اخیر'
    EARLIER = 'E', 'قبلتر'


class Manager_CustomUser(AbstractUser):
    username =models.CharField(max_length=20,primary_key=True,unique=True)
    email = models.EmailField()
    phonenumber = models.PositiveSmallIntegerField(default=0)


    def __str__(self) -> str:
        return self.username
'''class Crew_CustomUser():
    pass
class Coach_CustomUser():
    pass
class Bodybuilder_CustomUser():
    pass
'''
#مدل های مجموعه موجودیت ها
#مدل باشگاه🔵
class Gyms (models.Model):
    #اسم =کلید اصلی
    name = models.CharField(primary_key=True,max_length=20)
   # workingtime=
    manager_name = models.CharField(unique=True,max_length=20)
    manager_cv = models.TextField()
    manager_password = models.CharField(max_length=15)
    facilities = models.TextField()
    capacity = models.PositiveSmallIntegerField()
    numberofmachines = models.IntegerField()
   # numberofworkers=
    foundationdate = models.DateField()
    email = models.EmailField()
   # address=
    #tuition =

    def __str__(self) -> str:
        return self.name

#مدل ورزشکاران🔵
class bodybuilders (models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    gender = models.CharField (max_length= 2, choices=Gender.choices , default=Gender.FEMALE)
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    nationalcode = models.PositiveSmallIntegerField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    phonenumber = models.PositiveSmallIntegerField()
    aim = models.TextField()
    illness = models.TextField()
    birthdate = models.DateField()
   # age = 

    def __str__(self) -> str:
        return self.firstname

    
#مدل ورکتایمز🔴
class work_times (models.Model):
    #گزینه های انتخاب کارکن: خدمه یا مربی؟
    class who_works (models.TextChoices):
        COACH = 'CO','coach'
        CREW = 'CR','crew'
    #گزینه های انتخاب روز هفته
    class weekdays(models.TextChoices):
        SHANBE = 'SHA','Sanbe'
        YEKSHANBE = '1SH','1shanbe'
        DOSHANBE = '2SH','2shanbe'
        SESHANBE = '3SH','3shanbe'
        CHARSHANBE = '4SH','4shanbe'
        PANJSHANBE = '5SH','5shanbe'
        JOMEE = 'JOM','Jomee'

    #id خودکار
    day = models.CharField(choices=weekdays.choices,max_length=10)
    start = models.TimeField()
    end = models.TimeField()
    coach_crew = models.CharField(max_length=2 , choices=who_works.choices)

    def __str__(self) -> str:
        return str([self.day,self.start,self.end])
    
#مدل کارکنان🔵
class workers (models.Model):
    nationalcode = models.PositiveSmallIntegerField(primary_key=True)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    gender = models.CharField (max_length= 2, choices=Gender.choices , default=Gender.FEMALE)
    password = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.firstname
    
#مدل مربیان🔵
class coaches (workers):
    sport_degree =models.TextField()
    experience = models.TextField()
    
#مدل حرکات🔴
class movements(models.Model):
    #کلید اصلی= نام
    name = models.CharField(primary_key=True,max_length=10)
    machine_name = models.CharField(max_length=10)
   # body_part =
    image = models.ImageField()

    def __str__(self) -> str:
        return self.name
    
#مدل آسیب ها✅
class damages(models.Model):
    body_part= models.CharField(max_length=10)
    what =  models.CharField(max_length=100)
    when = models.CharField(max_length= 2 ,choices=damagedwhen.choices ,default=damagedwhen.EARLIER)

    def __str__(self) -> str:
        return self.what


#مدل های مجموعه ارتباط هایی که به شکل مجموعه موجودیت در آمده اند
#مدل قرارداد🔴
class Agreement(models.Model):
    pass
    #id = خودکار
   # hours = 
   # salary =

#مدل برنامه(ورزشی)🔴
class program(models.Model):
    finish_date = models.DateField(null=True)
   # tuition =
  #  howmany_days =

#مدل عضویت🔴
class Membership(models.Model):
    pass

# ارتباطاتی که با کلید خارجی و نه به صورت مدل جداگانه پیاده سازی میشوند
#عضویت در کدام باشگاه؟🔴
#کدام ورزشکاران عضو باشگاه اند؟🔴
#ورزشکار-برنامه 🔴
#برنامه نویسی(مربی -برنامه)🔵
#حرکات-برنامه(لیست)🔴
#آسیب - ورزشکار🔴
#قرارداد-باشگاه🔵
#قرارداد_ورک تایم🔵
#قرارداد -کارکنان🔵


#مدل های مجموعه ارتباط هایی که صفت دارند(مدل های میانی/واسطه)
#رزرو🔵
class Reserve():
    pass
