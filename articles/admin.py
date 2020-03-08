from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class CustomArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Article, CustomArticleAdmin)
admin.site.register(Comment)