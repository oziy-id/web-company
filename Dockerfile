# Gunakan Python versi terbaru
FROM python:3.10

# Set folder kerja di dalam server
WORKDIR /code

# Salin file kebutuhan dulu biar cache aman
COPY ./requirements.txt /code/requirements.txt

# Install kebutuhan (Django, dll)
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Salin semua sisa file codingan
COPY . /code

# Berikan izin agar database bisa diedit
RUN chmod 777 .

# ============================================
# KUNCI KEBERHASILAN ADA DI BARIS BAWAH INI
# ============================================
# Kita paksa Django jalan di Port 7860 (Sesuai aturan Hugging Face)
CMD ["python", "manage.py", "runserver", "0.0.0.0:7860"]
