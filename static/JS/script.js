    function sendMessage() {
      const userInput = document.getElementById("userInput");
      const sendBtn = document.getElementById("sendBtn");
      const responseArea = document.getElementById("response");

      const message = userInput.value.trim();

      // Boş mesaj kontrolü
      if (!message) {
        responseArea.textContent = "❗ Lütfen bir metin girin.";
        return;
      }

      // Girdi ve butonu devre dışı bırak
      userInput.disabled = true;
      sendBtn.disabled = true;
      responseArea.textContent = "⏳ Yanıt bekleniyor...";

      fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
      })
        .then(res => {
          if (!res.ok) throw new Error('Sunucu hatası: ' + res.status);
          return res.json();
        })
        .then(data => {
          responseArea.textContent = data.response;
        })
        .catch(err => {
          responseArea.textContent = '🚫 Hata: ' + err.message;
        })
        .finally(() => {
          userInput.disabled = false;
          sendBtn.disabled = false;
          userInput.focus();
        });
    }

    // Enter tuşuna basınca gönderme işlemi
    document.getElementById('userInput').addEventListener('keydown', function(e) {
      if (e.key === 'Enter') {
        sendMessage();
      }
    });