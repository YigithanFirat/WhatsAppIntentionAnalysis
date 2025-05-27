# WhatsApp Intention Analysis / WhatsApp Niyet Analizi

---

## 📌 Proje Hakkında / About the Project

Bu proje, WhatsApp mesajlarından kullanıcı niyetlerini analiz etmek amacıyla geliştirilmiştir.  
Mesajlardaki metinler "bilgi" ve "şikayet" gibi sınıflara ayrılarak sınıflandırma yapılır.  
Doğal Dil İşleme (NLP) teknikleri ve makine öğrenmesi algoritmaları kullanılarak, metinlerin anlamı ve niyeti çıkarılır.  

This project is developed to analyze user intentions from WhatsApp messages.  
Texts in messages are classified into classes such as "information" and "complaint".  
Natural Language Processing (NLP) techniques and machine learning algorithms are used to extract the meaning and intention behind the texts.

---

## ⚙️ Özellikler / Features

- Türkçe WhatsApp mesajlarını sınıflandırma  
- "Bilgi" ve "Şikayet" sınıflandırması  
- Veri temizleme ve ön işleme  
- TF-IDF vektörleştirme  
- Multinomial Naive Bayes sınıflandırıcı  
- Eğitim, test ve doğruluk raporlama  
- Basit API ile entegre edilebilirlik  

- Classification of Turkish WhatsApp messages  
- "Information" and "Complaint" classification  
- Data cleaning and preprocessing  
- TF-IDF vectorization  
- Multinomial Naive Bayes classifier  
- Training, testing, and accuracy reporting  
- Easily integrable via a simple API  

---

## 🚀 Başlangıç / Getting Started

### Gereksinimler / Requirements

- Python 3.x  
- pandas  
- scikit-learn  
- nltk  
- Flask (opsiyonel, API için)  

```bash
pip install pandas scikit-learn nltk flask
```