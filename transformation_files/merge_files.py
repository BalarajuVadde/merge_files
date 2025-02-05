import pandas as pd
import os

def merge_csv_file():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_dir = os.path.join(base_dir, "csv_files")
    output_file = os.path.join(input_dir, "merged_orders.csv")

    customers_file = os.path.join(input_dir, "customers.csv")
    orders_file = os.path.join(input_dir, "orders.csv")

    customers_df = pd.read_csv(customers_file)
    orders_df = pd.read_csv(orders_file)

    merged_df = orders_df.merge(customers_df, on="CustomerID", how="right")

    merged_df.to_csv(output_file, index=False)

    return output_file
