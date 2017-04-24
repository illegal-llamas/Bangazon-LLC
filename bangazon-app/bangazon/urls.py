from django.conf.urls import url, include
from rest_framework import routers
from bangazon.api import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'producttypes', views.ProductTypeViewSet)
router.register(r'employeetypes', views.EmployeeTypeViewSet)
router.register(r'computers', views.ComputerTypeViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
