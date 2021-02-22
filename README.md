# drf-quasar-media-server

Web application for playing video on a local network on a computer or mobile device.

A standard HTML5 player is used as a video player. The following formats were tested: mp4, webm.

## Project setup

1. Change environment variables in **.env** and **backend/.env** files
   1. PORT - port for connecting to the web application
   2. POSTGRES_USER - database username
   3. POSTGRES_PASSWORD - database password
   4. POSTGRES_DB - database name
   5. TIMEZONE - time zone
   6. DJANGO_SUPERUSER_USERNAME - admin username
   7. DJANGO_SUPERUSER_EMAIL - admin email
   8. DJANGO_SUPERUSER_PASSWORD - admin password
2. Uncomment the lines in the file **backend/prestart.sh** to create tables in the database and add an administrator account (after the first run with the command **docker-compose up**, comment out again)

    ```sh
    export $(egrep -v '^#' .env | xargs)
    python manage.py migrate
    python manage.py createsuperuser \
      --noinput \
      --username $DJANGO_SUPERUSER_USERNAME \
      --email $DJANGO_SUPERUSER_EMAIL
    ```

3. Change the path to the video folder in the **docker-compose.prod.yml** file.

    ```yml
    # EXAMPLE
    webserver:
      volumes:
        - </DIR1/DIR2/VIDEOS>:/media
    ```

## Run web application

1. [Install Docker](https://docs.docker.com/engine/install/)
2. Run Docker containers in command line from project folder: `docker-compose -f docker-compose.prod.yml up -d`
3. Open browser on computer or mobile device: `<SERVER IP, EXAMPLE: 192.168.0.21>:<YOUR PORT, default port 8080>`
