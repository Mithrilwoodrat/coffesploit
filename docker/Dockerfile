FROM ubuntu:latest
MAINTAINER woodrat
WORKDIR /root

RUN apt-get update&&\
    apt-get install -y build-essential&&\
    apt-get install -y gcc&&\
    apt-get install -y python2.7&&\
    apt-get install -y nmap
    
#install pip
COPY get-pip.py /root/

RUN python get-pip.py

CMD rm get-pip.py

#install python requirements
ADD requirements.txt /root/

CMD pip2 install -r requirements.txt

COPY src /root/ 

EXPOSE 5000     