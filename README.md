# Youtube Videos API
**API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.**


# Highlights of the project:
- Used Django Server for backend
- PEP-8 Coding guidelines followed
- Docker used to containerize the project
- Dashboard to view all videos in database
- Asynchronously sync the database with Youtube APIs
- Expose videos available in the database as REST API

# Run Locally:
### Server can be run in two ways:

1. **Micro services** - Runs the API server and the Youtube-Database sync service separately. More scalable approach.
2. **Monolith** - Runs the API server along with the Youtube-Database sync service running asynchronously. This is less scalable as increasing the instances would increase the number of times the data is synced in the given interval and this may waste resources as well as consume the API Key quota unnecessarily.

* ## Using Docker - 
  **Uses Micro services**\
   **Make sure you have docker and docker-compose installed. If not, refer: https://docs.docker.com/install/**
   - Create an .env file from the .env.example.
   - Download [Docker-compose file form this repo](https://github.com/pnshiralkar/youtube-videos-api/docker-compose.yml)
   - Run `sudo docker-compose up`
* ### Download code and run - 
    **1. [Download](https://github.com/pnshiralkar/youtube-videos-api/archive/master.zip) and extract the zip of Project and cd inside**\
    **OR**\
    `git clone https://github.com/pnshiralkar/youtube-videos-api.git`\
    `cd youtube-videos-api`\
    **2.** `sudo pip install virtualenv`\
    **3.** `virtualenv venv`\
    **4.** `source venv/bin/activate`\
    **5.** `cd src`\
    **6.** `pip install -r requirements.txt`\
    **7.** Create an .env file from the .env.example in /src directory.\
    **8. Run Migrations -** `python manage.py makemigrations && python manage.py migrate`\
    **9. Running server:**
    - Monolithic way: Run `python manage.py runserver_with_sync`
    - Microservice way: Run in 2 different terminals: `python manage.py sync_with_youtube` and `python manage.py runserver`

    