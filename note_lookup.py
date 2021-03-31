naturals = ["A", "B", "C", "D", "E", "F", "G", "R"]

rests = ["9", ":", ";", "<"]


class LookupNote:
    # key signature lookup table, used when parsing input for playback
    key_sig = {
        "C": {},
        "Db": {"B": 0, "E": 0, "A": 0, "D": 0, "G": 0},
        "D": {"F": 2, "C": 2},
        "Eb": {"B": 0, "E": 0, "A": 0},
        "E": {"F": 2, "C": 2, "G": 2, "D": 0},
        "F": {"B": 0},
        "Gb": {"B": 0, "E": 0, "A": 0, "D": 0, "G": 0, "C": 0},
        "G": {"F": 2},
        "Ab": {"B": 0, "E": 0, "A": 0, "D": 0},
        "A": {"F": 2, "C": 2, "G": 2},
        "Bb": {"B": 0, "E": 0},
        "B": {"F": 2, "C": 2, "G": 2, "D": 0, "A": 2}
    }

    @staticmethod
    def get_note(note, octave, length, accidental, key_sig):
        octave_adjust = octave * 7
        note_string = ""

        # check if a rest, then return symbol from rest lookup table (formula cannot be made for these)
        if note.upper() == "R":
            if length == 8:
                note_string = rests[0]
            elif length == 4:
                note_string = rests[1]
            elif length == 2:
                note_string = rests[2]
            elif length == 1:
                note_string = rests[3]
        else:
            # if not a rest, use the ascii table and the octave adjuster to grab the note symbol from the
            # segment of the table that deals with that note length

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

            # check for accidentals, then append a sign to the beginning depending if it exists
            # use another ascii table offset for the correct area to calculate what symbol to grab
            if accidental == 0:
                flat = 224 + ((ord(note) - 65) + octave_adjust)
                note_string = chr(flat) + note_string
            elif accidental == 2:
                sharp = 208 + ((ord(note) - 65) + octave_adjust)
                note_string = chr(sharp) + note_string
            elif accidental == 3 and note in LookupNote.key_sig[key_sig]:
                natural = 240 + ((ord(note) - 65) + octave_adjust)
                note_string = chr(natural) + note_string

        return note_string + "="

    @staticmethod
    def convert_to_rest(note):
        char = ord(note)

        # check sections of ascii table that deals with that specific note length symbol
        if 64 <= char <= 79:
            return "9"
        elif 80 <= char <= 94:
            return ":"
        elif 96 <= char <= 111:
            return ";"
        elif 112 <= char <= 126:
            return "<"
        elif char == 32:
            return "="  # default space if it messes up somehow

        return ""

    @staticmethod
    def get_rest(length):
        rest = ""

        # simply grab rest from note length
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

        # check against rests and specific sections of ascii table to see what length the note sits in
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
        # check if the string is a rest or in the notes section of the ascii table to check if it can be replaced with
        # a rest or another note
        if 64 <= ord(note) <= 126 or note in rests:
            return True
        return False

    @staticmethod
    def breakable(rest):
        # check if it is a large rest/note that can be split in half
        return 58 <= ord(rest) <= 60 or 80 <= ord(rest) <= 126
