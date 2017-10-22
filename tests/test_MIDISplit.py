from miditools import MIDISplit
from mido import MidiFile, MetaMessage, MidiTrack



def test_write_empty_midi_file():
    MIDISplit.write_midi_file("TestOut.mid", MidiFile())
    assert True

def test_write_midi_file():
    output = MidiFile()
    output.add_track(name="test_track")
    output.ticks_per_beat=724
    output.type = 1
    MIDISplit.write_midi_file("TestOut.mid", output)

