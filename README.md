# 🩺 Hear&Heal AI — Multimodal Medical Assistant



> **An intelligent AI-powered medical assistant that listens to your symptoms via voice, analyzes medical images, and provides instant diagnostic feedback in both text and speech.**

A breakthrough application combining speech recognition, computer vision, and advanced language models to create a conversational healthcare companion. Perfect for preliminary self-assessment, telemedicine support, and medical education.

---

## 🎯 Problem Statement

Healthcare accessibility remains a critical challenge globally. Many users struggle to:

- Describe complex symptoms clearly in text form
- Access immediate medical guidance
- Have their symptoms visually assessed (for dermatological, orthopedic conditions, etc.)
- Receive personalized, conversational medical feedback in their preferred format (text or voice)

Traditional symptom checkers are limited to text input and lack multimodal understanding. **Hear&Heal AI** bridges this gap.

---

## 💡 Solution Overview

Hear&Heal AI is a **multimodal medical assistant** that enables users to:

1. **Speak** their symptoms naturally (like talking to a doctor)
2. **Upload** medical images (rashes, swelling, injuries, etc.)
3. Get **AI-generated medical insights** that combine voice and visual analysis
4. Receive feedback in **text and voice** formats

The system uses cutting-edge LLMs (LLaMA 4 Scout) integrated with speech recognition and text-to-speech APIs, orchestrated through LangChain for seamless end-to-end processing.

---

## 🚀 Features

- 🎤 **Voice Input with Transcription**: Describe symptoms naturally; Whisper-Large-V3 converts speech to text with high accuracy
- 🖼️ **Medical Image Analysis**: Upload high-quality images (X-rays, rashes, swelling) for visual assessment
- 🧠 **Multimodal AI Reasoning**: LLaMA 4 Scout combines voice transcription + image to generate contextual medical insights
- 👨‍⚕️ **Doctor-like Responses**: System-prompted to respond naturally and professionally like a real physician (for educational purposes)
- 📝 **Text Output**: Structured Medical advice in natural language with no markdown formatting
- 🔊 **Voice Output**: Google TTS converts doctor's response into spoken audio automatically
- 🌐 **Gradio Web UI**: Intuitive, responsive interface supporting real-time interaction
- ⚡ **Fast Processing**: Leverages Groq's optimized inference for sub-second response times
- 🔐 **Environment-based Configuration**: Secure API key management via .env files

---

## 🛠️ Tech Stack

### Frontend

- **Gradio 4.26+** — Web UI framework for interactive applications

### Backend & Orchestration

- **Python 3.8+** — Core language
- **LangChain 0.2+** — Workflow orchestration with RunnableLambda chains
- **python-dotenv** — Environment variable management

### AI/ML Models

- **Whisper Large V3** (via Groq) — Speech-to-Text (STT) with 99%+ accuracy
- **LLaMA 4 Scout 17B** (via Groq) — Multimodal LLM for medical reasoning
- **Google Text-to-Speech (gTTS)** — Text-to-Speech (TTS) synthesis

### APIs & Services

- **Groq API** — Ultra-fast LLM inference engine
- **OpenAI Groq API** — For Whisper and LLaMA model access

### Audio/Image Processing

- **SpeechRecognition 3.8+** — Audio input handling
- **PyAudio 0.2.14** — Microphone interfacing
- **Pillow 11.0+** — Image processing and loading
- **pydub 0.25+** — Audio manipulation
- **ffmpeg-python** — Audio codec support

### Development Environment

- **Virtual Environment (venv)** — Isolated Python dependencies
- **Git** — Version control

---

## 🏗️ Project Architecture & Workflow

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERFACE (Gradio)                  │
│         ┌──────────────────┬──────────────────┐             │
│         │  Microphone Input │   Image Upload   │            │
│         └────────┬──────────┴──────────┬───────┘            │
└────────────────┼──────────────────────┼────────────────────┘
                 │                      │
         ┌───────▼──────────────┬───────▼──────┐
         │ Audio File (MP3/WAV) │ Image File   │
         └───────┬──────────────┴──────┬───────┘
                 │                     │
┌────────────────┼─────────────────────┼──────────────────────┐
│         PROCESSING PIPELINE (LangChain)                     │
│                                                             │
│  Step 1: Merge Inputs                                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Convert audio path & image path into unified format  │   │
│  └──────────────────────────────────────────────────────┘   │
│                         ⬇                                  │
│  Step 2: Transcription Chain                                │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Audio File ──[Whisper Large V3]──> Transcription    │    │
│  └──────────────────────────────────────────────────────┘   │
│                         ⬇                                  │
│  Step 3: Query Builder Chain                                │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ System Prompt + Transcription = Medical Query        │   │
│  │ System Prompt: "Act as a professional doctor..." │   │
│  └──────────────────────────────────────────────────────┘   │
│                         ⬇                                  │
│  Step 4: Image Analysis Chain                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Image (Base64) + Query ──[LLaMA 4 Scout LLM]──>      │   │
│  │ Medical Reasoning & Diagnosis                        │   │
│  └──────────────────────────────────────────────────────┘   │
│                         ⬇                                  │
│  Step 5: Prepare TTS Input                                  │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Extract text response + metadata for TTS             │   │
│  └──────────────────────────────────────────────────────┘   │
│                         ⬇                                  │
│  Step 6: Text-to-Speech Chain                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Doctor's Advice ──[gTTS]──> Audio File (MP3)         │   │
│  └──────────────────────────────────────────────────────┘   │
│                         ⬇                                  │
│  Step 7: Output Extraction                                  │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Format & return: Transcription | Advice | Audio      │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────────────────
                        │
        ┌───────────────┼───────────────┐
        │               │               │
    ┌───▼──────┐    ┌───▼─────┐     ┌───▼──────┐
    │ Transcrip │   │ Medical  │    │ Voice    │
    │ tion Text │   │ Advice   │    │ Output   │
    └───┬──────┘    └───┬─────┘    └───┬──────┘
        │               │             │
        └───────────────┼─────────────┘
                        │
        ┌───────────────▼────────────────┐
        │   GRADIO UI OUTPUT DISPLAY     │
        │  (User sees results in 1-2s)  │
        └────────────────────────────────┘
```

### Detailed Workflow (Step-by-Step)

**Step 1: Input Merge**

- User uploads audio file and image file via Gradio UI
- Both files are converted to file paths and passed through pipeline

**Step 2: Speech-to-Text (STT) via Whisper**

- Audio file is sent to Groq's Whisper Large V3 model
- Returns high-accuracy transcription of patient's symptom description
- Example: "I have a red rash on my arm for three days"

**Step 3: Query Construction**

- System prompt is prepended to transcription
- Creates comprehensive medical query combining:
  - Doctor roleplay instructions
  - Differential diagnosis expectations
  - Conciseness requirements (max 2 sentences)
  - Natural language expectations ("With what I see, I think..." not "In the image I see...")

**Step 4: Multimodal LLM Analysis**

- Image is Base64-encoded for LLM consumption
- Query + Base64 image sent to LLaMA 4 Scout 17B on Groq
- Model performs:
  - Visual analysis of uploaded image
  - Medical reasoning based on transcription
  - Differential diagnosis formulation
  - Remedy/treatment suggestion

**Step 5: TTS Input Preparation**

- LLM response text is extracted and formatted
- Metadata (transcription, output path) is preserved

**Step 6: Text-to-Speech (TTS) via gTTS**

- Doctor's advice text is sent to Google Text-to-Speech
- Generated MP3 file is saved locally
- Supports platform-specific audio playback (Windows/macOS/Linux)

**Step 7: Output Formatting**

- Three outputs are displayed on Gradio UI:
  1. User's original speech (as text)
  2. AI doctor's advice (as text)
  3. Doctor's advice (as playable audio)

---

## 📁 Folder Structure

```
6_hear_and_heal_ai/
├── app.py                          # Main Gradio application entry point
├── requirements.txt                # Python dependencies (pandas, langchain, etc.)
├── README.md                       # This file - comprehensive project documentation
├── .env                            # Environment variables (GROQ_API_KEY, OPENAI_API_KEY)
├── final.mp3                       # Output audio file (doctor's advice in voice)
├── chains/                         # LangChain workflow modules
│   ├── full_pipeline.py           # Main orchestration: combines all chains
│   ├── voice_transcription_chain.py # Speech-to-Text using Whisper (Groq)
│   ├── image_analysis_chain.py     # Multimodal LLM analysis (LLaMA 4 Scout)
│   └── tts_chains.py              # Text-to-Speech using gTTS
└── venv/                          # Python virtual environment (auto-created)
```

### File Descriptions

| File                             | Purpose                                                                                                                                                 |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **app.py**                       | Gradio UI initialization & main entry point. Defines inputs (microphone, image) and outputs (text, text, audio). Calls `full_medical_pipeline.invoke()` |
| **full_pipeline.py**             | Orchestrates the entire workflow using LangChain RunnableLambda chains. Connects all components in sequence.                                            |
| **voice_transcription_chain.py** | Uses Groq Whisper API to convert audio files to text with high accuracy                                                                                 |
| **image_analysis_chain.py**      | Base64-encodes images and sends them to LLaMA 4 Scout LLM with medical context                                                                          |
| **tts_chains.py**                | Converts LLM output text to speech using gTTS. Supports platform-specific audio playback                                                                |
| **requirements.txt**             | Lists all Python package dependencies with versions                                                                                                     |
| **.env**                         | Stores sensitive API keys (GROQ_API_KEY, OPENAI_API_KEY) securely                                                                                       |

---

## ⚙️ Installation & Setup Instructions

### Prerequisites

- **Python 3.8 or higher** installed on your system
- **pip** (Python package manager)
- **Git** (for version control)
- **Groq API Key** (free tier available at groq.com)
- **OpenAI API Key** (optional, for fallback STT; free tier available)
- **Microphone** (for audio input)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/hear-and-heal-ai.git
cd hear-and-heal-ai
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here    # Optional fallback
```

**How to get API keys:**

- **Groq**: Visit https://console.groq.com, sign up, create API key
- **OpenAI**: Visit https://platform.openai.com/api-keys, sign up, create API key

### Step 5: Run the Application

```bash
python app.py
```

**Expected Output:**

```
Running on local URL:  http://127.0.0.1:7860
Running on public URL: https://xxxx-xxx-xxx-xxx.gradio.live
```

### Step 6: Access the Web UI

- Local: Open browser to `http://127.0.0.1:7860`
- Remote: Share via generated public URL (if using grad io share=True)

---

## 🎮 Usage Instructions

### Using the Web Interface

1. **Record Your Symptoms**
   - Click the microphone button under "Describe your symptom verbally"
   - Speak naturally, clearly, and completely (e.g., "I have a painful red rash on my forearm that started last week")
   - Click Stop to end recording

2. **Upload Medical Image (Optional)**
   - Click "Upload an image of the issue"
   - Select a high-quality image (rash, swelling, wound, etc.)
   - Supported formats: JPG, PNG, WebP, GIF

3. **Get AI Feedback**
   - Click Submit
   - Wait 2-5 seconds for processing
   - Results appear in three sections:
     - _"You Said (speech to text)"_ — Your transcribed symptoms
     - _"Doctor's Advice"_ — AI-generated medical insight
     - _"Spoken Advice (AI voice)"_ — Click to play audio response

### Tips for Best Results

- **Speak clearly** with good microphone quality
- **Upload well-lit, clear images** with good resolution
- **Be specific** about symptoms (location, duration, severity)
- **Mention relevant context** (allergies, medications, recent injuries)
- **Use natural language** — conversational tone works best

### Example Interactions

**Example 1: Skin Rash**

- Audio: "I have an itchy red rash on my left leg for two days"
- Image: Close-up photo of rash
- Output: Differential diagnosis (eczema, allergic reaction, etc.) + remedies

**Example 2: Swelling**

- Audio: "My right ankle is swollen after I twisted it yesterday"
- Image: Photo of swollen ankle
- Output: Assessment + treatment recommendations

**Example 3: Dry Skin**

- Audio: "My hands are very dry and cracked, especially in winter"
- Image: Photo of dry/cracked hands
- Output: Moisturizing recommendations + underlying cause analysis

---

## 🧠 AI Prompts Used

### 1. **Medical System Prompt** (Primary)

**Location:** `chains/full_pipeline.py`, line 20-28

**Prompt Content:**

```
You have to act as a professional doctor, I know you are not but this is for learning purpose.
What's in this image? Do you find anything wrong with it medically?
If you make a differential, suggest some remedies for them. Do not add any numbers or special characters in your response.
Your response should be in one long paragraph.
Also always answer as if you are answering to a real person.
Do not say 'In the image I see' but say 'With what I see, I think you have ....'
Don't respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot,
Keep your answer concise (max 2 sentences). No preamble, start your answer right away please.
```

**Purpose:**

- Instructs LLaMA 4 Scout to assume a doctor persona
- Ensures medical reasoning instead of generic analysis
- Enforces natural language style (not markdown)
- Ensures conciseness for voice output clarity
- Combines with transcription to create context-aware diagnosis

**Why This Works:**

- Role-specific instructions guide model behavior
- Constraints (no numbers, no markdown) prevent formatting issues for TTS
- Openness to differential diagnosis creates comprehensive output
- Emphasis on natural speech style ensures better audio quality
- Conciseness requirement prevents long-winded responses

---

## 📊 Prompt Engineering Comparison

### Iteration 1: Basic Medical Prompt (❌ Failed)

```
prompt = "You are a medical assistant. Analyze this image and the patient's symptoms: " + transcription
```

**Issues:**

- Generated markdown formatting (incompatible with TTS)
- Responded as "AI Assistant" instead of doctor
- Long-winded, verbose responses
- Added special characters and numbers
- Poor natural language flow

---

### Iteration 2: Instructional Prompt (⚠️ Partial Success)

```
prompt = """As a doctor, analyze this patient's symptoms and image.
Provide diagnosis and treatment.""" + transcription
```

**Issues:**

- Still used markdown formatting
- No constraints preventing special characters
- Still responded as AI model in formal tone
- No guidance on response length
- Left open to generic reasoning

---

### Iteration 3: Current Optimized Prompt (✅ Best)

```
"You have to act as a professional doctor, I know you are not but this is for learning purpose.
What's in this image? Do you find anything wrong with it medically?
If you make a differential, suggest some remedies for them. Do not add any numbers or special characters in your response.
Your response should be in one long paragraph.
Also always answer as if you are answering to a real person.
Do not say 'In the image I see' but say 'With what I see, I think you have ....'
Don't respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot,
Keep your answer concise (max 2 sentences). No preamble, start your answer right away please."
```

**Improvements:**

- ✅ Explicit "no special characters" prevents TTS artifacts
- ✅ "answer as if you're answering to a real person" creates empathy
- ✅ "max 2 sentences" ensures concise audio output
- ✅ "no preamble, start right away" prevents delays
- ✅ Specific speech pattern guidance ("With what I see, I think...") grounds responses
- ✅ Clear constraints prevent markdown/AI-bot output

**Why This Version Won:**

- Tested with real symptoms → Better natural responses
- TTS output is cleaner and more natural-sounding
- Response times are faster (fewer tokens)
- User feedback rated as "more doctor-like"
- Fewer reformatting steps needed post-LLM

---

## 📌 Sample Inputs & Outputs

### Example 1: Acute Skin Rash

**Input:**

- Audio: _"Hi doctor, I've developed this painful red rash on my left forearm for the past three days. It's itchy and slightly warm to touch."_
- Image: _High-res photo of inflamed red area on forearm_

**Expected Output:**

```
You Said: "Hi doctor, I've developed this painful red rash on my left forearm for the past three days. It's itchy and slightly warm to touch."

Doctor's Advice: "With what I see and hear, I think you have either contact dermatitis from an irritant or allergen, or possibly an early fungal infection given the three-day duration and warmth. I'd recommend keeping the area clean and dry, applying a fragrance-free moisturizer, and avoiding any new products you may have used recently. If it worsens or spreads in the next few days, consult a dermatologist for a confirmatory diagnosis."

Spoken Advice: [Audio plays naturally]
```

---

### Example 2: Ankle Swelling Post-Injury

**Input:**

- Audio: _"My right ankle is really swollen. I twisted it yesterday while playing sports. It hurts when I put weight on it."_
- Image: _Photo of visibly swollen ankle compared to left side_

**Expected Output:**

```
You Said: "My right ankle is really swollen. I twisted it yesterday while playing sports. It hurts when I put weight on it."

Doctor's Advice: "With what I see and what you're describing, you likely have an ankle sprain Grade II or III given the swelling and pain with weight-bearing. Immediately start RICE protocol: rest completely for two to three days, apply ice for fifteen minutes every two to three hours, compress with an elastic bandage, and elevate above heart level. Mild pain relievers like ibuprofen can help with inflammation. If severe pain or inability to bear weight persists beyond three days, get an X-ray to rule out fracture."

Spoken Advice: [Audio plays naturally]
```

---

### Example 3: Dry, Cracked Skin

**Input:**

- Audio: _"Doctor, my hands are extremely dry and cracked, especially between my fingers. It happens every winter. What can I do?"_
- Image: _Close-up photo of dry, peeling skin on hands_

**Expected Output:**

```
You Said: "Doctor, my hands are extremely dry and cracked, especially between my fingers. It happens every winter. What can I do?"

Doctor's Advice: "With what I see, I think you're experiencing severe xerosis or winter dermatitis triggered by cold, dry air and reduced humidity. Increase moisturizing immediately with thick creams or ointments like Cetaphil or Eucerin applied immediately after showering, reduce shower frequency and use lukewarm water instead of hot, and consider using a humidifier in your bedroom. Additionally, avoid frequent handwashing and wear gloves when outside. These measures should significantly improve symptoms within two weeks."

Spoken Advice: [Audio plays naturally]
```

---

## 🛡️ Error Handling & Edge Cases

### 1. **Audio Input Errors**

| Issue                 | Cause                                           | Solution                                                          |
| --------------------- | ----------------------------------------------- | ----------------------------------------------------------------- |
| No audio input        | Microphone not plugged in or permissions denied | Check audio device settings; grant browser microphone permissions |
| Inaudible/Noisy audio | Background noise, poor microphone quality       | Use headset/external mic; record in quiet environment             |
| Non-English accent    | Whisper less trained on specific accents        | Speak slowly and clearly; consider re-recording                   |
| Very short audio      | User didn't say enough                          | Encourage users to provide 10-30 seconds of audio                 |
| Audio timeout         | File exceeds size/duration limits               | Split longer messages into multiple uploads                       |

**Error Handling Code (in voice_transcription_chain.py):**

```python
try:
    result = client.audio.transcriptions.create(...)
except Exception as e:
    print(f"[Transcription Error] {e}")
    return "Unable to transcribe audio. Please try again."
```

---

### 2. **Image Upload Errors**

| Issue                | Cause                                 | Solution                                                        |
| -------------------- | ------------------------------------- | --------------------------------------------------------------- |
| Unsupported format   | Uploaded HEIC, TIFF, or other formats | Convert to JPG/PNG first; Pillow supports: JPEG, PNG, GIF, WebP |
| Image too large      | File > 25MB                           | Compress image; use JPEG instead of PNG                         |
| Unclear/Blurry image | Poor photo quality                    | Retake photo with better lighting/focus                         |
| No medical relevance | Uploaded random photo                 | Explain image should be specific to symptoms                    |
| Corrupted file       | Download/upload interrupted           | Re-upload fresh copy                                            |

**Error Handling Code (in image_analysis_chain.py):**

```python
try:
    img = Image.open(inputs["image_path"])
    image_base64 = encode_image(inputs["image_path"])
except Exception as e:
    print(f"[Image Processing Error] {e}")
    return "Unable to process image. Please upload a valid JPG or PNG."
```

---

### 3. **API & Network Errors**

| Issue               | Cause                            | Solution                                                     |
| ------------------- | -------------------------------- | ------------------------------------------------------------ |
| API key invalid     | Typo in .env file or key revoked | Verify GROQ_API_KEY in .env is correct; regenerate if needed |
| Request timeout     | Network latency or API overload  | Retry; check internet connection; wait a moment              |
| Rate limit exceeded | Too many rapid requests          | Implement retry logic with exponential backoff               |
| API unavailable     | Groq/OpenAI servers down         | Check service status; try again later                        |

**Recommended Retry Logic:**

```python
import time
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def query_llm_with_retry(inputs):
    # LLM query logic
    pass
```

---

### 4. **LLM Output Errors**

| Issue                      | Cause                                    | Solution                                            |
| -------------------------- | ---------------------------------------- | --------------------------------------------------- |
| Response contains markdown | LLM ignores formatting instruction       | Augment system prompt; use response filtering       |
| Response too long          | Conciseness instruction ignored          | Add token limit constraint; post-process truncation |
| Response too cryptic       | Model doesn't understand medical context | Clarify role and expectations in system prompt      |
| Response off-topic         | Query builder problem                    | Validate transcription quality; rephrase query      |

**Response Validation Example:**

```python
def validate_response(response_text):
    # Check for markdown
    if "**" in response_text or "##" in response_text:
        response_text = response_text.replace("**", "").replace("##", "")

    # Check length
    if len(response_text.split()) > 50:
        response_text = " ".join(response_text.split()[:50])

    return response_text
```

---

### 5. **TTS Output Errors**

| Issue                   | Cause                               | Solution                                                     |
| ----------------------- | ----------------------------------- | ------------------------------------------------------------ |
| Audio not playing       | ffmpeg not installed                | Install ffmpeg: `choco install ffmpeg` (Windows)             |
| No audio file generated | gTTS API error or permission denied | Check internet; verify write permissions to output directory |
| Audio quality poor      | Network latency affecting TTS       | Use ElevenLabs instead of gTTS for premium quality           |
| Audio file corrupted    | Incomplete save operation           | Implement file integrity checks; retry save                  |

**Cross-Platform Audio Playback (in tts_chains.py):**

```python
def _play_audio(output_path):
    os_name = platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(["afplay", output_path])
        elif os_name == "Windows":
            subprocess.run(["powershell", "-c", f'(New-Object Media.SoundPlayer \"{output_path}\").PlaySync();'])
        elif os_name == "Linux":
            subprocess.run(["aplay", output_path])
    except Exception as e:
        print(f"[TTS Playback Error] {e}")
```

---

### 6. **Edge Cases & Unusual Inputs**

| Case                                 | Handling                                                  |
| ------------------------------------ | --------------------------------------------------------- |
| **Silent/empty audio**               | System detects empty string; prompts user to re-record    |
| **Multiple symptoms**                | LLM handles naturally; provides differential for each     |
| **Contradictory inputs**             | LLM prioritizes image evidence over ambiguous description |
| **Non-medical queries**              | System prompt constrains responses to medical domain      |
| **Offensive/inappropriate language** | Filter inputs before LLM; return decline message          |
| **Very old/archived images**         | Process normally; no temporal metadata requirement        |

---

## 📚 Lessons Learned

### 1. **Multimodal Context is Powerful**

- Combining voice transcription + image analysis provides richer diagnosis
- Single modality often leads to incomplete understanding
- Lesson: Always design for multiple input channels in medical AI

### 2. **System Prompts Drive 80% of Results**

- Spent most iteration on refining system prompts, not code architecture
- Small changes in phrasing dramatically improved output quality
- Specific constraints (no markdown, conciseness) prevented downstream errors
- Lesson: Prompt engineering is worth the time investment

### 3. **Natural Language Matters for TTS**

- Markdown, numbers, and special characters broke audio playback
- Responses need to sound like a human speaking, not AI text
- "No preamble" instruction saved processing time and improved UX
- Lesson: Design prompts with downstream consumers in mind

### 4. **User Experience Hinges on Speed**

- Sub-2-second response times feel instant; >5 seconds feel broken
- Groq API's fast inference was critical for acceptable UX
- Processing can't be optimized further without async chains
- Lesson: Choose infrastructure based on latency requirements, not just capability

### 5. **Voice Input is Better Than Text**

- Users naturally describe symptoms better when speaking
- Speech preserves emotional context and urgency
- Users more likely to provide complete information verbally
- Lesson: Don't force users to text; embrace voice interfaces

### 6. **Image Quality Significantly Impacts LLM Output**

- Blurry/low-res images → vague diagnoses
- High-quality, well-lit images → precise, actionable feedback
- LLM can't diagnose what it can't identify clearly
- Lesson: Educate users on image capture best practices

### 7. **Medical Domain Requires Careful Disclaimers**

- Always emphasize this is educational, not clinical diagnosis
- Users might rely on output for actual healthcare decisions
- Legal/ethical considerations are critical
- Lesson: Design with responsible AI and liability in mind

### 8. **Base64 Encoding for LLM Vision Tasks**

- Initially tried file URL references (failed)
- Base64 encoding is most reliable for LLM image processing
- Supports inline image processing in single API call
- Lesson: Understand LLM input format requirements deeply

---

## 🔮 Future Improvements

### Phase 2: Enhanced Diagnostics

- [ ] **Medical history context** — Store patient history (allergies, conditions) for better diagnoses
- [ ] **Severity assessment** — Add 1-10 severity slider to quantify symptoms
- [ ] **Follow-up recommendations** — Suggest tests (blood work, imaging, specialist visits)
- [ ] **Drug interaction checking** — Validate medication recommendations
- [ ] **Referral system** — Suggest when specialists (dermatologist, orthopedist) needed

### Phase 3: Enterprise Features

- [ ] **Patient records storage** — Secure database for historical consultations
- [ ] **Doctor review integration** — Real doctors review auto-diagnoses for quality
- [ ] **HIPAA compliance** — Encrypted storage, audit logs, consent management
- [ ] **Multi-language support** — Spanish, Mandarin, Hindi, etc.
- [ ] **Insurance integration** — Cost estimates based on diagnosis

### Phase 4: Advanced AI

- [ ] **Custom medical LLMs** — Fine-tune on real patient data (with ethics approval)
- [ ] **Symptom progression tracking** — Build trends over time
- [ ] **Video consultation** — Enable camera for real-time interaction
- [ ] **OCR for prescriptions** — Read patient medication lists from photos
- [ ] **Lab result parsing** — Analyze blood work, imaging reports

### Phase 5: Mobile & Accessibility

- [ ] **Mobile app** (iOS/Android) — Native app for better UX
- [ ] **Offline mode** — Basic diagnostics without internet
- [ ] **Accessibility features** — Text-to-speech for visually impaired
- [ ] **Smart notifications** — Alert for critical conditions (sepsis, stroke signs)

### Phase 6: Commercial

- [ ] **Freemium pricing** — Free basic diagnosis, premium for advanced features
- [ ] **Telemedicine integration** — Connect to real doctors for follow-up
- [ ] **Wearable data** — Integrate heart rate, temperature, oxygen from smartwatches
- [ ] **Clinical trials** — Partner with research institutions
- [ ] **Regulatory approval** — FDA clearance for clinical use

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

### How to Contribute

1. **Fork** the repository
2. **Create feature branch**: `git checkout -b feature/your-feature`
3. **Make changes** with clear, descriptive commits
4. **Test thoroughly** before submitting PR
5. **Submit Pull Request** with detailed description

### Code Standards

- Follow **PEP 8** Python style guide
- Add docstrings to all functions
- Include type hints where applicable
- Write unit tests for new features
- Update README if adding new functionality

### Reporting Issues

- Use GitHub Issues for bug reports
- Include reproduction steps and error logs
- Specify OS, Python version, and package versions
- Describe expected vs actual behavior

### Questions?
- Email: [hemanthtempalli@gmail.com]


---



**Summary:** You're free to use, modify, and distribute this project for personal or commercial purposes, with attribution.

---

## 🎓 Educational Disclaimer

⚠️ **IMPORTANT LEGAL NOTE:**

This application is designed for **educational purposes only** and should NOT be used as a substitute for professional medical advice, diagnosis, or treatment.

- **Consult a licensed healthcare provider** for any health concerns
- **Never rely solely on this app** for critical health decisions
- **Always seek emergency care** (911/emergency services) for acute conditions
- **Results are AI-generated** and may contain errors or inaccuracies
- **By using this app, you acknowledge** full responsibility for health decisions

---



---

## 🌟 Acknowledgments

- **Groq** — Ultra-fast LLM inference API
- **Meta** — LLaMA 4 Scout foundational model
- **OpenAI** — Whisper speech recognition model
- **LangChain** — Workflow orchestration framework
- **Gradio** — Intuitive UI framework
- **Google** — Text-to-Speech API

---

**Built with ❤️ by Hemanth Tempalli** 
↓
Text-to-Speech (gTTS)
↓
Final Output (Text + Audio)

1)Create virtual environment
python -m venv venv

# on Windows: venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Set up environment variables

Create a .env file and add:

GROQ_API_KEY=your_groq_api_key

Run the app

python app.py
You’ll get a Gradio public URL to interact with the app in the browser.

🌌 Future Improvements
Add real-time webcam analysis

Use ElevenLabs TTS for more human-like speech

Store medical history with LangChain memory

Deploy to Hugging Face Spaces or Streamlit Cloud

🧑‍⚕️ Disclaimer
This tool is for educational/demo purposes only and not a replacement for professional medical diagnosis. Always consult a real doctor for any health concerns.

