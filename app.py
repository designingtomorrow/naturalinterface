import os
import openai
import gradio as gr

openai.api_key = os.getenv("OPENAI_API_KEY")

def transcribe(audio):
    audio_file = open("audio.wav", "wb")
    audio_file.write(audio)
    audio_file.close()
    with open("audio.wav", "rb") as f:
        transcript = openai.Audio.transcribe("whisper-1", f)
    return transcript["text"]

def reply(text):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": text}]
    )
    return response["choices"][0]["message"]["content"]

def full_pipeline(audio):
    text = transcribe(audio)
    answer = reply(text)
    return answer

iface = gr.Interface(
    fn=full_pipeline,
    inputs=gr.Audio(source="microphone", type="binary"),
    outputs="text",
    live=True,
    title="AI Voice Agent",
    description="Speak to the mic and receive a response powered by GPT-4o."
)

iface.launch()
