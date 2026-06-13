# Import locale module
import locale

# Set locale to Spanish (Spain)
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

# Function to format currency
def format_currency(value):
    # Use locale.currency to format
    return locale.currency(value, grouping=True)

# Import datetime for date handling
from datetime import datetime

# Function to format date
def format_date(dt):
    # Use locale's appropriate date format
    return dt.strftime("%x")

# Example usage
if __name__ == "__main__":
    # Sample number
    amount = 1234567.89
    # Sample date
    today = datetime.now()
    # Print formatted results
    print('Monto', format_currency(amount))
    print('Fecha', format_date(today))
