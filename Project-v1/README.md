## Proje Açıklaması

Bu proje, tıbbi raporlardan istatistiksel veriler çıkarmak ve bunları JSON formatında sunmak için geliştirilmiş bir araçtır. FastAPI kullanılarak bir API oluşturulmuştur. API, kullanıcının mesajını alır, GPT-3.5 modelini kullanarak sistem mesajıyla birlikte bir konuşma gerçekleştirir ve sonucu JSON formatında döndürür.

## OpenAI API Anahtarı

Projenin çalışması için OpenAI API anahtarınıza ihtiyaç vardır. Anahtarınızı güvenli bir şekilde saklamak için `.env` dosyası kullanılmalıdır. Projeyi kullanmadan önce, projenin `backend` dizininde `.env` adında bir dosya oluşturun ve aşağıdaki şekilde API anahtarınızı tanımlayın:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Kurulum

Proje bağımlılıklarını yüklemek için aşağıdaki komutu çalıştırın:

```
pip install -r requirements.txt
```

## Uygulamayı Başlatma

### Backend (API) Başlatma

Projenin backend kısmını başlatmak için `backend` klasör dizinine gidin ve terminalden aşağıdaki komutu çalıştırın:

```
uvicorn main:app --reload
```

Bu komut, FastAPI uygulamanızı başlatır ve herhangi bir kod değişikliği yapıldığında otomatik olarak yeniden yükler.

### Frontend (Web Sayfası) Başlatma

1. Projenin `frontend` klasör dizinine gidin.

2. Frontend dosyalarını bir code editor (örneğin Visual Studio Code) ile açın.

3. "Open with Live Server" (Canlı Sunucuda Aç) veya benzer bir seçenek ile dosyayı canlı olarak başlatın. 

   - Alternatif olarak, `index.html` dosyasına doğrudan çift tıklayarak da web sayfasını tarayıcınızda çalıştırabilirsiniz.

Bu adımlar, projenin backend (API) kısmını başlatmanın yanı sıra frontend (web sayfası) dosyalarını canlı olarak çalıştırmanın yollarını açıklamaktadır. 

