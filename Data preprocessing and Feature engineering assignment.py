# Data preprocessing and Feature engineering assignment
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Load the dataset
file_path = 'C:\\Users\\Owner\\Documents\\GitHub\\AI Course final assignments\\example_dataset.csv'
df = pd.read_csv(file_path)

# Step 1: Remove duplicates
df.drop_duplicates(inplace=True)

# Step 2: Handle missing values
numerical_imputer = SimpleImputer(strategy='mean')
numerical_columns = df.columns
df[numerical_columns] = numerical_imputer.fit_transform(df[numerical_columns])

# Step 3: Feature engineering
df['interaction_term'] = df['feature_1'] * df['feature_2']  # Interaction term
df['feature_sum'] = df['feature_3'] + df['feature_4']       # Sum feature
df['feature_ratio'] = df['feature_5'] / (df['feature_1'] + 0.001)  # Ratio feature

# Step 4: Scale numerical features
scaler = StandardScaler()
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# Save the preprocessed dataset
df.to_csv("preprocessed_dataset.csv", index=False)
