# scraper
Check kimsufi for dedicated server.
This tiny script goes to the kimsufi site to find out if the SK10 servers are available, if they are it uses twilio to send notification at once.
It uses python filecompare to make a distinction between and old entry on the kimsufi site and a new entry. I have succesfully detected one, real time change.
I set the cron to run every second. But so far, I have not been able to snag a kimsufi server. 

I hope this helps you.
