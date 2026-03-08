import pandas as pd
import data_jobs.data_access as da
from ast import literal_eval


# convert job_posted_date(string) to datetime.
def clean_date(df):
    df = df.copy()
    df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
    return df

# converting each row of 'job_skill' column to list 
def clean_skills(df):
    df = df.copy()
    df['job_skills'] = df['job_skills'].map(lambda x: literal_eval(x) 
                                          if pd.notna(x) else x)
    return df

#creating new columns for month and year of job_posted_date
def add_month(df):
    mod_data = df.copy()
    mod_data['job_posted_month']=mod_data.job_posted_date.dt.month
    return mod_data

def add_year():
    mod_data = clean_date()
    mod_data['job_posted_year']=mod_data.job_posted_date.dt.year
    return mod_data