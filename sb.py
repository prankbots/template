from lineX import *
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
butt = codecs.open("importible/button.json","r","utf-8")
fill = codecs.open("importible/filler.json","r","utf-8")
imag = codecs.open("importible/image.json","r","utf-8")
boob = codecs.open("importible/booble.json","r","utf-8")
tek = codecs.open("importible/teks.json","r","utf-8")
button = json.load(butt)
filler = json.load(fill)
image = json.load(imag)
booble = json.load(boob)
teks = json.load(tek)
me = LINE()
TEMP_ID = "1635019713"
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
      to = template.to
      if pesan == "button" or pesan == "Button":
        me.sendFlex(to, button["button"])
      elif pesan == "filler" or pesan == "Filler":
        me.sendFlex(to, filler["filler"])
      elif pesan == "image" or pesan == "Image":
        me.sendFlex(to, image["images"])
      elif pesan == "teks" or pesan == "Teks":
        me.sendFlex(to, teks["teks"])
      elif pesan == "booble" or pesan == "Booble":
        me.sendFlex(to, booble["booble"])
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
    me.log("WHILE TRUE\n" + str(e))
