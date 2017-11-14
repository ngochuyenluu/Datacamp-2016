#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 21:23:22 2016

@author: ngochuyenluu
"""

import pandas as pd

df = pd.read_csv("./train1.csv")

def df_describe():
    return print("data for analysis: ", df.describe())

def df_head():
    return print ("data head: ", df.head())

def answer_1():
    return df[df['']]
    
