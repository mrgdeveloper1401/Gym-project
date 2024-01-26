from collections.abc import Iterable
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,UserManager,BaseUserManager
from django.db import models
from PIL import Image
from django.utils import timezone
from datetime import date
# Create your models here.  
#✅= کلاس نویسی
#✅✅= ران و دیباگ



#گزینه های انتخاب کارکن: خدمه یا مربی؟🔵✅
class who_works (models.TextChoices):
    COACH = 'CO','مربی'
    CREW = 'CR','خدمه'
#گزینه های انتخاب روز هفته🔵✅
class weekdays(models.TextChoices):
    SHANBE = 'SHA','شنبه'
    YEKSHANBE = '1SH','یکشنبه'
    DOSHANBE = '2SH','دوشنبه'
    SESHANBE = '3SH','سه شنبه'
    CHARSHANBE = '4SH','چهارشنبه'
    PANJSHANBE = '5SH','پنجشنبه'
    JOMEE = 'JOM','جمعه'
#گزینه های انتخاب زمان آسیب دیدن 🔵✅
class damagedwhen (models.TextChoices):
    RECENT_MONTHS = 'RM',' ماه های اخیر'
    EARLIER = 'E', 'قبلتر'
# گزینه های انتخاب جنسیت🔵✅
class Gender(models.TextChoices):
    FEMALE = 'FM','Female'
    MALE = 'ML','Male'
#گزینه های انتخاب تعداد روز برنامه ورزشی✅
class program_days(models.TextChoices):
    two = 'two', 'دو جلسه ای'
    three = 'three', 'سه جلسه ای'
    four = 'four', 'چهار جلسه ای'
#گزینه های انتخاب استان✅
class province(models.TextChoices):
    ardebil = 'ardebil','اردبیل'
    esfahan='esfahan', "اصفهان"
    alborz= 'alborz', "البرز"
    ilam = 'ilam' ,"ایلام"
    azarsharq ='azarsharq', "آذربایجان شرقی"
    azarqarb = 'azarqarb', "آذربایجان غربی"
    bushehr= 'bushehr', "بوشهر"
    tehran ='tehran', "تهران"
    charmahal='charmahal', "چهارمحال وبختیاری"
    khorasanj='khorasanj', "خراسان جنوبی"
    khorasanr='khorasanr', "خراسان رضوی"
    khorasansh='korasansh', "خراسان شمالی"
    khuzestan='khuzestan', "خوزستان"
    zanjan='zanjan', "زنجان"
    semnan='semnan', "سمنان"
    sistan='sistan', "سیستان وبلوچستان"
    fars='fars', "فارس"
    qazvin='qazvin', "قزوین"
    qom='qom', "قم"
    kord='kord', "کردستان"
    kerm='kerm', "کرمان"
    kermanshah = 'kermanshah', 'کرمانشاه'
    kohgiluyeh = 'kohgiluyeh', 'کهگیلویه وبویراحمد'
    golestan = 'golestan', 'گلستان'
    gilan = 'gilan', 'گیلان'
    lorestan = 'lorestan', 'لرستان'
    mazandaran = 'mazandaran', 'مازندران'
    markazi = 'markazi', 'مرکزی'
    hormozgan = 'hormozgan', 'هرمزگان'
    hamadan = 'hamadan', 'همدان'
    yazd = 'yazd', 'یزد'


#مدل حرکات ورزشی🔵✅
class movements(models.Model):
    name = models.CharField(primary_key=True,max_length=25)
    machine_name = models.CharField(max_length=15)
    body_part = models.TextField()
    image = models.ImageField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name
#مدل ورکتایمز🔵✅
class work_time(models.Model):

    day = models.CharField(choices=weekdays.choices,max_length=10)
    start = models.TimeField()
    end = models.TimeField()
    durationtime = models.DurationField(null=True,blank=True)
    coach_crew = models.CharField(max_length=2 , choices=who_works.choices)

    #ذخیره خودکار مدت زمان
    def save(self):
        if self.start and self.end  and self.start < self.end:
            self.durationtime = self.end -self.start
        else:
            self.durationtime = 0
        super().save()

    def __str__(self):
        return str(self.day,self.start,self.end)
#مدل آسیب ها🔵✅  
class damage(models.Model):

    body_part= models.CharField(max_length=20)
    what =  models.CharField(max_length=100)
    when = models.CharField(max_length=10 ,choices=damagedwhen.choices ,default=damagedwhen.EARLIER)

    def __str__(self) -> str:
        return self.what


#ساخت یوزرهای سفارشی🔵✅ 
class custom_user(AbstractUser):
    objects = UserManager()
    email = models.EmailField(primary_key=True)
    is_gymManager = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_crew = models.BooleanField(default=False)
    is_bodybuilder = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
#sqlite3 your_database_name.db
#.schema app1_custom_user


#مدل های مجموعه موجودیت ها
    
#مدل باشگاه(مدیرباشگاه)🔵✅
class Gym(models.Model):
    user = models.OneToOneField(custom_user, on_delete=models.PROTECT,primary_key = True, related_name = 'gym')
    #نام مدیر باشگاه، ایمیل، شماره تلفن، جنسیت --> مدل یوزرسفارشی   
    gender = models.CharField (max_length= 2, choices=Gender.choices , default=Gender.FEMALE)
    phonenumber = models.IntegerField(null=True,blank = True)

    manager_cv = models.TextField(blank=True, null = True)
    gym_name = models.CharField(unique=True,max_length=20)
    foundationdate = models.DateField()
    facilities = models.TextField()
    capacity = models.PositiveSmallIntegerField()
    numberofmachines = models.IntegerField()
    numbofworkers= models.IntegerField(default=0)
    #address fields 
    province = models.CharField(max_length= 20,choices = province.choices,default = province.gilan)
    city = models.CharField(max_length = 20)
    street= models.CharField(max_length= 20)
    valley= models.CharField(max_length=15)
    building = models.CharField(max_length = 15)
    address =models.JSONField(default= dict,blank= True)
    #tuition fields
    program_price = models.DecimalField(max_digits= 10, decimal_places= 2)
    tuition_8_sessions = models.DecimalField(max_digits=10, decimal_places=2)
    tuition_12_sessions = models.DecimalField(max_digits=10, decimal_places=2)
    tuition_16_sessions = models.DecimalField(max_digits=10, decimal_places=2)
    tuition = models.JSONField(default= dict,blank= True)
   
    workingtime = models.JSONField(null = True,blank=True)#🟥

    #تابع محاسبه و ذخیره سازی تعداد کارکنان، آدرس ، شهریه و زمان کاری
    def save(self,*args, **kwargs):

        #تعداد کارکنان
        num_workers = Agreement.objects.filter(gym = self).count()
        self.numofworkers = num_workers

        #آدرس
        self.address = {
            'province': self.province,
            'city': self.city,
            'street': self.street,
            'valley': self.valley,
            'building': self.building
        }

        #شهریه
        self.tuition = {
            'program_price': self.program_price,
            'training_price': {
                '8_sessions': self.tuition_8_sessions,
                '12_sessions': self.tuition_12_sessions,
                '16_sessions': self.tuition_16_sessions
            }
        }

        #زمان کاری🟥
        self.workingtime = Agreement.objects.filter(gym = self,coach_crew = "CO").values('work_times')

        super().save(*args,**kwargs)

    def __str__(self):
        return self.gym_name

#مدل ورزشکاران🔵✅
class bodybuilder (models.Model):
    user = models.OneToOneField(custom_user, on_delete = models.PROTECT, primary_key = True, related_name = 'bodybuilder')
    #نام ورزشکار، ایمیل، شماره تلفن، جنسیت --> مدل یوزرسفارشی    
    gender = models.CharField (max_length= 2, choices=Gender.choices , default=Gender.FEMALE)
    phonenumber = models.IntegerField(null=True,blank = True)

    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    aim = models.TextField()
    illness = models.TextField(null = True,blank=True)
    birthdate = models.DateField(null=True)
    age = models.IntegerField(null = True,blank = True)
    Damage = models.ManyToManyField(damage,related_name="who_damaged",blank=True)
    
    #تابع برای ذخیره سازی خودکار سن
    def save(self):
        today = date.today()
        birthdate = self.birthdate
        self.age = today.year - birthdate.year - ((today.month,today.day)<(birthdate.month,birthdate.day))
        return super().save()

'''from app1.models import bodybuilder,custom_user
from datetime import date
ali = bodybuilder(username='ali',email = 'a@gmail.come',phonenumber = 1234,height = 120,weight =51,aim=' ',birthdate = date(2002,1,1))
ali.save()
     '''

    
#مدل مربیان🔵✅
class coach (models.Model):
    user = models.OneToOneField(custom_user, on_delete = models.PROTECT,primary_key = True, related_name = 'coach')
    #نام مربی، ایمیل، شماره تلفن، جنسیت --> مدل یوزرسفارشی      
    gender = models.CharField (max_length= 2, choices=Gender.choices , default=Gender.FEMALE)
    phonenumber = models.IntegerField(null=True,blank = True)

    sport_degree =models.TextField()
    experience = models.TextField(blank =True,null =True)  
#مدل خدمه🔵✅
class crew (models.Model):
    
    user = models.OneToOneField(custom_user, on_delete = models.PROTECT, primary_key = True, related_name = 'crew')
    gender = models.CharField (max_length= 2, choices=Gender.choices , default=Gender.FEMALE)
    phonenumber = models.IntegerField(null=True,blank = True)


#مدلهای مجموعه ارتباط هایی که به شکل مجموعه موجودیت در آمده اند
#مدل قرارداد🔵✅
class Agreement(models.Model):
    start_date=models.DateField()
    end_date=models.DateField()
    Hours=models.DurationField(blank=True,default = 0)
    salary=models.DecimalField(max_digits=5,decimal_places=2)

    #شرکت کنندگان در قرارداد
    gym = models.ForeignKey(Gym,on_delete =models.CASCADE,related_name = 'agreements' )
    coach_crew = models.CharField(max_length = 2, choices = who_works.choices)
    coach = models.ForeignKey(coach,on_delete=models.CASCADE,related_name = 'agreements',null = True)
    crew = models.ForeignKey(crew,on_delete= models.CASCADE,related_name = 'agreements',null = True )
    work_times = models.ManyToManyField(work_time,related_name='agreements')

    #محاسبه ساعات کار🟥
    def save(self,*args, **kwargs):
        for duration in self.work_times.objects.values('duration'):
            self.Hours += duration
        super().save(*args,**kwargs)

#مدل برنامه(ورزشی)🔵✅
class program(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    howmany_days = models.CharField(max_length=6,choices = program_days.choices)
    tuition = models.DecimalField(max_digits=10,decimal_places=2)
    coach = models.ForeignKey(coach,on_delete= models.DO_NOTHING,related_name = "programs")
    bodybuilder = models.ManyToManyField(bodybuilder,related_name="programs")
    movements = models.ManyToManyField(movements, related_name='programs')
'''
class Reservation (models.Models):
    class custom_user = models.ForeignKey(class custom_user,on-delet=models.CASCADE)
    START_date = models.DateField()
    End_date = models.DateField()
    Reservatio_type = models.CharField(max_length=100)
    Payment_status = models.BooleanField()
    
    def __str__(self):
        return
    f"{self.custom_user.username}
    Reservation"
    
'''
#مدل عضویت🔵✅
class Membership(models.Model):
    gym = models.ForeignKey(Gym,on_delete=models.CASCADE, related_name = 'memberships')
    bodybuilder = models.ForeignKey(bodybuilder, on_delete = models.CASCADE, related_name= 'memberships')


#رزرو🔵✅
class Reserve(models.Model):
    member = models.ManyToManyField(Membership,related_name='reservations')
    work_time = models.ManyToManyField(work_time,related_name= 'reservations')
  







