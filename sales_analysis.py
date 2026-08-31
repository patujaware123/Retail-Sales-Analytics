import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ============================================================
# 1. CREATE / LOAD DATA
# ============================================================

data = {
    "order_id": [
        1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,
        1011,1012,1013,1014,1015,1016,1017,1018,1019,1020
    ],

    "customer_name": [
        "Aarav","Priya","Rohan","Sneha","Aditya","Neha","Rahul","Ananya",
        "Vikram","Kavya","Ishaan","Meera","Arjun","Pooja","Karan",
        "Simran","Manish","Riya","Nikhil","Sakshi"
    ],

    "category": [
        "Electronics","Electronics","Electronics","Furniture","Furniture",
        "Electronics","Home","Electronics","Furniture","Home",
        "Electronics","Electronics","Furniture","Electronics","Home",
        "Electronics","Furniture","Electronics","Home","Furniture"
    ],

    "product": [
        "Laptop","Monitor","Printer","Sofa","Office Chair","Keyboard",
        "Table Lamp","Mouse","Bookshelf","Coffee Maker","Laptop","Printer",
        "Office Chair","Monitor","Wall Clock","Keyboard","Sofa","Mouse",
        "Table Lamp","Bookshelf"
    ],

    "price": [
        15000,9500,12000,12000,8000,7000,9000,5000,6000,4000,
        15000,9000,8000,5000,7000,6000,3000,5000,4000,8000
    ],

    "quantity": [
        3,2,3,2,3,2,2,2,2,2,
        3,3,2,2,2,2,2,1,1,2
    ],

    "region": [
        "North","South","East","West","North","South","East","North",
        "West","South","North","East","South","West","East","North",
        "South","West","East","North"
    ],

    "payment_method": [
        "Credit Card","UPI","Debit Card","Cash","Credit Card","UPI",
        "Cash","Credit Card","Debit Card","UPI","UPI","Credit Card",
        "Cash","Debit Card","UPI","Credit Card","UPI","Credit Card",
        "Cash","Debit Card"
    ],

    "order_date": [
        "2026-01-05","2026-01-07","2026-01-10","2026-01-12","2026-01-15",
        "2026-01-18","2026-01-20","2026-01-23","2026-01-25","2026-01-28",
        "2026-02-02","2026-02-05","2026-02-08","2026-02-10","2026-02-12",
        "2026-02-15","2026-02-18","2026-02-20","2026-02-23","2026-02-28"
    ]
}

df = pd.DataFrame(data)


# ============================================================
# 2. CALCULATE REVENUE
# ============================================================

df["revenue"] = df["price"] * df["quantity"]


# ============================================================
# 3. SAVE DATASET
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "sales.csv")

df.to_csv(DATA_PATH, index=False)


# ============================================================
# 4. BASIC DATA INFORMATION
# ============================================================

print("\n================ DATASET INFO ================")

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)


# ============================================================
# 5. MISSING VALUES
# ============================================================

print("\n================ MISSING VALUES ================")

print(df.isnull().sum())


# ============================================================
# 6. DUPLICATE RECORDS
# ============================================================

print("\n================ DUPLICATES ================")

print("Duplicate rows:", df.duplicated().sum())


# ============================================================
# 7. CONVERT DATE
# ============================================================

df["order_date"] = pd.to_datetime(df["order_date"])

print("\nOrder date data type:")
print(df["order_date"].dtype)


# ============================================================
# 8. REVENUE VALIDATION
# ============================================================

print("\n================ REVENUE VALIDATION ================")

df["calculated_revenue"] = df["price"] * df["quantity"]

revenue_mismatches = (
    df["revenue"] != df["calculated_revenue"]
).sum()

print("Revenue mismatches:", revenue_mismatches)


# ============================================================
# 9. BASIC STATISTICS
# ============================================================

print("\n================ STATISTICAL SUMMARY ================")

print(df[["price", "quantity", "revenue"]].describe())


# ============================================================
# 10. KEY BUSINESS KPIs
# ============================================================

print("\n================ KEY KPIs ================")

total_orders = len(df)
total_quantity = df["quantity"].sum()
total_revenue = df["revenue"].sum()
average_order_value = df["revenue"].mean()

print("Total Orders:", total_orders)
print("Total Quantity:", total_quantity)
print("Total Revenue:", total_revenue)
print("Average Order Value:", round(average_order_value, 2))


# ============================================================
# 11. CATEGORY ANALYSIS
# ============================================================

print("\n================ CATEGORY ANALYSIS ================")

category_analysis = (
    df.groupby("category")
      .agg(
          total_revenue=("revenue", "sum"),
          total_quantity=("quantity", "sum"),
          total_orders=("order_id", "count")
      )
      .sort_values("total_revenue", ascending=False)
)

print(category_analysis)


# ============================================================
# 12. REGION ANALYSIS
# ============================================================

print("\n================ REGION ANALYSIS ================")

region_analysis = (
    df.groupby("region")
      .agg(
          total_revenue=("revenue", "sum"),
          total_quantity=("quantity", "sum"),
          total_orders=("order_id", "count")
      )
      .sort_values("total_revenue", ascending=False)
)

print(region_analysis)


# ============================================================
# 13. PRODUCT ANALYSIS
# ============================================================

print("\n================ PRODUCT ANALYSIS ================")

product_analysis = (
    df.groupby("product")
      .agg(
          total_revenue=("revenue", "sum"),
          total_quantity=("quantity", "sum"),
          total_orders=("order_id", "count")
      )
      .sort_values("total_revenue", ascending=False)
)

print(product_analysis)


# ============================================================
# 14. PAYMENT METHOD ANALYSIS
# ============================================================

print("\n================ PAYMENT METHOD ANALYSIS ================")

payment_analysis = (
    df.groupby("payment_method")
      .agg(
          total_revenue=("revenue", "sum"),
          total_orders=("order_id", "count")
      )
      .sort_values("total_revenue", ascending=False)
)

print(payment_analysis)


# ============================================================
# 15. MONTHLY REVENUE ANALYSIS
# ============================================================

print("\n================ MONTHLY REVENUE ================")

df["month"] = df["order_date"].dt.to_period("M").astype(str)

monthly_analysis = (
    df.groupby("month")
      .agg(
          total_revenue=("revenue", "sum"),
          total_orders=("order_id", "count")
      )
      .sort_index()
)

print(monthly_analysis)


# ============================================================
# 16. TOP 5 PRODUCTS
# ============================================================

print("\n================ TOP 5 PRODUCTS ================")

top_5_products = product_analysis.head(5)

print(top_5_products)


# ============================================================
# 17. HIGHEST REVENUE CATEGORY
# ============================================================

print("\n================ BEST CATEGORY ================")

best_category = category_analysis["total_revenue"].idxmax()

print("Highest revenue category:", best_category)


# ============================================================
# 18. HIGHEST REVENUE REGION
# ============================================================

print("\n================ BEST REGION ================")

best_region = region_analysis["total_revenue"].idxmax()

print("Highest revenue region:", best_region)


# ============================================================
# 19. HIGHEST REVENUE PRODUCT
# ============================================================

print("\n================ BEST PRODUCT ================")

best_product = product_analysis["total_revenue"].idxmax()

print("Highest revenue product:", best_product)


# ============================================================
# 20. REVENUE CHART BY CATEGORY
# ============================================================

plt.figure(figsize=(8, 5))

category_analysis["total_revenue"].plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ============================================================
# 21. MONTHLY REVENUE CHART
# ============================================================

plt.figure(figsize=(8, 5))

monthly_analysis["total_revenue"].plot(kind="line", marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()


# ============================================================
# 22. FINAL MESSAGE
# ============================================================

print("\n================ ANALYSIS COMPLETED ================")

print("Python Sales Analysis completed successfully!")

# ============================================================
# CATEGORY-WISE REVENUE ANALYSIS
# ============================================================

category_revenue = (
    df.groupby("category")["revenue"]
      .sum()
      .sort_values(ascending=False)
)

print("\n================ CATEGORY REVENUE ================")
print(category_revenue)

# Chart
plt.figure(figsize=(8, 5))

category_revenue.plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# ============================================================
# REGION-WISE REVENUE ANALYSIS
# ============================================================

region_revenue = (
    df.groupby("region")["revenue"]
      .sum()
      .sort_values(ascending=False)
)

print("\n================ REGION REVENUE ================")
print(region_revenue)

# Chart
plt.figure(figsize=(8, 5))

region_revenue.plot(kind="bar")

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# ============================================================
# PRODUCT-WISE REVENUE ANALYSIS
# ============================================================

product_revenue = (
    df.groupby("product")["revenue"]
      .sum()
      .sort_values(ascending=False)
)

print("\n================ PRODUCT REVENUE ================")
print(product_revenue)

# Top 5 Products
print("\n================ TOP 5 PRODUCTS ================") 
print(product_revenue.head(5))

# Chart
plt.figure(figsize=(10, 6))

product_revenue.head(10).plot(kind="bar")

plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ============================================================
# PAYMENT METHOD ANALYSIS
# ============================================================

payment_revenue = (
    df.groupby("payment_method")["revenue"]
      .sum()
      .sort_values(ascending=False)
)

print("\n================ PAYMENT METHOD REVENUE ================")
print(payment_revenue)

# Chart
plt.figure(figsize=(8, 5))

payment_revenue.plot(kind="bar")

plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Revenue")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
# ============================================================
# MONTHLY REVENUE TREND
# ============================================================

monthly_revenue = (
    df.groupby(df["order_date"].dt.to_period("M"))["revenue"]
      .sum()
)

monthly_revenue.index = monthly_revenue.index.astype(str)

print("\n================ MONTHLY REVENUE ================")
print(monthly_revenue)

# Calculate month-over-month change
if len(monthly_revenue) >= 2:
    first_month = monthly_revenue.iloc[0]
    last_month = monthly_revenue.iloc[-1]

    change_percent = ((last_month - first_month) / first_month) * 100

    print("\nRevenue Change:", round(change_percent, 2), "%")

# Chart
plt.figure(figsize=(8, 5))

monthly_revenue.plot(kind="line", marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()

# ============================================================
# BEST & WORST PERFORMING PRODUCTS
# ============================================================

product_performance = (
    df.groupby("product")
      .agg(
          total_revenue=("revenue", "sum"),
          total_quantity=("quantity", "sum"),
          total_orders=("order_id", "count")
      )
      .sort_values("total_revenue", ascending=False)
)

print("\n================ PRODUCT PERFORMANCE ================")
print(product_performance)

# Best Product
best_product = product_performance.index[0]

# Worst Product
worst_product = product_performance.index[-1]

print("\nBest Performing Product:", best_product)
print("Best Product Revenue:",
      product_performance.loc[best_product, "total_revenue"])

print("\nLowest Performing Product:", worst_product)
print("Lowest Product Revenue:",
      product_performance.loc[worst_product, "total_revenue"])

# ============================================================
# CUSTOMER-WISE REVENUE ANALYSIS
# ============================================================

customer_analysis = (
    df.groupby("customer_name")
      .agg(
          total_revenue=("revenue", "sum"),
          total_orders=("order_id", "count"),
          total_quantity=("quantity", "sum")
      )
      .sort_values("total_revenue", ascending=False)
)

print("\n================ CUSTOMER ANALYSIS ================")
print(customer_analysis)

# Top 5 Customers
print("\n================ TOP 5 CUSTOMERS ================")
print(customer_analysis.head(5))

# ============================================================
# CUSTOMER-WISE REVENUE ANALYSIS
# ============================================================

customer_analysis = (
    df.groupby("customer_name")
      .agg(
          total_revenue=("revenue", "sum"),
          total_orders=("order_id", "count"),
          total_quantity=("quantity", "sum")
      )
      .sort_values("total_revenue", ascending=False)
)

print("\n================ CUSTOMER ANALYSIS ================")
print(customer_analysis)

# Top 5 Customers
print("\n================ TOP 5 CUSTOMERS ================")
print(customer_analysis.head(5))
# ============================================================
# PROFESSIONAL BUSINESS VISUALIZATIONS
# ============================================================

# 1. Revenue by Category
plt.figure(figsize=(8, 5))

category_revenue.plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# 2. Revenue by Region
plt.figure(figsize=(8, 5))

region_revenue.plot(kind="bar")

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# 3. Top 10 Products
plt.figure(figsize=(10, 6))

product_revenue.head(10).plot(kind="bar")

plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()


# 4. Monthly Revenue Trend
plt.figure(figsize=(8, 5))

monthly_revenue.plot(kind="line", marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()


print("\n================ VISUALIZATION COMPLETED ================")
print("All business charts generated successfully!")