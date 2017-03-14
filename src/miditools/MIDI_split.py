#!/usr/bin/env python3
"""

"""
#
# Separate MIDI channels from a MIDI FILE
#

from mido import MidiFile, MetaMessage, MidiTrack
import logging
import os
import sys
import getopt

CHANNEL_MESSAGES = ['note_off', 'note_on', 'polytouch', 'control_change', 'program_change', 'pitchwheel', 'aftertouch']


def write_midi_file(filename, pattern):
    """
    Outputs a MIDI pattern as a MIDI file
    :param filename:
    :param pattern:
    :return:
    """
    logging.debug("Exporting MIDI channel to file://%s." % filename)
    if len(pattern.tracks[0]) > 0:
        # TODO: reinclude all META MESSAGES BEFORE SAVING
        logging.info("Generating output file: %s" % filename)
        pattern.save(filename)


def filter_events(pattern):
    """
    Splits events from the input MIDI file to separate MIDI channels and a META channel
    :param pattern:
    :return: an array of channels and a meta channel (array of META messages)
    """
    channels = {}
    metas = []
    current_time = 0.
    for message in pattern:
        current_time += int(message.time * 960)

        if isinstance(message, MetaMessage):
            if message.type != 'text':
                metas.append({'message': message, 'abs_time': current_time})

        elif message.type in CHANNEL_MESSAGES:
            # We do +1 because MIDI channels usually start numbering at 1 and channel 10 is usually drums one.
            chan = 'c' + str(message.channel + 1)
            if chan not in channels:
                channels[chan] = []
            channels[chan].append({'message': message, 'abs_time': current_time})

        else:
            logging.error("Caught unexpected MIDI message: %s" % repr(message))

    return channels, metas


def convert_list_to_track(evt_list):
    """
    Converts a list of events to a MIDI track with relative times
    :param evt_list:
    :return:
    """
    track = MidiTrack()
    current_time = 0

    for event in evt_list:
        print(event)
        msg = event['message']
        atm = event['abs_time']
        rel_time = int(atm - current_time)
        msg.time = rel_time
        track.append(msg)
        current_time = atm

    return track


def split_instruments(channel):
    """
    Splits a single MIDI channel into as many single instrument channels.

    :param channel:
    :return:
    """
    tracks = {}
    track = []

    # FIXME if track does not start with program_change, then behavior is unknown
    for event in channel:
        msg = event['message']
        atm = event['abs_time']

        if msg.type == 'program_change':
            pgm = msg.program
            if pgm not in tracks:
                track = []
                tracks[pgm] = track
                track.append({'message': msg, 'abs_time': atm})
            else:
                track = tracks[pgm]
        else:
            track.append({'message': msg, 'abs_time': atm})

    return tracks


def read_midi_file(filename):
    """
    Loads a MIDI File into Memory as a MIDI pattern
    :param filename:
    :return:
    """
    pattern = MidiFile(filename)
    logging.debug(repr(pattern))
    return pattern


def usage(msg=""):
    """
    Displays expected options to be passed when calling this program
    :param msg:
    :return:
    """
    if msg != "":
        print("Launch returned error: %s" % msg)

    print("\nOptions: ")
    print("  -i|--input <INPUT FILE PATH>   : Defines input MIDI file")
    print("  -o|--output <OUTPUT PATH>      : Defines ouptut directory")
    print("  -v|--verbose                   : sets verbose output")
    print("  -h|--help                      : displays this message")


def append_metas(track, metas):
    """
    Appends META information to any list of events.
    :param track:
    :param metas:
    :return:
    """
    pattern = []
    chan = -1
    midx = 0
    for cidx in range(len(track)):
        evt = track[cidx]
        msg = evt['message']
        abs_time = evt['abs_time']

        if chan == -1:
            chan = msg.channel
        meta = metas[midx]

        while meta['abs_time'] <= abs_time and midx < len(metas):
            logging.debug('%8d - Adding META %s' % (meta['abs_time'], repr(meta['message'])))
            pattern.append(meta)
            midx += 1
            meta = metas[midx]
        pattern.append(evt)
    return pattern


def main(argv):
    """
    Launches MIDI splitter, parses parameters and runs if possible.
    :param argv:
    :return:
    """
    try:
        optlist, args = getopt.getopt(argv, 'hvi:o:', ["help", "verbose", "input=", 'output='])
    except getopt.GetoptError as error:
        logging.error(error)
        usage()
        sys.exit(2)

    input_file = ""
    output_dir = ""
    input_set = False
    output_set = False
    verbose = False
    for o, a in optlist:
        if o in ['-h', '--help']:
            usage()
            sys.exit()
        if o in ["-v", "--verbose"]:
            verbose = True
        elif o in ['-i', '--input']:
            input_file = a
            if os.path.isfile(input_file):
                input_set = True
        elif o in ['-o', '--output']:
            output_dir = a
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            if os.path.isdir(output_dir):
                output_set = True
        else:
            assert False, "unhandled option"

    if verbose:
        logging.basicConfig(filename='MIDI_split.log', level=logging.DEBUG)
        logging.info("Logging set to verbose level.")

    else:
        logging.basicConfig(filename='MIDI_split.log', level=logging.WARNING)
        logging.warning("Logging set to quiet level.")

    assert input_set and output_set, "Missing options"

    in_pattern = read_midi_file(input_file)
    base_name = os.path.basename(input_file).rsplit('.', 1)[0]
    channels, metas = filter_events(in_pattern)
    logging.debug(repr(metas))
    ch = 0

    for chan in channels:
        instruments = split_instruments(channels[chan])

        if instruments is not None:
            cpt = 0
            for instrument in instruments:
                logging.debug("Appending instrument %s to output" % instrument)
                fname = os.path.join(output_dir, "%s_%s-p%s.mid" % (base_name, chan, instrument))
                logging.debug("Output file: %s" % fname)
                out_pattern = MidiFile(ticks_per_beat=in_pattern.ticks_per_beat, charset=in_pattern.charset,
                                       type=in_pattern.type)
                # out_pattern.tracks.append(instruments[instrument])
                out_pattern.tracks.append(convert_list_to_track(append_metas(instruments[instrument], metas)))

                cpt += 1
                write_midi_file(fname, out_pattern)
        ch += 1


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except AssertionError as err:
        usage(msg=str(err))
