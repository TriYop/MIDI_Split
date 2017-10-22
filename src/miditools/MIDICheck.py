#!/bin/env python
#

import logging

from miditools import MIDIConstants
logging.basicConfig(level=logging.INFO, format=MIDIConstants.MIDI_LOG_FORMATTER)
logger = logging.getLogger("miditools.MIDISplit")


"""
Checks if MIDI file describes "valid music"
"""


def check_note(inst, note):
    """
    Tells if the real instrument can play the given note
    :param inst: instrument number
    :param note: played note
    :return: boolean telling if instrument can play the given note
    """
    if inst < 0 or inst > 128 or note < 0 or note > 128:
        return False;
    return MIDIConstants.MIDI_VALID_NOTES[inst][0] <= note <= MIDIConstants.MIDI_VALID_NOTES[inst][1]


def check_channel(instrument, evt_list):
    result = True
    if evt_list is not None:
        for event in evt_list:
            message = event['message']
            if message.type == 'note_on':
                if not check_note(instrument, message.note):
                    logger.warn("Instrument %d (%s) cannot play note %d (%s)." % (
                        instrument, instrument, message.note, MIDIConstants.MIDI_NOTES_NAMES[message.note]))
                    result = False

                else:
                    logger.debug("Instrument %d (%s) can play note %d" %(instrument, instrument, message.note))
    return result
