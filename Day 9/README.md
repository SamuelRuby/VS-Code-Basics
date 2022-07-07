Web App with FLASK, NGROK, INVICIFY & FASTAPI


WE ARE GOING TO CREATE A WEB APPLICATION USING 2 SEPERATE FRAMEWORKS AND THEN MAKE IT ACCESSIBLE TO THE INTERNET AND RUN SCHEDULED JOBS AND WORKFLOWS WITH THESE.

CHALLENGE: MAKE IT EASY TO RUN MY WEB SCRAPING EVENTS AND MAKE IT ACCESSIBLE TO THE INTERNET, WITHOUT NO MANUAL INTERFERENCE

WE'LL USE FLASK AND FASTAPI TO MAKE LOCAL RUNNING WEBSERVERS, AND THEN USE NGROK TO GIVE US A LIVE URL, AND USE INVICIFY TO TRIGGER NGROK ENDPOINT (TO GIVE US WEBHOOK DATA ON A SCHEDULED TIME MAYBE EVERY HOUR)


flask and fastapi- are microframeworks.



Links below::---

https://www.ngrok.com - expose a locally running server to a live URL endpoint securely. Ngrok makes it easy to "deploy" your locally running web app to the internet, it's perfect for testing or handling a minimal amount of requests. And yes, there's a free tier.


https://www.invictify.com - send webhooks on your schedule to trigger any kind of task. Invicity replaces the need to run your own worker process (like using Celery and Redis) and there's a free tier.