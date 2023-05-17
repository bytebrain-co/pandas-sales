import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV file into a DataFrame
df = pd.read_csv("sales_data.csv")

# 2. Display the first 5 rows of the DataFrame
print(df.head(5))

# 3. Calculate and display the total sales for each product
total_sales = df.groupby("Product")["Sales"].sum()
print("\nTotal Sales by Product:")
print(total_sales)

# 4. Calculate and display the average sales per month
df["Date"] = pd.to_datetime(df["Date"])  # Convert "Date" column to datetime
df["Month"] = df["Date"].dt.month  # Extract month from "Date"
average_sales = df.groupby("Month")["Sales"].mean()
print("\nAverage Sales per Month:")
print(average_sales)

# 5. Find and display the month with the highest total sales
highest_month = total_sales.idxmax()
print("\nMonth with the Highest Total Sales:", highest_month)

# 6. Create a bar plot to visualize the monthly sales
monthly_sales = df.groupby("Month")["Sales"].sum()
monthly_sales.plot(kind="bar")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales")
plt.show()
