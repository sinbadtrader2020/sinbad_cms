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

#BlogAdmin folder setting.py file need to edit the databes
DATABASES = {
    'default': {
       
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        
        'NAME': 'blog', #database name

        'USER': 'postgres',  #postgres user name

        'PASSWORD': 'admin', #postgres password

        'HOST': '127.0.0.1', #host name

        'PORT': '5432' #port number
    }
}


# after installation and connecting database make migration
./manage.py makemigrations
./manage.py migrate
#ceate a superuser
#this user will have all the permission of sinbad admib panel
./manage.py createsuperuser

# run the project Port address
./manage.py runserver Portaddress
Example: ./manage.py runserver 8000





#the api address Http//hostadress:port/api/blogs/
Example:http://127.0.0.1:8000/api/blogs/