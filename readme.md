#### Repo

-  https://github.com/centrodph/fullstack-tp

-  Front End: http://localhost:3000
-  Back End: http://localhost:8000
    -  Admin: http://localhost:8000/admin
    -  Docs: http://localhost:8000/doc
    -  Open API: http://localhost:8000/api

#### Setup steps

-  yarn front:install

    `$ cd client && yarn install`

-  yarn server:install

    `$ source env/bin/activate && cd api && pip install -r requirements.txt`

-  yarn front:start

    `$ cd client && yarn dev`

-  yarn server:start

    `$ source env/bin/activate && cd api && python manage.py runserver`

-  yarn server:migrate

    `$ cd api && python manage.py migrate`

-  yarn server:makemigrations

    `$ cd api && python manage.py makemigrations`

-  yarn server:createsuperuser

    `$ cd api && python manage.py createsuperuser`


#### Development

-  yarn front:start
-  yarn server:start

#### Login using

- admin admin

- User-Interviewer 8kLNEheFS@2M7PT


#### BackEnd screenshots

- API
<img width="1410" alt="Screen Shot 2022-06-20 at 19 55 06" src="https://user-images.githubusercontent.com/2073951/174686663-06b58376-255a-46d0-8816-613c7cf9b7a5.png">

- Models
<img width="1392" alt="Screen Shot 2022-06-20 at 19 55 15" src="https://user-images.githubusercontent.com/2073951/174686667-d1b10fcd-c9da-4f10-a61a-cda70d7cef4c.png">

- ADMIN
<img width="1407" alt="Screen Shot 2022-06-20 at 19 55 28" src="https://user-images.githubusercontent.com/2073951/174686669-e516f49a-ce1a-409e-be43-4fc5fae03be3.png">





#### FrontEnd screenshots


- login with user/pass
<img width="1046" alt="Screen Shot 2022-06-20 at 19 39 38" src="https://user-images.githubusercontent.com/2073951/174685693-bed61c00-0300-4bc3-a9d8-80bb46567b81.png">

- login errors
<img width="1237" alt="Screen Shot 2022-07-04 at 14 11 16" src="https://user-images.githubusercontent.com/2073951/177197259-4494a390-3030-418a-99e0-6e965234862e.png">


- ir a entrevista o ver resultados
<img width="1062" alt="Screen Shot 2022-07-04 at 14 13 23" src="https://user-images.githubusercontent.com/2073951/177197318-f138852a-48b5-4776-9f90-d877209ef3cd.png">


- resultados de entrevista
<img width="1061" alt="Screen Shot 2022-07-04 at 14 14 30" src="https://user-images.githubusercontent.com/2073951/177197374-ca422a7f-5e4e-4b6e-a127-8b442662bd08.png">


- ir a la entrevista es para ejecutar el cuestionario
<img width="1043" alt="Screen Shot 2022-06-20 at 19 40 23" src="https://user-images.githubusercontent.com/2073951/174685697-24bcbf89-1c32-4ac8-a350-b70a4296a869.png">

- abm candidatos list
<img width="1033" alt="Screen Shot 2022-06-20 at 19 40 45" src="https://user-images.githubusercontent.com/2073951/174685705-186a53c9-66a0-4698-b53a-146ec0d0d043.png">

- abm candidatos create
<img width="1040" alt="Screen Shot 2022-06-20 at 19 40 55" src="https://user-images.githubusercontent.com/2073951/174685708-0203119a-946f-44c0-999a-f9c36c6667ce.png">


- abm candidatos edit
<img width="1035" alt="Screen Shot 2022-06-20 at 19 41 07" src="https://user-images.githubusercontent.com/2073951/174685709-97cffff5-7f18-4045-89f4-ab765231f2d2.png">


- list
<img width="1043" alt="Screen Shot 2022-06-20 at 19 41 22" src="https://user-images.githubusercontent.com/2073951/174685712-f3491101-307d-424a-b63d-1f968731900b.png">

- Interview complex form
<img width="1044" alt="Screen Shot 2022-06-20 at 19 41 33" src="https://user-images.githubusercontent.com/2073951/174685715-283dcd8a-19d9-4f31-81c0-c4b939e84682.png">


### TODO

 - [X] Add login using JWT
 - [X] Add security to Candidates
 - [ ] Add security to Interviews
 - [ ] Add security to Questions
 - [ ] Add security to Challenges



#### Deploy Guidelines


-  https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-deploy

- EBCli install: https://github.com/aws/aws-elastic-beanstalk-cli-setup



#### ec2 no implementado


- https://www.youtube.com/watch?v=u0oEIqQV_-E

-   apt-get update
-   apt-get upgrade -y
-   apt-get install libgdal-dev
-   apt install python3-pip
-   pip install virtualenv
-   pip install GDAL
-   virtualenv env
-   git clone https://github.com/centrodph/fullstack-tp.git
-   source env/bin/activate
-   pip install django
-   pip install gunicorn
-   apt-get install -y nginx
    -   start nginx: nginx
-   apt-get install npm
-   npm install -g yarn
-   apt-get install supervisor
    - add supervisor config:
        - cd /etc/supervisor/conf.d/
        - touch gunicorn.conf
        [program:gunicorn]
        directory=/home/ubuntu


-   AWS: config inbound rules for security group

-   cd fullstack/api
-   gunicorn --bind 0.0.0.0:8000 interview_project.wsgi:application

Open aplication: http://ec2-18-236-160-0.us-west-2.compute.amazonaws.com:8000/doc
