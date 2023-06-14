FROM ubuntu:23.04

RUN apt update && apt-get -y upgrade && apt install --no-install-recommends -y python3 pipx python3-venv git && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /

RUN git clone "https://github.com/webcomics/dosage.git" && cd dosage && pipx install -e .[css,bash,dev] && pipx ensurepath

RUN mkdir /webcomics

ENTRYPOINT ["/root/.local/bin/dosage"]
CMD ["/root/.local/bin/dosage","--help"]