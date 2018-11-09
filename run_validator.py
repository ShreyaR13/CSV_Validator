import csv
import sys
from utility import read_row_from_csv, get_field_name, get_all_rules, load_exchange_rate_dict
import os.path

ALL_RULES = get_all_rules()
VALID_CSV_FILE = 'data/valid.csv'
INVALID_CSV_FILE = 'data/invalid.csv'


def run_rules(master_cvs_file, exchange_rate_cvs_file):
    """ This function runs the rules over master video CSV and creates two CSVs.
    It returns grand total.
    :rtype: float
    """
    field_names_list = ['id',
                        'title',
                        'total_likes',
                        'total_purchases',
                        'unit_price_in_usd']
    # You can even call this if you don't want to ha    rd-code column names.
    # field_names_list = get_field_name(MASTER_CSV_FILE)

    load_exchange_rate_dict(exchange_rate_cvs_file)

    with open(VALID_CSV_FILE, 'wb') as valid_videos_csv, \
            open(INVALID_CSV_FILE, 'wb') as invalid_videos_csv:
        valid_csv_writer = csv.DictWriter(valid_videos_csv, fieldnames=field_names_list)
        invalid_csv_writer = csv.DictWriter(invalid_videos_csv, fieldnames=field_names_list)
        valid_csv_writer.writeheader()
        invalid_csv_writer.writeheader()

        final_grand_total = 0
        sale_key = 'unit_price_in_usd'

        for row in read_row_from_csv(master_cvs_file):
            if all([fn(**row) for fn in ALL_RULES]):
                valid_csv_writer.writerow(row)
                final_grand_total += float(row.get(sale_key, 0))
            else:
                invalid_csv_writer.writerow(row)

        print 'Grand Total of all the videos in valid.csv: %s' % final_grand_total
    return final_grand_total


def main():
    if len(sys.argv) < 3:
        print 'Please pass in the Master Video.cvs file path. Eg. data/videos.csv and \n Exchange Rate CSV file path'
        return

    master_cvs_file = sys.argv[1]
    if not os.path.isfile(master_cvs_file):
        print 'Provided %s master file does not exist' % master_cvs_file
        return

    exchange_rate_cvs_file = sys.argv[2]
    if not os.path.isfile(exchange_rate_cvs_file):
        print 'Provided %s exchange rate file does not exist' % exchange_rate_cvs_file
        return
    run_rules(master_cvs_file, exchange_rate_cvs_file)


if __name__ == "__main__":
    main()
