from django.conf.urls import url, include
from rest_framework import routers
from bangazon.api import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'producttypes', views.ProductTypeViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
