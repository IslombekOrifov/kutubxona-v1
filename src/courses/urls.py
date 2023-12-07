from django.urls import path

from . import views


urlpatterns = [
    path('online/list/', views.OnlineCoursesAPIView.as_view()),
    path('offline/list/', views.OfflineCoursesAPIView.as_view()),
    path('detail/<pk>/', views.CourseDetailAPIView.as_view()),
]
