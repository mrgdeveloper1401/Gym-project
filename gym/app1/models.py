from django.db import models

# Create your models here.


#مدل باشگاه
class Gyms (models.Model):
    #اسم =کلید اصلی
    '''name=
    workingtime=
    manager=
    facilities=
    capacity=
    numberofmachines=
    numberofworkers=
    foundationdate=
    email=
    phonenumber=
    address=
    tuition='''

#مدل ورزشکاران
class bodybuilders (models.Model):
    #کدملی = کلید اصلی
    '''firstname=
    lastname =
    gender = 
    height =
    weight =
    nationalcode=
    email = 
    password =
    phonenumber = 
    aim = 
    illness =
    birthdate=
    age =

    '''
#مدل ورکتایمز
class work_times (models.Model):
    #id خودکار
    '''day =
    start=
    end=
    coach_crew=
    '''
#مدل کارکنان
class workers (models.Model):
    #کد ملی کلید اصلی
    '''firstname=
    lastname= 
    gender=
    nationalcode=
    password=
    '''
#مدل مربیان
class coaches (workers):
    '''cv=
    experience=
    '''
#مدل حرکات
class movements(models.Model):
    #کلید اصلی= نام
    '''name = 
    machine_name=
    body_part=
    image=
    '''
#مدل آسیب ها
class damages(models.Model):
    '''body_part=
    what=
    when='''