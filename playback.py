from note import Note
from variables import Variables
import winsound

class Playback:
    def __init__(self, text):
        self.score = text

    def parse(self):
        print(len(self.score))

        array = self.score[7:]

        measures = array.split("!")

        for i in range(len(measures)):
            individual_notes = measures[i].split("=")

            for j in range(len(individual_notes)):
                if individual_notes[j] != "" and individual_notes[j] != "\n":
                    note = Note(individual_notes[j])
                    print(note.get_test_string())

    @staticmethod
    def play_tone(note, octave, accidentals):
        if note.upper() == "R":
            return

        note_name = note.upper() + str(octave)

        if accidentals == 0:
            frequency = Note.flat_frequencies[note_name]
        elif accidentals == 1:
            frequency = Note.natural_frequencies[note_name]
        else:
            frequency = Note.sharp_frequencies[note_name]

        winsound.Beep(frequency, 200)
