
import pandas as pd
import mysql.connector
from getpass import getpass

# ==========================================
# STEP 1: CONNECT TO MYSQL
# ==========================================

password = getpass("Enter your MySQL root password: ")

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password=password,
    database="customer_shopping_analysis"
)

cursor = connection.cursor()

print("\nConnected to MySQL successfully!")

# ==========================================
# STEP 2: LOAD THE CLEANED CSV
# ==========================================

file_path = (
    "data/cleaned/"
    "customer_shopping_behavior_cleaned.csv"
)

df = pd.read_csv(file_path)

print("CSV loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# ==========================================
# STEP 3: CREATE THE MYSQL TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS customer_shopping (
    `Customer ID` INT PRIMARY KEY,
    Age INT,
    Gender VARCHAR(20),
    `Item Purchased` VARCHAR(50),
    Category VARCHAR(50),
    `Purchase Amount (USD)` DECIMAL(10,2),
    Location VARCHAR(100),
    Size VARCHAR(10),
    Color VARCHAR(30),
    Season VARCHAR(20),
    `Review Rating` DECIMAL(4,2),
    `Subscription Status` VARCHAR(10),
    `Shipping Type` VARCHAR(50),
    `Discount Applied` VARCHAR(10),
    `Promo Code Used` VARCHAR(10),
    `Previous Purchases` INT,
    `Payment Method` VARCHAR(50),
    `Frequency of Purchases` VARCHAR(50)
)
""")

print("Table is ready!")

# ==========================================
# STEP 4: INSERT THE CSV DATA
# ==========================================

insert_query = """
INSERT INTO customer_shopping (
    `Customer ID`, Age, Gender, `Item Purchased`,
    Category, `Purchase Amount (USD)`, Location,
    Size, Color, Season, `Review Rating`,
    `Subscription Status`, `Shipping Type`,
    `Discount Applied`, `Promo Code Used`,
    `Previous Purchases`, `Payment Method`,
    `Frequency of Purchases`
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""

# Convert pandas missing values to Python None
df = df.astype(object).where(pd.notna(df), None)

# Convert rows to tuples for MySQL
records = list(df.itertuples(index=False, name=None))

try:
    cursor.executemany(insert_query, records)
    connection.commit()

    print("Data imported successfully!")
    print("Rows inserted:", cursor.rowcount)

except mysql.connector.Error as error:
    connection.rollback()
    print("Import failed:", error)

finally:
    # ==========================================
    # STEP 5: VERIFY THE IMPORT
    # ==========================================

    cursor.execute("SELECT COUNT(*) FROM customer_shopping")
    total_rows = cursor.fetchone()[0]

    print("\nTotal rows currently in MySQL:", total_rows)

    cursor.close()
    connection.close()

    print("MySQL connection closed.")
