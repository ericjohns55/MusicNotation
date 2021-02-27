import note_lookup


class Note:
    def __init__(self, name, octave, accidental):
        self.name = name
        self.octave = octave
        self.accidental = accidental

        self.normalize()

    def normalize(self):
        if self.accidental == 0:
            if self.name == "C":
                self.name = "B"
                self.accidental = 1
                self.octave -= 1
        elif self.accidental == 2:
            if self.name == "B":
                self.name = "C"
                self.accidental = 1
                self.octave += 1

    def get_name(self):
        return self.name

    def get_octave(self):
        return self.octave

    def get_accidental(self):
        return self.accidental

    def check_sound_range(self):
        if not 3 <= self.octave <= 6:
            return False

        char = ord(self.name.lower())

        if self.octave == 3 and 99 <= char <= 101:
            return False
        elif self.octave == 6 and not 99 <= char <= 102:
            return False
        elif self.octave == 6 and self.name == "F" and self.accidental == 2:
            return False
        elif self.octave == 3 and self.name == "F" and self.accidental == 0:
            return False

        return True

    def get_sound_file(self):
        if self.check_sound_range():
            note_file = ""

            if self.accidental == 0:
                note_file = note_lookup.flats[self.name]
            elif self.accidental == 1:
                note_file = self.name
            else:
                note_file = note_lookup.sharps[self.name]

            note_file += str(self.octave)

            return note_file
        else:
            return "NONE"
