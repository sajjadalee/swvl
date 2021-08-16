# swvl

Sending Notification/Group Notifications to targets.

Acheived this with multithreading used celery for the tasks management and redis for the message broker.

Used Signals to start a nwe worker process whenever a request for notifications has been made.

Track the status of any notification using UUID.

Dockerized the solution for running it in 3 very simple steps:

1 : sudo docker-compose build
2 : sudo docker-compose up
3 : sudo docker-compose run web python manage.py createsuperuser

Exposed Endpoints:

1 : /api/token/ (to get the access of a token for the user thats created)
2 : localhost:8000/ (POST)
3 : localhost:8000/ (GET)
