# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    return entry


def format_date(entry, locale):
    if locale == 'en_US':
        return entry.date.strftime('%m/%d/%Y')
    elif locale == 'nl_NL':
        return entry.date.strftime('%d-%m-%Y')


def format_description(entry):
    if len(entry.description) > 25:
        return entry.description[:22] + '...'
    else:
        return entry.description.ljust(25)


def format_change(entry, currency, locale):
    change_str = ''
    if entry.change < 0:
        change_str = '('
    if currency == 'USD':
        change_str += '$'
    elif currency == 'EUR':
        change_str += u'€'
    change_value = abs(int(entry.change / 100.0))
    if locale == 'nl_NL':
        change_str += f'{change_value:,.2f}'.replace('.', ',').replace(',', '.')
    else:
        change_str += f'{change_value:,.2f}'
    if entry.change < 0:
        change_str += ')'
    else:
        change_str += ' '
    return change_str.rjust(13)


def sort_entries(entries):
    return sorted(entries, key=lambda e: (e.date, e.change, e.description))


def format_entries(currency, locale, entries):
    entries = sort_entries(entries)
    table = ''
    if locale == 'en_US':
        table += 'Date       | Description               | Change       \n'
    elif locale == 'nl_NL':
        table += 'Datum      | Omschrijving              | Verandering  \n'
    for entry in entries:
        table += format_date(entry, locale) + ' | '
        table += format_description(entry) + ' | '
        table += format_change(entry, currency, locale) + '\n'
    return table
