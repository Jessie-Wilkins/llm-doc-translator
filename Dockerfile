FROM ubuntu:24.04

RUN apt-get update \ 
&& apt-get install tesseract-ocr tesseract-ocr-chi-sim python3 python3-pip -y \
&& python3 -m pip install easyocr langchain opencv-python