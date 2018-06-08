import sys
import rtmidi

def send_string(string):
    midiout = rtmidi.MidiOut()
    outport = [port[0] for port in enumerate(midiout.get_ports()) if port[1].startswith('reface DX')][0]
    midiout.open_port(outport)

    for i, s in enumerate(string[:10].ljust(10, ' ')):
        midiout.send_message([0xf0, 0x43, 0x10, 0x7f, 0x1c, 0x05, 0x30, 0x00, i, ord(s), 0xf7])
    
    midiout.close_port()

if __name__ == '__main__':
    send_string(sys.argv[1])
