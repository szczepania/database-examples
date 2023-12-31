# database-examples

## Sales Data Analysis with SQL and Python

### **Overview**

This simple Python application demonstrates data analysis and SQL operations using SQLite. The application simulates a
scenario where sales data is stored in a SQLite database, and analysis is performed on the data. Additionally, it
showcases a join operation between the sales and customers tables.

### **Features**

1. **Sales Data Analysis:**

- Calculate total sales, average price, and visualize monthly sales trends.
- Identify the highest-selling product.

2. **Join Operation:**

- Perform a join operation between the sales and customers tables based on customer_id.
- Display the joined data, including customer information for each sale.

### **Prerequisites**

- Python 3.x
- Required Python packages (install using pip install pandas matplotlib faker)

### **Usage**

1. Clone the repository:

```commandline
git clone https://github.com/szczepania/database-examples.git
```

2. Change to the directory:

```
cd database-examples/exercices/
```

3. Install the required Python packages:

```commandline
pip install pandas matplotlib faker
```

4. Run the Python scripts:

```
python sales.py
```

```
python sales_data_with_customers.py
```

3. View the generated plots and query results in the console.

### **Database Files**

- **`sales_data.db`**: Contains the sales data.
- **`sales_data_with_customers.db`**: Includes both sales and customer data with a join operation.

### **Additional Notes**

- The script uses the Faker library to generate random data for demonstration purposes.
- Feel free to customize the script for your specific data and analysis requirements.
