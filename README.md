# epharma Microservice

In this we are trying to make a e-pharmacy web application with microservice architecture following devOps principes and practices powered with Test Driven Development(TDD) approach.

# Project Desired State and current Status

Currently this application contains User login features and further in the project we are likely to incorporated features like book Appointment, Drug Finder, Symptom checker etc.

We have unittests for the login funtion ready up until now and We are currently working on automating the builds with Jenkins CI. 

This Repository contains code only in develop branch as no staging and deployment have taken place.

# to up and run the Application follow the steps in order in your terminal

### set the service ip as localhost
$ export REACT_APP_USERS_SERVICE_URL=http://localhost

### to build the containers for the first time
$ docker-compose -f docker-compose-dev.yml build

### to run the containers
$ docker-compose -f docker-compose-dev.yml up -d

### to recreate the db 
$ docker-compose -f docker-compose-dev.yml run users python manage.py recreate-db

### to add some sample data into empty db
$ docker-compose -f docker-compose-dev.yml run users python manage.py seed-db

After this step we can look at http://localhost/ to see our app up and running.

### To stop the containers:
$ docker-compose -f docker-compose-dev.yml stop

### To bring down the containers:
$ docker-compose -f docker-compose-dev.yml down

# tests

### to run the users tests with coverage
$ docker-compose -f docker-compose-dev.yml run users python manage.py cov

### to do linting of the project folder
docker-compose -f docker-compose-dev.yml run users flake8 project

### to run the tests on the client UI
$ docker-compose -f docker-compose-dev.yml run client npm test
