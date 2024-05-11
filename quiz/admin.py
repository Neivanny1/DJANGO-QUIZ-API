from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]

    search_fields = [
        'name',
    ]

@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]
    search_fields = [
        'title',
    ]
class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text', 
        'is_right'
        ]
@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
        ]
    list_display = [
        'title', 
        'quiz',
        'date_updated'
        ]
    inlines = [
        AnswerInlineModel, 
        ]
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text', 
        'is_right', 
        'question'
        ]