FROM ubuntu

RUN mkdir -p /home/app
RUN apt-get update -y \
    && apt-get install -y \
        python3 \
        python3-pip \
        vim \
        net-tools \
        iputils-ping

COPY . /home/app

CMD ["python3","/home/app/echo-client.py"]
WORKDIR /home/app