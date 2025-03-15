"""
author: Ivan Tian
Date: 2025-3-11
Functions:
    1.company stock price + company basic information + company finance key number
    2.compare two companies' stock price 
    3.show two companies' financial reports
"""

from flask import Flask, render_template, request, redirect, url_for,session
import pandas as pd
import 