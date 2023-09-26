from django.contrib import admin

from .models import Article

# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","date")
    class Meta:
   
        db_table = 'ModelName1'
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'