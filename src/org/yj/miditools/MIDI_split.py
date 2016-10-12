#
# Separate MIDI channels from a MIDI FILE
#

from mido import MidiFile, MetaMessage, MidiTrack, Message
import logging
import os


def write_midi_file(filename, pattern):
    logging.debug(repr(pattern))
    if len(pattern.tracks[0]) > 0:
        # TODO: reinclude all META MESSAGES BEFORE SAVING
        logging.info("Generating output file: %s" % filename)
        pattern.save(filename)


def filter_events(pattern):
    # instruments = []
    channels = {}
    metas = []
    current_time = 0.
    for message in pattern:
        # curr_pattern = MidiFile(type=pattern.type, ticks_per_beat=pattern.ticks_per_beat)
        # curr_pattern.tracks.append(message)
        current_time += int(message.time * 960)

        # print("[%s] Message: %s " % (current_time, message))

        if isinstance(message, MetaMessage):
            if message.type != 'text':
                metas.append((message, current_time))

        elif message.type == 'note_on' or message.type == 'note_off' or message.type == 'program_change':
            chan = 'c' + str(message.channel)
            if chan not in channels:
                channels[chan] = []
            channels[chan].append({'message': message, 'abs_time': current_time})

        else:
            logging.error("Caught unexpected MIDI message: " % repr(message))

    return channels, metas


def filter_instruments(channel):
    instruments = []
    current_instrument = 0
    track = MidiTrack()
    instruments.append(track)
    current_pgm_time = {current_instrument: 0}
    for event in channel:
        msg = event['message']
        # print(repr(event))
        if msg.type == 'program_change':
            track = MidiTrack()
            instruments.append(track)
            current_instrument = msg.program
            if current_instrument not in current_pgm_time:
                current_pgm_time[current_instrument] = 0
                track.append(Message('program_change', program=current_instrument, time=0))
            rel_time = event['abs_time'] - current_pgm_time[current_instrument]

        else:
            rel_time = int(event['abs_time'] - current_pgm_time[current_instrument])
            # Tous les fichiers ne vont utiliser que le canal 0
            track.append(Message(msg.type, channel=msg.channel, note=msg.note, velocity=msg.velocity, time=rel_time))
        current_pgm_time[current_instrument] = event['abs_time']
    return instruments


def read_midi_file(filename):
    pattern = MidiFile(filename)
    logging.debug(repr(pattern))
    return pattern


def main():
    logging.basicConfig(filename='MIDI_split.log', level=logging.DEBUG)

    # TODO replace fixed test dir and file names with params
    in_pattern = read_midi_file(os.path.join(os.environ.get('HOME'), "workspace/MIDI_Tools/resources/20150902.mid"))
    channels, metas = filter_events(in_pattern)

    # instruments = []

    ch = 0

    for chan in channels:
        instruments = filter_instruments(channels[chan])
        cpt = 0
        for instrument in instruments:
            os.path.join(os.environ.get('HOME'), "workspace/MIDI_Tools/resources/20150902.mid")
            fname = os.path.join(os.environ.get('HOME'),
                                 "workspace/MIDI_Tools/resources/20150902_%s-%s.mid" % (ch, cpt))
            out_pattern = MidiFile(ticks_per_beat=in_pattern.ticks_per_beat, charset=in_pattern.charset,
                                   type=in_pattern.type)
            out_pattern.tracks.append(instrument)

            cpt += 1
            write_midi_file(fname, out_pattern)
        ch += 1


if __name__ == '__main__':
    main()
