#!/bin/bash

mkdir /opt/MSPod
cd /opt/MSPod

curl -o MSPod.py https://raw.githubusercontent.com/NathanOrdSec/MorningSomewhereUtils/main/MorningSomewhereWebhook>

read -p "Enter your Discord Forum Webhook URL: " URL
echo $URL

sed -i "s/{INSERT DISCORD FORUM CHANNEL WEBHOOK HERE}/$URL/g" /opt/MSPod2/MSPod.py

curl -o /etc/systemd/system/MSPodWebhook.service https://raw.githubusercontent.com/NathanOrdSec/MorningSomewhereUt>

systemctl enable MSPodWebhook.service
systemctl daemon-reload
systemctl start MSPodWebhook.service
