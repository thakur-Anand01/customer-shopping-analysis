import pandas as pd

df = pd.read_csv("data/customer_shopping_behavior_raw.csv")

print("Shape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nReview Rating statistics:")
print(df["Review Rating"].describe())
# Fill missing Review Rating values with the mean
mean_rating = df["Review Rating"].mean()

df["Review Rating"] = df["Review Rating"].fillna(mean_rating)

print("Mean rating used:", mean_rating)
print("Missing ratings after filling:", df["Review Rating"].isnull().sum())
# checking after mean.
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDataset shape after cleaning:")
print(df.shape)

# Save the cleaned dataset
df.to_csv("data/cleaned/customer_shopping_behavior_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")

# Load the cleaned dataset again
cleaned_df = pd.read_csv(
    "data/cleaned/customer_shopping_behavior_cleaned.csv"
)

print("\n--- Cleaned Data Validation ---")

print("Shape:", cleaned_df.shape)

print("\nMissing values:")
print(cleaned_df.isnull().sum())

print("\nDuplicate rows:", cleaned_df.duplicated().sum())

print("\nFirst 5 rows:")
print(cleaned_df.head())

# Check unique values in categorical columns

categorical_columns = [
    "Gender",
    "Category",
    "Season",
    "Subscription Status",
    "Shipping Type",
    "Discount Applied",
    "Promo Code Used",
    "Payment Method",
    "Frequency of Purchases"
]

for column in categorical_columns:
    print(f"\n{column}:")
    print(sorted(df[column].dropna().unique()))

    # Check numerical columns

numerical_columns = [
    "Age",
    "Purchase Amount (USD)",
    "Review Rating",
    "Previous Purchases"
]

for column in numerical_columns:
    print(f"\n{column}:")
    print(df[column].describe())

    # Check duplicate customer IDs

print("\nTotal customer IDs:", df["Customer ID"].count())
print("Unique customer IDs:", df["Customer ID"].nunique())
print("Duplicate customer IDs:", df["Customer ID"].duplicated().sum())

# EDA 1: Number of purchases by product category

print("\nPurchase count by category:")
print(df["Category"].value_counts())

# EDA 2: Average purchase amount by category

average_purchase = df.groupby("Category")["Purchase Amount (USD)"].mean()

print("\nAverage purchase amount by category:")
print(average_purchase.sort_values(ascending=False).round(2))

# EDA 3: Average purchase amount by gender

gender_spending = df.groupby("Gender")["Purchase Amount (USD)"].agg(
    ["count", "mean", "sum"]
)

print("\nPurchase analysis by gender:")
print(gender_spending.round(2))

# EDA 4: Purchase analysis by subscription status

subscription_analysis = df.groupby("Subscription Status")[
    "Purchase Amount (USD)"
].agg(["count", "mean", "sum"])

print("\nPurchase analysis by subscription status:")
print(subscription_analysis.round(2))


# ==========================================
# EDA 5: Discount usage and purchase amount
# ==========================================

print("\n--- Discount Analysis ---")

discount_analysis = df.groupby("Discount Applied")[
    "Purchase Amount (USD)"
].agg(["count", "mean", "sum"])

print(discount_analysis.round(2))


# ==========================================
# EDA 6: Payment method distribution
# ==========================================

print("\n--- Payment Method Distribution ---")

payment_counts = df["Payment Method"].value_counts()
payment_percentages = (
    df["Payment Method"].value_counts(normalize=True) * 100
)

payment_analysis = pd.DataFrame({
    "Count": payment_counts,
    "Percentage": payment_percentages.round(2)
})

print(payment_analysis)


# ==========================================
# EDA 7: Purchase frequency analysis
# ==========================================

print("\n--- Purchase Frequency Analysis ---")

frequency_analysis = df.groupby("Frequency of Purchases")[
    "Purchase Amount (USD)"
].agg(["count", "mean", "sum"])

print(frequency_analysis.sort_values("count", ascending=False).round(2))


# ==========================================
# EDA 8: Product category by season
# ==========================================

print("\n--- Category by Season ---")

category_season = pd.crosstab(
    df["Category"],
    df["Season"]
)

print(category_season)


# ==========================================
# EDA 9: Average purchase amount by season
# ==========================================

print("\n--- Seasonal Purchase Analysis ---")

season_analysis = df.groupby("Season")[
    "Purchase Amount (USD)"
].agg(["count", "mean", "sum"])

print(season_analysis.round(2))


# ==========================================
# EDA 10: Final summary
# ==========================================

print("\n--- Final EDA Summary ---")

print("Total records:", len(df))
print("Unique customers:", df["Customer ID"].nunique())
print(
    "Overall average purchase amount:",
    round(df["Purchase Amount (USD)"].mean(), 2)
)
print(
    "Overall total purchase amount:",
    df["Purchase Amount (USD)"].sum()
)
print(
    "Average review rating:",
    round(df["Review Rating"].mean(), 2)
)

print(
    "\nMost common category:",
    df["Category"].value_counts().idxmax()
)

print(
    "Most common payment method:",
    df["Payment Method"].value_counts().idxmax()
)

print(
    "Most common purchase frequency:",
    df["Frequency of Purchases"].value_counts().idxmax()
)


# ==========================================
# Save cleaned dataset again
# ==========================================

df.to_csv(
    "data/cleaned/customer_shopping_behavior_cleaned.csv",
    index=False
)

print("\nEDA completed. Cleaned dataset saved.")



# ==========================================
# EDA 11: Customer Spending by Age Group
# ==========================================

print("\n--- Customer Spending by Age Group ---")

# Create age groups
age_bins = [17, 25, 35, 45, 55, 65, 70]
age_labels = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "56-65",
    "66-70"
]

df["Age Group"] = pd.cut(
    df["Age"],
    bins=age_bins,
    labels=age_labels
)

# Analyze purchase amounts by age group
age_analysis = df.groupby(
    "Age Group",
    observed=False
)["Purchase Amount (USD)"].agg(
    ["count", "mean", "sum"]
)

print(age_analysis.round(2))



# ==========================================
# EDA 12: Discount Usage by Age Group
# ==========================================

print("\n--- Discount Usage by Age Group ---")

discount_age_analysis = pd.crosstab(
    df["Age Group"],
    df["Discount Applied"],
    margins=True
)

print(discount_age_analysis)

# Calculate discount usage percentage within each age group
discount_percentage = pd.crosstab(
    df["Age Group"],
    df["Discount Applied"],
    normalize="index"
) * 100

print("\nDiscount Usage Percentage by Age Group:")
print(discount_percentage.round(2))

