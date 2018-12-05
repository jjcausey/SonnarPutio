FROM linuxserver/sonarr

COPY . /sonarr_putio
RUN apt update
RUN apt install -y python-pip
RUN pip install /sonarr_putio