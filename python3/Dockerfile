FROM python:3

#libgl1-mesa-glx for opencv-python
RUN apt-get update && apt-get install -y nano cmake libgl1-mesa-glx

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY apps/hello.py /usr/src/app/
VOLUME /usr/src/app

ENTRYPOINT ["python"]
CMD ["hello.py"]
