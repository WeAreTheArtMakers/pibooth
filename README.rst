.. image:: https://wearetheartmakers.com/us/images/2024/07/13/piboothtr.png

|PythonVersions| |PypiPackage| |Downloads| |Tests| |Codecov|

``pibooth`` projesi, Raspberry Pi için saf Python'da kutudan çıktığı gibi kullanılabilen bir fotokabin uygulaması sağlar. GitHub kullanıcılarının bazı gerçekleştirmelerini keşfetmek için `wiki <https://github.com/pibooth/pibooth/wiki>`_ sayfasına göz atın ve kendi versiyonunuzun fotoğraflarını bize göndermekten çekinmeyin.

.. image:: https://wearetheartmakers.com/us/images/2024/07/13/modbooth_samples.png
   :align: center
   :alt: Ayarlar

Özellikler
----------

* Arayüz Danca, Felemenkçe, İngilizce, Fransızca, Almanca, Macarca, Norveççe, Türkçe, Portekizce (Portekiz ve Brezilya), İspanyolca ve İsveççe dillerinde mevcuttur (özelleştirilebilir)
* 1'den 4'e kadar fotoğraf çekebilir ve bunları son bir resimde birleştirebilir
* gPhoto2, OpenCV ve Raspberry Pi ile uyumlu tüm kameraları destekler
* Raspberry Pi GPIO üzerindeki donanım düğmeleri ve lambaları destekler
* Tamamen donanım düğmeleri / klavye / fare / dokunmatik ekran ile kontrol edilir
* Raspberry Pi başlangıcında otomatik başlatma
* Boşta kalma sırasında son sıradan çekilen fotoğrafları animasyon olarak gösterme
* Son fotoğrafları ve bireysel çekimleri depolama
* CUPS sunucusu kullanarak son fotoğrafları yazdırma (yazdırma kuyruğu göstergesi)
* Son fotoğrafın üzerine özelleştirilebilir yazılar ekleyebilme (özelleştirilebilir yazı tipleri, renkler, hizalamalar)
* Son fotoğrafın üzerine özelleştirilebilir arka plan(lar) ve kaplama(lar) ekleyebilme
* Tüm ayarlar bir yapılandırma dosyasında mevcuttur (en yaygın seçenekler grafik bir arayüzde)
* Eklenti sistemi sayesinde yüksek düzeyde özelleştirilebilir, topluluk tarafından geliştirilen eklentileri PyPI'dan yükleyebilir veya kendi eklentinizi geliştirebilirsiniz.

Donanım
----------

1. **DM PD170 Metal USB 3.1 Flash Bellek 64 GB**
   - Yüksek hızda veri transferi ve depolama için kullanılacak.

2. **Raspberry Pi 5 8GB**
   - Proje için ana kontrol ve işlem birimi olarak kullanılacak.

3. **SanDisk 32GB Extreme Pro MicroSDHC Hafıza Kartı**
   - Raspberry Pi için yüksek hızlı hafıza kartı. 100 MB/sn'ye kadar okuma hızı.

4. **Resmi Raspberry Pi 5 USB-C güç kaynağı 27 W, USB-C güç kaynağı, beyaz**
   - Raspberry Pi'yi güvenilir ve stabil bir şekilde beslemek için kullanılacak.

5. **3 Model B+ Dokunmatik Ekran LCD Ekran için 5 İnç Monitör Dokunmatik Ekran Kılıfı Standı Tutucu - Siyah**
   - Bu kılıf standı tutucu, 5 inç dokunmatik ekranı desteklemek ve kolay kullanım sağlamak için tasarlanmıştır.

6. **Raspberry Pi Aktif Soğutucu**
   - Raspberry Pi'nin aşırı ısınmasını önlemek ve performansını artırmak için kullanılacak aktif soğutma çözümü.

7. **waveshare 5 inç TFT LCD Ekran B 800x480 Raspberry Pi Dirençli Dokunmatik Ekran HDMI Monitör**
   - Bu ekran, 800x480 çözünürlük sunar ve Raspberry Pi ile uyumlu dirençli dokunmatik özelliklere sahiptir. BB Siyah, Raspbian, Ubuntu, Kali, Retropie, Win10 IOT/Win10/8.1/8/7 işletim sistemlerini destekler.

8. **Raspberry Pi Kamera Modülü V2 - (Raspberry Pi)**
   - Yüksek kaliteli fotoğraf ve video kaydı yapabilen bu kamera modülü, Raspberry Pi projelerinizde görüntü işleme ve güvenlik sistemleri için idealdir.

Kurulum 
---------

**pibooth, çeşitli cihazlarda ve işletim sistemlerinde çalışacak şekilde tasarlanmıştır. Aşağıdaki talimatlar, pibooth’u nasıl kuracağınızı açıklar.**

**Gereksinimler**

	•	-Python 3.7 veya üstü
	•	-pip (Python paket yöneticisi)
	•	-Bir Raspberry Pi

**Adım 1: Python ve pip Yükleme**

-Python ve pip’i henüz yüklemediyseniz, aşağıdaki adımları izleyerek yükleyin.

-Ubuntu/Debian

-sudo apt update
-sudo apt install python3 python3-pip

**macOS**

-macOS için, Homebrew kullanarak Python ve pip’i yükleyebilirsiniz.

-brew install python

**Windows**

-Windows için, Python.org adresinden Python yükleyicisini indirin ve yükleme sırasında “pip” seçeneğini işaretlediğinizden emin olun.

**Adım 2: pibooth’u Yükleme**

-pip kullanarak pibooth’u kolayca yükleyebilirsiniz.

-pip install pibooth

**Adım 3: Raspberry Pi Kurulum**

-Eğer pibooth’u bir Raspberry Pi üzerinde çalıştırmak istiyorsanız, aşağıdaki ek adımları izleyin.

**Raspberry Pi Kamera Modülü Kurulumu**

-Raspberry Pi üzerinde kamera modülünü etkinleştirmek için raspi-config aracını kullanın.

-sudo raspi-config

-Ardından “Interfacing Options” -> “Camera” seçeneğini seçin ve etkinleştirin. -Raspberry Pi’nizi yeniden başlatmanız gerekecek.

**Ek Python Kütüphanelerini Yükleme**

-sudo apt update
-sudo apt install python3-picamera

**Adım 4: pibooth’u Çalıştırma**

-Kurulum tamamlandıktan sonra, pibooth’u aşağıdaki komutla başlatabilirsiniz.

-pibooth

**Adım 5: Yapılandırma**

-pibooth’u kendi ihtiyaçlarınıza göre yapılandırmak için, ~/.config/pibooth/pibooth.cfg dosyasını düzenleyin. Bu dosya, pibooth’un davranışını ve özelliklerini kontrol etmenizi sağlar, düzenlenmiş pibooth.cfg dosyasını ve translation.cfg dosyasını ~/.config/pibooth içine sürükleyip bırakın.

Belgeler
--------

.. image:: https://raw.githubusercontent.com/pibooth/pibooth/master/docs/images/documentation.png
   :align: center
   :alt: Belgeler
   :target: https://pibooth.readthedocs.io/en/stable
   :height: 200px

Eklentiler
----------

Pibooth ile uyumlu bilinen eklentilerin listesi

Pibooth organizasyonunun eklentileri
====================================

- `pibooth-picture-template <https://github.com/pibooth/pibooth-picture-template>`_
- `pibooth-google-photo <https://github.com/pibooth/pibooth-google-photo>`_
- `pibooth-sound-effects <https://github.com/pibooth/pibooth-sound-effects>`_
- `pibooth_dropbox <https://github.com/pibooth/pibooth-dropbox>`_
- `pibooth-qrcode <https://github.com/pibooth/pibooth-qrcode>`_
- `pibooth-extra-lights <https://github.com/pibooth/pibooth-extra-lights>`_

Üçüncü taraf eklentiler
=======================

Üçüncü taraf eklentiler GitHub'da veya `PyPI'da <https://pypi.org/search/?q=pibooth>`_ bulunabilir.
İşte kısa bir liste:

- `pibooth-lcd-display <https://pypi.org/project/pibooth-lcd-display>`_
- `pibooth-oled-display <https://pypi.org/project/pibooth-oled-display>`_
- `pibooth-neopixel_spi <https://github.com/peteoheat/pibooth-neopixel_spi>`_
- `pibooth-telegram-upload <https://pypi.org/project/pibooth-telegram-upload>`_
- `pibooth-s3-upload <https://pypi.org/project/pibooth-s3-upload>`_

Sponsorlar
----------

Sponsorlarımıza büyük teşekkürler:

- `@andhey <https://github.com/andhey>`_
- `@vo55 <https://github.com/vo55>`_
- `@laurammiller <https://github.com/laurammiller>`_
- `@neilrenfrey <https://github.com/neilrenfrey>`_
- `@agrovista <https://github.com/agrovista>`_
- `@mozdi <https://github.com/mozdi>`_
- `@MikkeBoomBoom <https://github.com/MikkeBoomBoom>`_
- `@fatgeek <https://github.com/fatgeek>`_
- `@STREETMONEYBSC <https://github.com/streetmoneybsc>`_
- `@STUDIOBRN <https://github.com/studiobrn>`_
- `@WATAM <https://github.com/wearetheartmakers>`_

Bu bizim için çok şey ifade ediyor!

.. |Pibooth| image:: https://raw.githubusercontent.com/pibooth/pibooth/master/docs/pibooth.png
   :align: middle

.. |PythonVersions| image:: https://img.shields.io/badge/python-3.6+-red.svg
   :target: https://www.python.org/downloads
   :alt: Python 3.6+

.. |PypiPackage| image:: https://badge.fury.io/py/pibooth.svg
   :target: https://pypi.org/project/pibooth
   :alt: PyPi package

.. |Downloads| image:: https://img.shields.io/pypi/dm/pibooth?color=purple
   :target: https://pypi.org/project/pibooth
   :alt: PyPi downloads

.. |Tests| image:: https://github.com/pibooth/pibooth/actions/workflows/tests.yml/badge.svg?branch=master
   :target: https://github.com/pibooth/pibooth/actions/workflows/tests.yml?query=branch%3Amaster
   :alt: Tests

.. |Codecov| image:: https://codecov.io/gh/pibooth/pibooth/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/pibooth/pibooth
    :alt: Codecov
