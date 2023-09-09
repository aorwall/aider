# -*- coding: utf-8 -*-
from datetime import datetime

class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.description = description
        self.change = change

def create_entry(date, description, change):
    return LedgerEntry(date, description, change)

def format_entries(currency, locale, entries):
    formatter = _get_formatter(currency, locale)
    return formatter.format(entries)

class _Formatter:
    def format(self, entries):
        raise NotImplementedError()

class _EnUsFormatter(_Formatter):
    def format(self, entries):
        # Generate Header Row
        table = 'Date'
        for _ in range(7):
            table += ' ' 
        table += '| Description'
        for _ in range(15):
            table += ' '
        table += '| Change'
        for _ in range(7):
            table += ' '

        for entry in sorted(entries):
            table += '\n'

            # Write entry date to table
            month = entry.date.month
            if month < 10:
                month = '0' + str(month)
            else:
                month = str(month)
            date_str = month
            date_str += '/'
            day = entry.date.day
            if day < 10:
                day = '0' + str(day)
            else:
                day = str(day)
            date_str += day
            date_str += '/'
            year = entry.date.year
            year = str(year)
            while len(year) < 4:
                year = '0' + year
            date_str += year
            table += date_str
            table += ' | '

            # Write entry description to table
            # Truncate if necessary
            description = entry.description
            if len(description) > 25:
                description = description[:22] + '...'
            table += description.ljust(25)
            table += ' | '

            # Write entry change to table
            change_str = _format_change(entry.change, currency)
            table += change_str.rjust(13)

        return table

class _NlNlFormatter(_Formatter):
    def format(self,