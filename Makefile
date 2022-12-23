.PHONY: install-python-packages
install-python-packages:
	pip install \
      "mkdocs-minify-plugin==0.6.2" \
      "mkdocs-redirects==1.2" \
      "mike==1.1.2" \
      "CairoSVG==2.5.2" \
      "jinja2==3.0.3"

.PHONY: build
build:
	docker compose build

.PHONY: run
run:
	docker compose up
