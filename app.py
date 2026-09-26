import google.generativeai as genai

# 1. Tempelkan API Key milikmu
API_KEY = "MASUKKAN_API_KEY_DI_SINI"

genai.configure(api_key=API_KEY)

# 2. Gunakan nama model terbaru
model = genai.GenerativeModel('models/gemini-3.8-flash')

print("==================================================")
print("   AI PROFESSIONAL RESUME BULLET GENERATOR   ")
print("==================================================")

kalimat_awal = input("\nMasukkan kalimat biasa dari CV kamu: ")

prompt = f"Ubah kalimat deskripsi pengalaman kerja/CV berikut menjadi kalimat yang sangat profesional, berbobot, dan disukai recruiter bidang IT: '{kalimat_awal}'"

print("\nSedang memproses dengan Gemini AI...")

response = model.generate_content(prompt)

print("\n--- HASIL VERSI PROFESIONAL ---")
print(response.text)
print("==================================================")