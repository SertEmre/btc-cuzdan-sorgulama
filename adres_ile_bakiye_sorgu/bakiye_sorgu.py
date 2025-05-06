import requests

def cüzdan_bakiye_sorgulama(adres):
    try:
        url = f"https://blockchain.info/rawaddr/{adres}"
        response = requests.get(url)
        
        if response.status_code != 200:
            raise Exception(f"API Hatası: {response.status_code}")

        data = response.json()

        bakiye= data.get('final_balance', 0)  
        bakiye_btc = bakiye/ 1e8 
        işlem_sayısı = data.get('n_tx', 0)  
        toplam_gelen = data.get('total_received', 0) / 1e8  #/1e8= 10^8'i ifade eder.BTC cinsinden daha okunabilir hale getirmek için kullanılan bir bölme işlemi
        toplam_gönderilen = data.get('total_sent', 0) / 1e8  

        print(f"\nCüzdan Adresi: {adres}")
        print(f"Toplam Bakiye: {bakiye_btc:.8f} BTC")
        print(f"Toplam İşlem Sayısı: {işlem_sayısı}")
        print(f"Toplam Gelen BTC: {toplam_gelen:.8f} BTC")
        print(f"Toplam Gönderilen BTC: {toplam_gönderilen:.8f} BTC")
    
    except requests.exceptions.RequestException as e:
        print(f"API isteği sırasında bir hata oluştu: {e}")
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")

cüzdan_adresi = input("Lütfen cüzdan adresini girin: ")
cüzdan_bakiye_sorgulama(cüzdan_adresi)
