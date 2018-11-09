import csv
import rules
import types

EXCHANGE_RATE_DICT = {}


def read_row_from_csv(file_path):
    """ This function reads the CSV row one by one. This helps to read large CVS files,
    It reads them in chunks.
    :rtype: generator
    """
    try:
        with open(file_path, "rb") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                yield row
    except IOError:
        print('An error occured trying to read the file.')


def load_exchange_rate_dict(exchange_file_path):
    """ This function loads the Exchange rate CSV into Dict.
    :rtype: None
    """
    for row in read_row_from_csv(exchange_file_path):
        EXCHANGE_RATE_DICT.update({row.get('currency', None): row.get('exchange_rate_from_usd', 1)})


def get_field_name(file_path):
    """ This function extracts the column headers from CSV.
    :rtype: list of str
    """
    try:
        with open(file_path, "rb") as file_read:
            csv_reader = csv.DictReader(file_read)
            rtn_field_names = csv_reader.fieldnames
        return rtn_field_names
    except IOError:
        print('An error occured trying to read the file.')


def get_all_rules():
    """ This function gather all the valid rules required to run.
    :rtype: list of function references
    """
    rtnRules = []

    for a in dir(rules):
        if isinstance(rules.__dict__.get(a), types.FunctionType):
            rtnRules.append(rules.__dict__.get(a))

    return rtnRules

    # return [rules.__dict__.get(a) for a in dir(rules) if isinstance(rules.__dict__.get(a), types.FunctionType)]