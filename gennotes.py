import sys
import json
import freq_note_converter
import pyphen

dic = pyphen.Pyphen(lang='en_US')

# Check if the correct number of arguments are passed
if len(sys.argv) < 2:
    print("Usage: gennotes.py <path_to_frequency_file> [lyrics_file]")
    sys.exit(1)

# File paths from command line arguments
frequency_file_path = sys.argv[1]
lyrics_file = sys.argv[2] if len(sys.argv) == 3 else None

def read_and_syllabify(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    processed_lines = []
    for line in lines:
        # Split the line into words, preserve line breaks
        words = line.strip().split()
        processed_words = [dic.inserted(word).split('-') for word in words]
        processed_words = [(' ' + sublist[0] if i == 0 else sublist[i]) for sublist in processed_words for i in range(len(sublist))]
        processed_lines.append(processed_words)
    return processed_lines

# Load the frequency data from the 'frequency.txt' file
frequency_data = []
with open(frequency_file_path, 'r') as file:
    for line in file:
         parts = line.strip().split('\t')
         if len(parts) == 3:
             time, frequency, length = parts
             frequency_data.append((float(time), float(frequency), float(length)))

# Update the data with the adjusted positions
updated_data = []
for time, frequency, length in frequency_data:
    note = freq_note_converter.from_freq(frequency).note_index-40 if frequency != 0 else None
    time = round(time * 20)
    length = round(length * 20)
    updated_data.append((time, length, note))


preview_start_beats = 0
preview_start_seconds = 0
gap_ms = 0

merged_data = []
if updated_data:
    # Initialize the first entry as the current note to compare with
    current_time, current_length, current_note = updated_data[0]

    first_time = current_time
    preview_start_beats = first_time
    preview_start_seconds = preview_start_beats / 20  # Convert the first timestamp to seconds
    gap_ms = preview_start_seconds * 1000  # Convert seconds to milliseconds

    for i in range(1, len(updated_data)):
        next_time, next_length, next_note = updated_data[i]
        
        # Check if the current note can be merged with the next one
        if current_note == next_note and (current_time + current_length) == next_time:
            # Extend the length of the current note
            current_length += next_length
        else:
            # Add the current note to the merged list before moving on
            merged_data.append((current_time - first_time, current_length, current_note))
            # Update the current note to the next one
            current_time, current_length, current_note = next_time, next_length, next_note
    
    # Don't forget to add the last note to the merged list
    merged_data.append((current_time - first_time, current_length, current_note))

base_filename = frequency_file_path.rsplit('.', 1)[0]

mp3_filename = base_filename + '.mp3'
cover_filename = base_filename + '.jpg'
video_filename = base_filename + '.mp4'

if lyrics_file != None:
    syllabified_lyrics = read_and_syllabify(lyrics_file)

# Print header lines
print(f"#TITLE:Title")
print(f"#ARTIST:Artist")
print(f"#LANGUAGE:English")
print(f"#CREATOR:lava")
print(f"#MP3:{mp3_filename}")
print(f"#COVER:{cover_filename}")
print(f"#VIDEO:{video_filename}")
print(f"#PREVIEWSTART:{preview_start_seconds:.3f}")
print(f"#BPM:300")
print(f"#GAP:{int(gap_ms)}")

j = 0
k = 0
for i in range(len(merged_data)):
    time, length, note = merged_data[i]
    if length > 1:
        length -= 1
    if lyrics_file == None:
        syllable = "-"
    elif k < len(syllabified_lyrics[j]):
        syllable = syllabified_lyrics[j][k]
        k += 1
    print(f": {time} {length} {note} {syllable}")
    # Check if this is not the last note and then if the gap to the next note is more than 15
    if i < len(merged_data) - 1:
        next_time = merged_data[i + 1][0]
        if time + length + 15 <= next_time:
            # Print the additional line
            print(f"- {time}")
            j += 1
            k = 0
