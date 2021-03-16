flats = {"C": "B", "D": "CS", "E": "DS", "F": "E", "G": "FS", "A": "GS", "B": "AS"}

sharps = {"C": "CS", "D": "DS", "E": "F", "F": "FS", "G": "GS", "A": "AS", "B": "C"}

naturals = ["A", "B", "C", "D", "E", "F", "G", "R"]

rests = ["9", ":", ";", "<"]

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

    @staticmethod
    def get_note_length(note):
        length = 0

        if note == "9" or 64 <= ord(note) <= 79:
            length = 8
        elif note == ":" or 80 <= ord(note) <= 94:
            length = 4
        elif note == ";" or 96 <= ord(note) <= 111:
            length = 2
        elif note == "<" or 112 <= ord(note) <= 126:
            length = 1

        return length

    @staticmethod
    def replaceable(note):
        if 64 <= ord(note) <= 126 or note in rests:
            return True
        return False

    @staticmethod
    def breakable(rest):
        return 58 <= ord(rest) <= 60
