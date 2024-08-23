from django.urls import path

from .views import (
    CategoryAPIView,
    CategoryListView,
    StartStepTestView,
    StartSubjectApi,
    StepDetailAPIView,
    SubjectTitleApiView,
    UserPopularSubject,
    SubjectSearchApiView,
    UserSubjectListApiView,
)

urlpatterns = [
    path("category/<int:pk>/", CategoryAPIView.as_view(), name="category-subject"),
    path(
        "start-subject/<int:subject_id>/",
        StartSubjectApi.as_view(),
        name="start-subject",
    ),
    path("subject-titles/", SubjectTitleApiView.as_view(), name="subject-titles"),
    path("userpopularsubject/", UserPopularSubject.as_view(), name="userpopularsubject"),
    path("categories/", CategoryListView.as_view(), name="categories"),
    path("steps/<int:pk>/", StepDetailAPIView.as_view(), name="step-detail"),
    path("steps/start-test/", StartStepTestView.as_view(), name="step-start-test"),
    path("subject-search/", SubjectSearchApiView.as_view(), name="subject-search"),
    path("user-subject-list/", UserSubjectListApiView.as_view(), name="user-subject-list"),
]