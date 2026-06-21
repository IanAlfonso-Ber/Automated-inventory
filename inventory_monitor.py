import pandas as pd

def load_inventory(file_path):
    # 1. load the data from a CSV file\
    """LOAD INVENTORY"""
    try:
        data = pd.read_csv(file_path)
        print("inventory loaded successfully")
        print('columns found in csv:', data.columns.tolist())
        return data
    except FileNotFoundError :
        print("file not found or corrupted")
        return None
def check_low_stock(df):
    """Filters and prints items that are low stock"""
    low_stock_items = df[df['Quantity'] < df['Threshold']]
    if not low_stock_items.empty:
        print("---- RESTOCK NEEDED-----")
        # .iterrows() allows us to loop through the filtered results
        for index, row in low_stock_items.iterrows():
            print(f"Item: {row['Item_Name']} | Current: {row['Quantity']} | Limit: {row['Threshold']}")
    else:
        print(" inventory levels are fine No restock needed")


if __name__=="__main__":
    file_name = 'inventory.csv'
    df = load_inventory(file_name)
    if df is not None:
        check_low_stock(df)

