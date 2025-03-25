# Dialogue Audio Generator CLI

## Overview

The **Dialogue Audio Generator CLI** is a Python-based tool designed to automatically generate audio files from dialogue scripts provided in JSON format. It leverages the **Kokoro** library to produce high-quality audio outputs, organized efficiently into directories for easy management.

## Features

- **Automatic Audio Generation:** Converts dialogue text from JSON files into audio.
- **Structured Output:** Automatically creates directories for each JSON dialogue file.
- **Customizable Characters:** Easily configure voices, speed, and character details.
- **Error Handling and Logging:** Robust logging system to quickly identify and resolve issues.

## Requirements

- Python >=3.12,<3.13
- Dependencies installed via Poetry:
  - `soundfile`
  - `kokoro`
  - `torch`, `torchaudio`, `torchvision` (PyTorch with CUDA support)
  - `transformers`

## Installation

Clone the repository and install dependencies:

```bash
git clone <your-repository-url>
cd mrb_audio_generator_cli
poetry install
```

## Usage

Place your JSON dialogue files in the root directory of the project. Files must follow the naming pattern `Dialogues*.json`:

Example structure:

```json
[
  {"id": "TEST-NARRATOR-001", "text": "Hello, welcome to the audio generator!", "speed": 0.7}
]
```

Run the script:

```bash
poetry run python mrb_audio_generator_cli/app.py
```

Generated audio files will be placed in separate directories named after each JSON file processed.

## Configuring Characters

Modify or add characters by editing the `self.characters` list in the script:

```python
self.characters = [
    {"id": "TEST-NARRATOR-001", "codename": "Operator", "name": "Lewis Carr", "voice": "bf_alice", "speed": 1.0}
]
```

- **id:** Matches dialogue entries to character configuration.
- **voice:** Sets the Kokoro voice.
- **speed:** Adjusts speech rate.

## Logging and Troubleshooting

The script outputs detailed logging information to the console, indicating successes, warnings, and errors. Logs include timestamps, log levels, and clear descriptions of encountered issues.

## License

This project is licensed under the MIT License.

## Author

- **mrb-sage** - [GitHub](https://github.com/mrb-sage)

---

Feel free to raise issues or contribute enhancements!

