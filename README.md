# Automated USDX Song Generator

## Overview
This project aims to automate the creation of songs for UltraStar Deluxe (USDX), a popular karaoke game. The ultimate goal is to streamline the process of generating playable USDX song files from any YouTube video, handling everything from downloading the audio and video to matching lyrics with notes.

## Current Process
1. **Get the MP3**: Obtain the MP3 file of your song, e.g., from YouTube.
2. **Vocal Track Isolation**: Use [VocalRemover.org](https://vocalremover.org/) to extract a vocals-only track from your MP3 file.
3. **Export Note Data**: Process the isolated vocal track with [Tony](https://code.soundsoftware.ac.uk/projects/tony/files) to export note data.
4. **Lyrics (Optional)**: If you have the lyrics, save them into a text file.
5. **Generate Notes**: Run `gennotes.py` with the note data (and optionally the lyrics file) to generate the USDX song file.
6. **Load Song in Ultrastar**: Check whether the line breaks match, if not, fix the lyrics text file and regenerate, if necessary, merge lines, or add empty lines, that's less work than fixing all the text in the editor
7. **Fix the Lyrics in Ultrastar**: Make sure the lyrics are on time, this part is the largest amount of manual work left (around 10-20 minutes). If there's only a single note with multiple words or syllables that are not split up - no worries, just make sure things are in the right place.
8. **Fix Syllable Breaks**: Use `splitnotes.py` to split up notes that contain multiple syllables or words
9. **Manual Adjustments**: Open the generated file in UltraStar and check/fix all remaining issues with notes, timings, and lyrics

## Future Vision
The project aspires to fully automate the USDX song creation process, including downloading resources and fine-tuning song files for immediate use in UltraStar Deluxe.
For most people this approach should be faster than alternatives to song text file creation.

## Development TODOs
[ ] Integrate with a Youtube Downloader Script
[ ] Script the call to vocalremover.org (or replace it with a local solution)
[ ] Automate Lyrics fetching
[ ] Better Tony integration (e.g. without GUI just input -> output )
[ ] Detect when lyrics and notes don't match -> show warning and fix without using Ultrastar

## Usage
```
# Generate a USDX song text file
python3 gennotes.py <path_to_file_from_tony> [lyrics_file] > <where_to_store>
# Split up notes with multiple syllables or words
python3 splitnotes.py <path_to_song_file> > <where_to_store>
```

## Contribution
Contributions are welcome to advance towards the fully automated vision, including improving note generation accuracy and lyrics matching.

