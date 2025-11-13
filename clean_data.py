import pandas as pd

# Load dataset
df = pd.read_excel("raw_data.xlsx")

# -------------------------------
# Step 1: Inspect data
# -------------------------------
print("Initial Shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())

# -------------------------------
# Step 2: Remove duplicates
# -------------------------------
df = df.drop_duplicates()

# -------------------------------
# Step 3: Handle missing values
# -------------------------------
# Fill missing age with mean age
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Fill missing purchase amount with median
df["Purchase_Amount"].fillna(df["Purchase_Amount"].median(), inplace=True)

# -------------------------------
# Step 4: Standardize text data
# -------------------------------
df["Gender"] = df["Gender"].str.strip().str.lower()
df["Gender"] = df["Gender"].replace({
    "m": "male",
    "f": "female"
})

df["Country"] = df["Country"].str.strip().str.title()
df["Country"] = df["Country"].replace({
    "Usa": "United States",
    "United States": "United States",
    "Uk": "United Kingdom"
})

# -------------------------------
# Step 5: Fix date format
# -------------------------------
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")
df["Join_Date"] = df["Join_Date"].dt.strftime("%d-%m-%Y")

# -------------------------------
# Step 6: Rename columns
# -------------------------------
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# -------------------------------
# Step 7: Save cleaned data
# -------------------------------
df.to_excel("cleaned_data.xlsx", index=False)

print("\nData cleaned and saved as cleaned_data.xlsx ✅")
