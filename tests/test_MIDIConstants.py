from miditools import MIDIConstants


def test_lists_sizes():
    assert len(MIDIConstants.MIDI_VALID_NOTES) == 128
    assert len(MIDIConstants.MIDI_NOTES) == 128
