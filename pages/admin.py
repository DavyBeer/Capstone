from django.contrib import admin
from .models import Cat1, Cat2, Cat3, Cat4, Cat5, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
    CommentInline,
]

admin.site.register(Cat1, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Cat2)
admin.site.register(Cat3)
admin.site.register(Cat4)
admin.site.register(Cat5)
