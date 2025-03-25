from TTS.utils.manage import ModelManager

def list_available_voices():
    """List all available voices using Coqui TTS API."""
    try:
        # Initialize ModelManager
        manager = ModelManager()

        # List all available models
        available_models = manager.list_models()

        print("Available Models / Voices:")
        for model in available_models:
            print(f"- {model}")
    except Exception as e:
        print(f"Error fetching voices: {str(e)}")


def list_voices_in_models():
    """List available models in Coqui TTS and attempt to determine voices from naming conventions."""
    try:
        # Initialize ModelManager
        manager = ModelManager()

        # List all available models
        available_models = manager.list_models()

        print("Available Models and their Voices (inferred from model names):")
        for model in available_models:
            # In the absence of direct voice metadata, we infer voices based on model name
            # Assuming model name contains information about the voice (e.g., 'en_female', 'en_male')
            voice_inferred = 'Unknown'  # Default if we can't infer the voice

            # Check if the model name contains 'female', 'male', or other identifiers
            if 'female' in model.lower():
                voice_inferred = 'Female Voice'
            elif 'male' in model.lower():
                voice_inferred = 'Male Voice'
            
            print(f"Model: {model}, Inferred Voice: {voice_inferred}")
    except Exception as e:
        print(f"Error fetching models and voices: {str(e)}")

# Example usage
list_voices_in_models()

# Example usage
# list_available_voices()
