"""schoolApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import rest_framework
from admissions import views as ad
from finance import views as fin
from restframework import views as re 


from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

from django.conf import settings
from django.conf.urls.static import static


import admissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newadm/', ad.addAdmissions),
    path('admreport/', ad.admissionReport, name='admreport'),
    path('home/', ad.homepage, name='home'),
    path('addnumbers/', ad.addnumbers),
    path('delete/<int:id>/', ad.deletestudent),
    path('admreport/delete/<int:id>', ad.deletestudent),
    path('update/<int:id>/', ad.updatestudent),
    path('treport/', login_required(ad.Teacherread.as_view()),name='trreport'),

    path('getteacher/<int:pk>/', login_required(ad.Getteacher.as_view())),
    path('treport/getteacher/<int:pk>/', login_required(ad.Getteacher.as_view())),


    path('insertteacher/', login_required(ad.Insertteacher.as_view())),


    path('updateteacher/<int:pk>/', login_required(ad.Updateteacher.as_view())),
    path('treport/updateteacher/<int:pk>/', login_required(ad.Updateteacher.as_view())),


    path('deleteteacher/<int:pk>/', login_required(ad.Deleteteacher.as_view())),
    path('treport/deleteteacher/<int:pk>/', login_required(ad.Deleteteacher.as_view())),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    
    
    

    
    



    



    
    


    

    path('selectclass/feecol/', fin.Feecollection),
    
    path('selectclass/feecol_10/', fin.Feecollection_10),
    path('feecol_10/', fin.Feecollection_10),

    path('selectclass/feecol_8/', fin.Feecollection_8),


    path('feecol/RegistrationForm/',fin.Registration),
    path('feedues/', fin.feeDuesReport),
    path('feecolreport/', fin.feeCollectionReport ),

    path('addblog/', fin.addblog ),
    path('viewblog/', fin.viewblog ),

    

    path('selectclass/',fin.selectclass),

    path('register/',ad.register, name='register'),
    path('',ad.signin, name='signin'),
    path('logout/', ad.logout, name='logout'),
    path('deleteaccount/', ad.deleteaccount),
    path('updateprofile/', ad.updateprofile),



    

    

    

    
    path('restread/', re.rest_read),
    path('restcreate/', re.rest_create),
    path('restupdate/<int:id>', re.rest_update),

    path('restdelete/<int:id>', re.rest_delete),
    


   
    
    path('about/', ad.about),
    path('aboutread/', ad.aboutread),


    path('listcreate/', re.Studentlistcreate.as_view()),
    path('delupdate/<int:pk>', re.Studentdelupdate.as_view()),





    #concerete api views

    path('listapi/', re.Studentlistapi.as_view()),

    path('createapi/', re.Studentcreateapi.as_view()),

    path('retrieveapi/<int:pk>', re.Studentretrieveapi.as_view()),
    path('updateapi/<int:pk>', re.Studentupdateapi.as_view()),
    path('destroyapi/<int:pk>', re.Studentdestroyapi.as_view()),




    path('lc/', re.Studentlc.as_view()),
    path('ru/<int:pk>', re.Studentru.as_view()),
    path('rd/<int:pk>', re.Studentrd.as_view()),
    path('rud/<int:pk>', re.Studentrud.as_view()),






    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
    


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
