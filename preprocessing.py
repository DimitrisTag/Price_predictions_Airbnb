# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:02:27 2021

@author: leontaridiss
"""
import numpy as np
import pandas as pd
df = pd.read_csv('data/listings.csv')
amenities_columns = pd.read_csv('data/amenities_columns.csv')

df = df[['host_response_time','host_response_rate','host_acceptance_rate', 'host_is_superhost', 'host_identity_verified' ,'neighbourhood_cleansed','room_type', 'accommodates', 'bathrooms_text', 'bedrooms','beds', 'amenities', 'price',
       'minimum_nights', 'maximum_nights', 'has_availability', 'number_of_reviews', 'review_scores_rating', 'review_scores_accuracy',
       'review_scores_cleanliness', 'review_scores_checkin',
       'review_scores_communication', 'review_scores_location',
       'review_scores_value', 'instant_bookable', 'reviews_per_month' ]]

# Get list of categorical variables
s = (df.dtypes == 'object')
object_cols = list(s[s].index)

print("Categorical variables:")
print(object_cols)

df.host_response_rate = df.host_response_rate.replace({'\%':''}, regex = True).astype(float)
df.host_acceptance_rate = df.host_acceptance_rate.replace({'\%':''}, regex = True).astype(float)

df.price = df.price.replace({'\$':''}, regex = True)
df.price = df.price.replace({'\,':''}, regex = True).astype(float)

# df['number_of_baths'] = df.bathrooms_text.str.replace(r'[^0-9]+', '')
# df['text_of_baths'] = df.bathrooms_text.str.extract('(\D+)', expand=False)

# df['number_of_baths'] = df.bathrooms_text.str.replace('^[^\d]*', '')

df['number_of_baths'] = df.bathrooms_text.str.replace(r"[a-zA-Z]",'')
df['number_of_baths'] = df.number_of_baths.replace({'\-':np.nan}, regex = True)
df['number_of_baths'] = df['number_of_baths'].astype(float)

 
c = df.bathrooms_text.str.split(' ', expand = True)
df['shared_bath'] = c[1]

df.shared_bath = df.shared_bath == 'shared'
df = df.drop(columns = ['bathrooms_text', 'amenities'], axis = 1)
df = pd.concat([df, amenities_columns], axis=1)

