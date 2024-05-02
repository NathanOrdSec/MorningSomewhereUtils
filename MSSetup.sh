#!/bin/bash

#Make Directory
mkdir /opt/MSPod
cd /opt/MSPod

#Install Requirements
apt install python3 python3-pip

pip3 install requests BeautifulSoup datetime discord_webhook time schedule pytz logging os

#Get Files
curl -o MSPod.py https://raw.githubusercontent.com/NathanOrdSec/MorningSomewhereUtils/main/MorningSomewhereWebhook.py

read -p "Enter your Discord Forum Webhook URL: " URL

#Replace Placeholder with Discord Webhook URL
sed -i "s@{INSERT DISCORD FORUM CHANNEL WEBHOOK HERE}@$URL@g" /opt/MSPod/MSPod.py

#Create system service and run it!
curl -o /etc/systemd/system/MSPodWebhook.service https://raw.githubusercontent.com/NathanOrdSec/MorningSomewhereUtils/main/mspod.service

systemctl enable MSPodWebhook.service
systemctl daemon-reload
systemctl start MSPodWebhook.service
