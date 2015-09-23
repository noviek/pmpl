#from django.conf.urls import patterns, include, url
from django.conf.urls import url
#from django.contrib import admin
from lists import views

#urlpatterns = patterns('',
urlpatterns = [
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', views.home_page, name='home'),
    #url(r'^lists/new$', 'lists.views.new_list', name='new_list'),
    #url(r'^lists/(\d+)/$', 'lists.views.view_list', name='view_list'),
    #url(r'^lists/(\d+)/add_item$', views.add_item, name='add_item'),
    
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),
]    
    #url(r'^admin/', include(admin.site.urls)),
#)
