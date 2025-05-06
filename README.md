Bu Python projesi, kullanıcıdan alınan bir Bitcoin cüzdan adresi ile Blockchain.info API'sini kullanarak aşağıdaki bilgileri döndürür:

- Toplam bakiye (BTC cinsinden)
- Toplam işlem sayısı
- Toplam gelen BTC miktarı
- Toplam gönderilen BTC miktarı

- API: [blockchain.info/rawaddr](https://blockchain.info/rawaddr)
- Bakiye ve transfer bilgileri satoshi cinsinden döner; okunabilirlik için BTC'ye çevrilir (`/ 1e8`).

## Lisans

MIT Lisansı
