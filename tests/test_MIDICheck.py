from miditools import MIDICheck
from miditools import MIDIConstants
from mido import Message

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

def test_check_chanel_no_note():
    pass

def test_check_channel_empty_list():
    # An empty channel is a muted instrument so no note out of range
    message_no1 = Message('note_on', note=100, velocity=3, time=0 )
    message_no2 = Message('note_on', note=127, velocity=3, time=0 )
    current_time = 0

    assert (MIDICheck.check_channel(0, [{'message': message_no1, 'abs_time': current_time},]))
    assert not (MIDICheck.check_channel(0, [{'message': message_no2, 'abs_time': current_time},]))
    assert (MIDICheck.check_channel(0, None))


def test_check_channel_nominal():
    assert (MIDICheck.check_channel(0, []))
