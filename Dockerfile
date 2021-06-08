FROM squidfunk/mkdocs-material:7.1.2
RUN apk add build-base
RUN pip install mkdocs-extra-sass-plugin

# Set working directory
WORKDIR /docs

# Expose MkDocs development server port
EXPOSE 8000

# Start development server by default
ENTRYPOINT ["mkdocs"]
CMD ["serve", "--livereload", "--dev-addr=0.0.0.0:8000"]
