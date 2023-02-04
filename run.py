import gspread
from pprint import pprint
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')

SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('my_sandwiches')
# sales = SHEET.worksheet('sales')
# data = sales.get_all_values()
# print(data)

def get_sales_data():
    """"
    Get sales figures input form the user
    """

    while True:

        print("Please enter sales data from the last market")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60")
        data_str = input("Enter your data here:")
        print(f"The data provided is {data_str}")
        sales_data = data_str.split(",")
        print(sales_data)
        if validate_date(sales_data):
            print("Data is valid!")
            break

    return sales_data

def validate_date(values):
    """
    check that there are 6 values
    check that the values can be converted to integers
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def update_sales_worksheet(data):
    """
        update sale data and inset into the worksheet
    """
    print("updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Update of worksheet successful!")

def calculate_surplus_data(sales_row):
    """
    calculate the surplus
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print (stock_row)




def main():
    """"
    run the program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    # update_sales_worksheet(data)
    calculate_surplus_data(sales_data)

main()