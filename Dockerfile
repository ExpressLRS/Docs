FROM squidfunk/mkdocs-material:9.4.2
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
CMD ["mkdocs", "serve", "--livereload", "--dev-addr=0.0.0.0:8000"]
