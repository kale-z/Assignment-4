"""DjUniFormCss URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import re_path
from django.contrib import admin
from mysite.views import *
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^addastudent/$',addastudent),
    re_path(r'^all-students/$',all_students),
    re_path(r'^addateacher/$',addateacher),
    re_path(r'^all-teachers/$',all_teachers),
    re_path(r'^addacourse/$',addacourse),
    re_path(r'^all-courses/$',all_courses),
    re_path(r'^enrollstudents/$',enrollstudents),
    re_path(r'^enrolledstudents/(\d+)$',enrolledstudents),

]