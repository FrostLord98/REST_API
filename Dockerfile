FROM python:3.12.4-alpine3.20

WORKDIR /rest_api

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt

RUN apk add --no-cache gcc musl-dev linux-headers

RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

RUN pip install -r requirements.txt


EXPOSE 5000

COPY . .

CMD ["flask", "run","--debug"]