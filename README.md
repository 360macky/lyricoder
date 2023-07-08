<p align="center">
  <img
    src=".github/logo.png"
    align="center"
    width="100"
    alt="Lyricoder"
    title="Lyricoder"
  />
  <h1 align="center">Lyricoder</h1>
</p>

<p align="center">
  Lyricoder is a script that generates a JSON file of song lyrics with timestamps.
</p>

## 🚀 Concept

Lyricoder is a script that generates a JSON file of song lyrics with timestamps. The script takes in a .mp3 file and the name of the song and outputs a JSON file with the lyrics and timestamps. The script uses [OpenAI Whisper](https://openai.com/research/whisper) to transcribe the song.

This script is useful for a music player app that could display the lyrics of the song as it is playing.

## 🌈 Installation

Clone the repository to your local machine and navigate into the directory:

```bash
git clone https://github.com/360macky/lyricoder.git
cd lyricoder
```

You will need to make the script executable and move it to a directory in your PATH. You can do this by running the following commands:

```bash
chmod +x lyricoder.py
sudo mv lyricoder.py /usr/local/bin/lyricoder
```

The `chmod` command makes the file executable and the `mv` command moves the file. `/usr/local/bin` is a common place to put user programs on macOS, and should be in your PATH.

Now, you should be able to run the script from anywhere using the `lyricoder` command:

```bash
lyricoder --input ./song.mp3 --name "Song Name" --output ./song.json
```

## 🪐 Usage

```bash
python lyricoder.py --input ./song.mp3 --name "Song Name" --output ./song.json
```

## 🛠 Core Development

The script takes in three command-line arguments: `--input` (the path to the .mp3 file), `--name` (the name of the song), and `--output` (the path to the output .json file).

The song is transcribed using OpenAI Whisper through a POST request to the Whisper API. The ASR system returns the transcribed text in SRT (SubRip Subtitle) format along with timestamps. The response is then parsed and converted into a JSON format.

The final output is a JSON file which includes each line of lyrics along with its start and end times. The JSON is structured as follows:

```json
{
  "Song Name": [
    {
      "id": 1,
      "start_time": "00:00:03",
      "end_time": "00:00:04",
      "text": "First line of lyrics"
    },
    {
      "id": 2,
      "start_time": "00:00:05",
      "end_time": "00:00:09",
      "text": "Second line of lyrics"
    },
    ...
  ]
}
```

This script includes error handling for failed transcription attempts and unexpected errors.

## 🤲 Contributing

Lyricoder is an open source project.

If you want to be the author of a new feature, fix a bug or contribute with something new.

Fork the repository and make changes as you like. [Pull requests](https://github.com/360macky/lyricoder/pulls) are warmly welcome.

## 📃 License

Distributed under the MIT License.
See [`LICENSE`](./LICENSE) for more information.
