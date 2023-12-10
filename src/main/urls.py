from django.urls import path

from . import views


urlpatterns = [
    path('landing/', views.MainAPIView.as_view()),
    path('center/history/', views.CenterHistoryAPIView.as_view()),
    path('center/confirmation/', views.CenterConfirmationAPIView.as_view()),
    path('leaders/', views.LeadersAPIView.as_view()),
    path('center/structure/', views.CenterStructureAPIView.as_view()),
    path('documents/category/', views.DocumentCategoryAPIView.as_view()),
    path('documents/<pk>/', views.DocumentAPIView.as_view()),
    path('monitoring/fillial/<pk>/', views.BranchAPIView.as_view()),
    path('event/list/', views.EventListAPIView.as_view()),
    path('event/detail/<pk>/', views.EventDetailAPIView.as_view()),
    path('user/contact/', views.UserContactCreateAPIView.as_view()),
    path('news/detail/<pk>/', views.NewsDetailAPIView.as_view()),
    
]
