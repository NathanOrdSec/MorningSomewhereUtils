#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import datetime
from discord_webhook import DiscordWebhook,DiscordEmbed
import time
import schedule
from pytz import timezone

webhookURL="{INSERT DISCORD FORUM CHANNEL WEBHOOK HERE}"

def descParse(raw):
    link=raw.find("a").get('href')
    linkName=raw.find("a").get_text()
    parsed=""""""
    parsed="\n\n".join(raw.strings)
    parsed=parsed.replace(linkName,"[{label}]({link})".format(label=linkName,link=link))
    return parsed

def requestHandler(url):
    if url is None:
        return None
    response=requests.get(url)
    time=0
    while (response==400 or response is None):
        print("In Wait Loop")
        time.sleep(120+time)
        response=requests.get(url)
        time+=60
    return response

def fetchHref(content):
    if content is None:
        return None,None
    else:
        urlDesc=content.get_text()
        URL=content.get('href')
    return urlDesc,URL

def soupParse(req,timeout):
    if req is None:
        if timeout>6000:
            exit()
        time.sleep(timeout+60)
        soupParse(req,timeout+60)
        return
    else:
        return BeautifulSoup(req.content, 'html.parser')


def main():
    #Fetch Date Category
    date = datetime.datetime.now()
    r = requestHandler('https://morningsomewhere.com/{year}/{month}/{day}'.format(year=date.strftime("%Y"),month=date.strftime("%m"),day=date.strftime("%d")))
    soup = soupParse(r,0)

    #Fetch Today's Podcast
    linkDesc,episodeLink=fetchHref(soup.find("a",class_="megaphone-button megaphone-button-hollow megaphone-button-medium"))
    #Fetch Podcast Page

    r = requestHandler(episodeLink)

    soup = soupParse(r,0)

    podTitle=soup.find("h1",class_="entry-title h2 mb-4 mb-sm-4 mb-md-4").get_text()
    linkdump=soup.find("div",class_="entry-content entry-single clearfix")
    desc=descParse(soup.find("figcaption",class_="wp-element-caption"))
    image=soup.find("img",class_="wp-post-image").get('data-orig-file')

    #Get Spotify Link
    spotify = linkdump.find("iframe").get("src").replace("/embed/","/")

    #Parse Linkdump
    p_tag = linkdump.find_all("p")
    linkdumpDict={}
    for pt in p_tag:
            if len(pt)==0:
                    break
            linkdumpDict[pt.get_text()]=[]
            for li in pt.find_next_siblings("ul")[0].find_all("a"):
                    links="* {text}: {link}".format(text=li.get_text(),link=li.get('href'))
                    linkdumpDict[pt.get_text()].append(links)

    #Setup Webhook
    webhook=DiscordWebhook(url=webhookURL,thread_name=podTitle,image="https://i0.wp.com/morningsomewhere.com/wp-content/uploads/2023/12/cropped-icon.png")
    titleEmbed = DiscordEmbed(title="", description="", color="FFFFFF")
    titleEmbed.set_image(url="https://morningsomewhere.com/wp-content/uploads/2023/12/logo-horiz-web-231211-sm.png")

    episodeEmbed = DiscordEmbed(title="{}".format(podTitle), description="{}".format(desc), color="FAD663")

    linkEmbed = DiscordEmbed(title="Link Dump", description=" ", color="ADC567")
    for key in linkdumpDict.keys():
        if len("\n".join(linkdumpDict[key]))>1024:
            linkTrunc=""""""
            for singleLink in linkdumpDict[key]:
                linkTrunc+="\n"+singleLink
                if len(linkTrunc)>=800:
                    break
            linkTrunc+="\n\nTruncated: See {}".format(link)
            print(linkTrunc)
            linkEmbed.add_embed_field(name=key, value=linkTrunc,inline=False)
        else:
            linkEmbed.add_embed_field(name=key, value=("\n".join(linkdumpDict[key])),inline=False)

    spotifyEmbed = DiscordEmbed(title="Morning Somewherde - Spotify", description="", url=spotify, color="80B770")

    appleEmbed = DiscordEmbed(title="Morning Somewhere - Apple Podcasts", description="", url="https://podcasts.apple.com/us/podcast/morning-somewhere/id1728257931", color="4E7E42")

    websiteEmbed = DiscordEmbed(title="Morning Somewhere Website", description="", url=episodeLink, color="2A5539")

    heroEmbed = DiscordEmbed(title="", description="", color="EEA63F")
    heroEmbed.set_image(url=image)

    webhook.add_embed(titleEmbed)
    webhook.add_embed(heroEmbed)
    webhook.add_embed(episodeEmbed)
    webhook.add_embed(linkEmbed)
    webhook.add_embed(spotifyEmbed)
    webhook.add_embed(appleEmbed)
    webhook.add_embed(websiteEmbed)
    response = webhook.execute()

schedule.every().day.at("06:10","US/Central").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
