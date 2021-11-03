FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app  

EXPOSE 5501

CMD [ "python3", "-m" , "discord", "run", "--host=0.0.0.0"]