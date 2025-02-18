class Ledger:
    def __init__(self, name='My Ledger', currency='USD'):
        self.name = name
        self.currency = currency
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def get_balance(self):
        balance = 0
        for entry in self.entries:
            balance += entry.change
        return balance

    def print_to_console(self, currency=None):
        if not currency:
            currency = self.currency
        print('-------------------------')
        print(f"{self.name} - {currency}")
        print('-------------------------')
        print()
        print('Date       | Description                     | Change')
        print('----------|-------------------------------|-------')
        print(self._get_table())
        print()
        total_balance = self.get_balance()
        if total_balance >= 0:
            sign = ''
        else:
            sign = '-'
        if currency == 'USD':
            total_balance_str = '$'
        elif currency == 'EUR':
            total_balance_str = u'€'
        total_balance_abs = abs(total_balance)
        total_balance_dollars = int(total_balance_abs / 100)
        total_balance_cents = int(total_balance_abs % 100)
        total_balance_str += '{:,.2f}'.format(total_balance_dollars).replace(',', '.')
        total_balance_str += ','
        total_balance_str += '{:02d}'.format(total_balance_cents)
        print(sign + total_balance_str + ' Total Balance')

    def _get_table(self):
        table = ''
        for entry in self.entries:
            # Write entry date to table
            day = entry.date.day
            day = str(day)
            if len(day) < 2:
                day = '0' + day
            date_str = day
            date_str += '-'
            month = entry.date.month
            month = str(month)
            if len(month) < 2:
                month = '0' + month
            date_str += month
            date_str += '-'
            year = entry.date.year
            year = str(year)
            while len(year) < 4:
                year = '0' + year
            date_str += year
            table += date_str
            table += ' | '

            # Write entry description to table
            # Truncate if necessary
            if len(entry.description) > 25:
                for i in range(22):
                    table += entry.description[i]
                table += '...'
            else:
                for i in range(25):
                    if len(entry.description) > i:
                        table += entry.description[i]
                    else:
                        table += ' '
            table += ' | '

            # Write entry change to table
            if currency == 'USD':
                change_str = '$ '
                if entry.change < 0:
                    change_str += '-'
                change_dollar = abs(int(entry.change / 100.0))
                dollar_parts = []
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                if len(dollar_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += dollar_parts[0]
                        dollar_parts.pop(0)
                        if len(dollar_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2: