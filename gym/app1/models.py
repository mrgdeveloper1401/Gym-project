from django.db import models

# Create your models here.
# گزینه های انتخاب جنسیت
class Gender(models.TextChoices):
    FEMALE = 'FM','Female'
    MALE = 'ML','Male'

#گزینه های انتخاب روز هفته
class weekdays(models.TextChoices):
    SHANBE = 'SHA','Sanbe'
    YEKSHANBE = '1SH','1shanbe'
    DOSHANBE = '2SH','2shanbe'
    SESHANBE = '3SH','3shanbe'
    CHARSHANBE = '4SH','4shanbe'
    PANJSHANBE = '5SH','5shanbe'
    JOMEE = 'JOM','Jomee'

#گزینه های انتخاب زمان کاری: خدمه یا مربی؟
class who_works (models.TextChoices):
    COACH = 'CO','coach'
    CREW = 'CR','crew'

#گزینه های انتخاب زمان آسیب دیدن ورزشکار
class damagedwhen (models.TextChoices):
    RECENT_MONTHS = 'RM',' ماه های اخیر'
    EARLIER = 'E', 'قبلتر'

#مدل باشگاه
class Gyms (models.Model):
    #اسم =کلید اصلی
    name=
    workingtime=
    manager_name =
    manager_cv =
    manager_password =
    facilities = models.TextField()
    capacity = models.PositiveSmallIntegerField(max_length=100)
    numberofmachines = models.IntegerField()
    numberofworkers=
    foundationdate = models.DateField()
    email = models.EmailField()
    phonenumber = 
    address=
    tuition =

#مدل ورزشکاران
class bodybuilders (models.Model):
    #کدملی = کلید اصلی
    firstname = models.CharField()
    lastname = models.CharField()
    gender = models.CharField (max_length= 2, choices=Gender.choices , default=Gender.FEMALE)
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    nationalcode=
    email = models.EmailField()
    password =
    phonenumber = 
    aim = models.TextField()
    illness = 
    birthdate = models.DateField()
    age = 

    
#مدل ورکتایمز
class work_times (models.Model):
    #id خودکار
    day = models.CharField(choices=weekdays.choices)
    start = models.TimeField()
    end = models.TimeField()
    coach_crew = models.CharField(max_length=2 , choices=who_works.choices)
    
#مدل کارکنان
class workers (models.Model):
    #کد ملی کلید اصلی
    firstname = models.CharField()
    lastname = models.CharField()
    gender = models.CharField (max_length= 2, choices=Gender.choices , default=Gender.FEMALE)
    nationalcode=
    password=
    
#مدل مربیان
class coaches (workers):
    sport_degree =
    experience = models.TextField()
    
#مدل حرکات
class movements(models.Model):
    #کلید اصلی= نام
    name = 
    machine_name = models.CharField()
    body_part =
    image = models.ImageField()
    
#مدل آسیب ها
class damages(models.Model):
    body_part= models.CharField()
    what =  models.CharField(max_length=100)
    when = models.CharField(max_length= 2 ,choices=damagedwhen.choices ,default=damagedwhen.EARLIER)