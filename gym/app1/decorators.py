# ساخت دکوریتور برای اینکه دسترسی به ویو ها را برای یوزر های مختلف محدود کنیم
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

#دکوریتور برای ویو ها که چک میکند آیا یوزری که لاگین کرده مدیر باشگاه است یا نه
#اگر نبود به صفحه لاگین برمیگرداند
def gymmanager_required(function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url='login'):
    
    actual_decorator = user_passes_test(
        lambda u:u.is_active and u.is_gymManager,  # بررسی اینکه آیا یوزر فعال است و آیا مدیرباشگاه است یا نه
        login_url=login_url,                    #اگر نبود،به صفحه لاگین برمیگرداند
        redirect_field_name=redirect_field_name)# اگر بود،به صفحه ی دیگری میبرد
    
   # if function:
    #    return actual_decorator(function)
    return actual_decorator


#دکوریتور برای ویو ها که چک میکند آیا یوزری که لاگین کرده ورزشکار است یا نه
#اگر نبود به صفحه لاگین برمیگرداند
def bodybuilder_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME,login_url='login'):

    actual_decorator = user_passes_test(
        lambda u:u.is_active and u.is_bodybuilder,  
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    #if function:
     #   return actual_decorator(function)
    return actual_decorator