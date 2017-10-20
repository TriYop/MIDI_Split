from miditools import MIDICheck
from miditools import MIDIConstants


def test_check_note_invalid_note():
    assert not (MIDICheck.check_note(0, -1))
    assert not (MIDICheck.check_note(0, 129))
    assert not (MIDICheck.check_note(0, MIDIConstants.MIDI_VALID_NOTES[0][0] - 1))
    assert not (MIDICheck.check_note(0, MIDIConstants.MIDI_VALID_NOTES[0][1] + 1))

def test_check_note_invalid_inst():
    assert not (MIDICheck.check_note(-1, 64))
    assert not (MIDICheck.check_note(129, 64))

def test_check_note_nominal():
    assert (MIDICheck.check_note(0, MIDIConstants.MIDI_VALID_NOTES[0][0]))
    assert (MIDICheck.check_note(0, MIDIConstants.MIDI_VALID_NOTES[0][1]))



