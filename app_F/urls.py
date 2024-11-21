from django.urls import path
from .views import stuRecordView, courseListView, enrollmentListView, instructorListView

urlpatterns = [
    path('s_record/', stuRecordView.as_view()),
    path('instructor/', instructorListView.as_view()),
    path('course/', courseListView.as_view()),
    path('enrollment/', enrollmentListView.as_view()),
]

