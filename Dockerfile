FROM python:latest

ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg opus-tools bpm-tools
RUN python -m pip install --upgrade pip
RUN python -m pip install wheel Pyrogram TgCrypto
RUN python -m pip install pytgcalls ffmpeg-python psutil
RUN python -m pip install tgintegration youtube-dl youtube_search requests

RUN wget -q https://github.com/Sadew451/FM/archive/sadew451.tar.gz && tar xf sadew451.tar.gz && rm sadew451.tar.gz

WORKDIR /FM-Sadew451
CMD python3 main.py

# docker build -t tgcalls .
# docker run -it --rm --env-file ./envfile --name tgvc-userbot tgcalls
