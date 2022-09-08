FROM ubuntu


RUN apt-get -o Acquire::Check-Valid-Until=false -o Acquire::Check-Date=false update && \
    apt-get -y install software-properties-common

# install requirements
RUN apt-get -y install nginx 
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install \
    # for python-mysql
    build-essential \
    libmariadb-dev \
    musl-dev

# ?
RUN apt-get -y dist-upgrade

# for uwsgi
# RUN apt-get -y install linux-headers-$(uname -r)
RUN apt-get -y install \
    linux-headers-generic

# for debug
RUN apt-get -y install curl

# change path
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

# install python packages
RUN mkdir -p /var/scat
ADD requirements.txt /var/scat/
RUN pip3 install -r /var/scat/requirements.txt

# copy project and nginx configuration
COPY default.conf /etc/nginx/conf.d/default.conf

# ?
EXPOSE 80
