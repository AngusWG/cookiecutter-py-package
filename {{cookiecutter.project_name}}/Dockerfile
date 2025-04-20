FROM python:3.12.9

ARG PKG
COPY requirements.txt /tmp
RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r /tmp/requirements.txt
COPY PKG /tmp
RUN pip3 install /tmp/${PKG}

RUN rm -rf /tmp/*

