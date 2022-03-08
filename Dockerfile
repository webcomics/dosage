FROM python:3.10-slim

WORKDIR /data

COPY . .

RUN     apt-get update && apt-get install -y    \
        git-core                            \
        python3-setuptools                  \
                                            && \
    apt-get clean && rm -Rf /var/lib/apt/lists/* && \
    python3 setup.py install

CMD dosage
