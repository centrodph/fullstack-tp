#  https://youtu.be/NAOsLaB6Lfc?t=3268
#  https://www.youtube.com/watch?v=s8po-frUVwg
FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y \
        libgdal-dev \
        binutils \
        libproj-dev \
        gdal-bin \
        python3-gdal \
        python3-venv
RUN apt-get install -y gcc python3
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
# RUN python3 -m venv /opt/venv
# RUN /opt/venv/bin/python3 -m pip install --upgrade pip
# RUN /opt/venv/bin/pip install -r requirements.txt
