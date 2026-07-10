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

# Full pipeline, mirrors .github/workflows/publish.yml
site:
	docker compose run --rm --entrypoint sh docs -c "\
	  python3 overrides/hooks/product_catalog.py && \
	  python3 overrides/hooks/blog_posts.py && \
	  zensical build --clean && \
	  python3 overrides/hooks/llms_txt.py && \
	  python3 overrides/hooks/redirects.py"

shell:
	docker compose run --rm --entrypoint sh docs

catalog:
	docker compose run --rm --entrypoint python3 docs overrides/hooks/product_catalog.py

# Needs aspell + aspell-en installed on the host
spellcheck:
	uv run --group spellcheck pyspelling --config .spellcheck.yml --spellchecker aspell --name Markdown
