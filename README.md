

```md
# Video Game store management with User and Admin Functionality

This Python program simulates an Store management platform where users can log in, browse products, purchase items, and view their account information. The program also features an admin interface to view product details, employee information, and sales data, and it generates various types of graphs for visualization using Matplotlib and Pandas.

## Features

### User Side
1. **Login**: Users can log in using their credentials.
2. **Sign Up**: New users can register an account with a name and password.
3. **Buy Products**: Users can browse available consoles and games from CSV files, select items to purchase, and track their total expenditure.
4. **Purchase History**: Purchase records are saved to a `money.csv` file, storing user names and purchase amounts.
5. **Graphical Visualizations**: The admin interface allows users to visualize employee salaries, product prices, and sales data with graphs (line, bar, pie, scatter).

### Admin Side
1. **View Employees**: Admin can view a list of employees from `employees.csv` and visualize their salaries with various graph options.
2. **View Products**: Admin can view product information (consoles and games) from CSV files and generate price charts.
3. **Sales**: Admin can view the sales records and visualize them using graphs.

## How to Run

### 1. Clone the Repository:
```bash
git clone https://github.com/your-username/ecommerce-platform.git
```

### 2. Install Dependencies:
This program uses `numpy`, `pandas`, and `matplotlib`. Install them using:
```bash
pip install numpy pandas matplotlib
```

### 3. Prepare the CSV Files:
You need to have the following CSV files in the same directory as the program:
- `console.csv`: Contains console product details (e.g., name, price, quantity).
- `games.csv`: Contains game product details (e.g., name, price, quantity).
- `employees.csv`: Contains employee data (e.g., name, salary).
- `login.csv`: Stores user login credentials.
- `money.csv`: Stores user purchase records.

### 4. Run the Program:
```bash
python ecommerce_platform.py
```

## How It Works

### Main Menu
- **User**: Log in as a user to browse and purchase products.
- **Admin**: Log in as an admin to manage the platform, view sales, employees, and generate graphs.
- **Employee**: View employee-specific information and products.

### User Features
1. **Login**: 
    - Users can log in with their name and password.
    - After logging in, users can browse products and make purchases.

2. **Sign Up**: 
    - New users can register by providing their name and setting a password.
    - User details are saved in `login.csv`.

3. **Buy Products**: 
    - Users can browse consoles or games, select items to buy, and view the total purchase cost.
    - The `money.csv` file records the user's purchases.

### Admin Features
1. **View Employees**: 
    - The admin can view a list of employees and their salaries.
    - Visualize employee salary data using different graph types.

2. **View Products**: 
    - The admin can view console and game products from CSV files.
    - Generate graphs to visualize product prices.

3. **Sales**: 
    - The admin can view the sales data recorded in `money.csv` and visualize it with graphs.

### Graph Options
- Line Graph
- Bar Graph
- Pie Graph
- Scatter Plot

## Example Usage

### 1. User Login and Purchase:
```
==============================
              MENU
==============================
 1. LOGIN
 2. New User? Sign Up
 3. Exit
Enter Choice: 1

Enter Name: JohnDoe
Enter Password: *****
WELCOME JohnDoe
```

```
==============================
             MENU
==============================
 1. Buy a product.
 2. Log out
Enter choice: 1
```

### 2. Admin View and Graph Generation:
```
==============================
              MENU
==============================
 1. View Employees.
 2. View products.
 3. Sales
 4. Exit
Enter Choice: 1

Employees:
    Name of Employee  Salary
0        Alice         50000
1        Bob           60000

What graph do u want?
 1. Line graph
 2. Bar graph
 3. Pie graph
 4. Scatter graph
Enter choice: 2
```

## Requirements

- Python 3.x
- `numpy`, `pandas`, `matplotlib` libraries

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This `README` covers all the key features, usage instructions, and a brief explanation of each section of the program. It also includes instructions on how to set up the necessary CSV files and install the dependencies.
