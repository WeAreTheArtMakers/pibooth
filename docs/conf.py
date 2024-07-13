# Sphinx belgeleme yapılandırıcı dosyası.
#
# Bu dosya, en yaygın seçeneklerin bir seçimini içerir. Tam listesi için dokümantasyona bakın:
# https://www.sphinx-doc.org/tr/master/usage/configuration.html

# -- Yol ayarları --------------------------------------------------------------

# Eğer eklentiler (veya autodoc ile belgelenecek modüller) başka bir dizindeyse,
# bu dizinleri burada sys.path'e ekleyin. Eğer dizin belgeleme köküne göre ise,
# os.path.abspath kullanarak mutlak yapın, burada gösterildiği gibi.

import sys
import os.path as osp

sys.path.insert(0, osp.dirname(osp.dirname(osp.abspath(__file__))))
import watam

# -- Proje bilgileri -----------------------------------------------------------

project = 'Watam ve WeAreTheArtMakers'
copyright = '2024, Watam ve WeAreTheArtMakers'
author = 'Watam ve WeAreTheArtMakers Ekibi'

# Tam sürüm, alpha/beta/rc etiketleri dahil
release = watam.__version__

# -- Genel yapılandırma -------------------------------------------------------

# Burada, dizeler olarak Sphinx eklenti modül adlarını ekleyin.
# Bunlar Sphinx ile gelen (adında 'sphinx.ext.*' olan) veya sizin özel
# eklentileriniz olabilir.
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx_copybutton'
]

# Burada belirtilen dizinler içindeki şablonları içeren yolları ekleyin, bu dizine göreli.
templates_path = ['_templates']

# Kaynak dosyaları ararken dikkate alınacak, kaynak dizinine göreli dosya ve dizinleri
# eşleştiren kalıpların listesi.
# Bu kalıp aynı zamanda html_static_path ve html_extra_path'i de etkiler.
exclude_patterns = []

# -- HTML çıktısı için seçenekler -------------------------------------------------

# HTML ve HTML Yardım sayfaları için kullanılacak tema. Dokümantasyonda
# yerleşik temaların bir listesi için bakın.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
}

# Otomatik olarak belgelenmiş üyelerin sıralaması 'alfabetik' (değer 'alphabetical'),
# üye türüne göre ('groupwise') veya kaynak sırasına göre ('bysource') olabilir.
# Varsayılan değer alfabetiktir.
autodoc_member_order = 'bysource'

add_module_names = False

# Özel statik dosyaları (örneğin stil sayfaları) burada belirtilen yollara ekleyin,
# bu dizine göreli. Bu dosyalar yerleşik statik dosyaların ardından kopyalanır,
# bu nedenle "default.css" adında bir dosya yerleşik "default.css" dosyasının üzerine yazar.
html_static_path = ['_static']

# Yan çubuğun üst kısmına yerleştirilecek bir resim dosyasının adı (bu dizine göreli).
# NOT: _static klasörüne konulmamalıdır, aksi takdirde Read The Docs'ta görüntülenmez
# (bir hata gibi görünüyor..??)
html_logo = 'pibooth.png'

# Dokümanların favicon'u olarak kullanılacak resim dosyasının adı (statik yolda).
# Bu dosya, bir Windows simge dosyası (.ico) olmalı ve 16x16 veya 32x32 piksel boyutunda olmalıdır.
html_favicon = '_static/favicon.ico'

# Eğer False ise, bir indeks oluşturulmaz.
html_use_index = True

# Eğer True ise, indeks her harf için ayrı sayfalara bölünür.
html_split_index = False

# Eğer True ise, sayfalara reST kaynaklarına bağlantılar eklenir.
html_show_sourcelink = False

# Eğer True ise, HTML altbilgisinde "Sphinx kullanılarak oluşturuldu" gösterilir. Varsayılan True'dur.
html_show_sphinx = False

# Eğer True ise, "(C) Telif Hakkı ..." HTML altbilgisinde gösterilir. Varsayılan True'dur.
html_show_copyright = True
