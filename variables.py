class Variables:
    # hold current selected options
    octave = 0
    accidental = 1
    note_length = 4

    # score playback and setup variables
    time_sig = "N"
    key_sig = "N"
    tempo = 0

    # hold current measure length to account for when to add measure line
    current_measure_length = 0.0

    # check if score came from file, if so load file_score on creation
    file_setup = False
    file_score = ""

    @staticmethod
    def get_measure_length():
        # cut time is a weird length to calculate, just hardcode it to 1
        if Variables.time_sig == "Cut":
            return 1.0

        # calculate the measure length based on beats divided by value
        # example: 4/4 becomes 1 (1 whole note long), 3/4 becomes .75 (half note plus whole note)
        time_array = Variables.time_sig.split("/")
        beats = float(time_array[0])
        value = float(time_array[1])
        return beats / value
