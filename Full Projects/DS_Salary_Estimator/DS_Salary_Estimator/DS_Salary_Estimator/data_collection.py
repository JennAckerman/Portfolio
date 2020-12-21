# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 18:09:16 2020

@author: Jen butt
"""


import glassdoor_scraper as gs


path = "C:/Users/Jen butt/Desktop/R and Python/Glassdoor job/chromedriver"

df = gs.get_jobs('data scientist', 'United States', 1000, False, path, 20)

df.to_csv('C:/Users/Jen butt/Desktop/R and Python/Glassdoor job/DS_Salary_Estimator/Jobs_list.csv')

