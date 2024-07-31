# # this code is to insert data randomly
# # restaurants_master


# import random
# import uuid
# import psycopg2
# from datetime import datetime, timedelta
# from faker import Faker

# # Initialize Faker
# fake = Faker()

# # Database connection parameters
# db_params = {
#     "host": "localhost",
#     "database": "foode_local",
#     "user": "postgres",
#     "password": "frank123",
#     "port": "5432"
# }

# # Connect to the database
# conn = psycopg2.connect(**db_params)
# cursor = conn.cursor()

# # Get the maximum existing restaurant_id
# cursor.execute("SELECT MAX(restaurant_id) FROM public.restaurants_master")
# max_id = cursor.fetchone()[0] or 0

# # List of restaurant types
# restaurant_types = [
#     "Delivery", "Casual Dining", "Quick Bite Outlet", "Take Away", 
#     "Fine Dining", "Cafe", "Pub", "Bar", "Lounge", "Food Court"
# ]

# # List of areas in Chennai
# areas = [
    # "Velacheri", "Adyar", "Tambaram", "Ashok Nagar", "Anna Nagar", "T Nagar", 
    # "Mylapore", "Besant Nagar", "Egmore", "Chrompet", "Nungambakkam", "Guindy", 
    # "Perungudi", "Thiruvanmiyur", "Porur", "Ramapuram", "Mount Road", 
    # "Paris Corner", "Alwarpet", "Little Mount", "St Thomas Mount", "Alandur", 
    # "Pallavaram", "Saidapet", "Valasaravakam", "Koyembedu"
# ]

# # Function to generate random restaurant data
# def generate_restaurant_data(id):
#     name = fake.company() + " " + random.choice(["Restaurant", "Eatery", "Diner", "Cafe", "Bistro"])
#     address = fake.street_address() + ", " + random.choice(areas) + ", Chennai"
    
#     # Generate delivery time with 5-minute intervals
#     start_time = random.randint(20, 55)  # Start time between 20 and 55 minutes
#     end_time = start_time + 5  # End time is always 5 minutes more than start time
#     delivery_time = f"{start_time}-{end_time}"
    
#     year_established = random.randint(1950, 2023)
#     average_cost = round(random.uniform(100, 5000), 2)
#     latitude = random.uniform(12.8, 13.2)
#     longitude = random.uniform(80.1, 80.3)
#     type_ = ", ".join(random.sample(restaurant_types, random.randint(1, 4)))
#     rating_count = f"{random.randint(1, 20)},{random.randint(100, 999)} Rating"
#     overall_rating = round(random.uniform(1, 5), 1)
#     updated_at = datetime.now() - timedelta(days=random.randint(0, 365))
#     order_count = random.randint(0, 1000)
#     booking_count = random.randint(0, 200)
#     prebooked_payment_count = random.randint(0, 100)
#     walkin_payment_count = random.randint(0, 300)

#     return (
#         id, str(uuid.uuid4()), name, address, "Chennai", random.choice(areas),
#         delivery_time, random.randint(6000000000, 9999999999),
#         fake.email(), fake.domain_name(), year_established, average_cost,
#         latitude, longitude, type_, rating_count, overall_rating,
#         random.choice([True, False]), random.choice([True, False]),
#         updated_at, order_count, booking_count, prebooked_payment_count,
#         walkin_payment_count, random.choice([True, False])
#     )

# # Generate and insert data
# num_records = 500  # Change this to the desired number of records

# for i in range(num_records):
#     data = generate_restaurant_data(max_id + i + 1)
#     cursor.execute("""
#         INSERT INTO public.restaurants_master (
#             restaurant_id, restaurant_uuid, name, address, city, area, delivery_time,
#             mobile_number, email, website, year_established, average_cost,
#             latitude, longitude, type, rating_count, overall_rating,
#             gst_applicable, is_veg, updated_at, order_count, booking_count,
#             prebooked_payment_count, walkin_payment_count, dine_out
#         ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """, data)

# # Commit the changes and close the connection
# conn.commit()
# cursor.close()
# conn.close()

# print(f"{num_records} records inserted successfully.")


# ----------------------*************** THIS IS FOR ALL OVER TAMIL NADU ******************---------------------------------

import random
import uuid
import psycopg2
from datetime import datetime, timedelta
from faker import Faker

# Initialize Faker
fake = Faker()

# Database connection parameters
db_params = {
    "host": "localhost",
    "database": "foode_local",
    "user": "postgres",
    "password": "frank123",
    "port": "5432"
}

# Connect to the database
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Get the maximum existing restaurant_id
cursor.execute("SELECT MAX(restaurant_id) FROM public.restaurants_master")
max_id = cursor.fetchone()[0] or 0

print(f"Current maximum restaurant_id: {max_id}")

# List of restaurant types
restaurant_types = [
    "Delivery", "Casual Dining", "Quick Bite Outlet", "Take Away", 
    "Fine Dining", "Cafe", "Pub", "Bar", "Lounge", "Food Court"
]

# Dictionary of Tamil Nadu districts and some areas within each
tamil_nadu_districts = {
    "Chennai": ["Velacheri", "Adyar", "Tambaram", "Ashok Nagar", "Anna Nagar", "T Nagar", 
    "Mylapore", "Besant Nagar", "Egmore", "Chrompet", "Nungambakkam", "Guindy", 
    "Perungudi", "Thiruvanmiyur", "Porur", "Ramapuram", "Mount Road", 
    "Paris Corner", "Alwarpet", "Little Mount", "St Thomas Mount", "Alandur", 
    "Pallavaram", "Saidapet", "Valasaravakam", "Koyembedu"],
    
    "Coimbatore": ["RS Puram", "Peelamedu", "Saibaba Colony", "Gandhipuram", "Singanallur"],
    "Madurai": ["Goripalayam", "Anaiyur", "Thirunagar", "Villapuram", "Simakkal"],
    "Salem": ["Hasthampatti", "Fairlands", "Suramangalam", "Alagapuram", "Ammapet"],
    "Tiruchirapalli": ["Srirangam", "Thillai Nagar", "Woraiyur", "K.K. Nagar", "Ariyamangalam"],
    "Tirunelveli": ["Palayamkottai", "Melapalayam", "Vannarpettai", "Thatchanallur", "Pettai"],
    "Vellore": ["Sathuvachari", "Katpadi", "Bagayam", "Gandhi Nagar", "Alamelumangapuram"],
    "Erode": ["Perundurai", "Bhavani", "Gobichettipalayam", "Sathyamangalam", "Kavundapadi"],
    "Thoothukudi": ["Bryant Nagar", "Third Mile", "Millerpuram", "Lourdammalpuram", "Pudukottai"],
    "Thanjavur": ["Kumbakonam", "Pattukottai", "Peravurani", "Orathanadu", "Papanasam"],
    "Kanyakumari": ["Nagercoil", "Kottar", "Vadasery", "Parvathipuram", "Suchindrum"]
}

# Generate random coordinates within the latitude and longitude range for each city
def get_lat_long(city):
    city_coords = {
        "Chennai": (13.0827, 80.2707),
        "Coimbatore": (11.0168, 76.9558),
        "Madurai": (9.9252, 78.1198),
        "Salem": (11.6643, 78.1460),
        "Tiruchirapalli": (10.7905, 78.7047),
        "Tirunelveli": (8.7139, 77.7567),
        "Vellore": (12.9165, 79.1325),
        "Erode": (11.3410, 77.7172),
        "Thoothukudi": (8.7642, 78.1348),
        "Thanjavur": (10.7867, 79.1378),
        "Kanyakumari": (8.0883, 77.5385)
    }
    base_lat, base_long = city_coords[city]
    latitude = base_lat + random.uniform(-0.1, 0.1)
    longitude = base_long + random.uniform(-0.1, 0.1)
    return latitude, longitude

def generate_restaurant_data(id):
    district = random.choice(list(tamil_nadu_districts.keys()))
    area = random.choice(tamil_nadu_districts[district])
    name = fake.company() + " " + random.choice(["Restaurant", "Eatery", "Diner", "Cafe", "Bistro"])
    address = fake.street_address() + ", " + area + ", " + district
    
    start_time = random.randint(20, 55)
    end_time = start_time + 5
    delivery_time = f"{start_time}-{end_time}"
    
    year_established = random.randint(1950, 2023)
    average_cost = round(random.uniform(100, 5000), 2)
    latitude, longitude = get_lat_long(district)
    type_ = ", ".join(random.sample(restaurant_types, random.randint(1, 4)))
    rating_count = f"{random.randint(1, 20)},{random.randint(100, 999)} Rating"
    overall_rating = round(random.uniform(1, 5), 1)
    updated_at = datetime.now() - timedelta(days=random.randint(0, 365))
    order_count = random.randint(0, 1000)
    booking_count = random.randint(0, 200)
    prebooked_payment_count = random.randint(0, 100)
    walkin_payment_count = random.randint(0, 300)

    return (
        id, str(uuid.uuid4()), name, address, district, area,
        delivery_time, random.randint(6000000000, 9999999999),
        fake.email(), fake.domain_name(), year_established, average_cost,
        latitude, longitude, type_, rating_count, overall_rating,
        random.choice([True, False]), random.choice([True, False]),
        updated_at, order_count, booking_count, prebooked_payment_count,
        walkin_payment_count, random.choice([True, False])
    )

# Generate and insert data
num_new_records = 490  # This will bring the total to 1000 (510 + 490)

for i in range(num_new_records):
    data = generate_restaurant_data(max_id + i + 1)
    cursor.execute("""
        INSERT INTO public.restaurants_master (
            restaurant_id, restaurant_uuid, name, address, city, area, delivery_time,
            mobile_number, email, website, year_established, average_cost,
            latitude, longitude, type, rating_count, overall_rating,
            gst_applicable, is_veg, updated_at, order_count, booking_count,
            prebooked_payment_count, walkin_payment_count, dine_out
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, data)

# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()

print(f"{num_new_records} new records inserted successfully.")
print(f"Total records after insertion: {max_id + num_new_records}")


#-------------*****************For dineout Offer Fields****************-----------------------

# import random
# import uuid
# import psycopg2
# from datetime import datetime, timedelta
# from faker import Faker

# # Initialize Faker
# fake = Faker()

# # Database connection parameters
# db_params = {
#     "host": "localhost",
#     "database": "foode_local",
#     "user": "postgres",
#     "password": "frank123",
#     "port": "5432"
# }

# # Connect to the database
# conn = psycopg2.connect(**db_params)
# cursor = conn.cursor()

# # Get restaurant_uuids where dine_out is True
# cursor.execute("SELECT restaurant_uuid FROM public.restaurants_master WHERE dine_out = TRUE")
# restaurant_uuids = cursor.fetchall()

# # Get the maximum existing offer_id from dine_out_offers
# cursor.execute("SELECT MAX(offer_id) FROM public.dine_out_offers")
# max_offer_id = cursor.fetchone()[0] or 0

# # Offer details
# offer_types = ["pre-book", "walk-in", "bank-offer"]
# booking_fees = [10.0, 15.0, 20.0, 25.0,30.0,35.0,40.0]

# bank_offers = [
#     ("HDFC", "USE INFINIA CARD | ABOVE 2500"),
#     ("HDFC", "USE DINERS BLACK CARD | ABOVE 2500"),
#     ("HDFC", "USE HDFC BANK CREDIT CARD | ABOVE 2500"),
#     ("HDFC", "FOODE HDFC BANK CREDIT CARD | ABOVE 100")
# ]

# pre_book_walk_in_offers = [
#     "flat 30% Off on total bill",
#     "flat 15% Off on total bill",
#     "flat 10% off on total bill",
#     "flat 50% off + free beer",
#     "10% cashback",
#     "15% off upto 1000"
# ]

# terms_and_conditions = [
#     "Offer is valid only on select restaurants.",
#     "Coupon code can be applied only once in 2 hr on this restaurant.",
#     "Other T&Cs may apply."
# ]

# # Function to generate random offer data
# def generate_offer_data(restaurant_uuid, offer_id):
#     offer_type = random.choice(offer_types)
    
#     if offer_type == "bank-offer":
#         bank_name, offer_description = random.choice(bank_offers)
#         booking_fee_description = "FREE"
#         booking_fee = "0.0"
#         coupon_code = None
#     else:
#         bank_name = None
#         offer_description = random.choice(pre_book_walk_in_offers)
#         booking_fee = random.choice(booking_fees)
#         booking_fee_description = f"{booking_fee} per guest"
#         coupon_code = "DINE" + str(random.randint(100, 999))
    
#     available_seats = random.randint(10, 100)
#     discount_percentage = random.randint(5, 50)
#     discount_amount = random.randint(100, 1000)
#     min_order_value = random.randint(100, 1000)
#     max_discount_amount = random.randint(100, 2000)
#     start_date = datetime.now().date()
#     end_date = (datetime.now() + timedelta(days=30)).date()
#     terms_and_conditions_text = random.choice(terms_and_conditions)
#     updated_at = datetime.now()

#     return (
#         restaurant_uuid, offer_type, offer_id, offer_description, available_seats,
#         booking_fee_description, booking_fee, bank_name, offer_description,
#         discount_percentage, discount_amount, min_order_value,
#         max_discount_amount, coupon_code, start_date, end_date,
#         terms_and_conditions_text, updated_at
#     )

# # Generate and insert data
# new_offer_id = max_offer_id + 1  # Start from the next available offer_id
# for restaurant_uuid in restaurant_uuids:
#     for _ in range(10):  # Generate 10 offers per restaurant
#         data = generate_offer_data(restaurant_uuid[0], new_offer_id)
#         cursor.execute("""
#             INSERT INTO public.dine_out_offers (
#                 restaurant_uuid, offer_type, offer_id, offer, available_seats,
#                 booking_fee_description, booking_fee, bank_name, offer_description,
#                 discount_percentage, discount_amount, min_order_value,
#                 max_discount_amount, coupon_code, start_date, end_date,
#                 terms_and_conditions, updated_at
#             ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """, data)
#         new_offer_id += 1  # Increment the offer_id for the next record

# # Commit the changes and close the connection
# conn.commit()
# cursor.close()
# conn.close()

# print("Dine-out offers generated and inserted successfully.")