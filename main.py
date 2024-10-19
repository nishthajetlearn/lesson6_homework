import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
# Make sure to provide the correct path to your dataset
df = pd.read_csv('titanic.csv')

# Data Analysis

# 1. Total number of men and women
gender_counts = df['Sex'].value_counts()

# 2. Average fare of men and women
average_fare = df.groupby('Sex')['Fare'].mean()

# 3. Class distribution (Pclass)
class_distribution = df['Pclass'].value_counts()

# Plotting

# 1. Bar graph for total number of men and women
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
gender_counts.plot(kind='bar', color=['blue', 'pink'])
plt.title('Total Number of Men and Women on Titanic')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)

# 2. Average fare of men and women
plt.subplot(1, 2, 2)  # 1st row, 2nd column, 2nd subplot
average_fare.plot(kind='bar', color=['blue', 'pink'])
plt.title('Average Fare of Men and Women')
plt.xlabel('Gender')
plt.ylabel('Average Fare')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# 3. Pie chart for the number of people of different classes present
plt.figure(figsize=(8, 8))
plt.pie(class_distribution, labels=class_distribution.index, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue', 'yellowgreen'])
plt.title('Distribution of Passengers by Class')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
