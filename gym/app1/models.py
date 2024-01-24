from collections.abc import Iterable
from django.contrib.auth.models import AbstractUser
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
    image = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.name
#مدل ورکتایمز🔵✅
class work_time(models.Model):

    day = models.CharField(choices=weekdays.choices,max_length=10)
    start = models.TimeField()
    end = models.TimeField()
    durationtime = models.DurationField(null=True)
    coach_crew = models.CharField(max_length=2 , choices=who_works.choices)

    #ذخیره خودکار مدت زمان
    def save(self):
        if self.start and self.end  and self.start < self.end:
            self.durationtime = self.end -self.start
        else:
            self.durationtime = None
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
    is_gymManager = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_crew = models.BooleanField(default=False)
    is_bodybuilder = models.BooleanField(default=False)
    user_name = models.CharField(max_length=10)
    email = models.EmailField(primary_key=True)
    phonenumber = models.IntegerField()
    gender = models.CharField (max_length= 2, choices=Gender.choices , default=Gender.FEMALE)


#مدل های مجموعه موجودیت ها
    
#مدل باشگاه(مدیرباشگاه)🔵
class Gym(models.Model):
    user = models.OneToOneField(custom_user, on_delete=models.PROTECT,primary_key = True, related_name = 'gym')
    #نام مدیر باشگاه، ایمیل، شماره تلفن، جنسیت --> مدل یوزرسفارشی   
    manager_cv = models.TextField()
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
    #tuition =
    #workingtime
    #تابع محاسبه و ذخیره سازی تعداد کارکنان
    def update_num_of_workers(self):
        num_workers = Agreement.objects.filter(gym = self).count()
        self.numofworkers = num_workers
        self.save()

    #تابع برای پیدا کردن زمان کاری یک باشگاه🟥
    def find_gym_workingtime(self):
        #از قرارداد های این باشگاه که با مربی ها بسته شده، ورک تایم های مربوطه را فراخوانی کن 
        workingtime = Agreement.objects.filter(gym = self,coach_crew = "CO").values('work_times')
        return workingtime


    def __str__(self):
        return self.gym_name

#مدل ورزشکاران🔵✅
class bodybuilder (models.Model):
    user = models.OneToOneField(custom_user, on_delete = models.PROTECT, primary_key = True, related_name = 'bodybuilder')
    #نام ورزشکار، ایمیل، شماره تلفن، جنسیت --> مدل یوزرسفارشی       
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    aim = models.TextField()
    illness = models.TextField(null = True)
    birthdate = models.DateField(null=True)
    age = models.IntegerField(null = True,blank = True)
    Damage = models.ManyToManyField(damage,related_name="who_damaged",null=True)
    
    #تابع برای ذخیره سازی خودکار سن
    def save(self):
        today = date.today()
        birthdate = self.birthdate
        self.age = today.year - birthdate.year - ((today.month,today.day)<(birthdate.month,birthdate.day))
        return super().save()
    
    def __str__(self) -> str:
        return self.user.user_name
'''from app1.models import bodybuilder,custom_user
from datetime import date
ali = bodybuilder(user_name='ali',email = 'a@gmail.come',phonenumber = 1234,height = 120,weight =51,aim=' ',birthdate = date(2002,1,1))
ali.save()
     '''

    
#مدل مربیان🔵✅
class coach (models.Model):
    user = models.OneToOneField(custom_user, on_delete = models.PROTECT,primary_key = True, related_name = 'coach')
    #نام مربی، ایمیل، شماره تلفن، جنسیت --> مدل یوزرسفارشی       
    sport_degree =models.TextField()
    experience = models.TextField()
    
#مدل خدمه🔵✅
class crew (models.Model):
    user = models.OneToOneField(custom_user, on_delete = models.PROTECT, primary_key = True, related_name = 'crew')


#مدلهای مجموعه ارتباط هایی که به شکل مجموعه موجودیت در آمده اند
#مدل قرارداد🔴
class Agreement(models.Model):
    start_date=models.DateField()
    end_date=models.DateField()
    Hours=models.TimeField()
    salary=models.DecimalField(max_digits=5,decimal_place=2)

    #شرکت کنندگان در قرارداد
    gym = models.ForeignKey(Gym,on_delete =models.PROTECT,related_name = 'agreements' )
    coach_crew = models.CharField(max_length = 2, choices = who_works.choices)
    coach = models.ForeignKey(coach,on_delete=models.PROTECT,related_name = 'agreements',null = True)
    crew = models.ForeignKey(crew,on_delete= models.PROTECT,related_name = 'agreements',null = True )
    work_times = models.ManyToManyField(work_time,on_delete=models.PROTECT,related_name='agreements')

    #محاسبه ساعات کار
    def calculating_hours(self):
        pass
    #محاسبه دستمزد
    def calculating_salary(self):
        pass

#مدل برنامه(ورزشی)🔴
'''class program(models.Model):
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
    class Reservation = models.Foreignkey(class Reservation)'''
    

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





  







