from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from django.utils import timezone
# Create your models here.  hthhyhyt
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

#گزینه های انتخاب زمان آسیب دیدن 
class damagedwhen (models.TextChoices):
    RECENT_MONTHS = 'RM',' ماه های اخیر'
    EARLIER = 'E', 'قبلتر'

# گزینه های انتخاب جنسیت
class Gender(models.TextChoices):
    FEMALE = 'FM','Female'
    MALE = 'ML','Male'

#ساخت یوزرهای سفارشی  
class custom_user(AbstractUser):
    email = models.EmailField(unique=True)
    is_gymManager = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_crew = models.BooleanField(default=False)
    is_bodybuilder = models.BooleanField(default=False)
    user_name = models.CharField(max_length=10,null=True)
    
'''class Crew_CustomUser():
    pass
class Coach_CustomUser():
    pass'''
#مدل آسیب ها✅
class damage(models.Model):

    body_part= models.CharField(max_length=20)
    what =  models.CharField(max_length=100)
    when = models.CharField(max_length=10 ,choices=damagedwhen.choices ,default=damagedwhen.EARLIER)

    def __str__(self) -> str:
        return self.what
    

#مدل های مجموعه موجودیت ها
#مدل باشگاه(مدیرباشگاه)🔵
class Gym(models.Model):
    gymManager =models.OneToOneField(custom_user,on_delete=models.PROTECT, primary_key=True)
    
    gym_name = models.CharField(unique=True,max_length=20)
   # workingtime=
    manager_cv = models.TextField()
    facilities = models.TextField()
    capacity = models.PositiveSmallIntegerField()
    numberofmachines = models.IntegerField()
   # numberofworkers=
    foundationdate = models.DateField()
   # address=null = true
    #tuition =
    #phonenumber

    def __str__(self):
        return self.gym_name

#مدل ورزشکاران🔵
class bodybuilder (models.Model):
    bodybuilder = models.OneToOneField(custom_user,on_delete=models.PROTECT,primary_key=True)
    
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    gender = models.CharField (max_length= 2, choices=Gender.choices , default=Gender.FEMALE)
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    nationalcode = models.PositiveSmallIntegerField(unique=True)
    email = models.EmailField()
    phonenumber = models.PositiveSmallIntegerField()
    aim = models.TextField()
    illness = models.TextField()
    birthdate = models.DateField()
   # age = 
    Damage = models.ManyToManyField(damage,related_name="who_damaged",null=True)

    def __str__(self) -> str:
        return self.firstname

    
#مدل ورکتایمز✅
class work_time(models.Model):

    #id خودکار
    day = models.CharField(choices=weekdays.choices,max_length=10)
    start = models.TimeField()
    end = models.TimeField()
    coach_crew = models.CharField(max_length=2 , choices=who_works.choices)

    def __str__(self):
        return str(self.day,self.start,self.end)
'''                                                                                                                      
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
    
    
class movements(models.Model):
    #کلید اصلی= نام
    name = models.CharField(primary_key=True,max_length=10)
    machine_name = models.CharField(max_length=10)
   # body_part =
    image = models.ImageField()

    def __str__(self) -> str:
        return self.name
    '''


#مدلهای مجموعه ارتباط ایی که به شکل مجموعه موجودیت در اومدن
#مدل قرارداد
class Agreement(models.Model):
    start_date=models.DateField()
    end_date=models.DateField()
    Hour=models.Time.Field()
    salary=models.DecimalField(max_digits=5,decimal_place=2)
    class Gym=models.Foreignkey(class Gym)
    class workers=models.Foreignkey(class workers,on-delet=models.CASCADE)
    class work_time=models.Foreignkey(class work_time,on-delet=models.CASCADE) 
    
#مدل برنامه(ورزشی
class program(models.Model):
    finish_date = models.DateField(null=True)
    tuition =models.floatfield
class Day(models.Model):
 DAYS_CHOICES=[
     ('دو روز','دو')
     ('سه روز','سه')
     ('چهار روز','چهار')
     ]
 days=models.charfild(max_lengh=2,choices=DAYS_CHOICES)
     
class Reservation (models.Models):
    class custom_user = models.ForeignKey(class custom_user,on-delet=models.CASCADE)
    START_date = models.DateField()
    End_date = models.DateField()
    Reservatio_type = models.CharField(max_length=100)
    Payment_status = models.BooleanField()
    
    def __str__(self):
        return
    f"{self.custom_user.user_name}
    Reservation"
    

#مدل عضویت🔴
class Membership(models.Model):
    class Gym = models.Foreignkey(class Gym)
    class bodybuilder = models.Foreignkey(class bodybuilder)
    class Reservation = models.Foreignkey(class Reservation)
    

# ارتباطاتی که با کلید خارجی و نه به صورت مدل جداگانه پیاده سازی میشوند
#عضویت در کدام باشگاه؟🔴
#کدام ورزشکاران عضو باشگاه اند؟🔴
#ورزشکار-برنامه 🔴
#برنامه نویسی(مربی -برنامه)🔴
#حرکات-برنامه(لیست)🔴
#آسیب - ورزشکار🔵
#قرارداد-باشگاه🔵
#قرارداد_ورک تایم🔵
#قرارداد -کارکنان🔵


#مدل های مجموعه ارتباط هایی که صفت دارند(مدل های میانی/واسطه)
#رزرو🔵
class Reserve():
    pass
