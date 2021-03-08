class Variables:
    octave = 4
    accidental = 1
    note_length = 8

    time_sig = "N"
    key_sig = "N"
    tempo = 0

    current_measure_length = 0.0

    @staticmethod
    def get_measure_length():
        if Variables.time_sig == "Cut":
            return 1.0

        time_array = Variables.time_sig.split("/")
        beats = float(time_array[0])
        value = float(time_array[1])
        return beats / value