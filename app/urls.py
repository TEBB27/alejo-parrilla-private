from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from . import views
from .views import menuListByCategory
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'menu', views.menuViewSet)
router.register(r'contact', views.contactViewSet)
router.register(r'booking',views.bookingViewSet)
router.register(r'recomendation', views.recomendationViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('docs/', include_docs_urls(title = 'probe API')),
    path('menu_item/by_category/<str:category>/', menuListByCategory.as_view()),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)