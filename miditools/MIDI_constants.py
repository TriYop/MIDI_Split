# Check if note may be played by selected instrument
MIDI_NOTES = dict(
    zip(
        "C-2", "C#-2", "D-2", "D#-2", "E-2", "F-2", "F#-2", "G-2", "G#-2", "A-2", "A#-2", "B-2",
        "C-1", "C#-1", "D-1", "D#-1", "E-1", "F-1", "F#-1", "G-1", "G#-1", "A-1", "A#-1", "B-1",
        "C0", "C#0", "D0", "D#0", "E0", "F0", "F#0", "G0", "G#0", "A0", "A#0", "B0",
        "C1", "C#1", "D1", "D#1", "E1", "F1", "F#1", "G1", "G#1", "A1", "A#1", "B1",
        "C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2",
        "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3",
        "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4",
        "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5",
        "C6", "C#6", "D6", "D#6", "E6", "F6", "F#6", "G6", "G#6", "A6", "A#6", "B6",
        "C7", "C#7", "D7", "D#7", "E7", "F7", "F#7", "G7", "G#7", "A7", "A#7", "B7",
        "C8", "C#8", "D8", "D#8", "E8", "F8", "F#8", "G8",
        range(0,128)
    )
)

MIDI_VALID_NOTES = {
    # Pianos
    0:(MIDI_NOTES['A0'],MIDI_NOTES['C8']), 1:(MIDI_NOTES['A0'],MIDI_NOTES['C8']), 2:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),
    3:(MIDI_NOTES['A0'],MIDI_NOTES['C8']), 4:(MIDI_NOTES['A0'],MIDI_NOTES['C8']), 5:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),

    # Clavecin
    6:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),
    # Clavi
    7:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),
    # Celesta, Glockenspiel, music box
    8:(MIDI_NOTES['A0'],MIDI_NOTES['C8']), 9:(MIDI_NOTES['A0'],MIDI_NOTES['C8']), 10:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),
    # Vibraphone, Marimba, Xylophone
    11:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),12:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),13:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),
    # Tubular Bells,
    14:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),
    # Dulcimer
    15:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),
    # Drawbar organ, Percussive Organ, Rock Organ
    16:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),17:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),18:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),
    # Church organ, Reed organ
    19:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),20:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),
    # Accordion, Harmonica, Bandoneon
    21:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),22:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),23:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),

    # Guitars and bass guitars
    # Acoustic Guitars
    24:(20,57), 25:(20,57),
    # Electric guitars
    26:(20,57), 27:(20,57), 28:(20,57),
    # Overdriven guitar, DIstortion guitar, Harmonics
    29:(20, 57), 30:(20,57), 31:(20,57),
    # Acoustic Bass, Fingered Bass, Picked bass
    32:(MIDI_NOTES['A0'],MIDI_NOTES['C8']), 33:(MIDI_NOTES['A0'],MIDI_NOTES['C8']), 34:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),
    # Fretless bass, slap 1 & 2
    35:(MIDI_NOTES['A0'],MIDI_NOTES['C8']), 36:(MIDI_NOTES['A0'],MIDI_NOTES['C8']), 37:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),
    # Synth bass
    38:(MIDI_NOTES['A0'],MIDI_NOTES['C8']), 39:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),

    # Orchestra Strings and timpani
    # Violin, viola, cello, doublebass
    40:(35,76),41:(28,64),42:(16,64),43:(8,42),
    # Tremolo, Pizzicato strings
    44:(MIDI_NOTES['A0'],MIDI_NOTES['C8']), 45:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),
    # Harp
    46:(4,83),
    # Timpani
    47:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),
    # String ensembles & Synth strings
    48:(MIDI_NOTES['A0'],MIDI_NOTES['C8']), 49:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),
    50:(MIDI_NOTES['A0'],MIDI_NOTES['C8']), 51:(MIDI_NOTES['A0'],MIDI_NOTES['C8']),

    # Choir & voice
    52:(18,61), 53:(18,61), 54:(18,61)
    }