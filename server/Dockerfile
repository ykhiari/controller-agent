FROM ubuntu

RUN mkdir -p /home/app
RUN apt-get update -y \
    && apt-get install -y \
        python3 \
        python3-pip \
        vim \
        net-tools \
        iputils-ping
RUN python3 -m pip install coloredlogs

COPY . /home/app
CMD ["python3","/home/app/echo-server.py"]

WORKDIR /home/app