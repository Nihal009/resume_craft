from django.urls import path
from .views import ResumeJobAPIView

urlpatterns=[
    path('api/resume-job/',ResumeJobAPIView.as_view(),name='resume_job_api')
]