import openai
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def handle_errors(e):
    if isinstance(e, openai.BadRequestError):
        print("Geçersiz bir istek gönderildi.")
    elif isinstance(e, openai.AuthenticationError):
        print("Kimlik doğrulama hatası. Lütfen API anahtarınızı kontrol edin.")
    else:
        print(f"Bir hata oluştu: {e}")
    print("Lütfen daha sonra tekrar deneyin.")


def chat_with_gpt(system_message, user_message, model_name):
    # GPT-3.5 API'na istek gönderir ve yanıtı döndürür.
    try:
        print("İstek gönderiliyor, lütfen bekleyin...")

        messages = [{"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}]
        completion = client.chat.completions.create(
            model=model_name,
            messages=messages,
            # temperature=0.2

        )
        assistant_response = completion.choices[0].message.content
        # assistant_response = response["choices"][0]["message"]["content"]
        return assistant_response.strip("\n").strip()
    except Exception as e:
        handle_errors(e)

def main(user_message_input):
    model_name = "gpt-3.5-turbo"

    system_message = """
        Doktor raporlarından istatistiksel verileri çıkarmak ve bunları JSON formatında sunmak için görevlendirildiniz.
        Aşağıdaki adımları izleyin:
        İlgili Verileri Belirleyin: Tıbbi raporları inceleyerek, önemli istatistiksel veri noktalarını belirleyin. 
        Veriler şunları içerebilir:
        Sayısal Değerler: Kan basıncı, kalp atış hızı, laboratuvar sonuçları (kolesterol, kan şekeri vb.), ilaç dozajları, süreler (semptomların uzunluğu vb.).
        Kategorik Değerler: Belirli semptomların, teşhislerin veya prosedürlerin görülme sayısı.
        Veri Çıkarma: Belirlenen veri noktalarını tıbbi raporlardan ayıklayın. Bu verileri, etiket, değer ve birimiyle birlikte belirtin.
        Çıktı: JSON Nesnesi: Tıbbi raporlardan çıkarılan istatistiksel verileri temsil eden iyi yapılandırılmış bir JSON nesnesi oluşturun. Bu nesne, tüm istatistikleri içermeli ve kolayca okunabilir olmalıdır.
        Cevapta sadece json formatındaki istatistiki veriler olsun.
        """

    user_message = user_message_input

    result = chat_with_gpt(system_message, user_message, model_name)
    print(result)
    return result

if __name__ == "__main__":
    main()

