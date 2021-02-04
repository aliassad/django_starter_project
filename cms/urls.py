from django.urls import path
from cms.views import (
    HomePageView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='cms_main_page'),
    path('dashboard/', HomePageView.as_view(), name='cms_dashboard'),
]
