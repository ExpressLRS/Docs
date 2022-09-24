FROM squidfunk/mkdocs-material:8.1.9
RUN apk add build-base
RUN pip install mkdocs-extra-sass-plugin "mkdocs-minify-plugin>=0.3" "mkdocs-redirects>=1.0" mike "jinja2==3.0.3"

# Set working directory
WORKDIR /docs

# Expose MkDocs development server port
EXPOSE 8000

# Start development server by default
ENTRYPOINT ["mkdocs"]
CMD ["serve", "--livereload", "--dev-addr=0.0.0.0:8000"]
