'''
We are working on a security system for a badged-access room in our company's building.

Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:

1. All employees who didn't use their badge while exiting the room – they recorded an enter without a matching exit.

2. All employees who didn't use their badge while entering the room  – they recorded an exit without a matching enter.

badge_records = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
]

find_mismatched_entries(badge_records)
# Expected output: ["Paul", "Curtis"], ["Martha"]

'''


class Record:
    def __init__(self, name, enter=0, exit=0):
        self.name = name
        self.enter = enter
        self.exit = exit
    def addEntry(self):
        self.enter += 1
    def addExit(self):
        self.exit += 1
    def exitNenter(self):
        return (self.exit > self.enter)
    def enterNexit(self):
        return (self.enter > self.exit)

def find_mismatched_entries(badge_records):
    records = read_record(badge_records)
    enterNexit = []
    exitNenter = []
    for record in records:

        if record.enterNexit():
            enterNexit.append(record.name)
        if record.exitNenter():
            exitNenter.append(record.name)

    result = str(enterNexit)+", "+str(exitNenter)
    print(result)
    return result


def read_record(badge_records):
    result = []
    name = []
    for record in badge_records:
        if record[0] not in name:
            if record[1] == "enter":
                new_record = Record(record[0], 1, 0)
            elif record[1] == "exit":
                new_record = Record(record[0], 0, 1)
            name.append(record[0])
            result.append(new_record)
        else:
            i = name.index(record[0])
            if record[1] == "enter":
                result[i].addEntry()
            else:
                result[i].addExit()
    return result


def main():
    badge_records = [
        ["Martha", "exit"],
        ["Paul", "enter"],
        ["Martha", "enter"],
        ["Martha", "exit"],
        ["Jennifer", "enter"],
        ["Paul", "enter"],
        ["Curtis", "enter"],
        ["Paul", "exit"],
        ["Martha", "enter"],
        ["Martha", "exit"],
        ["Jennifer", "exit"], ]

    find_mismatched_entries(badge_records)

if __name__ == '__main__':
    main()