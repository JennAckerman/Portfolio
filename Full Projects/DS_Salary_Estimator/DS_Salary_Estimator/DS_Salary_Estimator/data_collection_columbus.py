# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 18:09:16 2020

@author: Jen butt
"""


import glassdoor_scraper as gs


path = "C:/Users/Jen butt/Desktop/R and Python/Glassdoor job/chromedriver"

df = gs.get_jobs('data scientist', 'Columbus, OH', 50, False, path, 15)

df.to_csv('C:/Users/Jen butt/Desktop/R and Python/Glassdoor job/DS_Salary_Estimator/Columbus_Jobs_list.csv')

