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

#creating new columns for month number and year from job_posted_date

def add_month(given_df):
    given_df['job_posted_month_no']=given_df.job_posted_date.dt.month
    return given_df

def add_year(given_df):
    given_df['job_posted_year']=given_df.job_posted_date.dt.year
    return given_df