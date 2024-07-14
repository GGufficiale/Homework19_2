from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def index(request):
    """Функция принимает параметр request (инфа от пользователя на фротэнде) и возвращает ответ"""
    if request.method == "POST":
        """В request хранится информация о методе, который отправлял пользователь"""
        name = request.POST.get('name')
        """И передается информация, которую заполнил пользователь"""
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'main/index.html')
