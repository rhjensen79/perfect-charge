FROM python:3.9-alpine3.15
LABEL maintainer="Robert Jensen - Robert@robert-jensen.dk"
WORKDIR /usr/src/app
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./app.py" ]
