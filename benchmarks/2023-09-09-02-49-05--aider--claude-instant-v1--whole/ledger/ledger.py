# -*- coding: utf-8 -*-
from datetime import datetime

class LedgerEntry:
  def __init__(self, date, description, change):
    self.date = date
    self.description = description
    self.change = change

def create_entry(date, description, change):
  return LedgerEntry(
    datetime.strptime(date, '%Y-%m-%d'),
    description,
    change
  )

def format_entries(currency, locale, entries):

  def format_date(date):
    date_string = date.strftime("%m/%d/%Y")
    if locale == 'nl_NL':
      date_string = date.strftime("%d-%m-%Y")
    return date_string

  def format_change(change, currency):
    if currency == 'USD':
      change_string = f"${change:,.2f}"
    elif currency == 'EUR':  
      change_string = f"€{change:,.2f}"
    return change_string

  header = ["Date", "Description", "Change"]
  if locale == 'nl_NL':
    header = ["Datum", "Omschrijving", "Wijziging"]

  table = "\n".join([
    "\t".join(header),
    *("\t".join([
      format_date(entry.date), 
      entry.description[:25],
      format_change(entry.change, currency)
    ]) for entry in sorted(entries, key=lambda e: (e.date, e.change, e.description)))
  ])

  return table
