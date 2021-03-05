import font_dictionary


class ScoreSetup:
    def __init__(self, time_sig, key_sig, tempo):
        self.time_sig = time_sig
        self.key_sig = key_sig
        self.tempo = tempo

    def get_setup(self):
        return "&=" + font_dictionary.key_sig_lookup[self.key_sig] + "=" + font_dictionary.time_sig_lookup[self.time_sig] + "=="