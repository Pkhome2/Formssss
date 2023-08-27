from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model  # получаем ДБ пользователей (модель)

User = get_user_model()


class Advertisement(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete= models.CASCADE)
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2)
    auction = models.BooleanField('Запрос скидки', help_text='Отметьте, если скдидки возможны')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField('Изображение', upload_to= 'advertisement/')

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'
    class Meta:
        db_table = 'advertisements'

    @admin.display(description="Дата созадния")
    def created_date(self):
        from django.utils import timezone, html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return html.format_html("<span style='color:green; font-weight: bold;'> Сегодня в {} </span>", created_time)
        return self.created_at.strftime("%d.%m.%y в %H:%M:%S")

    @admin.display(description="Дата обновления")
    def updated_date(self):
        from django.utils import timezone, html
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return html.format_html("<span style='color:green; font-weight: bold;'> Сегодня в {} </span>", updated_time)
        return self.updated_at.strftime("%d.%m.%y в %H:%M:%S")

    @admin.display(description="Картинка")
    def image_preveuw(self):
        from django.utils import html
        return html.format_html('<img src="{}" alt="", style= "width:60px; height:60px">', self.image.url)
