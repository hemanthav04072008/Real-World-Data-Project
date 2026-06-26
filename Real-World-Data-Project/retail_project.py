import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Create Total Sales column
df["Total Sales"] = df["Price"] * df["Quantity"]

print("Dataset:")
print(df)

print("\nSummary:")
print(df.describe())

# Total sales by category
category_sales = df.groupby("Category")["Total Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (₹)")
plt.tight_layout()
plt.show()

# Pie Chart
plt.figure(figsize=(6,6))
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()