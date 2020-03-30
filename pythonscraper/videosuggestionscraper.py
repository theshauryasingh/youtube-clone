# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 23:51:41 2020

@author: Lenovo
"""

from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
chromedriver_path = 'J://microverse_projects//youtube-clone//pythonscraper//chromedriver_win32/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)
sleep(2)

webdriver.get('https://www.youtube.com/watch?v=uBB7t_eZOO4&list=TLPQMjYwMzIwMjC1cT3972MR0g&index=21')
sleep(3) 

for i in range(1,12):
    print(webdriver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[2]/div/div[3]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-video-renderer[" + str(i) + "]/div[1]/div/div[1]/a/h3/span").text)
    print(webdriver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[2]/div/div[3]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-video-renderer[" + str(i) + "]/div[1]/div/div[1]/a/div/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/div/div/yt-formatted-string").text)
    print(webdriver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[2]/div/div[3]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-video-renderer[" + str(i) + "]/div[1]/div/div[1]/a/div/ytd-video-meta-block/div[1]/div[2]/span[1]").text)
    a = webdriver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[2]/div/div[3]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-video-renderer[' + str(i) + ']/div[1]/ytd-thumbnail/a/yt-img-shadow/img')
    print(str(a.get_attribute("src")).split('?sqp')[0])
