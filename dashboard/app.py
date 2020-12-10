#!/usr/bin/env python
# coding: utf-8

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
import json
import string
import spacy
from spacy.lang.en import English
import numpy as np
from matplotlib import rc, pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

july20_db = 'data/job_ads_container_large_july2020.csv'
oct20_db = 'data/job_ads_container_large_july2020.csv'
dec20_db = 'data/job_ads_container_dec20.csv'

