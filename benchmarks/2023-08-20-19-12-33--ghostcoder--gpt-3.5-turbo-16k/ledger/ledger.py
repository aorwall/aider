# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.description = description
        self.change = change


def create_entry(date, description, change):
    entry = LedgerEntry(date, description, change)
    return entry


def format_entries(currency, locale, entries):
    if locale == 'en_US':
        # Generate Header Row
        table = 'Date       | Description               | Change       \n'

        while len(entries) > 0:
            # Find next entry in order
            min_entry_index = -1
            for i in range(len(entries)):
                entry = entries[i]
                if min_entry_index < 0:
                    min_entry_index = i
                    continue
                min_entry = entries[min_entry_index]
                if entry.date < min_entry.date:
                    min_entry_index = i
                    continue
                if (
                    entry.date == min_entry.date and
                    entry.change < min_entry.change
                ):
                    min_entry_index = i
                    continue
                if (
                    entry.date == min_entry.date and
                    entry.change == min_entry.change and
                    entry.description < min_entry.description
                ):
                    min_entry_index = i
                    continue
            entry = entries[min_entry_index]
            entries.pop(min_entry_index)

            # Write entry date to table
            date_str = entry.date.strftime('%m/%d/%Y')
            table += date_str
            table += ' | '

            # Write entry description to table
            # Truncate if necessary
            if len(entry.description) > 25:
                table += entry.description[:22]
                table += '...'
            else:
                table += entry.description.ljust(25)

            table += ' | '

            # Write entry change to table
            if currency == 'USD':
                change_str = ''
                if entry.change < 0:
                    change_str = '('
                change_str += '${:,.2f}'.format(abs(entry.change) / 100)
                if entry.change < 0:
                    change_str += ')'
                else:
                    change_str += ' '
                table += change_str.rjust(13)
            elif currency == 'EUR':
                change_str = ''
                if entry.change < 0:
                    change_str = '('
                change_str += '€{:,.2f}'.format(abs(entry.change) / 100)
                if entry.change < 0:
                    change_str += ')'
                else:
                    change_str += ' '
                table += change_str.rjust(13)
        return table
    elif locale == 'nl_NL':
        # Generate Header Row
        table = 'Datum      | Omschrijving              | Verandering  \n'

        while len(entries) > 0:
            # Find next entry in order
            min_entry_index = -1
            for i in range(len(entries)):
                entry = entries[i]
                if min_entry_index < 0:
                    min_entry_index = i
                    continue
                min_entry = entries[min_entry_index]
                if entry.date < min_entry.date:
                    min_entry_index = i
                    continue
                if (
                    entry.date == min_entry.date and
                    entry.change < min_entry.change
                ):
                    min_entry_index = i
                    continue
                if (
                    entry.date == min_entry.date and
                    entry.change == min_entry.change and
                    entry.description < min_entry.description
                ):
                    min_entry_index = i
                    continue
            entry = entries[min_entry_index]
            entries.pop(min_entry_index)

            # Write entry date to table
            date_str = entry.date.strftime('%d-%m-%Y')
            table += date_str
            table += ' | '

            # Write entry description to table
            # Truncate if necessary
            if len(entry.description) > 25:
                table += entry.description[:22]
                table += '...'
            else:
                table += entry.description.ljust(25)

            table += ' | '

            # Write entry change to table
            if currency == 'USD':
                change_str = '$ '
                if entry.change < 0:
                    change_str += '-'
                change_str += '{:,.2f}'.format(abs(entry.change) / 100)
                change_str += ' '
                table += change_str.rjust(13)
            elif currency == 'EUR':
                change_str = '€ '
                if entry.change < 0:
                    change_str += '-'
                change_str += '{:,.2f}'.format(abs(entry.change) / 100)
                change_str += ' '
                table += change_str.rjust(13)
        return table