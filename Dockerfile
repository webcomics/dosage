FROM python:3.10-slim

WORKDIR /data

COPY . .

RUN apt-get update && apt-get install -y         \
    libxml2-dev                                  \
    libxslt1-dev                                 \
    python3-pip                                  \
    &&						 \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install -e .[css,bash,dev]

CMD dosage
