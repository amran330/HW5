# Revision number 1 / 12/15/24
## Begin - Amran Rahim (12/15/24) 

import random
import uuid

# Step One: Data Collector
def generate_user_data():
    usernames = ["user1", "user2", "user3", "user4", "user5"]
    birthdates = ["01/10/1990", "03/15/1985", "05/20/1995", "07/25/1980", "09/30/2000"]
    addresses = ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St", "222 Cedar St"]
    ssn = [str(random.randint(100, 999)) + "-" + str(random.randint(10, 99)) + "-" + str(random.randint(1000, 9999)) for _ in range(5)]
    product_purchased = ["ID-prod123", "ID-prod456", "ID-prod789", "ID-prod101", "ID-prod222"]
    salesperson = ["sales1", "sales2", "sales3", "sales4", "sales5"]
    
    users = []
    for i in range(5):
        user = {
            "username": usernames[i],
            "password": str(uuid.uuid4()),  # Generate a random password
            "birthdate": birthdates[i],
            "address": addresses[i],
            "ssn": ssn[i],
            "productPurchased": product_purchased[i],
            "salesperson": salesperson[i]
        }
        users.append(user)
    return users

# Step Two: Key/Value Pairs
def create_key_value_pairs(users):
    user_data = {}
    for user in users:
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        user_data[user_id] = user
    return user_data

# Step Three: Search Engine
def search_users_by_state(users, state):
    matching_users = []
    for user in users.values():
        if state in user["address"]:
            matching_users.append(user)
    return matching_users

if __name__ == "__main__":
    # Step One: Generate user data
    user_records = generate_user_data()
    
    # Step Two: Create key/value pairs
    user_data_store = create_key_value_pairs(user_records)
    
    # Step Three: Search users by state
    state_to_search = "Main St"  # Example: Search for users with addresses containing "Main St"
    matching_users = search_users_by_state(user_data_store, state_to_search)
    
    # Print the matching users
    for user in matching_users:
        print(user)

# 2/15/2024
## End - Amran Rahim 
