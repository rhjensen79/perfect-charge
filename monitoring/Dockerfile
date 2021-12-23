FROM python:3.10
LABEL maintainer="Robert Jensen - Robert@robert-jensen.dk"
ENV TZ="Europe/Copenhagen"
WORKDIR /usr/src/app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt && \
    mkdir -p .streamlit && \
    mv config.toml .streamlit
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]