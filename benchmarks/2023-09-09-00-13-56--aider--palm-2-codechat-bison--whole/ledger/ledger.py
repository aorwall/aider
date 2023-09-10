# -*- coding: utf-8 -*-

"""
This file contains code for printing a nicely formatted ledger, given a locale
(American or Dutch) and a currency (US dollar or euro).
"""

from datetime import datetime


class LedgerEntry:
    """
    Represents a ledger entry.

    Attributes:
        date: The date of the entry.
        description: The description of the entry.
        change: The change amount of the entry.
    """

    def __init__(self, date, description, change):
        """
        Initializes a new LedgerEntry object.

        Args:
            date: The date of the entry.
            description: The description of the entry.
            change: The change amount of the entry.
        """
        self.date = date
        self.description = description
        self.change = change


def format_entries(currency, locale, entries):
    """
    Formats a list of ledger entries into a nicely formatted table.

    Args:
        currency: The currency of the entries.
        locale: The locale of the entries.
        entries: A list of LedgerEntry objects.

    Returns:
        A string containing the formatted table.
    """

    # Generate header row

    if locale == "en_US":
        table = "Date"
        for _ in range(7):
            table += " "
        table += "| Description"
        for _ in range(15):
            table += " "
        table += "| Change"
        for _ in range(7):
            table += " "

    elif locale == "nl_NL":
        table = "Datum"
