from note_lookup import LookupNote
from variables import Variables
import winsound

class Note:
    natural_frequencies = {
        "A0": 220, "B0": 247, "C0": 262, "D0": 294, "E0": 330, "F0": 349, "G0": 392,
        "A1": 440, "B1": 494, "C1": 523, "D1": 587, "E1": 659, "F1": 698, "G1": 784,
        "A2": 880
    }

    sharp_frequencies = {
        "A0": 233, "B0": 262, "C0": 277, "D0": 311, "E0": 349, "F0": 370, "G0": 415,
        "A1": 466, "B1": 523, "C1": 554, "D1": 622, "E1": 698, "F1": 740, "G1": 831,
        "A2": 932
    }

    flat_frequencies = {
        "A0": 208, "B0": 233, "C0": 247, "D0": 277, "E0": 311, "F0": 330, "G0": 370,
        "A1": 415, "B1": 466, "C1": 494, "D1": 554, "E1": 622, "F1": 659, "G1": 740,
        "A2": 831
    }

    def __init__(self, note_excerpt):
        self.note_excerpt = note_excerpt
        self.octave = 0

        self.duration = 500
        self.frequency = 440

        self.note_symbol = note_excerpt if len(note_excerpt) == 1 else note_excerpt[-1]
        self.note_name = self.get_note_name(self.note_symbol)
        self.length = LookupNote.get_note_length(self.note_symbol)

        if self.octave < 0:
            self.note_name = "R"

        if len(note_excerpt) == 1:
            self.accidental = 1

            if self.note_name in LookupNote.key_sig[Variables.key_sig]:
                self.accidental = LookupNote.key_sig[Variables.key_sig][self.note_name]
        elif len(note_excerpt) == 2:
            accidental_symbol = note_excerpt[0]

            if 208 <= ord(accidental_symbol) <= 222:
                self.accidental = 2
            elif 224 <= ord(accidental_symbol) <= 238:
                self.accidental = 0
            elif 240 <= ord(accidental_symbol) <= 254:
                self.accidental = 1

        self.prepare_for_playback()

    def prepare_for_playback(self):
        note_and_octave = self.note_name + str(self.octave)

        if "R" in note_and_octave:
            frequency = 37
        else:
            if self.accidental == 0:
                frequency = self.flat_frequencies[note_and_octave]
            elif self.accidental == 1:
                frequency = self.natural_frequencies[note_and_octave]
            else:
                frequency = self.sharp_frequencies[note_and_octave]

        beat_time = 60000 / Variables.tempo

        self.duration = int(beat_time / (self.length / 4))
        self.frequency = frequency

    def play(self):
        winsound.Beep(self.frequency, self.duration)

    def get_note_name(self, note_excerpt):
        note_length = LookupNote.get_note_length(note_excerpt)

        if note_length == 8:
            octave_adjust = int((ord(note_excerpt) - 64) / 7)
            note_name = ord(note_excerpt) + 1 - (7 * octave_adjust)
        elif note_length == 4:
            octave_adjust = int((ord(note_excerpt) - 80) / 7)
            note_name = -16 + ord(note_excerpt) + 1 - (7 * octave_adjust)
        elif note_length == 2:
            octave_adjust = int((ord(note_excerpt) - 96) / 7)
            note_name = -32 + ord(note_excerpt) + 1 - (7 * octave_adjust)
        elif note_length == 1:
            octave_adjust = int((ord(note_excerpt) - 112) / 7)
            note_name = -48 + ord(note_excerpt) + 1 - (7 * octave_adjust)
        else:
            octave_adjust = 0
            note_name = 81

        self.octave = octave_adjust

        #ord(note_excerpt) + 1 - octave_adjust

        return chr(note_name)

    def get_string(self):
        return self.note_excerpt
