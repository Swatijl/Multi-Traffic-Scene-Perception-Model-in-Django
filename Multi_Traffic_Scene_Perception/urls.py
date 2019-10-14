"""Multi_Traffic_Scene_Perception URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from Multi_Traffic_Scene_Perception import settings
from user import views as view_user
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('^$',view_user.index,name="index"),
    url('user/register', view_user.register, name="register"),
    url('user/homepage',view_user.homepage,name="homepage"),
    url('user_uplolad_page',view_user.user_uplolad_page,name="user_uplolad_page"),
    url(r'^gryscale/(?P<pk>\d+)/$',view_user.gryscale,name='gryscale'),
    url(r'^viewlist/(?P<pk>\d+)/$',view_user.viewlist,name='viewlist'),
    url('traffic_images',view_user.traffic_images,name="traffic_images"),
    url('categoryanalysis/(?P<chart_type>\w+)',view_user.categoryanalysis_chart,name="categoryanalysis_chart"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

