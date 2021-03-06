# Youtube Videos API
**API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.**


# Highlights of the project:
- Used Django Server for backend
- PEP-8 Coding guidelines followed
- Docker used to containerize the project
- Admin Dashboard to view all videos in database
- Multiple API Keys can be added from the admin dashboard
- Asynchronously sync the database with Youtube APIs
- Expose videos available in the database as REST API

# Run Locally:
### Server can be run in two ways:

1. **Micro services** - Runs the API server and the Youtube-Database sync service separately. More scalable approach.
2. **Monolith** - Runs the API server along with the Youtube-Database sync service running asynchronously. This is less scalable as increasing the instances would increase the number of times the data is synced in the given interval and this may waste resources as well as consume the API Key quota unnecessarily.

* ## Using Docker - 
  **Uses Micro services**\
   **Make sure you have docker and docker-compose installed. If not, refer: https://docs.docker.com/install/**
   - Create an .env file from the [.env.example file from repo](https://github.com/pnshiralkar/youtube-videos-api/blob/main/.env.example).
   - Download [Docker-compose file form this repo](https://github.com/pnshiralkar/youtube-videos-api/blob/main/docker-compose.yml)
   - Run `docker-compose up`
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
    **9. Collect Static files -** `python manage.py collectstatic` (Required for Admin Dashboard)\
    **10. Running server:**
    - Monolithic way: Run `python manage.py runserver_with_sync`
    - Microservice way: Run in 2 different terminals: `python manage.py sync_with_youtube` and `python manage.py runserver`

# Details of Project:
 - As soon as the server is started, the sync service starts syncing the database with Youtube API at an interval set in .env file (default 10s)
 - Admin dashboard can be accessed at <base_url>/admin. The default database supplied has admin credentials - Username = admin , Password = admin
 - The API Keys can be added from admin dashboard. Please add an API Key to database from dashboard. 
 - The videos in the database are available as REST API at <base_url>/videos
 - The response defaults to 50 videos at once. To view next ones, use <base_url>/videos?page=<page_num>. The response includes previous and next page numbers.
 - The videos dashboard is available in admin dashboard itslef, at <base_url>/admin/videos/video.
 - The console logs all the requests coming to the server, as well as the sync activity details.
