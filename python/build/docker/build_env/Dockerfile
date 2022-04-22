FROM liyaodev/base-cpu-u18-py3.8:v1.0.0
LABEL maintainer=liyaodev

RUN echo 'root:root' | chpasswd

# 构建Tini的多服务容器
RUN wget -O /tini https://github.com/krallin/tini/releases/download/v0.19.0/tini && \
    chmod +x /tini
ENTRYPOINT ["/tini", "--"]

WORKDIR /www/server

COPY ./bootcamp/requirements.txt ./bootcamp/requirements.txt
RUN pip3 install -r ./bootcamp/requirements.txt
# -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com

ENV PYTHONUNBUFFERED 1

CMD ["tail", "-f", "/dev/null"]
EXPOSE 8888
