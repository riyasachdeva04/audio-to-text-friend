import openai
import speech_recognition as sr
import ffmpeg

openai.api_key = "XXX"

def convert_audio_to_wav(input_file, output_file):
    (
        ffmpeg.input(input_file)
        .output(output_file, format="wav")
        .overwrite_output()
        .run(capture_stdout=True, capture_stderr=True)
    )

def transcribe_audio(audio_path):
    r = sr.Recognizer()
    audio = sr.AudioFile(audio_path)

    with audio as source:
        audio_data = r.record(source)

    transcription = r.recognize_google(audio_data)
    return transcription

def convert_audio_to_text(audio_path):
    wav_path = "path/to/converted_audio.wav"
    convert_audio_to_wav(audio_path, wav_path)
    transcription = transcribe_audio(wav_path)
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the appropriate GPT-3.5 model
        prompt=transcription,
        max_tokens=100  # Adjust this parameter to limit the length of the generated text
    )

    generated_text = response.choices[0].text.strip()
    return generated_text


audio_path = "path/to/audio.wav"
converted_text = convert_audio_to_text(audio_path)

print("Generated Text:", converted_text)
