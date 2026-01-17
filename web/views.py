from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def career(request):
    # Kita tidak perlu logika email di sini lagi
    # Karena HTML form sudah menanganinya langsung via FormSubmit
    return render(request, 'career.html')

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def faq(request):
    return render(request, 'faq.html')
