from django.shortcuts import render

# Halaman Depan (Home) - INI YANG TADI HILANG
def home(request):
    return render(request, 'home.html')

# Halaman Career (Versi Baru dengan Pesan Sukses)
def career(request):
    # Cek apakah ada tanda '?success=true' di alamat URL dari FormSubmit
    pesan_sukses = None
    if request.GET.get('success') == 'true':
        pesan_sukses = "✅ ALHAMDULILLAH! Lamaran Anda berhasil terkirim. Tim HRD kami akan segera memeriksanya."

    # Kita tidak perlu logika email python di sini lagi
    # Karena HTML form sudah menanganinya langsung via FormSubmit
    return render(request, 'career.html', {'pesan_sukses': pesan_sukses})

# Halaman Lainnya (Jangan sampai hilang lagi)
def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def faq(request):
    return render(request, 'faq.html')
