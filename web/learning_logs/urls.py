from django.urls import path,re_path

from . import views

urlpatterns=[
    #r'^$'：这是一个正则表达式，
    # ^表示字符串开始，$表示字符串结束，所以它只匹配空路径（即网站的根 URL /）
    #views.index：指向 views.py中的 index视图函数。
    #name='index'：给这个 URL 模式命名，方便在模板或视图中使用 reverse('index')进行反向解析。
    re_path(r'^$', views.index, name='index'),

    re_path(r'^topics/$', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    re_path(r'^new_topic/$',views.new_topic,name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

]



