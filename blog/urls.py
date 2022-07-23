from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

#to make it more specific
app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bloghome, name='blog_home'),
    path('blogprojects/', views.blogprojects, name='blogprojects'),
    path('<int:blog_id>/', views.detail, name='detail'),
    #blog_id is the name given by us to refer whtever int comes after blog/
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
