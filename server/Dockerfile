FROM ubuntu

RUN mkdir -p /home/app
RUN useradd -ms /bin/bash admin
RUN apt-get update -y \
    && apt-get install -y \
        python3 \
        python3-pip \
        vim \
        net-tools \
        iputils-ping
RUN python3 -m pip install coloredlogs

COPY . /home/app
RUN chown -R admin:admin /home/app
RUN chmod -R 777 /home/app
USER admin
CMD ["python3","/home/app/echo-server.py"]

WORKDIR /home/app