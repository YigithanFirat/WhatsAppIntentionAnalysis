import tkinter as tk
from tkinter import scrolledtext
import joblib
import re
import nltk
from nltk.corpus import stopwords

# Stopwords'i indir (ilk çalıştırmada gerekebilir)
nltk.download("stopwords")

# Model ve TF-IDF vectorizer'ı yükle
model = joblib.load("chatbot_model.pkl")           # Model dosyası
vectorizer = joblib.load("tfidf_vectorizer.pkl")   # TF-IDF dosyası

# Türkçe stopwords listesi
turkce_stopwords = set(stopwords.words("turkish"))

# Temizleme fonksiyonu
def temizle(metin):
    metin = metin.lower()
    metin = re.sub(r"<.*?>", "", metin)
    metin = re.sub(r"http\S+|www\.\S+", "", metin)
    metin = re.sub(r"[^\w\s]", "", metin)
    metin = re.sub(r"\s+", " ", metin)
    kelimeler = metin.strip().split()
    kelimeler = [kelime for kelime in kelimeler if kelime not in turkce_stopwords]
    return " ".join(kelimeler)

# Cevap üretme fonksiyonu
def cevapla():
    kullanici_mesaji = entry.get()
    temiz_mesaj = temizle(kullanici_mesaji)
    tfidf = vectorizer.transform([temiz_mesaj])
    tahmin = model.predict(tfidf)[0]
    
    sohbet_penceresi.insert(tk.END, f"Sen: {kullanici_mesaji}\n")
    sohbet_penceresi.insert(tk.END, f"Bot: Bu bir {tahmin} mesajı.\n\n")
    sohbet_penceresi.see(tk.END)
    entry.delete(0, tk.END)

# Ana pencere
pencere = tk.Tk()
pencere.title("Niyet Analizi Chatbot")
pencere.geometry("600x600")
pencere.config(bg="#5762FF")

# Sohbet penceresi
sohbet_penceresi = scrolledtext.ScrolledText(
    pencere, 
    wrap=tk.WORD, 
    width=60, 
    height=20, 
    bg="#5762FF", 
    fg="white", 
    font=("Arial", 16, "bold")
)
sohbet_penceresi.pack(pady=10)

# Kullanıcı giriş kutusu
entry = tk.Entry(
    pencere, 
    width=60, 
    bg="white", 
    fg="black", 
    font=("Arial", 16, "bold")
)
entry.pack(pady=10)

# Gönder butonu
gonder_butonu = tk.Button(
    pencere, 
    text="Gönder", 
    command=cevapla, 
    bg="#3B49DF", 
    fg="white", 
    font=("Arial", 16, "bold")
)
gonder_butonu.pack(pady=5)

# Uygulama döngüsü
pencere.mainloop()