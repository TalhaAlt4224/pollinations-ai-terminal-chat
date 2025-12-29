import requests

def ai_soru_sor(soru):
    # Senin seçtiğin hızlı ve anonim model
    model = "openai" 
    url = f"https://text.pollinations.ai/{soru}?model={model}"
    
    print("AI Düşünüyor...")
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        return "Bir hata oluştu!"

print("--- Pollinations AI Sohbet Programına Hoş Geldin ---")
while True:
    kullanici_sorusu = input("\nSoru Sor (Çıkmak için 'exit' yaz): ")
    if kullanici_sorusu.lower() == 'exit':
        break
    
    cevap = ai_soru_sor(kullanici_sorusu)
    print(f"\nAI Yanıtı: {cevap}")