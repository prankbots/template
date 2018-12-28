from lineX import *
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
butt = codecs.open("importible/button.json","r","utf-8")
button = json.load(butt)
me = LINE()
TEMP_ID = "1623679774"
channel = Channel(me, TEMP_ID)
oepoll = OEPoll(me)
meProfile = me.getProfile()
meM = me.getProfile().mid
def resp(flex):
  try:
    if flex.type == 0:
      return
    if flex.type == 25:
      template = flex.message
      pesan = template.text
    if template.toType == 0 or template.toType == 1 or template.toType == 2:
        if template.toType == 0:
          if template._from != me.profile.mid:
            to = template._from
          else:
            to = template.to
        elif template.toType == 1:
          to = template.to
        elif template.toType == 2:
          to = template.to
        if template.contentType == 0:
          if pesan is None:
            return
          else:
            if pesan == "button":
              me.sendFlex(to, button["button"])
            elif pesan == "flex":
              template1 = ("https://stickershop.line-scdn.net/stickershop/v1/product/1169/LINEStorePC/main.png;compress=true?__=20161019")
              template2 = ("https://stickershop.line-scdn.net/stickershop/v1/product/1008584/LINEStorePC/main.png;compress=true")
              template3 = ("https://stickershop.line-scdn.net/stickershop/v1/product/1054797/LINEStorePC/main.png;compress=true?__=20161019")
              data = {
                "type": "flex",
                "altText": "{} membagikan flex".format(str(meProfile.displayName)),
                "contents": {
                  "type": "bubble",
                  "body": {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "md",
                    "contents": [
                      {
                        "type": "image",
                        "url": template1,
                      },
                      {
                        "type": "image",
                        "url": template2,
                      },
                      {
                        "type": "image",
                        "url": template3,
                      }
                    ]
                  }
                }
              }
              me.sendFlex(to,data)
  except Exception as e:
    print(e)
    if flex.type == 59:
      print(flex)
while True:
  try:
    ops=oepoll.singleTrace(count=50)
    if ops != None:
      for flex in ops: 
        resp(flex)
        oepoll.setRevision(flex.revision)       
  except Exception as e:
    me.log("EROR WHILE TRUE\n" + str(e))
