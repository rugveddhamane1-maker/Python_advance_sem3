import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create customer churn dataset
data = {
    "CustomerID": range(1001, 1011),
    "Age": [25, 34, 45, np.nan, 29, 52, 41, 36, 60, 23],
    "MonthlyCharges": [40, 75, 90, 55, np.nan, 100, 80, 65, 120, 35],
    "Tenure": [2, 12, 24, 8, 5, 36, 18, 14, 48, 1],
    "Contract": [
        "Monthly", "Yearly", "Monthly", "Monthly", "Yearly",
        "Yearly", "Monthly", "Yearly", "Yearly", "Monthly"
    ],
    "Churn": [
        "Yes", "No", "Yes", "No", "Yes",
        "No", "No", "No", "No", "Yes"
    ]
}

df = pd.DataFrame(data)

# Display original dataset
print("ORIGINAL CUSTOMER DATASET:")
print(df)

# Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Handle missing values using column mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

df["MonthlyCharges"] = df["MonthlyCharges"].fillna(
    df["MonthlyCharges"].mean()
)

# Remove duplicate records
df = df.drop_duplicates()

# Display cleaned dataset
print("\nCLEANED DATASET:")
print(df)

# Generate summary statistics
print("\nSUMMARY STATISTICS:")
print(df[["Age", "MonthlyCharges", "Tenure"]].describe())

# Average monthly charges according to churn
print("\nAVERAGE MONTHLY CHARGES BY CHURN:")
print(df.groupby("Churn")["MonthlyCharges"].mean())

# Count customers who churned
print("\nCUSTOMER CHURN COUNTS:")
print(df["Churn"].value_counts())

# Visualization 1: Customer churn count
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Count")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# Visualization 2: Customer tenure distribution
plt.figure(figsize=(6, 4))
sns.histplot(data=df, x="Tenure", bins=5)
plt.title("Customer Tenure Distribution")
plt.xlabel("Tenure (Months)")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# Visualization 3: Monthly charges by churn
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="Churn", y="MonthlyCharges")
plt.title("Monthly Charges by Churn Status")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.show()