.PHONY: install-python-packages
install-python-packages:
	pip install \
      "mkdocs-minify-plugin==0.7.1" \
      "mkdocs-redirects==1.2.1" \
      "mkdocs-static-i18n==1.2.2" \
      "mkdocs-git-committers-plugin-2==2.3.0" \
      "mkdocs-git-revision-date-localized-plugin==1.2.4" \
      "CairoSVG==2.7.1" \
      "jinja2==3.1.3" \
      "pngquant==3.0.3"

.PHONY: build
build:
	docker compose build

.PHONY: run
run:
	docker compose up
