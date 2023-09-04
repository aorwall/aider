from typing import List
import datetime

class Ledger:
    def __init__(self, filepath=None):
        self._entries = []
        self._filepath = None
        if filepath is not None:
            with open(filepath, 'r') as f:
                lines = [line.strip() for line in f.readlines()]
            for line in lines:
                parts = line.split('|')
                date = datetime.datetime.strptime(parts[0], '%Y-%m-%d').date()
                desc = parts[1].strip()
                change = int(float(parts[2])*100)
                self.record(date, desc, change)

    @property
    def size(self):
        return len(self._entries)

    def record(self, date, description, change):
        assert type(date) == datetime.date
        assert type(description) == str
        assert type(change) == int
        self._entries.append(Entry(date, description, change))

    def get_balance(self, date=None):
        balance = 0
        if date is None:
            date = datetime.date.today()
        for entry in self._entries:
            if entry.date <= date:
                balance += entry.change
        return balance

    def write_to_file(self, filepath):
        with open(filepath, 'w+') as f:
            for entry in self._entries:
                f.write('%s\n' % (entry))

    def __repr__(self):
        s = ''
        for entry in self._entries:
            s += '%s\n' % (entry)
        return s[:-1]

    def __iter__(self):
        yield from self._entries

class Entry:
    def __init__(self, date, description, change):
        self.date = date
        self.description = description
        self.change = change

    def __eq__(self, other):
        return (self.date == other.date and self.description == other.description and self.change == other.change)

    def __hash__(self):
        return hash((self.date, self.description, self.change))

    def __lt__(self, other):
        return self.date < other.date

    def __gt__(self, other):
        return self.date > other.date

    def __le__(self, other):
        return self.date <= other.date

    def __ge__(self, other):
        return self.date >= other.date

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return '%s | %s | $%.2f' % (self.date.isoformat(), self.description, self.change/100.0)

def demo():
    l = Ledger('ledger.txt')
    print(l)
    print('\nsize:', l.size)
    print('\nget_balance(\'2019-12-31\'):', l.get_balance(datetime.date(2019, 12, 31)))
    print('\nget_balance(\'2020-06-30\'):', l.get_balance(datetime.date(2020, 6, 30)))
    print('\nget_balance():', l.get_balance())
    l.record(datetime.date(2020, 7, 1), 'New entry', -12345)
    print('\nl after new entry:')
    print(l)
    l.write_to_file('new_ledger.txt')
    print('\ncontents of new_ledger.txt:')
    with open('new_ledger.txt', 'r') as f:
        print(f.read())

if __name__ == '__main__':
    demo()


if __name__ == "__main__":
    demo()