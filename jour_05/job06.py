def roundUp(notes):
    roundup_notes = []
    for note in notes:
        if note >= 40 and note % 5 >= 3:
            roundup_notes.append(note + (5 - note % 5))
        else:
            roundup_notes.append(note)
    print(roundup_notes)

notes = [72, 68, 88, 91, 42, 83, 82]
roundUp(notes)



