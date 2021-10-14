from prettytable import PrettyTable
import pandas as pd
import datetime

table = PrettyTable()
table.field_names = ['id', 'name', 'price', 'expires']

def read_csv_data(filename):
    df = pd.read_csv(filename, index_col=False)
    return df

def generate_data(filename, value):
    df = read_csv_data(filename)
    PRICE_MIN, PRICE_MAX, EXPIRES_START, EXPIRES_STOP = value.split(' ')

    EXPIRES_START = datetime.datetime.strptime(EXPIRES_START, '%b-%d-%Y').strftime('%m/%d/%Y')
    EXPIRES_STOP = datetime.datetime.strptime(EXPIRES_STOP, '%b-%d-%Y').strftime('%m/%d/%Y')

    df = df[(df['price'] >= float(PRICE_MIN))&(df['price'] <= float(PRICE_MAX))]

    res_df = df[(df['expires'] >= EXPIRES_START)&(df['expires'] <= EXPIRES_STOP)]

    res_df.set_index('id', inplace=True)
    
    return res_df



def display_table(data):
    """
    Display product table
    """

    for (index, name, price, expires) in zip(data.index, data.name, data.price, data.expires):
        table.add_row([index, name, price, datetime.datetime.strptime(expires, '%m/%d/%Y').strftime('%b-%d-%Y')])

    # table.add_row([1, 'First sample item', 1.23, 'JAN-01-2019'])
    # table.add_row([2, 'Second sample item', 2.34, 'JAN-02-2019'])
    print(table)
    table.clear_rows()


def start():
    """
    Start accepting user input
    Quit program when user types 'exit'
    """

    while True:
        value = input('> ')
        if value == 'exit':
            break
        
        data = generate_data('products.csv', value)
        display_table(data)


if __name__ == '__main__':
    start()
