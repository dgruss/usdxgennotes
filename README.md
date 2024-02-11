# Automated USDX Song Generator

## Overview
This project aims to automate the creation of songs for UltraStar Deluxe (USDX), a popular karaoke game. The ultimate goal is to streamline the process of generating playable USDX song files from any YouTube video, handling everything from downloading the audio and video to matching lyrics with notes.

## Current Process
1. **Get the MP3**: Obtain the MP3 file of your song, e.g., from YouTube.
2. **Vocal Track Isolation**: Use [VocalRemover.org](https://vocalremover.org/) to extract a vocals-only track from your MP3 file.
3. **Export Note Data**: Process the isolated vocal track with [Tony](https://code.soundsoftware.ac.uk/projects/tony/files) to export note data.
4. **Lyrics (Optional)**: If you have the lyrics, save them into a text file.
5. **Generate Notes**: Run `gennotes.py` with the note data (and optionally the lyrics file) to generate the USDX song file.
6. **Manual Adjustments**: Open the generated file in UltraStar to fix notes, timings, and lyrics as necessary (it will be necessary!).

## Future Vision
The project aspires to fully automate the USDX song creation process, including downloading resources and fine-tuning song files for immediate use in UltraStar Deluxe.
For most people this approach might already be faster than the other alternatives to song creation.

## Usage
```
python3 gennotes.py <path_to_file_from_tony> [lyrics_file]
```

## Contribution
Contributions are welcome to advance towards the fully automated vision, including improving note generation accuracy and lyrics matching.

