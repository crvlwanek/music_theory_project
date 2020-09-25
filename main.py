from scale import *

"""
MUSIC THEORY PROJECT
- currently builds a scale of note objects
- working in every key and all modes of the
  major scale
"""

print("This program builds a scale from a note and major scale mode of your choice")

while True:
    note_name = input("Pick a note to be your key center:\n")
    try:
        center = pick_note(note_name[0].upper() + note_name[1:])
    except KeyError:
        print("Please enter a valid note name (ex. Ab, C, F#)\n")
        continue
    mode_name = input(f"Pick a mode for your {center.name} scale:\n")
    try:
        kso = KeySignature(center, mode_name.lower())
    except ValueError:
        print(f"{note_name} {mode_name} is not a valid key center/mode pair, please try another")
        continue
    scale = Scale(kso)
    print()
    print(f"Here is your {scale.name}:")
    for note in scale.scale:
        print(note.name, end=' ')
    print("\n")
