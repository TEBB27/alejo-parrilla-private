from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'menu', views.menuViewSet)
router.register(r'contact', views.contactViewSet)
router.register(r'booking',views.bookingViewSet)
router.register(r'recomendation', views.recomendationViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('docs/', include_docs_urls(title = 'probe API'))
]