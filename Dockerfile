FROM squidfunk/mkdocs-material:8.5.11
RUN apk add \
    build-base \
    libxml2-dev \
    libxslt \
    libxslt-dev \
    dumb-init

WORKDIR /docs
COPY ./Makefile ./Makefile
RUN make install-python-packages

EXPOSE 8000

ENTRYPOINT ["dumb-init"]
CMD ["mkdocs", "serve", "--livereload", "--dev-addr=127.0.0.1:8000"]
