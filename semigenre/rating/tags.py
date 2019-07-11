"""Tags for track attributes."""


BRASS = {
    'horns'
}


HARMONIES = {
    'single-backup',
    'multipart-harmony',
    'choir'
}


KEYBOARD = {
    'rhodes-organ',
    'hammond-organ',
    'electric-keyboard',
    'grand-piano',
    'synth'
}


PERCUSSION = {
    'snaps',
    'claps',
    'cymbals',
    'snare',
    'drum-fills',
    'shaker',
    'drum-pad'
}


STRINGS = {
    'electric-guitar',
    'acoustic-guitar',
    'electric-bass',
    'banjo',
    'violin',
    'string-section',
    'pedal-steel'
}


THEORY = {
    'maj7',
    'diminished',
    'suspended',
    'min7',
    'dom7',
    'accelerando'
}


VOCALS = {
    'female',
    'male'
}


ALL = BRASS | HARMONIES | KEYBOARD | PERCUSSION | STRINGS | THEORY | VOCALS

TAG_GROUPS = {
    'brass': BRASS,
    'harmonies': HARMONIES,
    'keyboard': KEYBOARD,
    'percussion': PERCUSSION,
    'strings': STRINGS,
    'theory': THEORY,
    'vocals': VOCALS
}
