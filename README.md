# MorningSomewhereUtils
A MorningSomewhere listener's side project. Not official. 
## MorningSomewhereWebhook.py

### install via script/curl
```
$ bash -c "$(curl -fsSL https://raw.githubusercontent.com/NathanOrdSec/MorningSomewhereUtils/main/MSSetup.sh)"
```
### install via script/wget
```
$ bash -c "$(wget https://raw.githubusercontent.com/NathanOrdSec/MorningSomewhereUtils/main/MSSetup.sh -O -)"
```
I have now exceeded the character limit on Discord messages due to my spaghetti code. In any event, if you drop a Discord forum channel webhook link into this program, install Python3 and the requirements using the terminal command
```
pip3 install requests BeautifulSoup datetime discord_webhook time schedule pytz logging os
```
on a computer, and then run the program somehow (I do crontab -e on Linux and add "@reboot /path/to/PythonProgram.py". A "Scheduled Task" that runs on reboot for Windows would work too); it ought to just work every day at 6:10 am CST in theory. If the podcast blog post is not live yet, it will sit and loop, waiting for it to go live. Once the blog post is up, this webhook too will create a forum thread with the link dump and episode information in it.

![image](https://github.com/NathanOrdSec/MorningSomewhereUtils/assets/81328905/17bc6122-8e85-4994-9517-f50efe43e4b9)

Of course, I am still testing, updating, and cleaning things up on the fly, though, so expect updates. 
