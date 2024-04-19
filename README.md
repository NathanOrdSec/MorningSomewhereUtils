# MorningSomewhereUtils

## MorningSomewhereWebhook.py
I have now exceeded the character limit on Discord messages due to my spaghetti code. In any event, if you drop a Discord forum channel webhook link into this program, install Python3 and the requirements using the terminal command
```
pip3 install requests BeautifulSoup datetime discord_webhook time schedule pytz
```
on a computer, and then run the program somehow (I do crontab -e on Linux and add "@reboot /path/to/PythonProgram.py". A "Scheduled Task" that runs on reboot for Windows would work too); it ought to just work every day at 6:10 am CST in theory. If the podcast blog post is not live yet, it will sit and loop waiting for it to go live. 

Of course, I am still testing, updating, and cleaning things up on the fly, though, so expect updates. 
