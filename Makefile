.PHONY: install-python-packages
install-python-packages:
	pip install \
      "mkdocs-minify-plugin==0.7.1" \
      "mkdocs-redirects==1.2.1" \
      "CairoSVG==2.7.1" \
      "jinja2==3.0.3" \
      "mkdocs-static-i18n==1.0.6" \
      "mkdocs-git-committers-plugin-2==1.2.0" \
      "mkdocs-git-revision-date-localized-plugin==1.2.0"

.PHONY: build
build:
	docker compose build

.PHONY: run
run:
	docker compose up
