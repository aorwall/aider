import re
from collections import defaultdict

INTERVALS = {
    'M': 2,
    'm': 1,
}

def _get_interval_pattern(pattern):
    pattern = re.sub('[b#]', '', pattern)
    return [INTERVALS[i] for i in pattern]

def _generate_scale(tonic, interval_pattern):
    scale = []
    current_note = tonic
    for interval in interval_pattern:
        scale.append(current_note)
        current_note += interval
    return scale

class Scale:
    def __init__(self, tonic):
        self._flats = False
        self._sharps = False
        self._key_signatures = defaultdict(list)
        self._set_key_signature(tonic)

    def chromatic(self):
        return ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def interval(self, intervals):
        interval_pattern = _get_interval_pattern(intervals)
        if self._flats:
            tonic = intervals[0].lower()
        else:
            tonic = intervals[0].upper()
        return _generate_scale(tonic, interval_pattern)

    def _set_key_signature(self, tonic):
        if tonic == 'c':
            self._flats = True
            self._key_signatures['f'].append('#')
            self._key_signatures['b'].append('#')
            self._key_signatures['e'].append('#')
            self._key_signatures['a'].append('#')
            self._key_signatures['d'].append('#')
            self._key_signatures['g'].append('#')
        elif tonic == 'g':
            self._sharps = True
            self._key_signatures['f'].append('#')
            self._key_signatures['c'].append('#')
            self._key_signatures['g'].append('#')
            self._key_signatures['d'].append('#')
            self._key_signatures['a'].append('#')
            self._key_signatures['e'].append('#')
            self._key_signatures['b'].append('#')
        elif tonic == 'd':
            self._flats = True
            self._key_signatures['f'].append('#')
            self._key_signatures['c'].append('#')
            self._key_signatures['g'].append('#')
            self._key_signatures['d'].append('#')
            self._key_signatures['a'].append('#')
            self._key_signatures['e'].append('#')
            self._key_signatures['b'].append('#')
        elif tonic == 'a':
            self._flats = True
            self._key_signatures['f'].append('#')
            self._key_signatures['c'].append('#')
            self._key_signatures['g'].append('#')
            self._key_signatures['d'].append('#')
            self._key_signatures['a'].append('#')
            self._key_signatures['e'].append('#')
            self._key_signatures['b'].append('#')
        elif tonic == 'e':
            self._flats = True
            self._key_signatures['f'].append('#')
            self._key_signatures['c'].append('#')
            self._key_signatures['g'].append('#')
            self._key_signatures['d'].append('#')
            self._key_signatures['a'].append('#')
            self._key_signatures['e'].append('#')
            self._key_signatures['b'].append('#')
        elif tonic == 'b':
            self._flats = True
            self._key_signatures['f'].append('#')
            self._key_signatures['c'].append('#')
            self._key_signatures['g'].append('#')
            self._key_signatures['d'].append('#')
            self._key_signatures['a'].append('#')
            self._key_signatures['e'].append('#')
            self._key_signatures['b'].append('#')
        else:
