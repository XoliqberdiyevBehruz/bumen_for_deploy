from django.contrib import admin

from .models import (
    Category,
    Club,
    ClubMeeting,
    Step,
    StepLesson,
    StepTest,
    Subject,
    SubjectTitle,
    TestAnswer,
    TestQuestion,
    UserSubject,
    UserTestResult,
    UserTotalTestResult,
    Vacancy,
)

admin.site.register(TestQuestion)


class SubjectTitleInline(admin.StackedInline):
    model = SubjectTitle
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "click_count")
    inlines = [SubjectTitleInline]


class SubjectInline(admin.StackedInline):
    model = Subject
    extra = 1


@admin.register(SubjectTitle)
class SubjectTitleAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    inlines = [SubjectInline]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type")


@admin.register(UserSubject)
class UserSubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
