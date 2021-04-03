# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:42:45 2021

@author: leontaridiss
"""

import numpy as np
import pandas as pd

df = pd.read_csv('data/listings.csv')

df = df[['host_response_time','host_response_rate','host_acceptance_rate', 'host_is_superhost', 'host_identity_verified' ,'neighbourhood_cleansed','room_type', 'accommodates', 'bathrooms_text', 'bedrooms','beds', 'amenities', 'price',
       'minimum_nights', 'maximum_nights', 'has_availability', 'number_of_reviews', 'review_scores_rating', 'review_scores_accuracy',
       'review_scores_cleanliness', 'review_scores_checkin',
       'review_scores_communication', 'review_scores_location',
       'review_scores_value', 'instant_bookable', 'reviews_per_month' ]]


amenities_list = list(df.amenities) 
amenities_list_string = " ".join(amenities_list) # group amenities in a string
amenities_list_string = amenities_list_string.replace('] [', ', ') # removing characters like []
amenities_list_string = amenities_list_string.replace('"', '') # make it more clean, removing "
x = amenities_list_string.split(", ") 
from collections import Counter
c = Counter(x)

amenities = pd.DataFrame(data = c.keys(), columns=['amenities'])
amenities = amenities.replace({'\[':''}, regex = True)
amenities = amenities.replace({'\]':''}, regex = True)

df.loc[df['amenities'].str.contains('24-hour check-in'), 'check_in_24h'] = 1
df.loc[df['amenities'].str.contains('Air conditioning|Central air conditioning|Window AC unit'), 'air_conditioning'] = 1
df.loc[df['amenities'].str.contains('Amazon Echo|Apple TV|Game console|Projector and screen|Smart TV'), 'high_end_electronics'] = 1
df.loc[df['amenities'].str.contains('BBQ grill|Fire pit|Propane barbeque|Barbecue utensils'), 'bbq'] = 1
df.loc[df['amenities'].str.contains('Balcony|Patio|Patio or balcony'), 'balcony'] = 1
df.loc[df['amenities'].str.contains('Beach view|Beachfront|Lake access|Mountain view|Ski-in/Ski-out|Waterfront'), 'nature_and_views'] = 1
df.loc[df['amenities'].str.contains('Bed linens'), 'bed_linen'] = 1
df.loc[df['amenities'].str.contains('Breakfast'), 'breakfast'] = 1
df.loc[df['amenities'].str.contains('TV|HDTV'), 'tv'] = 1
df.loc[df['amenities'].str.contains('Coffee maker|Espresso machine|Nespresso machine'), 'coffee_machine'] = 1
df.loc[df['amenities'].str.contains('Cooking basics|Electric stove|Toaster|Baking sheet|Microwave|Oven|Stove'), 'cooking_basics'] = 1
df.loc[df['amenities'].str.contains('Dishwasher|Dryer|Washer'), 'white_goods'] = 1
df.loc[df['amenities'].str.contains('Elevator'), 'elevator'] = 1
df.loc[df['amenities'].str.contains('Exercise equipment|Gym|gym'), 'gym'] = 1
df.loc[df['amenities'].str.contains('Family/kid friendly|Children|children'), 'child_friendly'] = 1
df.loc[df['amenities'].str.contains('parking|Free parking on premises|Paid parking garage off premises|Paid parking on premises|Paid parking off premises'), 'parking'] = 1
df.loc[df['amenities'].str.contains('Garden|Outdoor|Sun loungers|Terrace|Garden or backyard'), 'outdoor_space'] = 1
df.loc[df['amenities'].str.contains('Host greets you'), 'host_greeting'] = 1
df.loc[df['amenities'].str.contains('Hot tub|Jetted tub|hot tub|Sauna|Pool|pool'), 'hot_tub_sauna_or_pool'] = 1
df.loc[df['amenities'].str.contains('Internet|Pocket wifi|Wifi|wifi|Ethernet connection'), 'internet'] = 1
df.loc[df['amenities'].str.contains('Long term stays allowed'), 'long_term_stays'] = 1
df.loc[df['amenities'].str.contains('Pets|pet|Cat(s)|Dog(s)|Pets allowed'), 'pets_allowed'] = 1
df.loc[df['amenities'].str.contains('Private entrance'), 'private_entrance'] = 1
df.loc[df['amenities'].str.contains('Safe|Security system|Smart lock|Window guards'), 'secure'] = 1
df.loc[df['amenities'].str.contains('Self check-in'), 'self_check_in'] = 1
df.loc[df['amenities'].str.contains('Smoking allowed'), 'smoking_allowed'] = 1
df.loc[df['amenities'].str.contains('Step-free access|Wheelchair|Accessible'), 'accessible'] = 1
df.loc[df['amenities'].str.contains('Suitable for events'), 'event_suitable'] = 1
df.loc[df['amenities'].str.contains('Netflix|netflix|HDTV with Netflix'), 'netflix'] = 1
df.loc[df['amenities'].str.contains('Indoor fireplace'), 'fireplace'] = 1
df.loc[df['amenities'].str.contains('Cable TV'), 'cable_tv'] = 1
df.loc[df['amenities'].str.contains('Luggage dropoff allowed'), 'luggage_dropof_allowed'] = 1

df = df.iloc[:,26:]
df = df.replace(np.nan, 0)















