# Host-only convenience wrappers around `docker compose`.
# CI invokes `docker compose` directly and never calls `make`.

.PHONY: install build run serve site shell spellcheck catalog

install:
	pip install "zensical==0.0.50"

build:
	zensical build --clean

run: serve

serve:
	docker compose up

site:
	docker compose run --rm docs build --clean

shell:
	docker compose run --rm --entrypoint sh docs

catalog:
	docker compose run --rm --entrypoint python3 docs overrides/hooks/product_catalog.py

spellcheck:
	pyspelling --config .spellcheck.yml --spellchecker aspell --name Markdown
