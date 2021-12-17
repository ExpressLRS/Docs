FROM squidfunk/mkdocs-material:8.0.3
RUN apk add build-base
RUN pip install mkdocs-static-i18n
RUN python3 localize.py

# Set working directory
WORKDIR /docs

# Expose MkDocs development server port
EXPOSE 8000

# Start development server by default
ENTRYPOINT ["mkdocs"]
CMD ["serve", "--livereload", "--dev-addr=0.0.0.0:8000"]
