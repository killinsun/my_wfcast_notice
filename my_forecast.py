#-*- coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

url  = 'https://weather.yahoo.co.jp/weather/jp/11/4310.html'
html = urllib.request.urlopen(url).read()

soup		= BeautifulSoup(html, 'html.parser')
fcastCity	= soup.find("div",		class_="forecastCity")

print("===================")
for fcast in fcastCity.select('div'):
	day			= fcast.find("p",	class_="date").get_text()
	weather		= fcast.find("p",	class_="pict").get_text()
	highTmp		= fcast.find("li",	class_="high").get_text()
	lowTmp		= fcast.find("li",	class_="low").get_text()
	print(day)
	print(weather)
	print(highTmp)
	print(lowTmp)
	print("--------------")
