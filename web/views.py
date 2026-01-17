from django.shortcuts import render
from django.core.mail import EmailMessage

# 1. LOGIKA HALAMAN HOME
def home(request):
    return render(request, 'home.html')

# 2. LOGIKA HALAMAN ABOUT
def about(request):
    return render(request, 'about.html')

# 3. LOGIKA HALAMAN FAQ
def faq(request):
    return render(request, 'faq.html')

# 4. LOGIKA HALAMAN CAREER (KIRIM EMAIL ADA DI SINI)
def career(request):
    pesan_status = ""
    if request.method == "POST":
        nama = request.POST.get('nama')
        posisi = request.POST.get('posisi_dilamar') # Tambahan baru
        email_pelamar = request.POST.get('email')
        file_cv = request.FILES.get('cv')

        if file_cv:
            subjek = f"Lamaran [{posisi}]: {nama}"
            isi = f"Halo HRD PT Dongcai,\n\nPelamar Baru untuk posisi: {posisi}\nNama: {nama}\nEmail: {email_pelamar}\n\nSilakan cek CV terlampir."
            
            email = EmailMessage(
                subject=subjek,
                body=isi,
                from_email='oziyy77@gmail.com',
to=['oziyy77@gmail.com'],

            )
            email.attach(file_cv.name, file_cv.read(), file_cv.content_type)
            
            try:
                email.send()
                pesan_status = "✅ Lamaran Berhasil Dikirim! Tunggu kabar dari HRD kami."
            except Exception as e:
                pesan_status = f"❌ Gagal kirim: {e}"

    return render(request, 'career.html', {'pesan': pesan_status})

def news(request):
    return render(request, 'news.html')
