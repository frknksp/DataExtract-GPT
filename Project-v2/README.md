# Doktor Raporundan İstatistiki Veriler

Bu proje, doktor raporlarından karaciğerle ilgili istatistiksel verileri çıkarmak için geliştirilmiştir.

## Proje Yapısı

- **`schema.py`**: Karaciğerle ilgili doktor raporlarını temsil etmek için bir `KaracigerRaporu` şeması içerir.
  
- **`app.py`**: Streamlit kütüphanesini kullanarak metin girişi veya dosya yükleme seçenekleri sunan ve verilerin işlenmesini sağlayan ana uygulama dosyasıdır.
  
- **`extractor.py`**: Metin girişlerinden veya dosyalardan ilgili verileri çıkarmak için OpenAI API'sını kullanan yardımcı bir modüldür.

## Dosya Yapısı ve Fonksiyonlar

- **`schema.py`**:
  - `KaracigerRaporu`: Karaciğerle ilgili tıbbi raporların yapısını tanımlayan bir Pydantic modeli.

- **`app.py`**:
  - `process_uploaded_file`: Yüklenen dosyayı okuyarak içeriğini işleyen ve metin olarak döndüren fonksiyon.
  - `download_json`: Çıktıyı JSON formatında indirmeyi sağlayan fonksiyon.
  - `main`: Streamlit arayüzünü oluşturan ve verilerin işlenmesini yöneten ana işlev.

- **`extractor.py`**:
  - `extract_text`: Metin girişlerinden verileri çıkarmak için kullanılan fonksiyon.

## Kullanım

1. Uygulamayı çalıştırmak için Python yüklü olmalıdır.
2. Gerekli kütüphaneleri yüklemek için `requirements.txt` dosyasını kullanın.
    ```
    pip install -r requirements.txt
    ```
3. Ana uygulamayı başlatmak için aşağıdaki komutu çalıştırın:
    ```
    streamlit run app.py
    ```
4. Uygulama açıldığında, metin girişi yapabilir veya doktor raporu dosyasını yükleyebilirsiniz.
5. Veri işlendiğinde, istatistiksel çıktıyı JSON formatında indirebilirsiniz.

## Notlar

- OpenAI API anahtarı girilmesi gereklidir.
- Dosya yükleme işlemi sadece PDF, DOCX ve TXT formatları için desteklenmektedir.
- Verilerin işlenmesi birkaç saniye sürebilir. Lütfen işlem sonuçlarını bekleyin.

