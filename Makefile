.PHONY: install-python-packages
install-python-packages:
	pip install \
      "mkdocs-minify-plugin==0.8.0" \
      "mkdocs-redirects==1.2.2" \
      "mkdocs-static-i18n==1.3.0" \
      "mkdocs-git-committers-plugin-2==2.5.0" \
      "mkdocs-git-revision-date-localized-plugin==1.4.5" \
      "cairosvg==2.8.1" \
      "jinja2==3.1.6"


.PHONY: build
build:
	docker compose build

.PHONY: run
run:
	docker compose up
