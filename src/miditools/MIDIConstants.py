# Check if note may be played by selected instrumenthttps://books.google.fr/books?id=VPl5DQAAQBAJ&pg=SA3-PA36-IA10&lpg=SA3-PA36-IA10&dq=valid+MIDI+notes+for+acoustic+instruments&source=bl&ots=r22FiPWbHv&sig=22xBajVHtOIVpysjN1G5gqEn4p4&hl=fr&sa=X&ved=0ahUKEwjpo8PolYXXAhVEXBQKHYPrBvQQ6AEIPTAH#v=onepage&q=valid%20MIDI%20notes%20for%20acoustic%20instruments&f=false
# See https://books.google.fr/books?id=VPl5DQAAQBAJ&pg=SA3-PA36-IA10&lpg=SA3-PA36-IA10&dq=valid+MIDI+notes+for+acoustic+instruments&source=bl&ots=r22FiPWbHv&sig=22xBajVHtOIVpysjN1G5gqEn4p4&hl=fr&sa=X&ved=0ahUKEwjpo8PolYXXAhVEXBQKHYPrBvQQ6AEIPTAH#v=onepage&q=valid%20MIDI%20notes%20for%20acoustic%20instruments&f=false
# for MIDI programming issues and automation options ...

MIDI_LOG_FORMATTER = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
MIDI_NOTES_NAMES = ["C-2", "C#-2", "D-2", "D#-2", "E-2", "F-2", "F#-2", "G-2", "G#-2", "A-2", "A#-2", "B-2",
                    "C-1", "C#-1", "D-1", "D#-1", "E-1", "F-1", "F#-1", "G-1", "G#-1", "A-1", "A#-1", "B-1",
                    "C0", "C#0", "D0", "D#0", "E0", "F0", "F#0", "G0", "G#0", "A0", "A#0", "B0",
                    "C1", "C#1", "D1", "D#1", "E1", "F1", "F#1", "G1", "G#1", "A1", "A#1", "B1",
                    "C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2",
                    "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3",
                    "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4",
                    "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5",
                    "C6", "C#6", "D6", "D#6", "E6", "F6", "F#6", "G6", "G#6", "A6", "A#6", "B6",
                    "C7", "C#7", "D7", "D#7", "E7", "F7", "F#7", "G7", "G#7", "A7", "A#7", "B7",
                    "C8", "C#8", "D8", "D#8", "E8", "F8", "F#8", "G8"]
MIDI_NOTES = dict(
    zip(
        MIDI_NOTES_NAMES,
        range(0, 128)
    )
)

# MIDI_REV_NOTES = {value: key for key, value in MIDI_NOTES.items()}

MIDI_VALID_NOTES = {
    # Pianos
    0: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 1: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    2: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    3: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 4: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    5: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),

    # Clavecin
    6: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Clavi
    7: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Celesta, Glockenspiel, music box
    8: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 9: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    10: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Vibraphone, Marimba, Xylophone
    11: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 12: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    13: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Tubular Bells,
    14: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),

    # Dulcimer
    15: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),

    # Drawbar organ, Percussive Organ, Rock Organ
    16: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 17: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    18: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Church organ, Reed organ
    19: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 20: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Accordion, Harmonica, Bandoneon
    21: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 22: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    23: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),

    # Guitars and bass guitars
    # Acoustic Guitars
    24: (20, 57), 25: (20, 57),
    # Electric guitars
    26: (20, 57), 27: (20, 57), 28: (20, 57),
    # Overdriven guitar, DIstortion guitar, Harmonics
    29: (20, 57), 30: (20, 57), 31: (20, 57),
    # Acoustic Bass, Fingered Bass, Picked bass
    32: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 33: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    34: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Fretless bass, slap 1 & 2
    35: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 36: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    37: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Synth bass
    38: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 39: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),

    # Orchestra Strings and timpani
    # Violin, viola, cello, doublebass
    40: (35, 76), 41: (28, 64), 42: (16, 64), 43: (8, 42),
    # Tremolo, Pizzicato strings
    44: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 45: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Harp
    46: (4, 83),
    # Timpani
    47: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # String ensembles & Synth strings
    48: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 49: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    50: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 51: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),

    # Choir & voice
    52: (18, 61), 53: (18, 61), 54: (18, 61),

    # Orchestra Hit
    55: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),

    # Brass Instruments
    56: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 57: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    58: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 59: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    60: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),

    # Brass ensembles & synth brass
    61: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 62: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    63: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),

    # Saxophones
    64: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 65: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    66: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 67: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),

    # other Woodwinds
    68: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 69: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    70: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 71: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),

    # Flutes
    72: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 73: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    74: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 75: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    76: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 77: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    78: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 79: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),

    # Synths
    # Lead synth
    80: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 81: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    82: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 83: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    84: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 85: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    86: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 87: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Pad Synths
    88: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 89: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    90: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 91: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    92: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 93: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    94: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 95: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Synth FX
    96: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 97: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    98: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 99: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    100: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 101: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    102: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 103: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),

    # Ethnic instruments
    # Sitar
    104: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Bandjo
    105: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Shamisen
    106: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Koto
    107: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Kalimba
    108: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Bagpipes
    109: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Fiddle
    110: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Shanai
    111: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Tinkle Bell
    112: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Agogo
    113: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Steel Drums
    114: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Woodblock
    115: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # melodic drums: Taiko Drums / Melodic tom / Synth Drum
    116: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 117: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    118: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Reverse cymbal
    119: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # articulations: Guitar fret noise / Breath noise
    120: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 121: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    # Sound ambiance
    122: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 123: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    124: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 125: (MIDI_NOTES['A0'], MIDI_NOTES['C8']),
    126: (MIDI_NOTES['A0'], MIDI_NOTES['C8']), 127: (MIDI_NOTES['A0'], MIDI_NOTES['C8'])

}
