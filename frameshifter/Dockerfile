# FROM python:3.6.9

# RUN apt update -y
# RUN apt install vim less jq -y

# COPY requirements.txt /requirements.txt
# COPY src /src
# COPY conf /conf

# RUN python3 -m pip install -i https://mirrors.aliyun.com/pypi/simple/ virtualenv
# RUN virtualenv scapyenv
# RUN . scapyenv/bin/activate && python3 -m pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt && deactivate
# COPY nginx.crt /usr/local/share/ca-certificates/nginx.crt
# RUN update-ca-certificates

FROM python:3.6.9

RUN apt update -y
RUN apt install vim less jq -y

COPY requirements.txt /requirements.txt
COPY src /src
COPY conf /conf

RUN python3 -m pip install -i https://mirrors.aliyun.com/pypi/simple/ virtualenv
RUN virtualenv scapyenv
RUN . scapyenv/bin/activate && python3 -m pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt && deactivate

COPY cert.pem /usr/local/share/ca-certificates/cert.pem
RUN update-ca-certificates
