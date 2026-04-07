import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# --- SETTINGS ---
num_orders = 5000
start_date = datetime(2026, 1, 1)

# --- 1. GENERATE DIM_MENU ---
menu_data = {
    'Item_ID': [101, 102, 103, 104, 105],
    'Item_Name': ['Margherita Pizza', 'Quinoa Salad', 'Truffle Fries', 'Miso Ramen', 'Iced Latte'],
    'Category': ['Hot', 'Cold', 'Crispy', 'Hot', 'Cold'],
    'Base_Prep_Time_Min': [12, 5, 6, 8, 3]
}
df_menu = pd.DataFrame(menu_data)

# --- 2. GENERATE DIM_KITCHENS ---
kitchen_data = {
    'Kitchen_ID': ['K01', 'K02', 'K03'],
    'Location': ['Downtown', 'Suburbia', 'Financial District'],
    'Chefs_On_Shift': [5, 3, 8]
}
df_kitchens = pd.DataFrame(kitchen_data)

# --- 3. GENERATE FACT_ORDERS ---
orders = []

for i in range(num_orders):
    # Randomly pick a date/time
    order_time = start_date + timedelta(
        days=random.randint(0, 60), 
        hours=random.randint(10, 22), 
        minutes=random.randint(0, 59)
    )
    
    # Pick a kitchen and menu item
    kitchen = random.choice(df_kitchens['Kitchen_ID'].values)
    item = df_menu.sample(1).iloc[0]
    
    # LOGIC: Friday Night Rush (Friday = 4)
    is_friday_night = (order_time.weekday() == 4 and order_time.hour >= 18)
    rush_multiplier = 1.5 if is_friday_night else 1.0
    
    # Timestamps
    prep_time = item['Base_Prep_Time_Min'] * rush_multiplier + random.uniform(1, 5)
    prep_finished = order_time + timedelta(minutes=prep_time)
    
    # Driver Logistics
    driver_wait = random.uniform(2, 10) # How long until driver arrives
    driver_departed = prep_finished + timedelta(minutes=driver_wait)
    
    distance = random.uniform(1.0, 15.0) # KM
    delivery_time = distance * 2 + random.uniform(5, 10) # 2 mins per km + traffic
    delivered_at = driver_departed + timedelta(minutes=delivery_time)
    
    # LOGIC: The "Soggy Factor" Rating
    # Base rating 5. If it's "Crispy" and takes > 20 mins to deliver, rating drops.
    rating = 5.0
    total_travel_time = (delivered_at - prep_finished).total_seconds() / 60
    
    if item['Category'] == 'Crispy' and total_travel_time > 15:
        rating -= (total_travel_time / 10) # Heavy penalty for cold fries
    elif total_travel_time > 30:
        rating -= 1.5 # General penalty for long waits
    
    rating = max(1, min(5, rating + random.uniform(-0.5, 0.5))) # Add some noise

    orders.append({
        'Order_ID': f'ORD-{1000+i}',
        'Timestamp_Order_Placed': order_time,
        'Timestamp_Prep_Finished': prep_finished,
        'Timestamp_Driver_Departed': driver_departed,
        'Timestamp_Delivered': delivered_at,
        'Kitchen_ID': kitchen,
        'Item_ID': item['Item_ID'],
        'Distance_KM': round(distance, 2),
        'Order_Value_USD': round(random.uniform(15, 50), 2),
        'Customer_Rating': round(rating, 1)
    })

df_orders = pd.DataFrame(orders)

# --- 4. EXPORT TO CSV ---
df_orders.to_csv('ghost_kitchen_orders.csv', index=False)
df_menu.to_csv('dim_menu.csv', index=False)
df_kitchens.to_csv('dim_kitchens.csv', index=False)

print("Files generated: ghost_kitchen_orders.csv, dim_menu.csv, dim_kitchens.csv")