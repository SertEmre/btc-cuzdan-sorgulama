Bu proje, bir Bitcoin cüzdan adresinin bakiyesini sorgulayan bir Python uygulamasıdır. Kullanıcı, geçerli bir cüzdan adresi girerek cüzdan bakiyesi, işlem sayısı, gelen ve gönderilen BTC miktarlarını öğrenebilir.

Cüzdan adresine ait bakiye, işlem sayısı, toplam gelen ve gönderilen BTC miktarlarını API üzerinden sorgulama.

adres_kontrol(adres): Verilen Bitcoin cüzdan adresinin geçerliliğini kontrol eder. Adresin uzunluğu 26 ile 42 karakter arasında olmalı ve geçerli Bitcoin adres formatlarına uymalıdır.

cüzdan_bakiye_sorgulama(adres): Geçerli bir Bitcoin cüzdan adresini sorgular ve API üzerinden cüzdan bakiyesi, işlem sayısı, gelen ve gönderilen BTC bilgilerini getirir.

API Kaynağı: blockchain.info API'si üzerinden cüzdan verileri alınır.

Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Detaylı bilgi için LICENSE dosyasına bakabilirsiniz.
