#go to the project directory ../Blogadmin And install the venv
sudo apt-get install python3
sudo apt-get install -y python3-pip
pip3 install virtualenv
virtualenv venv
.venv/bin/activate OR source venv/bin/activate

#inside the venv install the packages
#install packages
pip install docutils

pip install djangorestframework

pip install django-ckeditor

pip install django-cors-headers

pip install psycopg2-binary

pip install requests 

pip install pillow

# after installation make migration
./manage.py makemigrations
./manage.py migrate

# run the project Port address
./manage.py runserver Portaddress
Example: ./manage.py runserver 8000





#the api address Http//address/api/blogs/
Exaple:http://127.0.0.1:8000/api/blogs/