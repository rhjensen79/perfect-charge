FROM python:3.9
LABEL maintainer="Robert Jensen - Robert@robert-jensen.dk"
LABEL org.opencontainers.image.version="0.0.1"
ENV TZ="Europe/Copenhagen"
WORKDIR /usr/src/app
COPY . .
COPY ../tools/. .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD [ "python", "app.py" ]
