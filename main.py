from random import randint

def get_emails(filename: str):
    # parses csv for email entries
    entries = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            line = line.split(',')
            if len(line) > 2:
                entries.append(line[1])
    entries.pop(0)
    return entries

def pick_entries(entries: list, draws: int):
    # chooses draws number of picks randomly, removing pick on each iteration
    picks = []
    while draws > 0:
        i = randint(0, (len(entries)-1))
        picks.append(entries.pop(i))
        draws -= 1
        
    return picks

def main():
    winners = pick_entries(get_emails("Giveaway.csv"), 3)
    print(winners)

if __name__ == "__main__":
    main()