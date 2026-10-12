FROM zensical/zensical:0.0.67

# WORKDIR, EXPOSE 8000, ENTRYPOINT and the default
# `serve --dev-addr=0.0.0.0:8000` CMD are inherited from the base image.

# git_info reads page dates and committers from git
RUN apk add --no-cache git

# Lets zensical.toml load the git_info Markdown extension
ENV PYTHONPATH=/docs/overrides/hooks
