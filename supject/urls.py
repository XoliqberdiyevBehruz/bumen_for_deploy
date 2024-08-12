from django.urls import path
from .views import CategoryAPIView, StartSubjectApi, StartSubjectAPIView

urlpatterns = [
    path('category/<int:pk>/', CategoryAPIView.as_view(), name='category-subject'),
    path('start-subject/<int:subject_id>/', StartSubjectApi.as_view(), name='start-subject'),
    path('start_subject_list/', StartSubjectAPIView.as_view(), name='start-subject-list'),
]