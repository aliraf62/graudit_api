FROM python:3.9-alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt && \
    apk add --no-cache git && \
    git clone https://github.com/wireghoul/graudit /graudit && \
    echo 'export PATH=$PATH:/graudit' >> ~/.bashrc

CMD [ "python", "./app.py" ]

