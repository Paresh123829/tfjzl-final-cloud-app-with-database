from django.contrib import admin

# Import all seven models.
from .models import (
    Course,
    Lesson,
    Instructor,
    Learner,
    Question,
    Choice,
    Submission,
)


# Display lessons inline when editing a course.
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Display choices inline when editing a question.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


# Define an inline for questions associated with a course.
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


# Configure the Course administration page.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# Configure the Question administration page.
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']


# Configure the Lesson administration page.
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# Register the models with Django Admin.
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)