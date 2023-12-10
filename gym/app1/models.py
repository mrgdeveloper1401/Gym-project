from django.db import models

# Create your models here.
#
# گزینه های انتخاب جنسیت
class Gender(models.TextChoices):
    FEMALE = 'FM','Female'
    MALE = 'ML','Male'




#گزینه های انتخاب زمان آسیب دیدن ورزشکار
class damagedwhen (models.TextChoices):
    RECENT_MONTHS = 'RM',' ماه های اخیر'
    EARLIER = 'E', 'قبلتر'

#مدل های مجموعه موجودیت ها
#مدل باشگاه
class Gyms (models.Model):
    #اسم =کلید اصلی
    name = models.CharField(primary_key=True)
    workingtime=
    manager_name = models.CharField(unique=True)
    manager_cv = models.TextField()
    manager_password = models.CharField(max_length=15)
    facilities = models.TextField()
    capacity = models.PositiveSmallIntegerField(max_length=100)
    numberofmachines = models.IntegerField()
    numberofworkers=
    foundationdate = models.DateField()
    email = models.EmailField()
    phonenumber = models.PositiveIntegerField(max_length=11)
    address=
    tuition =

    def __str__(self) -> str:
        return self.name

#مدل ورزشکاران
class bodybuilders (models.Model):
    firstname = models.CharField()
    lastname = models.CharField()
    gender = models.CharField (max_length= 2, choices=Gender.choices , default=Gender.FEMALE)
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    nationalcode = models.PositiveSmallIntegerField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    phonenumber = models.PositiveIntegerField(max_length=11)
    aim = models.TextField()
    illness = models.TextField()
    birthdate = models.DateField()
    age = 

    def __str__(self) -> str:
        return self.firstname

    
#مدل ورکتایمز
class work_times (models.Model):
    #گزینه های انتخاب زمان کاری: خدمه یا مربی؟
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
    day = models.CharField(choices=weekdays.choices)
    start = models.TimeField()
    end = models.TimeField()
    coach_crew = models.CharField(max_length=2 , choices=who_works.choices)

    def __str__(self) -> str:
        return str([self.day,self.start,self.end])
    
#مدل کارکنان
class workers (models.Model):
    nationalcode = models.PositiveSmallIntegerField(primary_key=True)
    firstname = models.CharField()
    lastname = models.CharField()
    gender = models.CharField (max_length= 2, choices=Gender.choices , default=Gender.FEMALE)
    password = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.firstname
    
#مدل مربیان
class coaches (workers):
    sport_degree =models.TextField()
    experience = models.TextField()
    
#مدل حرکات
class movements(models.Model):
    #کلید اصلی= نام
    name = models.CharField(primary_key=True)
    machine_name = models.CharField()
    body_part =
    image = models.ImageField()

    def __str__(self) -> str:
        return self.name
    
#مدل آسیب ها
class damages(models.Model):
    body_part= models.CharField()
    what =  models.CharField(max_length=100)
    when = models.CharField(max_length= 2 ,choices=damagedwhen.choices ,default=damagedwhen.EARLIER)

    def __str__(self) -> str:
        return self.what


#مدل های مجموعه ارتباط هایی که به شکل مجموعه موجودیت در آمده اند
#مدل قرارداد
class Agreement(models.Model):
    #id = خودکار
    hours = 
    salary =

#مدل برنامه(ورزشی)
class program(models.Model):
    finish_date = models.DateField(null=True)
    tuition =
    howmany_days =

#مدل عضویت
#مدل 


#مدل های مجموعه ارتباط ها(مدل های میانی/واسطه)
#عضویت در کدام باشگاه؟
#کدام ورزشکاران عضو باشگاه اند؟
#رزرو
#ورزشکار-برنامه 
#برنامه نویسی(مربی -برنامه)
#قرارداد-باشگاه
#قرارداد_ورک تایم
#قرارداد -کارکنان
#آسیب - ورزشکار