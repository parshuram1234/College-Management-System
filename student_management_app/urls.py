from django.contrib import admin
from django.urls import path, include
from student_management_app import views
from student_management_app import StudentViews, StaffViews, HodViews


urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.loginUser, name="login"),
    #path('logout_user', views.logout_user, name="logout_user"),
    #path('registration', views.registration, name="registration"),
    path('doLogin', views.doLogin, name="doLogin"),
    path('doRegistration', views.doRegistration, name="doRegistration"),


    # URLS for Student
    path('student_home/', StudentViews.student_home, name='student_home'),

    # URLS for Staff
    path('staff_home/', StaffViews.staff_home, name='staff_home'),

    # URLS for Admin
    path('admin_home/', HodViews.admin_home, name='admin_home'),
]
# https://codingbowl.com/blog/setting-hostname-windows-django-local-lan/
#https://video.search.yahoo.com/search/video;_ylt=Awr48tMmBEhpsasNPctXNyoA;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3Nj?type=E210US714G91912&p=how+to+deploy+django+application+gunicorn+with+apache+windows+system&fr=mcafee&turl=https%3A%2F%2Ftse4.mm.bing.net%2Fth%2Fid%2FOVP.h8BvOd4DfXTHeJP9ozNGjwHgFo%3Fpid%3DApi%26w%3D296%26h%3D156%26c%3D7%26p%3D0&rurl=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DKItpu15ZmkY&tit=How+To+Deploy+Django+on+Windows+server+Using+Apache&pos=21&vid=a633cf91d900224d66075446ba819bf1&sigr=KN88HQ87xjHP&sigt=GCdQ0F7iVgQC&sigi=KQdzR14qh_uq
# how to deploy django application gunicorn with apache windows system