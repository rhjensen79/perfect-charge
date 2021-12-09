FROM python:3.9-alpine3.15
LABEL maintainer="Robert Jensen - Robert@robert-jensen.dk"
LABEL org.opencontainers.image.version="0.0.1"
WORKDIR /usr/src/app
COPY . ./
RUN pip3 install -r requirements.txt
CMD [ "python", "./app.py" ]
