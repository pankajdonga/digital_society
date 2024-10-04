from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import *

# ********
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
# ********


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('',views.userlogin),
    path('index/',views.index,name='index'),
    path('signup/',views.signup),
    path('verifyotp/',views.verifyotp, name='verifyotp'),
    path('invoiceReport/<int:id>',views.invoiceReport, name='invoiceReport'),
    path('notice/',views.notice, name='notice'),
    path('event/',views.event,name='event'),
    path('societymember/',views.societymember),
    path('watchman/',views.watchman),
    path('profile/',views.profile),
    path('user_logout/',views.user_logout),
    path('pdf/',views.pdf, name='pdf'),

    # Password reset url
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='socmember/password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='socmember/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='socmember/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name='socmember/password_reset_complete.html'),name='password_reset_complete'),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)