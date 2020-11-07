from django.contrib import admin
from .models import Cat1, Cat2, Cat3, Cat4, Cat5, Comment, Comment2, Comment3, Comment4, Comment5

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class CommentInline2(admin.TabularInline):
    model = Comment2
    extra = 0

class CommentInline3(admin.TabularInline):
    model = Comment3
    extra = 0

class CommentInline4(admin.TabularInline):
    model = Comment4
    extra = 0

class CommentInline5(admin.TabularInline):
    model = Comment5
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
    CommentInline,
]

class ArticleAdmin2(admin.ModelAdmin):
    inlines = [
    CommentInline2,
]

class ArticleAdmin3(admin.ModelAdmin):
    inlines = [
    CommentInline3,
]

class ArticleAdmin4(admin.ModelAdmin):
    inlines = [
    CommentInline4,
]

class ArticleAdmin5(admin.ModelAdmin):
    inlines = [
    CommentInline5,
]

admin.site.register(Cat1, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Cat2, ArticleAdmin2)
admin.site.register(Comment2)
admin.site.register(Cat3, ArticleAdmin3)
admin.site.register(Comment3)
admin.site.register(Cat4, ArticleAdmin4)
admin.site.register(Comment4)
admin.site.register(Cat5, ArticleAdmin5)
admin.site.register(Comment5)
