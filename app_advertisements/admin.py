from django.contrib import admin
from .models import Advertisement

class Advertisements_admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'description', 'price', 'auction', 'created_date', 'updated_date', 'image', 'image_preveuw'] # здесь прописываем отображаемые поля БД
    list_filter = ['auction', 'created_at']  # добавляем возможность фильтрации
    actions = ['make_auction_as_false', 'make_auction_as_true', 'image_preveuw'] # чтобы action работал, для него нужно создать функцию

    # добавляет разделение на подразделы при добавлении нового объекта
    fieldsets = (
        ('Общее', {
            'fields' : ('title', 'description', 'user', 'image'),
            'classes': ['collapse']
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']   # чтобы можно было сворачивать поле
        }),
    )
    @admin.action(description="Убрать возможность торга")
    def make_auction_as_false(self, request, queryset):  # request - запрос, queryset - набор объектов, с которым надо сделать action
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


# Управляем классом Advertisement через класс Advertisements_admin
admin.site.register(Advertisement, Advertisements_admin)

# Register your models here.
