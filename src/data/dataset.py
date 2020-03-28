#!/usr/bin/python3

import pandas as pd
import os
import json
import requests
from subprocess import Popen, PIPE


def download_us_states_mortality_rates_dataset():
    process = Popen([os.path.join(os.path.dirname(__file__), 'worldometers_webscraper.rb')], stdout=PIPE, stderr=PIPE)
    mortality_rate_data = json.loads(process.communicate()[0].decode().strip())
    df = pd.DataFrame(mortality_rate_data)
    df['mortality_rate'] = pd.Series([df['deaths'][i] / df['cases'][i] if df['cases'][i] > 0 else 0 for i in df.index])
    df.to_csv(os.path.join(os.path.dirname(__file__), 'datasets', 'us_states_mortality_rates.csv'), index=False)


def download_country_mortality_rates_dataset():
    response = requests.get('https://datahub.io/core/covid-19/r/time-series-19-covid-combined.csv')
    with open(os.path.join(os.path.dirname(__file__), 'datasets', 'country_mortality_rates.csv'), 'wb') as file:
        file.write(response.content)
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'datasets', 'country_mortality_rates.csv'))
    df = df.loc[df['Date'] == df['Date'].max()]
    df = df.drop(['Date', 'Lat', 'Long'], axis=1)
    df = df.rename(columns={'Deaths': 'deaths', 'Confirmed': 'cases', 'Country/Region': 'country', 'Province/State': 'state'})
    df = df.reset_index(drop=True)
    df['mortality_rate'] = pd.Series([df['deaths'][i] / df['cases'][i] if df['cases'][i] > 0 else 0 for i in df.index])
    df.to_csv(os.path.join(os.path.dirname(__file__), 'datasets', 'country_mortality_rates.csv'), index=False)


def merge_mortality_rates_datasets():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'datasets', 'country_mortality_rates.csv'))
    df2 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'datasets', 'us_states_mortality_rates.csv'))
    df = df.drop(df.loc[df['country'] == 'US'].index)
    df = df.reset_index(drop=True)
    for i in df2.index:
        df = df.append(pd.Series(['US', df2['states'][i], df2['cases'][i], df2['deaths'][i], df2['mortality_rate'][i]], index=['country', 'state', 'cases', 'deaths', 'mortality_rate']), ignore_index=True)
    df = df.sort_values(['country', 'state'])
    df.to_csv(os.path.join(os.path.dirname(__file__), 'datasets', 'mortality_rates.csv'), index=False)
