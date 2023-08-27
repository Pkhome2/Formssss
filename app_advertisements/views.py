from django.shortcuts import render
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse
from django.shortcuts import redirect



def index(request):
    '''Здесь мы берём все объекты базы данных (Из созданного нами в моделс.ру класса Advertisement)
        с помощью метода objects.all (метод берётся из класса Моделс от Джанго)'''

    advertisement = Advertisement.objects.all()
    #advertisement - Это у нас итерируемый объект QuerySet, который имеет такой вид
    ''' QuerySet[ < Advertisement: Advertisement(id=1,title=Объявление №1, price = 100.00) >,
     < Advertisement: Advertisement(id=2, title=Продаю ноутбук, price = 40000.00) >] '''

    # объявляем параметр контекст, который будет отвечать за перенос каких-то переменных в слой темплейт (то есть, собственно на страницы HTML, который должен быть словарём
    # В данном случае мы передаём в контекст всю информацию из БД
    # по такой же схеме будерм работать в index.html
    # for i in advertisement:
    #     print(i.id, i.price, i.title )
    # цикл фор в файле html будет работать по ключу в указанном ниже словаре context

    context = {"advertisement" : advertisement}
    return render(request, "index.html", context=context)  # можно вместо context=context просто context


def top_sellers(request):
    return render(request, "top-sellers.html")


def advertisement_post(request):
    # если пришёл запрос от пользователя на добавление инормации
    if request.method == "POST":
        # заполняем форму информацией, которую прислал пользователь
        form = AdvertisementForm(request.POST, request.FILES)
        # Если форма заполнена верно
        if form.is_valid():
            # создаём новый объект объявления (объект класса Advertisement из models.py)
            advertisement = Advertisement(**form.cleaned_data)
            # добавляем туда пользователя, остновываясь на пользователя, который отправил форму
            advertisement.user = request.user
            # сохраняем
            advertisement.save()
            # формируем ссылку на переход на остновную страницу
            url = reverse("")
            # выполняем переход
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, "advertisement-post.html", context)


def login(request):
    return render(request, "login.html")


def profile(request):
    return render(request, "profile.html")


def register(request):
    return render(request, "register.html")


