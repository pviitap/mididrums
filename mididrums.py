"""
Start zynaddsubfx:
zynaddsubfx --output alsa --load-instrument='/usr/share/zynaddsubfs/banks/olivers-100/0032-Drum Kit.xiz' --no-gui
"""

import time
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(1)
else:
    midiout.open_virtual_port("Virtual output")

def play_notes(notes):
    for note in notes:
        midiout.send_message([0x90, note, 112])
    time.sleep(0.3)
    for note in notes:
        midiout.send_message([0x90, note, 0])

tom=36
hat=60
snare=57

while True:
    play_notes([tom,hat])
    play_notes([hat])

    play_notes([snare, hat])
    play_notes([tom, hat])

    play_notes([hat])
    play_notes([tom, hat])

    play_notes([hat])
    play_notes([tom,hat])

del midiout
