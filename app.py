from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import os

app = Flask(__name__)
CORS(app)

MODEL_PATH = "chatbot_model.pkl"
VECTORIZER_PATH = "tfidf_vectorizer.pkl"

if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    raise FileNotFoundError("❌ Gerekli .pkl dosyaları bulunamadı.")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(VECTORIZER_PATH, "rb") as f:
    vectorizer = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        print("📥 Gelen JSON:", data)

        if not data or 'message' not in data:
            return jsonify({'response': 'Lütfen geçerli bir metin gönderin.'}), 400

        user_input = data['message'].strip()
        print("💬 Kullanıcı mesajı:", user_input)

        if not user_input:
            return jsonify({'response': 'Lütfen bir metin girin.'}), 400

        transformed_input = vectorizer.transform([user_input])
        print("✅ Vektörleştirme tamam")

        raw_pred = model.predict(transformed_input)[0]
        print("🔍 Model tahmini (ham):", raw_pred)

        # Tırnakları temizle, küçük harfe çevir
        label = str(raw_pred).strip().lower().replace('"', '').replace("'", "")
        print("🔍 Normalleştirilmiş etiket:", label)

        if label == 'bilgi':
            response = '📘 Bu bir **bilgi metni** olarak sınıflandırıldı.'
        elif label == 'şikayet':
            response = '🛑 Bu bir **şikayet metni** olarak sınıflandırıldı.'
        else:
            response = '❓ Metin sınıflandırılamadı.'

        return jsonify({'response': response})

    except Exception as e:
        print("❌ Sunucu tarafında hata:", e)
        return jsonify({'response': f'Sunucu hatası: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)