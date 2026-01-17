from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
import logging

# Siapkan pencatat error (agar muncul di Logs Hugging Face)
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')

def career(request):
    pesan_status = None

    if request.method == 'POST':
        try:
            # 1. Ambil data dari formulir
            posisi = request.POST.get('posisi_dilamar')
            nama = request.POST.get('nama')
            whatsapp = request.POST.get('no_hp')
            email_pelamar = request.POST.get('email')
            file_cv = request.FILES.get('cv') # Ambil file PDF

            # 2. Susun Judul & Isi Email
            judul_email = f"LAMARAN BARU: {posisi} - {nama}"
            isi_email = f"""
            Ada pelamar baru masuk via website!
            
            Nama: {nama}
            Posisi: {posisi}
            WhatsApp: {whatsapp}
            Email: {email_pelamar}
            
            Silakan cek lampiran PDF untuk melihat CV lengkapnya.
            """

            # 3. Siapkan Email (Pakai EmailMessage agar bisa kirim Lampiran/Attachment)
            email = EmailMessage(
                subject=judul_email,
                body=isi_email,
                from_email=settings.EMAIL_HOST_USER, # Pengirim (Email Kamu)
                to=[settings.EMAIL_HOST_USER],       # Penerima (Kirim ke Diri Sendiri)
                reply_to=[email_pelamar],            # Agar kalau di-reply langsung ke pelamar
            )

            # 4. Pasang Lampiran PDF (Jika ada)
            if file_cv:
                email.attach(file_cv.name, file_cv.read(), file_cv.content_type)

            # 5. KIRIM!
            email.send(fail_silently=False)
            
            # Jika sampai sini berarti SUKSES
            print("✅ SUKSES! Email berhasil dikirim ke server Gmail.")
            pesan_status = "✅ Lamaran Berhasil Dikirim! Cek email Anda."

        except Exception as e:
            # Jika GAGAL, catat errornya di Logs
            print(f"❌ ERROR FATAL SAAT KIRIM EMAIL: {e}")
            pesan_status = f"❌ Gagal kirim: {e}"

    return render(request, 'career.html', {'pesan': pesan_status})

# Halaman lain (biarkan standar)
def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def faq(request):
    return render(request, 'faq.html')
