def career(request):
    # Cek apakah ada tanda '?success=true' di alamat URL
    pesan_sukses = None
    if request.GET.get('success') == 'true':
        pesan_sukses = "✅ ALHAMDULILLAH! Lamaran Anda berhasil terkirim. Tim HRD kami akan segera memeriksanya."

    # Kita tidak perlu logika email di sini lagi
    # Karena HTML form sudah menanganinya langsung via FormSubmit
    # Kita cuma kirim pesan_sukses (kalau ada) ke HTML
    return render(request, 'career.html', {'pesan_sukses': pesan_sukses})
