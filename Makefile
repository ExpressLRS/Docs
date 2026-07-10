# Host-only convenience wrappers around `docker compose`.
# CI invokes `docker compose` directly and never calls `make`.

.PHONY: install build run serve site shell spellcheck

install:
	pip install "zensical==0.0.32"

build:
	zensical build --clean

run: serve

serve:
	docker compose up

site:
	docker compose run --rm docs build --clean

shell:
	docker compose run --rm --entrypoint sh docs

spellcheck:
	pyspelling --config .spellcheck.yml --spellchecker aspell --name Markdown
