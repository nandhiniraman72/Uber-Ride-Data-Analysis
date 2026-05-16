# ============================================
# Uber Ride Data Analysis Project
# ============================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display Settings
plt.rcParams['figure.figsize'] = (10,6)
sns.set_style("whitegrid")

# ============================================
# Sample Uber Dataset
# ============================================

data = {
    'START_DATE': ['2025-01-01 08:00:00', '2025-01-02 09:30:00',
                   '2025-01-03 18:00:00', '2025-01-04 10:15:00',
                   '2025-01-05 20:45:00', '2025-01-06 07:20:00',
                   '2025-01-07 14:10:00', '2025-01-08 19:30:00',
                   '2025-01-09 11:00:00', '2025-01-10 16:40:00'],
    
    'CATEGORY': ['Business', 'Personal', 'Business', 'Business',
                 'Personal', 'Business', 'Personal', 'Business',
                 'Personal', 'Business'],
    
    'START': ['Bangalore', 'Chennai', 'Hyderabad', 'Mumbai',
              'Delhi', 'Bangalore', 'Chennai', 'Hyderabad',
              'Mumbai', 'Delhi'],
    
    'STOP': ['Mumbai', 'Delhi', 'Bangalore', 'Chennai',
             'Hyderabad', 'Mumbai', 'Delhi', 'Bangalore',
             'Chennai', 'Hyderabad'],
    
    'MILES': [15.2, 8.5, 12.4, 6.8, 18.1,
              10.5, 7.3, 14.2, 9.6, 16.7],
    
    'PURPOSE': ['Meeting', 'Shopping', 'Business Meeting',
                'Office', 'Visit Friends', 'Airport',
                'Entertainment', 'Client Meeting',
                'Travel', 'Conference']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Date Column
df['START_DATE'] = pd.to_datetime(df['START_DATE'])

# ============================================
# Basic Dataset Information
# ============================================

print("First 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# ============================================
# Missing Values Check
# ============================================

print("\nMissing Values")
print(df.isnull().sum())

# ============================================
# Ride Category Analysis
# ============================================

category_count = df['CATEGORY'].value_counts()

print("\nRide Category Count")
print(category_count)

# Visualization
sns.countplot(x='CATEGORY', data=df)

plt.title('Ride Category Distribution')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

# ============================================
# Total Miles Travelled
# ============================================

total_miles = df['MILES'].sum()

print("\nTotal Miles Travelled:", total_miles)

# ============================================
# Average Ride Distance
# ============================================

average_miles = df['MILES'].mean()

print("\nAverage Ride Distance:", average_miles)

# ============================================
# Purpose Analysis
# ============================================

purpose_count = df['PURPOSE'].value_counts()

print("\nRide Purpose Count")
print(purpose_count)

# Bar Plot
purpose_count.plot(kind='bar')

plt.title('Ride Purpose Analysis')
plt.xlabel('Purpose')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# ============================================
# Monthly Ride Analysis
# ============================================

df['MONTH'] = df['START_DATE'].dt.month_name()

monthly_rides = df.groupby('MONTH')['MILES'].sum()

print("\nMonthly Ride Analysis")
print(monthly_rides)

# Line Plot
monthly_rides.plot(marker='o')

plt.title('Monthly Ride Trend')
plt.xlabel('Month')
plt.ylabel('Miles Travelled')
plt.show()

# ============================================
# Top Start Locations
# ============================================

start_locations = df['START'].value_counts()

print("\nTop Start Locations")
print(start_locations)

# Visualization
sns.barplot(x=start_locations.index,
            y=start_locations.values)

plt.title('Most Frequent Start Locations')
plt.xlabel('Location')
plt.ylabel('Number of Rides')
plt.show()

# ============================================
# Correlation Analysis
# ============================================

numeric_df = df[['MILES']]

correlation = numeric_df.corr()

print("\nCorrelation Matrix")
print(correlation)

# Heatmap
sns.heatmap(correlation,
            annot=True,
            cmap='coolwarm')

plt.title('Correlation Heatmap')
plt.show()

# ============================================
# Peak Ride Hours
# ============================================

df['HOUR'] = df['START_DATE'].dt.hour

hourly_rides = df['HOUR'].value_counts().sort_index()

print("\nRide Count by Hour")
print(hourly_rides)

# Visualization
hourly_rides.plot(kind='line', marker='o')

plt.title('Peak Ride Hours')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Rides')
plt.grid(True)
plt.show()

# ============================================
# Key Insights
# ============================================

print("\nKey Insights")
print("1. Business rides were more frequent than personal rides.")
print("2. Most rides occurred during working hours.")
print("3. Bangalore and Mumbai were common ride locations.")
print("4. Travel and meetings were major ride purposes.")

# ============================================
# Save Processed Data
# ============================================

df.to_csv('processed_uber_data.csv', index=False)

print("\nProcessed dataset saved successfully.")
