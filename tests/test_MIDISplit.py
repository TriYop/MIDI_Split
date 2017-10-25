import getopt

from mido import MidiFile

from miditools import MIDISplit


def test_write_empty_midi_file():
    MIDISplit.write_midi_file("TestOut.mid", MidiFile())
    assert True


def test_write_midi_file():
    output = MidiFile()
    output.add_track(name="test_track")
    output.ticks_per_beat = 724
    output.type = 1
    MIDISplit.write_midi_file("TestOut.mid", output)


def test_parse_empty_options():
    argv = []
    optlist, args = optlist, args = getopt.getopt(argv, 'hvi:o:', ["help", "verbose", "input=", 'output='])
    input_file, output_dir = MIDISplit.parse_options(optlist, args)

    assert input_file == None
    assert output_dir == None

def test_parse_verbose_options():
    argv = ["-v"]
    optlist, args = optlist, args = getopt.getopt(argv, 'hvi:o:', ["help", "verbose", "input=", 'output='])
    input_file, output_dir = MIDISplit.parse_options(optlist, args)

    assert input_file == None
    assert output_dir == None

def test_parse_unknown_options():
    argv = ["-i:test.mid -o:test -p --kiwi"]
    optlist, args = optlist, args = getopt.getopt(argv, 'hvi:o:', ["help", "verbose", "input=", 'output='])
    input_file, output_dir = MIDISplit.parse_options(optlist, args)

    assert input_file == None
    assert output_dir == None


def test_parse_valid_options():
    argv = ["-i:test.mid --output=test"]
    optlist, args = optlist, args = getopt.getopt(argv, 'hvi:o:', ["help", "verbose", "input=", 'output='])
    input_file, output_dir = MIDISplit.parse_options(optlist, args)

    assert input_file == None
    assert output_dir == None

