FROM python:3.8-slim-buster

WORKDIR /app

#first requiremnts is one which is in our project folder 
# second requirement is inside our app folder which is in docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# COPY . .
#8000 is container port through which outside world can connect to container
# CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
