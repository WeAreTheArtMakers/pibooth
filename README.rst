|Pibooth|

|PythonVersions| |PypiPackage| |Downloads| |Tests| |Codecov|

``pibooth`` projesi, Raspberry Pi için saf Python'da kutudan çıktığı gibi kullanılabilen bir fotokabin uygulaması sağlar. GitHub kullanıcılarının bazı gerçekleştirmelerini keşfetmek için `wiki <https://github.com/pibooth/pibooth/wiki>`_ sayfasına göz atın ve kendi versiyonunuzun fotoğraflarını bize göndermekten çekinmeyin.

.. image:: https://raw.githubusercontent.com/pibooth/pibooth/master/docs/images/background_samples.png
   :align: center
   :alt: Ayarlar

Özellikler
----------

* Arayüz Danca, Felemenkçe, İngilizce, Fransızca, Almanca, Macarca, Norveççe, Portekizce (Portekiz ve Brezilya), İspanyolca ve İsveççe dillerinde mevcuttur (özelleştirilebilir)
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
