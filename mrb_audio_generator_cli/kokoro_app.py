import json
import os
import glob
import logging
import soundfile as sf
from kokoro import KPipeline

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DialogueAudioGenerator:
    def __init__(self, lang_code='a'):
        self.pipeline = KPipeline(lang_code=lang_code)
        self.characters = [
            {"id": "TEST-NARRATOR-001", "codename": "Operator", "name": "Lewis Carr", "voice": "bf_alice", "speed": 1.0}
        ]

    def create_directories_and_generate_audio(self, pattern='Dialogues*.json'):
        for filepath in glob.glob(pattern):
            dirname = os.path.splitext(os.path.basename(filepath))[0]
            logging.info(f'Processing file: {filepath}')

            try:
                os.makedirs(dirname, exist_ok=True)
                logging.info(f'Directory created or already exists: {dirname}')

                with open(filepath, 'r', encoding='utf-8') as json_file:
                    dialogues = json.load(json_file)
            except Exception as e:
                logging.error(f'Error reading or creating directory for {filepath}: {e}')
                continue

            for idx, item in enumerate(dialogues, 1):
                matching_chars = [char for char in self.characters if char["id"] == item["id"]]
                if not matching_chars:
                    logging.warning(f'Character ID {item["id"]} not found in characters list.')
                    continue

                char = matching_chars[0]
                self._generate_audio_for_item(dirname, idx, item, char)

    def _generate_audio_for_item(self, dirname, idx, item, char):
        try:
            generator = self.pipeline(
                item["text"],
                voice=char["voice"],
                speed=char["speed"],
                split_pattern=r'\n+'
            )
            for i, (_, _, audio) in enumerate(generator):
                filename = os.path.join(dirname, f'Dialogue-{idx}-{char["name"].replace(" ", "-")}.wav')
                sf.write(filename, audio, 24000)
                logging.info(f'Audio file saved: {filename}')

        except Exception as e:
            logging.error(f'Error generating audio for dialogue {idx}: {e}')


if __name__ == '__main__':
    generator = DialogueAudioGenerator(lang_code='a')
    generator.create_directories_and_generate_audio()
