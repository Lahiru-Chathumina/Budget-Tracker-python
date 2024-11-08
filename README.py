# README.py - Python script to display project information

def display_project_info():
    project_info = """
    ===========================
    Budget Tracker Application
    ===========================

    A budget tracker application developed in Python that helps users manage and analyze their personal finances 
    by logging expenses and viewing detailed reports. This application utilizes CSV for data storage and provides 
    an intuitive interface for effective financial management.

    Features:
    ----------
    - Add new budget entries with date, category, description, and amount.
    - View all budget entries.
    - Calculate total amount spent based on logged entries.

    Requirements:
    -------------
    - Python 3.x
    - Standard Python libraries (no external libraries required)
      - csv - For reading and writing data to CSV files.
      - datetime - For managing date-related functionality.

    Installation:
    -------------
    1. Clone the repository:
       ```bash
       git clone https://github.com/yourusername/budget-tracker.git
       cd budget-tracker
       ```

    2. Run the application:
       ```bash
       python budget_tracker.py
       ```

    Usage:
    ------
    1. **Add a New Budget Entry**:
       - Enter date, category, description, and amount to log a new expense.
    
    2. **View All Budget Entries**:
       - View all your logged expenses in a tabular format.

    3. **Calculate Total Amount Spent**:
       - Calculate the total amount spent from all logged entries.

    Project Structure:
    -------------------
    - budget_tracker.py           # Main Python script for the budget tracker functionality.
    - expenses.csv               # CSV file storing all expense data.
    - README.md                  # This file.

    Future Features:
    ----------------
    - Expense Category Breakdown: Filter and display expenses by category.
    - Monthly Summary: Provide a monthly summary of your expenses.
    - Budget Goal: Allow users to set and track budget goals.
    - Graphical Reports: Generate graphs to visualize your spending.

    License:
    --------
    This project is licensed under the MIT License.

    Contributions:
    --------------
    Feel free to fork the project, submit issues, and create pull requests for improvements.
    """
    
    print(project_info)

# Display project information
if __name__ == "__main__":
    display_project_info()
