
def validate_sales(column_key='total_purchases', **row):
    """ This rule validates sale.
    'The video must have over 200 sales.'
    :rtype: boolean
    """
    total_sales = row[column_key]
    if total_sales:
        if int(total_sales) > 200:
            return True
    return False


def validate_likes(column_key='total_likes', **row):
    """ This rule validates likes.
    'The video must have over 10 likes.'
    :rtype: boolean
    """
    total_likes = row[column_key]
    if total_likes:
        if int(total_likes) > 10:
            return True
    return False


def validate_title(column_key='title', **row):
    """ This rule validates title.
    'The video title must be shorter than 30 characters.'
    :rtype: boolean
    """
    title = row[column_key]
    if len(title) < 30:
        return True
    return False


def validate_cost(column_key='unit_price_in_usd', **row):
    """ This rule validates video price.
    'The video price must be under 20 Euros or under 25 Canadian Dollars.'
    :rtype: boolean
    """
    from utility import EXCHANGE_RATE_DICT

    max_euro = 20
    euro_exchange = EXCHANGE_RATE_DICT.get('EUR', None)
    if not euro_exchange:
        print 'Exchange Rate of Euro is NA, hence using USD'
        euro_exchange = 1

    max_canadian= 25
    canadian_exchange = EXCHANGE_RATE_DICT.get('CAD', None)
    if not canadian_exchange:
        print 'Exchange Rate of Canadian Dollar is NA, hence using USD'
        canadian_exchange = 1

    total_cost = row[column_key]
    if total_cost:
        if float(total_cost) < float(max_canadian/float(canadian_exchange)) or \
                float(total_cost) < float(max_euro/float(euro_exchange)):
            return True
    return False


# def validate_country(column_key='country', **row):
#     """ This rule validates title.
#     'The video title must be shorter than 30 characters.'
#     :rtype: boolean
#     """
#     country = row[column_key]
#     valid_country = ['USA', 'Canada']
#     if country in valid_country:
#         return True
#     return False
