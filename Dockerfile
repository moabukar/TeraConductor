FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update 
RUN apt-get install -y  curl python3 gnupg2 lsb-release software-properties-common python3-pip && apt-get clean all &&\
    pip3 install awscli && pip3 install awscli --upgrade && curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - && \
    apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" && \
    apt-get update && apt-get install packer ansible terraform nodejs npm wget -y && npm install -g aws-cdk 

