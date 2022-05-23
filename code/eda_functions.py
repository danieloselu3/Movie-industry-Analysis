# we now work on removing the dolar sign, commars, and converting the data type to integer
# we will write a functio to do the above

def clean_column(df, column_to_clean, item_to_clean):
    """A function that takes in a dataset, column, item
        and removes the item from the specified column
    """
    return df[column_to_clean].map(lambda x: x.replace(f'{item_to_clean}', ""))