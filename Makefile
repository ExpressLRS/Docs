.PHONY: install-python-packages
install-python-packages:
	pip install \
      "mkdocs-minify-plugin==0.7.1" \
      "mkdocs-redirects==1.2.1" \
<<<<<<< HEAD
      "mkdocs-static-i18n==1.2.2" \
      "mkdocs-git-committers-plugin-2==1.2.0" \
      "mkdocs-git-revision-date-localized-plugin==1.2.4" \
      "cairosvg==2.7.1" \
      "jinja2==3.1.3"
=======
      "CairoSVG==2.7.1" \
      "jinja2==3.0.3" \
      "mkdocs-static-i18n==1.0.6" \
      "mkdocs-git-committers-plugin-2==1.2.0" \
      "mkdocs-git-revision-date-localized-plugin==1.2.0"
>>>>>>> parent of 73e32de9 (bump versions; add optimize)

.PHONY: build
build:
	docker compose build

.PHONY: run
run:
	docker compose up
