#!/bin/env python
#

import logging
from miditools import MIDI_constants

logger = logging.getLogger("miditools.MIDI_split")

"""
Checks if MIDI file describes "valid music"
"""

def check_note(inst, note):
    return note>=MIDI_constants.VALID_NOTES[inst][0] and note<=MIDI_constants.VALID_NOTES[inst][1]

def check_channel(instrument, evt_list):
    for event in evt_list:
        message = event['message']
        if message.type == 'note_on':
            if not check_note(instrument, message.note):
                logger.warn("Instrument %d (%s) cannot play note %d (%s)" %(instrument, instrument, event, ))
