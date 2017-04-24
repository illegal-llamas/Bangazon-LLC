from django.conf.urls import url, include
from rest_framework import routers
from bangazon.api import views
from django.contrib import admin

#docs: http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
#routers models This router is similar to SimpleRouter as above, 
#but additionally includes a default API root view, that returns a response containing hyperlinks to all the list views. 
#It also generates routes for optional .json style format suffixes.
router = routers.DefaultRouter()
#docs: http://www.django-rest-framework.org/api-guide/routers/#usage
#There are two mandatory arguments to the register() method:
# prefix - The URL prefix to use for this set of routes.
# viewset - The viewset class
router.register(r'producttypes', views.ProductTypeViewSet)
router.register(r'paymenttypeinfo', views.CustomerPaymentTypeViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
