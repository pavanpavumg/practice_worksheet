# # def login(username,password):
# #     return username == 'pavan' and password == 'admin123'
# # assert login('pavan', 'admin123') == True
# # print("hello welcome")


# 1 
# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# arr = list(map(int, input("Enter numbers: ").split()))
# bubble_sort(arr)
# print("Sorted:", arr)

# x = int(input("Enter element to search: "))
# pos = binary_search(arr, x)
# print(f"Element {x} found at index {pos}." if pos != -1 else f"{x} not found.")





# 2
# # Banking System (Simplified)

# customers = {}       # {acc_no: [name, age, acc_type, balance]}
# transactions = {}    # {acc_no: [list of transactions]}
# MIN_BALANCE = 1000

# def create_account():
#     acc = input("Enter new account number: ")
#     if acc in customers:
#         print("Account already exists!\n"); return
#     name = input("Name: ")
#     age = int(input("Age: "))
#     acc_type = input("Type (Saving/Current): ")
#     balance = float(input("Initial Balance: "))
#     customers[acc] = [name, age, acc_type, balance]
#     transactions[acc] = [f"Account created with {balance}"]
#     print("Account created.\n")

# def deposit():
#     acc = input("Account No: ")
#     if acc not in customers: print("Not found.\n"); return
#     amt = float(input("Deposit Amount: "))
#     customers[acc][3] += amt
#     transactions[acc].append(f"Deposited {amt}")
#     print("Deposit successful.\n")

# def withdraw():
#     acc = input("Account No: ")
#     if acc not in customers: print("Not found.\n"); return
#     amt = float(input("Withdraw Amount: "))
#     if customers[acc][3] >= amt:
#         customers[acc][3] -= amt
#         transactions[acc].append(f"Withdrew {amt}")
#         print("Withdraw successful.\n")
#     else: print("Insufficient balance.\n")

# def check_balance():
#     acc = input("Account No: ")
#     if acc not in customers: print("Not found.\n"); return
#     bal = customers[acc][3]
#     print(f"Balance: {bal}")
#     if bal < MIN_BALANCE:
#         print("⚠️ Warning: Balance below minimum!\n")

# def transfer():
#     src, dest = input("From Acc: "), input("To Acc: ")
#     if src not in customers or dest not in customers:
#         print("Invalid account(s).\n"); return
#     amt = float(input("Amount to Transfer: "))
#     if customers[src][3] >= amt:
#         customers[src][3] -= amt
#         customers[dest][3] += amt
#         transactions[src].append(f"Transferred {amt} to {dest}")
#         transactions[dest].append(f"Received {amt} from {src}")
#         print("Transfer successful.\n")
#     else: print("Insufficient balance.\n")

# def view_customers():
#     if not customers: print("No customers.\n"); return
#     for acc, (name, age, typ, bal) in customers.items():
#         print(f"{acc} -> {name}, {age} yrs, {typ}, Balance: {bal}")
#     print()

# def view_transactions():
#     acc = input("Account No: ")
#     if acc not in transactions: print("Not found.\n"); return
#     print(f"\nTransactions for {acc}:")
#     for t in transactions[acc]: print("-", t)
#     print()

# def main():
#     menu = {
#         '1': create_account, '2': deposit, '3': withdraw,
#         '4': check_balance, '5': transfer,
#         '6': view_customers, '7': view_transactions
#     }
#     while True:
#         print("\n--- Banking Menu ---\n1.Create 2.Deposit 3.Withdraw 4.Balance 5.Transfer 6.Customers 7.History 8.Exit")
#         ch = input("Choice: ")
#         if ch == '8': print("Goodbye!"); break
#         menu.get(ch, lambda: print("Invalid!\n"))()
# main()


# 3

# class Employee:
#     def __init__(self, name, emp_id, age, position):
#         self.name, self.emp_id, self.age, self.position = name, emp_id, age, position

#     def calculate_salary(self):
#         pass

#     def display_details(self):
#         pass


# class PermanentEmployee(Employee):
#     def __init__(self, name, emp_id, age, position, basic_salary):
#         super().__init__(name, emp_id, age, position)
#         self.basic_salary = basic_salary

#     def calculate_salary(self):
#         return self.basic_salary * 1.3   # 30% extra benefits

#     def display_details(self):
#         print(f"\n--- Permanent Employee ---")
#         print(f"Name: {self.name}, ID: {self.emp_id}, Age: {self.age}, Position: {self.position}")
#         print(f"Basic Salary: {self.basic_salary}, Total Salary: {self.calculate_salary()}")


# class ContractEmployee(Employee):
#     def __init__(self, name, emp_id, age, position, hourly_rate, hours_worked):
#         super().__init__(name, emp_id, age, position)
#         self.hourly_rate, self.hours_worked = hourly_rate, hours_worked

#     def calculate_salary(self):
#         return self.hourly_rate * self.hours_worked

#     def display_details(self):
#         print(f"\n--- Contract Employee ---")
#         print(f"Name: {self.name}, ID: {self.emp_id}, Age: {self.age}, Position: {self.position}")
#         print(f"Hourly Rate: {self.hourly_rate}, Hours Worked: {self.hours_worked}, Total Salary: {self.calculate_salary()}")


# class EmployeeDatabase:
#     def __init__(self):
#         self.employees = {}

#     def add_employee(self, emp):
#         self.employees[emp.emp_id] = emp
#         print("Employee added successfully.\n")

#     def view_all(self):
#         if not self.employees:
#             print("No employees found.\n")
#             return
#         for emp in self.employees.values():
#             emp.display_details()

#     def search(self, emp_id):
#         if emp_id in self.employees:
#             self.employees[emp_id].display_details()
#         else:
#             print("Employee not found.\n")


# def main():
#     db = EmployeeDatabase()
#     while True:
#         print("\n1. Add Permanent\n2. Add Contract\n3. View All\n4. Search by ID\n5. Exit")
#         choice = input("Enter choice: ")

#         if choice == '1':
#             emp = PermanentEmployee(
#                 input("Name: "),
#                 input("ID: "),
#                 int(input("Age: ")),
#                 input("Position: "),
#                 float(input("Basic Salary: "))
#             )
#             db.add_employee(emp)

#         elif choice == '2':
#             emp = ContractEmployee(
#                 input("Name: "),
#                 input("ID: "),
#                 int(input("Age: ")),
#                 input("Position: "),
#                 float(input("Hourly Rate: ")),
#                 float(input("Hours Worked: "))
#             )
#             db.add_employee(emp)

#         elif choice == '3':
#             db.view_all()

#         elif choice == '4':
#             db.search(input("Enter ID: "))

#         elif choice == '5':
#             print("Exiting...")
#             break

#         else:
#             print("Invalid choice.\n")


# if __name__ == "__main__":
#     main()

# 4

# # Step 1: Load the CSV file
# df = pd.read_csv("order.csv")
# print(df)

# # a. Remove rows with any missing (NaN) values
# df = df.dropna()

# # b. Remove duplicate rows
# df = df.drop_duplicates()
# print(df)

# # Convert to numeric (in case data was read as string)
# df["Quantity"] = pd.to_numeric(df["Quantity"], errors='coerce')
# df["Price"] = pd.to_numeric(df["Price"], errors='coerce')
# df

# # Replace zero or negative values with NaN
# df.loc[df["Quantity"] <= 0, "Quantity"] = pd.NA
# df.loc[df["Price"] <= 0, "Price"] = pd.NA
# print(df)


# # Drop rows again that now contain NaN
# df = df.dropna()
# print(df)


# df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y", errors='coerce')
# df.head()


# # b. Create a new column 'TotalAmount' = Quantity * Price
# df["TotalAmount"] = df["Quantity"] * df["Price"]
# df.head()

# # Step 4: Save the cleaned and prepared data to a new CSV file
# df.to_csv("cleaned_data.csv", index=False)


# 5

# # Import necessary libraries 
# import pandas as pd 
# import matplotlib.pyplot as plt 
 
# # Load the dataset 
# df = pd.read_csv('flipkart_data.csv') 
 
# # Show the first few rows 
# df 


# print(df.isnull().sum()) 


# df = df.dropna() 
# print(df.isnull().sum()) 

# # Remove duplicates 
# df.drop_duplicates(inplace=True) 
# print(df) 

# # Filter out rows where Price <= 0 or Rating <= 0 
# df = df[(df['Price'] > 0) & (df['Rating'] > 0)] 
# df.head() 

# # Convert Discount Percentage to numeric 
# df['Discount Percentage'] = df['Discount Percentage'].astype(str).str.replace('%', 
# '').astype(float) 
 
# df.head() 

# #Bar Plot: Top 10 Brands by Average Price 
 
# top_brands = 
# df.groupby('Brand')['Price'].mean().sort_values(ascending=False).head(10) 
 
# plt.figure(figsize=(10, 5)) 
# top_brands.plot(kind='bar', color='skyblue') 
# plt.title('Top 10 Brands by Average Price') 
# plt.xlabel('Brand') 
# plt.ylabel('Average Price') 
# plt.xticks(rotation=30) 
# plt.tight_layou


 
# #Histogram: Rating Distribution 
 
# plt.figure(figsize=(8, 5)) 
# plt.hist(df['Rating'], bins=10, color='orange', edgecolor='black') 
# plt.title('Distribution of Product Ratings') 
# plt.xlabel('Rating') 
# plt.ylabel('Frequency') 
# plt.grid(True) 
# plt.tight_layout() 
# plt.show() 


# #Pie Chart: Category Distribution 
 
# category_counts = df['Category'].value_counts() 
# plt.figure(figsize=(8, 8)) 
# plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', 
# startangle=140) 
# plt.title('Product Distribution by Category') 
# plt.axis('equal') 
# plt.tight_layout() 
# plt.show() 

# #Scatter Plot: Price vs Rating (Colored by Category) 
 
# plt.figure(figsize=(10, 6)) 
 
# for category in df['Category'].unique(): 
#     subset = df[df['Category'] == category] 
#     plt.scatter(subset['Price'], subset['Rating'], label=category, alpha=0.6) 
 
# plt.title('Price vs Rating by Category') 
# plt.xlabel('Price') 
# plt.ylabel('Rating') 
# plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left') 
# plt.grid(True) 
# plt.tight_layout() 
# plt.show() 



# 6

 
# import numpy as np 
# import matplotlib.pyplot as plt 
 
# arr = np.array([10, 2, 30, 4, 50, 6, 70, 8]) 
# print("Original Array:\n", arr) 

 
# reshaped = arr.reshape(2, 4) 
# print("\nReshaped Array (2x4):\n", reshaped) 

#  Searching for the value 50 
# index_50 = np.where(arr == 50) 
# print("\nIndex of 50 in array:", index_50) 

# # Splitting the array into 2 equal parts 
# split_arr = np.array_split(arr, 2) 
# print("\nSplit Array into 2 parts:") 
# for part in split_arr: 
#     print(part) 

 
# #Using np.array_split (unequal parts allowed) 
# arr1 = np.array([10, 22, 2, 30, 33, 4, 6, 50, 6, 8]) 
# split2 = np.array_split(arr1, 4) 
# print("\nSplit into 4 unequal parts using np.array_split:") 
# for part in split2: 
#     print(part) 

# # Broadcasting: Add 5 to every element 
# df1 = np.array([1, 2, 3, 4, 5]) 
# data = df1 + 5 
# print("\nOriginal Data:\n", df1) 
# print("After Broadcasting (data + 5):\n", data) 

# # 1. Line Plot  
 
# x = np.linspace(0, 10, 100)  # 100 points from 0 to 10 
# y = 2 * x + 1                # Linear function y = 2x + 1 
# plt.plot(x, y, label='y = 2x + 1') 
# plt.title('Line Plot') 
# plt.xlabel('x') 
# plt.ylabel('y') 
# plt.legend() 
# plt.grid(True) 


 
# #Scatter Plot 
# x = np.random.rand(50) 
# y = np.random.rand(50) 
 
# plt.scatter(x, y, color='purple', alpha=0.7) 
# plt.title('Scatter Plot') 
# plt.xlabel('x') 
# plt.ylabel('y') 
# plt.grid(True) 
# plt.show() 

# # 3. Pie Chart - Distribution 
# slices = np.array([25, 35, 20, 20]) 
# labels = ['Python', 'Java', 'C++', 'Others'] 
# colors = ['gold', 'lightgreen', 'lightcoral', 'lightskyblue'] 
# plt.figure(figsize=(6, 6)) 
# plt.pie(slices, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90) 
# plt.title("Pie Chart: Programming Language Preference") 
# plt.axis('equal') 
# plt.show() 


 
# # 4 Subplots (Multiple Graphs in One Figure). 
 
# x = np.linspace(0, 10, 100) 
# y1 = x 
# y2 = x**2 
# y3 = np.sqrt(x) 
# y4 = np.log(x + 1) 
 
# fig, axs = plt.subplots(2, 2, figsize=(10, 8)) 
 
# axs[0, 0].plot(x, y1) 
# axs[0, 0].set_title('y = x') 
 
# axs[0, 1].plot(x, y2) 
# axs[0, 1].set_title('y = x^2') 
 
# axs[1, 0].plot(x, y3) 
# axs[1, 0].set_title('y = √x') 
 
# axs[1, 1].plot(x, y4) 
# axs[1, 1].set_title('y = log(x+1)') 
 
# plt.tight_layout() 
# plt.show() 



# 7

 
# import matplotlib.pyplot as plt 
# import numpy as np 
# ## 1. Line Plot - Average Monthly Temperature in Bangalore 
# print("--- 1. Displaying a Line Plot: Average Monthly Temperature in Bangalore ---") 
 
# # Data for our plot 
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 
# # Average temperature in Celsius for each month in Bangalore 
# temperatures_celsius = [22, 25, 28, 30, 29, 26, 25, 25, 25, 24, 23, 22] 
 
# # Create the plot with a green line and circle markers 
# plt.plot(months, temperatures_celsius, marker='o', linestyle='--', color='g') 
# plt.title("Average Monthly Temperature in Bangalore") 
# plt.xlabel("Month") 
# plt.ylabel("Average Temperature (°C)") 
# plt.grid(True) 
# plt.tight_layout() 
# plt.show()

# # 2. Bar Chart - Population of Bangalore 
# print("\n--- 2. Displaying a Bar Chart: Population Growth of Bangalore ---") 
# years = ['1991', '2001', '2011', '2021 (Est.)'] 
# population_millions = [4.1, 6.5, 9.6, 12.7] 
# plt.bar(years, population_millions, color='skyblue') 
# plt.title("Population of Bangalore Over the Decades") 
# plt.xlabel("Year") 
# plt.ylabel("Population (in Millions)") 
# plt.show() 

# # 3. Pie Chart - Commute Methods in Bangalore 
# print("\n--- 3. Displaying a Pie Chart: Commute Methods in Bangalore ---") 
# # Data for the pie chart 
# commute_methods = ['Personal Vehicle (Bike/Car)', 'BMTC Bus', 'Auto Rickshaw', 'Cab 
# (Ola/Uber)', 'Metro'] 
# percentages = [50, 20, 15, 10, 5] # These are example percentages 
# plt.pie(percentages, labels=commute_methods, autopct='%1.1f%%', startangle=90) 
 
# # Add a title 
# plt.title("Common Commute Methods in Bangalore") 
# # 'axis('equal')' ensures that the pie chart is a perfect circle. 
# plt.axis('equal') 
# # Show the chart 
# plt.show()


# # 4. Scatter Plot - Property Prices in Bangalore 
# print("\n--- 4. Displaying a Scatter Plot: Property Price vs. Distance from Center ---") 
# # Sample data: distance from city center (MG Road) vs. property price 
# distance_from_center_km = [2, 5, 8, 12, 15, 18, 20, 25] 
# price_per_sqft_inr = [15000, 12000, 9500, 7000, 6500, 5000, 4800, 4000] 
# # Create the scatter plot with red dots 
# plt.scatter(distance_from_center_km, price_per_sqft_inr, color='red') 
# plt.title("Bangalore Property Price vs. Distance from City Center") 
# plt.xlabel("Distance from Center (km)") 
# plt.ylabel("Approx. Price per sq. ft. (INR)") 
# plt.grid(True)


# # 5. Histogram - Air Quality Index (AQI) Distribution 
# print("\n--- 5. Displaying a Histogram: Bangalore AQI Distribution ---") 
# aqi_data = np.random.normal(loc=90, scale=25, size=500) 
# # Create the histogram. We'll sort the data into 20 bins. 
# plt.hist(aqi_data, bins=20, color='purple', edgecolor='black') 
# # Add titles and labels 
# plt.title("Distribution of Daily AQI Readings in Bangalore") 
# plt.xlabel("Air Quality Index (AQI)") 
# plt.ylabel("Frequency (Number of Days)") 
# # Show the histogram 
# plt.show()

# # 7. Box Plot - Comparing Cab Fares 
# print("\n--- 7. Displaying a Box Plot: Comparing Bangalore Cab Fares ---") 
# np.random.seed(10) # Using a seed ensures we get the same random numbers every time 
# off_peak_fares = np.random.normal(loc=450, scale=50, size=100) 
# peak_fares = np.random.normal(loc=700, scale=100, size=100) 
# # Combine the datasets into a list 
# fare_data = [off_peak_fares, peak_fares] 
# # Create the box plot 
# plt.boxplot(fare_data) 
# # Add a title and labels 
# plt.title("Cab Fare Distribution: Peak vs. Off-Peak Hours") 
# plt.ylabel("Fare in INR (₹)") 
# # Set the labels for the x-axis to correspond to our datasets 
# plt.xticks([1, 2], ['Off-Peak Hours', 'Peak Hours']) 
# # Show the plot 
# plt.show()


# 8


# # Import libraries 
# import seaborn as sns 
# import matplotlib.pyplot as plt 
 
# # Set Seaborn theme 
# sns.set_theme(style="darkgrid") 
 
# # Load the diamonds dataset 
# diamonds = sns.load_dataset("diamonds") 
 
# # 1. Count Plot - Count of diamonds by cut 
# plt.figure(figsize=(7, 5)) 
# sns.countplot(x="cut", hue="cut", data=diamonds, palette="Set2", legend=False) 
# plt.title("Count of Diamonds by Cut") 
# plt.show() 

 
# # 2. Bar Plot - Average price by cut 
# plt.figure(figsize=(7, 5)) 
# sns.barplot(x="cut", y="price",  hue="cut", data=diamonds, palette="pastel") 
# plt.title("Average Price by Cut") 
# plt.show() 

# # 3. Box Plot - Price distribution by clarity 
# plt.figure(figsize=(10, 5)) 
# sns.boxplot(x="clarity", y="price", hue="clarity", data=diamonds, palette="coolwarm", 
# legend=False) 
 
# plt.title("Box Plot of Price by Clarity") 
# plt.xticks(rotation=45) 
# plt.show() 


# # Violin Plot: Carat vs Color (Diamonds) 
# plt.figure(figsize=(10, 5)) 
# sns.violinplot(x="color", y="carat", hue="color", data=diamonds, palette="muted", 
# legend=False) 
# plt.title('Carat Distribution by Color') 
# plt.xlabel('Color Grade') 
# plt.ylabel('Carat') 
# plt.show() 

# # 5. Heatmap - Correlation matrix for numeric features 
# plt.figure(figsize=(8, 6)) 
# numeric_diamonds = diamonds.select_dtypes(include='number') 
# corr_matrix = numeric_diamonds.corr() 
# sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu", fmt=".2f") 
# plt.title("Correlation Heatmap") 
# plt.show() 

# # 6. Pair Plot - Pairwise relationships between numeric features (sample only 1000 rows 
# for performance) 
# sample_diamonds = diamonds.sample(n=1000, random_state=1) 
# sns.pairplot(sample_diamonds, hue="cut", diag_kind="kde", palette="husl") 
# plt.suptitle("Pairwise Relationships (Sample of Diamonds)", y=1.02) 
# plt.show() 


# 9

# # Import necessary libraries 
# import pandas as pd 
# import matplotlib.pyplot as plt 
# import seaborn as sns 
 
# # Set the style for seaborn plots for better aesthetics 
# sns.set(style="whitegrid") 
 
# # Load the dataset from the provided CSV file 
# df = pd.read_csv('diabetes.csv') 
 
# # Display the first 5 rows 
# print("First 5 rows of the dataset:") 
# display(df.head()) 

# # Get a concise summary of the dataframe 
# print("\nDataset Information:") 
# df.info() 

# # Select only the numerical columns for analysis (all columns in this case are numeric) 
# numerical_cols = df.columns 
 
# # Create a dictionary to hold our calculated statistics 
# stats_dict = { 
#     'Mean': df[numerical_cols].mean(), 
#     'Median': df[numerical_cols].median(), 
#     'Mode': df[numerical_cols].mode().iloc[0], # Mode can have multiple values, we take the 
# first 
#     'Variance': df[numerical_cols].var(), 
#     'Standard Deviation': df[numerical_cols].std(), 
#     'Skewness': df[numerical_cols].skew(), 
#     'Kurtosis': df[numerical_cols].kurtosis() 
# } 
 
# # Convert the dictionary to a DataFrame for nice formatting 
# summary_stats_df = pd.DataFrame(stats_dict) 
 
# print("Descriptive Univariate Statistics:") 
# display(summary_stats_df) 

# # Get the frequency count of the 'Outcome' variable 
# outcome_frequency = df['Outcome'].value_counts() 
# print("Frequency of Outcome variable:") 
# print(outcome_frequency) 
 
# # Optional: Visualize the Outcome frequency with a count plot 
# plt.figure(figsize=(6, 4)) 
# sns.countplot(x='Outcome', data=df) 
# plt.title('Frequency of Diabetes Outcome') 
# plt.xticks([0, 1], ['No Diabetes', 'Diabetes']) # Set user-friendly labels 
# plt.show() 

# 10

 
# # Import necessary libraries 
# import pandas as pd 
# import seaborn as sns 
# import matplotlib.pyplot as plt 
 
# # Set the style for seaborn plots 
# sns.set(style="whitegrid") 
 
# # Load the Iris dataset 
# df = sns.load_dataset('iris') 
 
# # Display the first 5 rows of the dataframe 
# print("First 5 rows of the dataset:") 
# display(df.head())

# df.hist(figsize=(15, 10), bins=20, color='skyblue', edgecolor='black') 
# plt.suptitle("Histograms of All Numerical Features", fontsize=16) 
# plt.tight_layout() 
# plt.show() 


# # Generate descriptive statistics for numerical columns 
# print("Descriptive Statistics:") 
# display(df.describe()) 
 
# # Check the distribution of the target variable 'species' 
# print("\nSpecies Distribution:") 
# print(df['species'].value_counts()) 
 
# # Calculate the mean of each feature for each species 
# print("\nMean of each feature per species:") 
# display(df.groupby('species').mean())

 
# #pairplot to visualize relationships between variables, colored by species 
# print("Pair Plot of Iris Dataset:") 
# sns.pairplot(df, hue='species', markers=["o", "s", "D"]) 
# plt.suptitle("Pair Plot of Iris Features", y=1.02) # Add a title above the plot 
# plt.show() 

# # Create box plots for each feature 
# print("\nBox Plots for each feature by species:") 
# plt.figure(figsize=(12, 8)) 
 
# # Loop through each feature 
# for i, feature in enumerate(df.columns[:-1]): 
#     plt.subplot(2, 2, i + 1) # Create a 2x2 grid of subplots 
#     sns.boxplot(x='species', y=feature, data=df) 
#     plt.title(f'Distribution of {feature}') 
 
# plt.tight_layout() 
# plt.show() 

# # Calculate the correlation matrix (only for numerical columns) 
 
# corr_matrix = df.corr(numeric_only=True) 
 
# # Plot the heatmap 
# print("\nCorrelation Matrix Heatmap:") 
# plt.figure(figsize=(8, 6)) 
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f") 
# plt.title('Correlation Matrix of Iris Features') 
# plt.show() 

