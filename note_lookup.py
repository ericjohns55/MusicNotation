flats = {
    "C": "B",
    "D": "CS",
    "E": "DS",
    "F": "E",
    "G": "FS",
    "A": "GS",
    "B": "AS"
}

sharps = {
    "C": "CS",
    "D": "DS",
    "E": "F",
    "F": "FS",
    "G": "GS",
    "A": "AS",
    "B": "C",
}

note_dictionary = {
    "16": {
        "Ab3": "à=",
        "A3": "=",
        "AS3": "Ð=",
        "Bb3": "á=",
        "B3": "=",
        "BS3": "Ñ=",
        "Cb4": "â=",
        "C4": "=",
        "CS4": "Ò=",
        "Db4": "ã=",
        "D4": "=",
        "DS4": "Ó=",
        "Eb4": "ä=",
        "E4": "=",
        "ES4": "Ô=",
        "Fb4": "å=",
        "F4": "=",
        "FS4": "Õ=",
        "Gb4": "æ=",
        "G4": "=",
        "GS4": "Ö=",
        "Ab4": "ç=",
        "A4": "=",
        "AS4": "×=",
        "Bb4": "è=",
        "B4": "=",
        "BS4": "Ø=",
        "Cb5": "é=",
        "C5": "=",
        "CS5": "Ù=",
        "Db5": "ê=",
        "D5": "=",
        "DS5": "Ú=",
        "Eb5": "ë=",
        "E5": "=",
        "ES5": "Û=",
        "Fb5": "ì=",
        "F5": "=",
        "FS5": "Ü=",
        "Gb5": "í=",
        "G5": "=",
        "GS5": "Ý=",
        "Ab5": "î=",
        "A5": "=",
        "AS5": "Þ="
    },

    "8": {
        "Ab3": "à@=",
        "A3": "@=",
        "AS3": "Ð@=",
        "Bb3": "áA=",
        "B3": "A=",
        "BS3": "ÑA=",
        "Cb4": "âB=",
        "C4": "B=",
        "CS4": "ÒB=",
        "Db4": "ãC=",
        "D4": "C=",
        "DS4": "ÓC=",
        "Eb4": "äD=",
        "E4": "D=",
        "ES4": "ÔD=",
        "Fb4": "åE=",
        "F4": "E=",
        "FS4": "ÕE=",
        "Gb4": "æF=",
        "G4": "F=",
        "GS4": "ÖF=",
        "Ab4": "çG=",
        "A4": "G=",
        "AS4": "×G=",
        "Bb4": "èH=",
        "B4": "H=",
        "BS4": "ØH=",
        "Cb5": "éI=",
        "C5": "I=",
        "CS5": "ÙI=",
        "Db5": "êJ=",
        "D5": "J=",
        "DS5": "ÚJ=",
        "Eb5": "ëK=",
        "E5": "K=",
        "ES5": "ÛK=",
        "Fb5": "ìL=",
        "F5": "L=",
        "FS5": "ÜL=",
        "Gb5": "íM=",
        "G5": "M=",
        "GS5": "ÝM=",
        "Ab5": "îN=",
        "A5": "N=",
        "AS5": "ÞN="
    },

    "4": {
        "Ab3": "àP=",
        "A3": "P=",
        "AS3": "ÐP=",
        "Bb3": "áQ=",
        "B3": "Q=",
        "BS3": "ÑQ=",
        "Cb4": "âR=",
        "C4": "R=",
        "CS4": "ÒR=",
        "Db4": "ãS=",
        "D4": "S=",
        "DS4": "ÓS=",
        "Eb4": "äT=",
        "E4": "T=",
        "ES4": "ÔT=",
        "Fb4": "åU=",
        "F4": "U=",
        "FS4": "ÕU=",
        "Gb4": "æV=",
        "G4": "V=",
        "GS4": "ÖV=",
        "Ab4": "çW=",
        "A4": "W=",
        "AS4": "×W=",
        "Bb4": "èX=",
        "B4": "X=",
        "BS4": "ØX=",
        "Cb5": "éY=",
        "C5": "Y=",
        "CS5": "ÙY=",
        "Db5": "êZ=",
        "D5": "Z=",
        "DS5": "ÚZ=",
        "Eb5": "ë[=",
        "E5": "[=",
        "ES5": "Û[=",
        "Fb5": "ì\=",
        "F5": "\=",
        "FS5": "Ü\=",
        "Gb5": "í]=",
        "G5": "]=",
        "GS5": "Ý]=",
        "Ab5": "î^=",
        "A5": "^=",
        "AS5": "Þ^="
    },

    "2": {
        "Ab3": "à`=",
        "A3": "`=",
        "AS3": "Ð`=",
        "Bb3": "áa=",
        "B3": "a=",
        "BS3": "Ña=",
        "Cb4": "âb=",
        "C4": "b=",
        "CS4": "Òb=",
        "Db4": "ãc=",
        "D4": "c=",
        "DS4": "Óc=",
        "Eb4": "äd=",
        "E4": "d=",
        "ES4": "Ôd=",
        "Fb4": "åe=",
        "F4": "e=",
        "FS4": "Õe=",
        "Gb4": "æf=",
        "G4": "f=",
        "GS4": "Öf=",
        "Ab4": "çg=",
        "A4": "g=",
        "AS4": "×g=",
        "Bb4": "èh=",
        "B4": "h=",
        "BS4": "Øh=",
        "Cb5": "éi=",
        "C5": "i=",
        "CS5": "Ùi=",
        "Db5": "êj=",
        "D5": "j=",
        "DS5": "Új=",
        "Eb5": "ëk=",
        "E5": "k=",
        "ES5": "Ûk=",
        "Fb5": "ìl=",
        "F5": "l=",
        "FS5": "Ül=",
        "Gb5": "ím=",
        "G5": "m=",
        "GS5": "Ým=",
        "Ab5": "în=",
        "A5": "n=",
        "AS5": "Þn="
    },

    "1": {
        "Ab3": "àp=",
        "A3": "p=",
        "AS3": "Ðp=",
        "Bb3": "áq=",
        "B3": "q=",
        "BS3": "Ñq=",
        "Cb4": "âr=",
        "C4": "r=",
        "CS4": "Òr=",
        "Db4": "ãs=",
        "D4": "s=",
        "DS4": "Ós=",
        "Eb4": "ät=",
        "E4": "t=",
        "ES4": "Ôt=",
        "Fb4": "åu=",
        "F4": "u=",
        "FS4": "Õu=",
        "Gb4": "æv=",
        "G4": "v=",
        "GS4": "Öv=",
        "Ab4": "çw=",
        "A4": "w=",
        "AS4": "×w=",
        "Bb4": "èx=",
        "B4": "x=",
        "BS4": "Øx=",
        "Cb5": "éy=",
        "C5": "y=",
        "CS5": "Ùy=",
        "Db5": "êz=",
        "D5": "z=",
        "DS5": "Úz=",
        "Eb5": "ë{=",
        "E5": "{=",
        "ES5": "Û{=",
        "Fb5": "ì|=",
        "F5": "|=",
        "FS5": "Ü|=",
        "Gb5": "í}=",
        "G5": "}=",
        "GS5": "Ý}=",
        "Ab5": "î~=",
        "A5": "~=",
        "AS5": "Þ~="
    }
}