flats = {"C": "B", "D": "CS", "E": "DS", "F": "E", "G": "FS", "A": "GS", "B": "AS"}

sharps = {"C": "CS", "D": "DS", "E": "F", "F": "FS", "G": "GS", "A": "AS", "B": "C"}

naturals = ["A", "B", "C", "D", "E", "F", "G", "R"]


class LookupNote:
    @staticmethod
    def get_note(note, octave, length, accidental):
        octave_adjust = octave * 7
        note_string = ""

        if length == 8:
            ascii_code = ord(note) - 1 + octave_adjust
            note_string += chr(ascii_code)
        elif length == 4:
            ascii_code = 16 + ord(note) - 1 + octave_adjust
            note_string += chr(ascii_code)
        elif length == 2:
            ascii_code = 32 + ord(note) - 1 + octave_adjust
            note_string += chr(ascii_code)
        elif length == 1:
            ascii_code = 48 + ord(note) - 1 + octave_adjust
            note_string += chr(ascii_code)

        if accidental == 0:
            flat = 224 + ((ord(note) - 65) + octave_adjust)
            note_string = chr(flat) + note_string
        elif accidental == 2:
            sharp = 208 + ((ord(note) - 65) + octave_adjust)
            note_string = chr(sharp) + note_string

        return note_string + "="

    @staticmethod
    def convert_to_rest(note):
        char = ord(note)

        if 64 <= char <= 79:
            return "9"
        elif 80 <= char <= 94:
            return ":"
        elif 96 <= char <= 111:
            return ";"
        elif 112 <= char <= 126:
            return "<"
        elif char == 32:
            return "="

        return ""

    @staticmethod
    def get_rest(length):
        rest = ""

        if length == 8:
            rest = "9"
        elif length == 4:
            rest = ":"
        elif length == 2:
            rest = ";"
        elif length == 1:
            rest = "<"

        return rest + "="
