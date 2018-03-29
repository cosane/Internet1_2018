from django.shortcuts import render, HttpResponse

def home_view(request):
    if request.user.is_authenticated():
        context = {
            'isim': 'Efe Coşan',
            'şehir': 'Manisa'
        }
    else:
        context = {
            'isim': 'Misafir',
            'şehir': 'Bilinmeyen Şehir'
        }
    return render(request, 'home.html', context)
