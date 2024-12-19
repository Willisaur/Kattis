numNotes, difference = map(int, input().split())
seen = set()
notes = list(note for note in (int(input()) for _ in range(numNotes)) if note not in seen and not seen.add(note))
notes.sort()

numRecordings = 1

lowest = notes[0]
for n in notes:
    if n - lowest > difference:
        lowest = n
        numRecordings += 1

print(numRecordings)
