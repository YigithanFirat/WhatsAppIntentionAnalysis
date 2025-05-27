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

- Türkçe WhatsApp mesajlarını sınıflandırma / Classification of Turkish WhatsApp messages
- "Bilgi" ve "Şikayet" sınıflandırması / "Information" and "Complaint" classification 
- Veri temizleme ve ön işleme / Data cleaning and preprocessing 
- TF-IDF vektörleştirme / TF-IDF vectorization
- Multinomial Naive Bayes sınıflandırıcı / Multinomial Naive Bayes classifier
- Eğitim, test ve doğruluk raporlama / Training, testing, and accuracy reporting 
- Basit API ile entegre edilebilirlik / Easily integrable via a simple API 

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

### Veri Seti / Dataset

niyet_verisi.csv dosyası içerisinde "text" ve "label" (bilgi/şikayet) sütunları bulunur.
Veri temizleme ve ön işleme bu dosya üzerinden yapılır.

The niyet_verisi.csv file contains "text" and "label" (information/complaint) columns.
Data cleaning and preprocessing are performed using this file.

## 📦 Kullanım / Usage

1. Veri temizleme ve ön işleme yapılır. / Data cleaning and preprocessing are performed.

2. TF-IDF ile metinler sayısal verilere dönüştürülür. / Texts are converted into numerical data using TF-IDF.

3. Naive Bayes algoritması ile model eğitilir. / The model is trained with the Naive Bayes algorithm.

4. Model, test verisi ile doğrulanır. / The model is validated on test data.

5. Flask API endpoint'ine mesaj gönderilerek sınıflandırma yapılabilir. / Classification can be done by sending messages to the Flask API endpoint.

## 📊 Model Performansı / Model Performance

• Eğitim ve test doğrulukları // Training and test accuracies

• Precision, recall, f1-score / Precision, recall, f1-score

• Confusion matrix görselleştirme / Confusion matrix visualization

## 🤝 Katkıda Bulunma / Contributing

Katkıda bulunmak isterseniz, lütfen bir "issue" açın veya direkt "pull request" gönderin.

If you want to contribute, please open an issue or submit a pull request directly.

## 📄 Lisans / License

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakınız.

This project is licensed under the MIT License. See the LICENSE file for details.

## İletişim / Contact
Proje sahibi: Yiğithan Fırat / Project Owner: Yiğithan Fırat
E-posta: yigithanfirat@gmail.com
E-mail: yigithanfirat@gmail.com

Thank you for checking out this project!
Bu projeyi incelediğiniz için teşekkürler!