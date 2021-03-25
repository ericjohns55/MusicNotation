class Playback:
    note_frequencies = [207.65, 220, 233.08, 246.94, 261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392, 415.3, 440, 466.16, 493.88, 523.25, 554.37, 587.33, 622.25, 659.25, 698.46, 739.99, 783.99, 830.61, 880, 932.33]

    def get_note_frequency(self, note, octave):
        index = (ord(note) - 65) + (7 * octave)
        return self.note_frequencies[index]