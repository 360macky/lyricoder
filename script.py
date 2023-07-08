import requests
import argparse
import json
import pysrt
import os

# Set up command line argument handling
parser = argparse.ArgumentParser(description='Convert song to lyrics with timestamps.')
parser.add_argument('--input', required=True, help='Input .mp3 file path.')
parser.add_argument('--name', required=True, help='Song name.')
parser.add_argument('--output', required=True, help='Output .json file path.')
args = parser.parse_args()

def main():
    try:
        # Define Whisper ASR API URL
        api_url = "https://api.openai.com/v1/audio/transcriptions"
        
        # Send POST request to Whisper API to transcribe song
        with open(args.input, 'rb') as audio_file:
            response = requests.post(
                api_url, 
                headers={"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}, 
                files={'file': audio_file},
                data={'model': 'whisper-1', 'response_format': 'srt'}
            )

        # If the request was successful, parse the response
        if response.status_code == 200:
            lyrics_srt = response.text
            lyrics_json = srt_to_json(lyrics_srt, args.name)
            
            # Export the lyrics in json format
            with open(args.output, 'w') as outfile:
                json.dump(lyrics_json, outfile)
            
            print(f"Lyrics exported to {args.output}")
        else:
            print(f"Failed to transcribe song: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def srt_to_json(srt_content, song_name):
    # Load the SRT file content using pysrt
    subs = pysrt.from_string(srt_content)

    # Prepare list to store all subtitle blocks
    subs_json = []

    # Iterate over all subtitle blocks
    for idx, sub in enumerate(subs):
        # Prepare individual subtitle block
        sub_json = {
            "id": idx + 1,
            "start_time": str(sub.start),
            "end_time": str(sub.end),
            "text": sub.text
        }
        # Append subtitle block to list
        subs_json.append(sub_json)

    # Combine all blocks in a json object
    lyrics_json = {song_name: subs_json}
    
    return lyrics_json

if __name__ == "__main__":
    main()
