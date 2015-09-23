#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from lists import views as list_views
from lists import urls as list_urls
#from django.contrib import admin


#urlpatterns = patterns('',
urlpatterns = [
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', views.home_page, name='home'),
    url(r'^$', list_views.home_page, name='home'),
    #url(r'^lists/new$', 'lists.views.new_list', name='new_list'),
    url(r'^lists/', include(list_urls)),
]
    #url(r'^lists/(\d+)/$', 'lists.views.view_list', name='view_list'),
    #url(r'^lists/(\d+)/add_item$', views.add_item, name='add_item'),
    
    #url(r'^admin/', include(admin.site.urls)),
#)
