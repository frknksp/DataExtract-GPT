import streamlit as st
from extractor import extract_text
import PyPDF2
import docx
import json

def process_uploaded_file(uploaded_file):
    file_contents = ""

    if uploaded_file is not None:
        file_type = uploaded_file.name.split(".")[-1].lower()

        if file_type == "pdf":
            pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                file_contents += page.extract_text()
        elif file_type == "docx":
            doc = docx.Document(uploaded_file)
            for para in doc.paragraphs:
                file_contents += para.text
        elif file_type == "txt":
            file_contents = uploaded_file.getvalue().decode("utf-8")

    return file_contents

def download_json(output):
    #print(output)
    #json_string = json.dumps(output, ensure_ascii=False, indent=4)
    #print(json_string)
    
    # eğer `output` JSON string ise 
    st.json(json.loads(output), expanded=False)
    st.download_button(
        label="Download JSON",
        file_name="data.json",
        mime="application/json",
        data=output.encode('utf-8'),
    )

def main():
    st.title("Raporlardan İstatistiki Çıktılar")
    st.sidebar.title("Metin Girişi veya Dosya Seçme")

    openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    text_input = st.sidebar.text_area("Metin girin", height=200)
    uploaded_file = st.sidebar.file_uploader("Doktor raporu seçiniz (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
    button_clicked = st.sidebar.button("Gönder")

    
    if uploaded_file is not None:
        st.subheader("Dosya İçeriği:")
        file_contents = process_uploaded_file(uploaded_file)
        if file_contents:
            st.write(file_contents)  # Dosya içeriğini ekrana yazdır
            
    if button_clicked:
        if not openai_api_key:
            st.warning("Lütfen OpenAI API Anahtarını girin.")
        elif not text_input and uploaded_file is None:
            st.warning("Lütfen metin girin veya bir dosya seçin.")
        else:
            if text_input:
                st.subheader("Girilen Metin:")
                st.write(text_input)
                with st.spinner("Veriler işleniyor..."):
                    output = extract_text(text_input, openai_api_key)
                    st.subheader("Json Çıktısı:")
                    st.write(output)
                    download_json(output)
            elif uploaded_file is not None:
                file_contents = process_uploaded_file(uploaded_file)
                if file_contents:
                    with st.spinner("Veriler işleniyor..."):
                        output = extract_text(file_contents, openai_api_key)
                        st.subheader("Json Çıktısı:")
                        st.write(output)
                        download_json(output)

    st.sidebar.caption('Doktor raporlarından istatistiki verileri çıkarmak için geliştirilmiştir.')
    st.sidebar.caption('Metin girişi yaptıktan veya dosya yükledikten sonra "Gönder" butonuna tıklayın. Sonuçlar 5-10 saniye içinde görünecektir.')
    st.sidebar.caption('Bu uygulama OpenAI API kullanmaktadır. API anahtarınızı girmeyi unutmayın.')

if __name__ == "__main__":
    main()
