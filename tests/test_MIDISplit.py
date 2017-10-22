from miditools import MIDISplit
from mido import MidiFile, MetaMessage, MidiTrack

def test_write_midi_file():
    MIDISplit.write_midi_file("TestOut", MidiFile())
    assert True
