FROM squidfunk/mkdocs-material:8.5.10
RUN apk add build-base
RUN pip install \
    "mkdocs-extra-sass-plugin==0.1.0" \
    "mkdocs-minify-plugin==0.6.2" \
    "mkdocs-redirects==1.2" \
    "mike==1.1.2" \
    "jinja2==3.0.3"

# Set working directory
WORKDIR /docs

# Expose MkDocs development server port
EXPOSE 8000

# Start development server by default
ENTRYPOINT ["mkdocs"]
CMD ["serve", "--livereload", "--dev-addr=0.0.0.0:8000"]
