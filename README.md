# MusicNotation

# Summary: 

   I will be creating a music notation program where people can write simple melodies for playback on piano. The project will have numerous features such as score playback, rhythms, chords, and dynamics. It will have a built in sound of piano for playback, and will preview note sounds as you input them into the score. The user will be able to pick the tempo, key signature, and time signature they want to write their piece in. The application will have an option to playback the score that the user has written.
    In creating this project, I will be learning python. I will be following online tutorials to get a feel for the language and its syntax, then use this knowledge to create the application and a graphical interface. The project’s interface will have the score visible on the top of the screen, then have buttons on the bottom to add notes and musical markings to the score. The user will be able to combine multiple features to create a small piece of music.
    
# Features

# Major Features:

Interface:

   The application will have a graphical interface where the user can see the scores they wrote and can see buttons with options on what they can do or input.
    
Score (musical):

   The score holds all the user inputted notes and musical markings. This will consist of a staff where the notes are placed on correct lines or spacers. The score will display dynamic markings, the time signature, the key signature, and the tempo.

Note Input:

   The user will be able to type in the note name on their keyboard (A, B, C, D, E, F, or G) to input it into the score. The notes will be displayed on the correct positioning on the staff and follow stem convention rules.
    
Key Signature:

   The user will be able to pick the key signature that the piece they want to write is in. They will have an option between all 12 common key signatures that exist through all music.
    
Time Signature:

   A time signature must be chosen so the program knows how many beats are in a measure and how long each beat is.
    
Tempo:

   The user must declare a tempo which will tell the program how fast to playback the score through.
    
Playback:

   The application will be able to play what the user has written with a piano sound. This will go through the entire score and play every note with the correct rhythm at the correct speed.
    
    
# Stretch Goals:

Chords: 

   Chords will let the users place multiple notes at once onto the score that will play simultaneously during playback. 
    
Dynamics:

   The user will be able to input any dynamic ranging from pianissimo to fortissimo. These dynamics will set the volume level of the playback and tell the user how loud the part they are writing is meant to be played. 

Complex Rhythms:

   Complex rhythms such as triplets or dotted notes can be inputted into the score. This lets the user write more elaborate pieces of music.
    
Persistent Data:

   The application will be able to save and load the user’s data to file so it can be pulled up and edited later.
   
Hardware Input: 

   The user will be able to use a raspberry pi fitted with a PiCap to press physical piano keys on a table and input notes into the score there. 
  
  
# Technologies: 

   The program will be written in Python, which is a new language for me. I will be creating the program in PyCharm and will deploy the program as a graphical application. I will be using the PyDub library, as it allows me to easily play multiple sounds at the same time, and set how long I want them to last. Tkinter will be used to create the graphical interface for the program, as it allows me to easily program an interface and add button listeners.
    
    
# Development Plan: 

Milestone 1:

   In milestone 1, I plan to have the visual interface done. It will consist of the staff rendered onto the application and each button added to the UI.
   
Milestone 2:

   By the second milestone, I will have the ability to add notes to the page finished. This includes having the time signature function implemented so the application knows how many notes can fit into each segment of the score.
    
Milestone 3:

   During the third milestone, I want to have the sound for score playback complete. The application will be able to play all the notes on the score with a piano sound font. This includes having the tempo correct and having the correct key signature function implemented.
    
Final Product:

   While turning in the final product, I need to have the final report done, and need to clean up the application. This includes having the correct notational conventions and making sure note stems go the correct way. This also includes having the notes group together with a bar going across the top if they are a tuplet of the same length.
    
    
# Challenges:

   It is going to be a challenge to learn a new programming language and try to immediately implement a difficult application into it. I have not designed a visual interface for a computer application in a few years, so figuring out how to make it work will be challenging too.
    A difficult part of this application will be rendering the notes onto the staff on the visual side. The stems need to be in the right direction and the notes need to follow proper musical convention with their spacing 
    A significant part of this program is score playback. I will have to figure out how to make sure the rhythms come across evenly and the correct notes are played where they are written. I will also have to make sure that the piece is playing at the right tempo that the user specified and ensure that the notes written are in the correct key signature.
    One of the hardest challenges is going to be placing the notes where the user wants. I need to consider how the stems will come out of the notes and how to place them in the specific part of the measure. Every note duration looks slightly different and I will have to consider how they will fit cleanly on the page with other notes. 

