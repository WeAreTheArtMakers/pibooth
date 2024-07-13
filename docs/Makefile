# Sphinx belgeleri için minimal Makefile
#

# Bu değişkenleri komut satırından ve aşağıdaki ilk iki değişken için ortamdan ayarlayabilirsiniz.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = build

# İlk sırada yer alacak şekilde ayarlayın ki, argümansız "make" komutu "make help" gibi davransın.
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Her hedefi yakala: Bilinmeyen tüm hedefleri Sphinx'in yeni "make modu" seçeneği kullanarak yönlendirir.
# $(O), $(SPHINXOPTS) için bir kısayoldur.
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) -E -j auto -T -v $(O)
