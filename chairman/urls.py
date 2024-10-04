from django.contrib import admin
from django.urls import path
from chairman import views

# ********
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
# ********

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('adminindex/',views.adminindex,name='adminindex'),
    path('adminmember/',views.adminmember,name='adminmember'),
    path('adminwatchman/',views.adminwatchman, name='adminwatchman'),
    path('adminnotice/',views.adminnotice, name='adminnotice'),
    path('adminevent/',views.adminevent, name='adminevent'),
    path('addmember/',views.addmember, name='addmember'),
    path('deletemember/<int:id>',views.deletemember, name='deletemember'),
    path('adminprofile/',views.adminprofile, name='adminprofile'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('createinvoice/',views.createinvoice, name='createinvoice'),
    path('addwatchman/',views.addwatchman, name='addwatchman'),
    path('deleteinvoice/<int:id>',views.deleteinvoice, name='deleteinvoice'),
    path('deletewatchman/<int:id>',views.deletewatchman,name='deletewatchman'),
    path('addevent/',views.addevent, name='addevent'),
    path('deleteevent/',views.deleteevent, name='deleteevent'),
]