
#please make copy or keep a backup of admin/media file for previous deployment
#and paste it after pulling from develop branch and then deploy

#go to the project directory ../Blogadmin And install the venv
sudo apt-get install python3
sudo apt-get install -y python3-pip
pip3 install virtualenv
virtualenv venv
.venv/bin/activate OR source venv/bin/activate

#inside the venv install the packages
#install packages

pip3 install -r requirements.txt

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

#inside admin folder check if static/images/sinbad-logo1.png is there
#If not the create the folder inside static
#you will find the logo in sinbad-logo1.png in base directory of the project 
   images/sinbad-logo1.png


# run the project Port address
./manage.py runserver Portaddress
Example: ./manage.py runserver 8000





#the api address Http//hostadress:port/api/blogs/
Example:http://127.0.0.1:8000/api/blogs/


