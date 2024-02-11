import sys
import pyphen

dic = pyphen.Pyphen(lang='en_US')

def process_line(line):
    # Split the line at the first occurrence of a number followed by a space to preserve lyrics spacing
    colon, time, length, note, lyrics = line.split(' ', 4)
    lyrics = lyrics.split('\n', 1)[0]
    length = int(length)
    
    # Prepare for syllable processing
    syllable_lengths = []  # To store lengths for each syllable
    syllables_with_space = []  # To store syllables with leading space if needed
    
    if lyrics:
        words = lyrics.strip().split(' ')
        if lyrics[0] == ' ':
            words[0] = ' ' + words[0]
        words = [words[0]] + [' ' + word for word in words[1:]]
        total_syllables = sum([len(dic.inserted(word).split('-')) for word in words])
        syllable_length = length / max(1, total_syllables)
        for word in words:
            split_syllables = dic.inserted(word).split('-')
            if word[0] == ' ':
                split_syllables = dic.inserted(word[1:]).split('-')
                split_syllables[0] = ' ' + split_syllables[0]
            for syllable in split_syllables:
                syllables_with_space.append(syllable)
                syllable_lengths.append(syllable_length)
    
    # Construct new lines
    new_lines = []
    current_time = int(time)
    for i, syllable in enumerate(syllables_with_space):
        rounded_time = int(round(current_time, 0))
        syllable_time = int(syllable_lengths[i]) if i < len(syllable_lengths) - 1 else length - sum([int(s) for s in syllable_lengths[:-1]])
        if syllable.strip() == lyrics.strip():
            syllable = lyrics
        new_line = f": {rounded_time} {syllable_time} {note} {syllable}"
        new_lines.append(new_line)
        current_time += syllable_lengths[i]
    
    return new_lines



# Read lines from the file specified in argv[1]
if len(sys.argv) > 1:
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith(":"):
                for new_line in process_line(line):
                    print(new_line)
            else:
                print(line, end='')
else:
    print("No file provided")
    sys.exit(1)
