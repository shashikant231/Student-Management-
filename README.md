### Installation Guide

Open terminal : ctrl+alt+T \
Inside new Folder
git clone https://github.com/shashikant231/Student-Management-.git

 ### Set up virtualenv
To create  - virtualenv env \
To activate - source/env/bin/activate
 
### Install Requirements file 
pip install -r requirements.txt

 
 ### prepare for migrations and then migrate
 python manage.py makemigrations \
 python manage.py migrate

 ### Run the server
 python manage.py runserver
 