# 🗣️ AI Voice Agent — Building the Interface Beyond the Screen

This repository contains the full implementation of a custom AI voice agent — the companion project to the article *“Giving Machines a Voice: Designing Natural Interfaces for Human-Machine Dialogue.”* It blends historical context with practical application, enabling anyone to create and deploy a conversational agent powered by OpenAI and ElevenLabs.

> The interface is no longer visual. It’s vocal — responsive, ambient, and human.

---

## 🧠 Overview

This agent transcribes your voice using OpenAI Whisper, interprets intent using GPT-4o, and speaks responses using ElevenLabs. Built on a modular Python stack, it can be run locally or deployed to a Hugging Face Space using Gradio.

---

## 🚀 Quick Start

### ▶️ Run Locally (macOS/Linux recommended)

#### 1. Clone the repository
```bash
git clone https://github.com/designingtomorrow/naturalinterface.git
cd naturalinterface
```

#### 2. Set up the environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 3. Create a `.env` file
```dotenv
OPENAI_API_KEY=your_openai_key
ELEVENLABS_API_KEY=your_elevenlabs_key
LIVEKIT_API_KEY=your_livekit_key
LIVEKIT_API_SECRET=your_livekit_secret
LIVEKIT_URL=wss://your.livekit.server
```

#### 4. Launch the agent
```bash
python app.py
```

Or, if using the Jupyter notebook version:
```bash
jupyter notebook
```

---

## 🌐 Deploy to Hugging Face (optional)

See the `/huggingface` folder for a minimal Gradio version that can be deployed to [Hugging Face Spaces](https://huggingface.co/spaces).

---

## 🛠️ Tech Stack

- [OpenAI Whisper](https://platform.openai.com/docs/guides/speech-to-text)
- [GPT-4o](https://openai.com/gpt-4o)
- [ElevenLabs](https://www.elevenlabs.io/)
- [LiveKit](https://livekit.io/)
- [Gradio](https://www.gradio.app/)

---

## 🧩 Use Cases

- Voice-based productivity agents  
- Custom AI companions or narrators  
- Educational tutors  
- Audio-driven design tools  
- Accessibility systems  

---

## 📚 Article Reference

Read the full article:  
[📝 Giving Machines a Voice](https://designingtomorrow.ai/journal))

---

## 🧾 License

This project is licensed under the MIT License.

---

© 2025 [designing tomorrow®](https://designingtomorrow.ai) · Built with clarity and intent.
