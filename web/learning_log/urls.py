"""
URL configuration for learning_log project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.contrib import admin
from django.urls import include ,path,re_path


#配置 Django Admin 后台，访问路径是 /admin/
#''表示匹配根路径（如 http://127.0.0.1:8000/）。
#include(('learning_logs.urls', 'learning_logs'), namespace='learning_logs')
#引入了 learning_logs应用的 urls.py文件。
# ('learning_logs.urls', 'learning_logs'):
#第一个参数 'learning_logs.urls'是要包含的 URL 模块。
#第二个参数 'learning_logs'是 app_name（应用的命名空间）。
#namespace='learning_logs'：
#这是项目的 URL 命名空间（Django 3.1+ 要求同时提供 app_name和 namespace）。

urlpatterns = [
    path('admin/', admin.site.urls),#后台地址
    path('', include(('learning_logs.urls', 'learning_logs'), namespace='learning_logs')),
    re_path(r'^users/', include(('users.urls', 'users'), namespace='users')),

]


