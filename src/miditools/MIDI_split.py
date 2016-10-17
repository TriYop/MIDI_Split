#
# Separate MIDI channels from a MIDI FILE
#
#

from mido import MidiFile, MetaMessage, MidiTrack, Message
import logging
import os
import sys
import getopt


def write_midi_file(filename, pattern):
    """
    Outputs a MIDI pattern as a MIDI file
    :param filename:
    :param pattern:
    :return:
    """
    logging.debug(repr(pattern))
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

        elif message.type == 'note_on' or message.type == 'note_off' or message.type == 'program_change':
            chan = 'c' + str(message.channel)
            if chan not in channels:
                channels[chan] = []
            channels[chan].append({'message': message, 'abs_time': current_time})

        else:
            logging.error("Caught unexpected MIDI message: " % repr(message))

    return channels, metas


def filter_instruments(channel):
    """
    Splits each instruments to a single file.
    :param channel:
    :return:
    """
    instruments = []
    current_instrument = 0
    track = MidiTrack()
    instruments.append(track)
    current_pgm_time = {current_instrument: 0}
    for event in channel:
        msg = event['message']
        if msg.type == 'program_change':
            track = MidiTrack()
            instruments.append(track)
            current_instrument = msg.program
            if current_instrument not in current_pgm_time:
                current_pgm_time[current_instrument] = 0
                track.append(Message('program_change', program=current_instrument, time=0))
                # rel_time = event['abs_time'] - current_pgm_time[current_instrument]

        else:
            rel_time = int(event['abs_time'] - current_pgm_time[current_instrument])
            track.append(Message(msg.type, channel=msg.channel, note=msg.note, velocity=msg.velocity, time=rel_time))
        current_pgm_time[current_instrument] = event['abs_time']
    return instruments


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


def main(argv):
    """
    Launches MIDI splitter, parses parameters and runs if possible.
    :param argv:
    :return:
    """
    logging.basicConfig(filename='MIDI_split.log', level=logging.WARNING)

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
    for o, a in optlist:
        if o in ['-h', '--help']:
            usage()
            sys.exit()
        if o in ["-v", "--verbose"]:
            logging.basicConfig(filename='MIDI_split.log', level=logging.DEBUG)
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

    assert input_set and output_set, "Missing options"

    in_pattern = read_midi_file(input_file)
    base_name = os.path.basename(input_file).rsplit('.', 1)[0]
    channels, metas = filter_events(in_pattern)
    logging.debug(repr(metas))
    ch = 0

    for chan in channels:
        instruments = filter_instruments(channels[chan])
        cpt = 0
        for instrument in instruments:
            fname = os.path.join(output_dir, "%s_%s-%s.mid" % (base_name, ch, cpt))
            out_pattern = MidiFile(ticks_per_beat=in_pattern.ticks_per_beat, charset=in_pattern.charset,
                                   type=in_pattern.type)
            out_pattern.tracks.append(instrument)

            cpt += 1
            write_midi_file(fname, out_pattern)
        ch += 1


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except AssertionError as err:
        usage(msg=str(err))
