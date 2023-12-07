from django.urls import path

from . import views


urlpatterns = [
    path('faqs/', views.FaqListAPIView.as_view()),
    path('contract/create/', views.ContractCreateAPIView.as_view()),
]
