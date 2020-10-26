import random
from setup.scale import Scale
from setup.key import KeySignature
from setup.pitchclass import PitchClass

# Picks a random major/minor scale and
# prints it to the screen

KEYS = ['C', 'a', 'F', 'd', 'Bb', 'g', 'Eb', 'c', 'Ab', 'f', 'Db', 'bb',
        'Gb', 'eb', 'B', 'g#', 'E', 'c#', 'A', 'f#', 'D', 'b', 'G', 'e']

print('Generating random key...')

k = random.choice(KEYS)

if k[0].isupper() is True:
    mode = 'major'
else:
    k = k.capitalize()
    mode = 'minor'

note = PitchClass(k)
key = KeySignature(note, mode)

print(f'Your key is {key.name}')
print('Generating scale...')

scale = Scale(key)

print(f'Here is  your {scale.name}:')
for note in scale:
    print(note.name, end=' ')
