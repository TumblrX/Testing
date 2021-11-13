FROM appium/appium:latest

#WORKDIR /root
#RUN apt-get update
#RUN apt-get install python3
#RUN apt-get update
#RUN apt-get install python-pip3

RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get install -y \
    python3.8 \
    python3-pip

RUN pip3 install --upgrade pip

RUN pip install Appium-Python-Client

COPY ./appium_test ./appium_test

RUN appium


