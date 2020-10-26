from setup.scale import *
from setup.pitchclass import PitchClass
from setup.key import KeySignature
from setup.constants.values import *
import pygame
import wave

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
        center = PitchClass(note_name[0].upper() + note_name[1:])
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
    scale_string = ""
    for note in scale:
        print(note.name, end=' ')
        scale_string += (note.name + " ")
    break


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Scale builder")

font = pygame.font.Font('freesansbold.ttf', 100)
text = font.render(scale_string, True, WHITE, None)
textRect = text.get_rect()
textRect.center = (SCREEN_WIDTH // 2, 85)

screen.fill(BLACK)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(14):
        pygame.draw.rect(screen, WHITE,
                         (int((i * SCREEN_WIDTH / NUM_WHITE_KEYS) + BUFFER / 2),
                          int(SCREEN_HEIGHT * 0.25),
                          int((SCREEN_WIDTH / NUM_WHITE_KEYS) - BUFFER),
                          int(SCREEN_HEIGHT * 0.75)))

    for i in range(13):
        if i != 2 and i != 6 and i != 9:
            pygame.draw.rect(screen, BLACK,
                             (int(((((i + 1) * SCREEN_WIDTH / NUM_WHITE_KEYS) + BUFFER / 2) -
                                   (SCREEN_WIDTH / (NUM_WHITE_KEYS - 1)) * 0.25)),
                              int(SCREEN_HEIGHT * 0.25),
                              int((SCREEN_WIDTH / (NUM_WHITE_KEYS - 1)) * 0.5),
                              int(SCREEN_HEIGHT * 0.45)))

    screen.blit(text, textRect)

    pygame.display.update()
