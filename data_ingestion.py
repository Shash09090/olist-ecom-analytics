import pandas as pd
import sqlite3

print("Loaing dataset...")

#Now we extract the files from the "data" folder
orders_df = pd.read_csv("data/olist_orders_dataset.csv")
customers_df = pd.read_csv("data/olist_customers_dataset.csv")
print("Merged datasets")
#Merging begins:
merged_df = pd.merge(orders_df, customers_df, on = "customer_id", how = "inner")
#Checking its shape
print(f"Orders data shape: {orders_df.shape}")
print(f"Customers data shape: {customers_df.shape}")
print("Data loaded successfully!")
#Merge codea above
print("Saving to SQL database")
#Load:
connection = sqlite3.connect("ecommerce_data.db")

merged_df.to_sql("Orders_customers",connection, if_exists = "replace", index = False)

connection.close()
print("Data saved to SQL database successfully!")