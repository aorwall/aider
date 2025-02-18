from datetime import datetime


class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.description = description
        self.change = change


def create_entry(date, description, change):
    return LedgerEntry(date, description, change)


def format_date(entry, locale):
    if locale == 'en_US':
        return entry.date.strftime('%m/%d/%Y')
    elif locale == 'nl_NL':
        return entry.date.strftime('%d-%m-%Y')


def format_description(entry):
    return entry.description[:22] + '...' if len(entry.description) > 25 else entry.description.ljust(25)


def format_change(entry, currency):
    change = abs(entry.change)
    change_str = f'{change // 100}.{change % 100:02d}'
    if currency == 'USD':
        change_str = f'${change_str}'
    elif currency == 'EUR':
        change_str = f'€{change_str}'
    return f'({change_str})' if entry.change < 0 else change_str.ljust(13)


def format_entries(currency, locale, entries):
    entries = sorted(entries, key=lambda e: (e.date, e.change, e.description))
    header = 'Date       | Description               | Change       ' if locale == 'en_US' else 'Datum      | Omschrijving              | Verandering  '
    return header + '\n'.join([f'{format_date(e, locale)} | {format_description(e)} | {format_change(e, currency)}' for e in entries])