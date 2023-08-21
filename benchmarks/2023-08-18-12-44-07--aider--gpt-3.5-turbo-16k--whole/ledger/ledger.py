import datetime

class Entry:
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = Entry()
    entry.date = date
    entry.description = description
    entry.change = change
    return entry


def format_date(date):
    if isinstance(date, str):
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
    return date.strftime('%m/%d/%Y')


def format_change(currency, change):
    if currency == 'USD':
        return f'${change:,.2f}'
    elif currency == 'EUR':
        return f'€{change:,.2f}'


def format_entries(currency, locale, entries):
    if locale == 'en_US':
        header_row = [
            'Date'.ljust(10),
            'Description'.ljust(25),
            'Change'.rjust(13)
        ]
    elif locale == 'nl_NL':
        header_row = [
            'Datum'.ljust(10),
            'Omschrijving'.ljust(25),
            'Verandering'.rjust(13)
        ]

    table = ' | '.join(header_row) + '\n'

    while entries:
        min_entry = min(entries, key=lambda entry: (entry.date, entry.change, entry.description))
        entries.remove(min_entry)

        date_str = format_date(min_entry.date)
        description_str = min_entry.description[:25].ljust(25)
        change_str = format_change(currency, min_entry.change).rjust(13)

        table += f'{date_str} | {description_str} | {change_str}\n'

    return table
