# Task 1 — TTS Dataset Analysis (Piper Context)

## 1. Overview

This document analyzes several standard text-to-speech (TTS) datasets and explains how their properties affect synthesized voice characteristics such as clarity, naturalness, accent, pitch, timbre, and emotional expressiveness. The focus is on single-speaker and multi-speaker corpora commonly used to train neural TTS systems similar to Piper TTS. [web:99][web:104]

The datasets covered are LJSpeech, VCTK, LibriTTS, Hi-Fi Multi-Speaker English TTS, and HUI-Audio-Corpus-German. Based on their design and recording conditions, this document derives practical guidelines for selecting and preparing datasets for diverse voice profiles. [web:99][web:108][web:104][web:110][web:106]

---

## 2. Core TTS Datasets

### 2.1 LJSpeech

- Single female English speaker reading non‑fiction book text; around 13,100 audio clips totaling approximately 24 hours. [web:99][web:102]  
- Audio format: 16-bit PCM, mono WAV, sampled at 22.05 kHz; each clip is 1–10 seconds long with an aligned text transcript. [web:98][web:107]  
- Text domain: public domain books, mostly neutral reading style without extreme emotion. [web:99][web:101]

**Voice characteristics supported**

- Very stable timbre and accent because data comes from a single speaker in a consistent studio-like environment. [web:99]  
- Reasonably clear and natural speech for general-purpose English voices, but limited accent and emotional diversity. [web:99][web:102]

---

### 2.2 VCTK Corpus

- Approximately 110 English speakers (both male and female), with each speaker reading about 400 sentences. [web:108][web:113]  
- Designed to cover multiple accents, especially a range of British accents and some non-native English speakers. [web:108][web:113]  
- Recordings captured in a controlled environment with high-quality microphones. [web:108]

**Voice characteristics supported**

- Good for modeling accent variation and building multi-speaker, accent-conditioned TTS systems. [web:108][web:113]  
- Timbre diversity (different speakers and genders) helps learn richer speaker embeddings but requires careful balancing to avoid over-representing certain accents. [web:108]

---

### 2.3 LibriTTS

- Large-scale multi-speaker English corpus derived from LibriVox audiobooks, around 585 hours of speech at 24 kHz. [web:104][web:109]  
- Includes train/dev/test splits and variants with normalized text, designed specifically for TTS training. [web:104]  
- Audio is segmented at sentence boundaries, and noisy or low-quality utterances are filtered out. [web:104][web:114]

**Voice characteristics supported**

- High naturalness and expressive prosody due to audiobook narration with varied intonation and pacing. [web:104][web:109]  
- Multi-speaker nature supports modeling different timbres and speaking styles but also introduces variability in recording conditions. [web:104]

---

### 2.4 Hi-Fi Multi-Speaker English TTS Dataset

- High-fidelity English TTS dataset with around 292 hours of speech from 10–11 speakers, each contributing at least 16–17 hours. [web:105][web:110]  
- Audio recorded at 44.1 kHz sampling rate with signal-to-noise ratio ≥32 dB and bandwidth ≥13 kHz to ensure high quality. [web:110][web:115]  
- Source material from LibriVox and Project Gutenberg, selecting segments with consistent quality and narration. [web:110]

**Voice characteristics supported**

- Very high clarity and rich timbre due to high sampling rate and carefully controlled noise levels. [web:110]  
- Suitable for models targeting premium “hi-fi” output where subtle nuances in pitch and brightness matter. [web:110][web:115]

---

### 2.5 HUI-Audio-Corpus-German

- High-quality German speech corpus with multiple speakers and separate “full” and “clean” subsets for TTS training. [web:106][web:111]  
- Audio recorded at 44.1 kHz with consistent recording conditions; the clean subset removes lower-quality or noisy segments. [web:111][web:116]  
- Designed to support robust German TTS in different domains. [web:106][web:111]

**Voice characteristics supported**

- Clear and natural German speech with consistent pronunciation, making it suitable for high-quality German voices. [web:106][web:111]  
- Clean subset improves stability and reduces artifacts in synthesized speech compared to using raw full data. [web:111][web:116]

---

## 3. Dataset Properties and Voice Characteristics

This section links dataset design choices to how a trained TTS voice sounds.

### 3.1 Sampling Rate and Bit Depth

- Higher sampling rates (24 kHz, 44.1 kHz) capture more high-frequency content, which improves perceived clarity, sharpness, and timbre detail; datasets like LibriTTS, Hi-Fi, and HUI use ≥24 kHz. [web:104][web:110][web:111]  
- 16-bit PCM with proper peak control avoids clipping and quantization noise, which supports smoother, artifact-free synthesis. [web:98][web:111]

**Impact on synthesized voice**

- Low sampling rates or inconsistent formats can make synthesized voices sound muffled or “telephone-like,” especially at high frequencies. [web:104][web:110]  
- Clean, uniform sampling rate across the dataset produces more consistent pitch, formants, and spectral envelope, improving naturalness. [web:104][web:112]

---

### 3.2 Noise Level and Recording Conditions

- LibriTTS filters out noisy utterances and enforces quality thresholds to remove severe background noise or distortions. [web:104]  
- Hi-Fi Multi-Speaker and HUI German emphasize high SNR and controlled recording conditions, and HUI provides a dedicated clean subset. [web:110][web:111]

**Impact on synthesized voice**

- High noise levels during training cause models to learn background hiss and unstable prosody, leading to artifacts during synthesis. [web:104][web:110]  
- Training on uniformly clean audio yields clearer voices and more accurate modeling of pauses and silence, which improves perceived naturalness. [web:110][web:111]

---

### 3.3 Speaker Count and Distribution

- LJSpeech: single female speaker, resulting in a very stable, single identity voice. [web:99][web:102]  
- VCTK and LibriTTS: many speakers with various accents, genders, and ages. [web:108][web:104]  
- Hi-Fi and HUI: moderate number of speakers with significant hours per speaker and well-documented metadata. [web:110][web:111]

**Impact on synthesized voice**

- Single-speaker datasets produce consistent timbre and accent but lack flexibility for other speaker identities. [web:99]  
- Multi-speaker datasets enable training models that can generate different speakers or speaker-conditioned voices, but require balancing so that frequent speakers do not dominate. [web:108][web:104]

---

### 3.4 Accent, Language, and Text Domain

- VCTK is intentionally diversified across UK accents and some non-native speakers. [web:108][web:113]  
- LibriTTS and Hi-Fi focus on English but include varied narrators and literary text. [web:104][web:110]  
- HUI-Audio-Corpus-German is targeted specifically at German TTS with controlled recordings. [web:106][web:111]

**Impact on synthesized voice**

- Training on the wrong accent or language relative to target usage produces foreign-sounding pronunciation and reduced intelligibility. [web:104][web:108]  
- Rich accent diversity cases (like VCTK) can be used for accent-controllable models, but may reduce clarity if accents are mixed without proper labeling or conditioning. [web:108][web:113]

---

### 3.5 Prosody, Emotion, and Speaking Style

- Audiobook-based datasets such as LibriTTS and Hi-Fi contain natural variation in pitch, tempo, and emphasis, including questions, exclamations, and emotional narration. [web:104][web:110]  
- LJSpeech is more neutral but still includes some variation in phrasing and emphasis across long-form reading. [web:99]

**Impact on synthesized voice**

- Expressive datasets allow models to learn richer prosody patterns, making synthesized speech sound less robotic and more human-like. [web:104][web:110]  
- If training data is predominantly flat, neutral speech, the model tends to produce monotone output even when given expressive text. [web:99][web:104]

---

### 3.6 Text Coverage and Phonetic Diversity

- LibriTTS uses a large, diverse text corpus from audiobooks, increasing coverage of phonemes, words, and sentence structures. [web:104][web:109]  
- Datasets with limited vocabulary or repetitive phrases cause the model to overfit specific patterns and struggle with rare or unseen words. [web:104][web:115]

**Impact on synthesized voice**

- Broad phonetic coverage improves pronunciation robustness and reduces unnatural pitch jumps on rare phoneme sequences. [web:104][web:115]  
- Adequate coverage of numerals, abbreviations, and domain-specific terms is critical for assistant-like voices or specialized domains. [web:104][web:109]

---

## 4. Guidelines for Selecting and Preparing Datasets

This section translates the observations above into actionable guidelines to design or choose training datasets for systems like Piper.

### 4.1 Match Dataset to Target Voice Profile

- For a **single, branded voice** (e.g., a consistent assistant voice), choose a single-speaker dataset or a filtered subset (similar to LJSpeech or one speaker from HUI). [web:99][web:111]  
- For **multi-speaker or accent-aware TTS**, choose corpora like VCTK or LibriTTS and ensure speaker and accent labels are available for conditioning. [web:108][web:104]

---

### 4.2 Ensure Audio Quality and Consistency

- Standardize audio to mono, 16-bit PCM, and at least 22.05 kHz; for premium quality voices, prefer 24 kHz or 44.1 kHz when supported by the model. [web:98][web:104][web:111]  
- Remove or down-weight utterances that contain strong background noise, clipping, or artifacts; leverage clean subsets (e.g., HUI clean, filtered LibriTTS) where possible. [web:110][web:111]

---

### 4.3 Control Prosody and Style in the Dataset

- Decide if the target voice should be neutral, conversational, or highly expressive, and select recordings accordingly; audiobook-style data is better for expressive prosody. [web:104][web:110]  
- Include a mix of sentence types (statements, questions, exclamations) to help the model learn appropriate intonation patterns for different punctuation. [web:104][web:109]

---

### 4.4 Text and Phonetic Coverage

- Analyze the text corpus for coverage of phonemes and word types; aim for balanced phoneme distribution rather than many repeats of a small set of sentences. [web:104][web:115]  
- Ensure that the dataset includes domain-specific terminology and numerals if the target application is an assistant or information system. [web:104][web:109]

---

### 4.5 Speaker Metadata and Balancing Strategies

- Maintain clear metadata: speaker ID, gender, accent, recording session, and environment; this supports speaker embeddings or conditional TTS. [web:108][web:104]  
- During training, use sampling strategies that balance per speaker (e.g., equal samples per speaker per batch) to avoid bias towards speakers with more recordings. [web:110][web:111]

---

### 4.6 Preprocessing and Alignment

- Normalize loudness and trim leading/trailing silence to stabilize training and reduce irrelevant variability. [web:104][web:111]  
- Ensure accurate alignment between text and audio segments (sentence-level or utterance-level) to improve attention and convergence in sequence-to-sequence TTS models. [web:104][web:112]

---

## 5. Diagrams (Mermaid)

### 5.1 Dataset Pipeline

flowchart LR
A[Raw Audio & Text Sources\n(Audiobooks, Scripts, Web Text)] --> B[Data Cleaning\n(remove noise, clipping, bad segments)]
B --> C[Segmentation\n(split into utterances)]
C --> D[Alignment\n(audio ↔ text)]
D --> E[Normalization\n(text, sampling rate, loudness)]
E --> F[Feature Extraction\n(mel-spectrograms, phonemes, prosody)]
F --> G[Training Dataset\n(ready for TTS models like Piper)]


This diagram illustrates the typical pipeline from raw recordings and text sources to a training-ready dataset used by TTS models like Piper, similar to how LibriTTS and HUI corpora are prepared. [web:104][web:111]

---

### 5.2 Feature Extraction Flow

flowchart LR
A[Audio Waveform] --> B[Preprocessing\n(resample, trim, normalize)]
B --> C[Acoustic Features\n(mel-spectrogram, energy)]
B --> D[Prosodic Features\n(pitch F0, duration, pauses)]

E[Text Transcripts] --> F[Text Normalization\n(expand numbers, abbreviations)]
F --> G[Phoneme/Character Sequences]

C --> H[TTS Model Input]
D --> H
G --> H

This diagram shows how audio and text are converted into features such as mel-spectrograms, prosody signals, and phoneme sequences, which are then fed into the TTS model. [web:104][web:82]

---

### 5.3 Voice Characteristic Mapping

flowchart LR
A[Dataset Properties] --> B[Learned Acoustic & Prosodic Space]
B --> C[Synthesized Voice Characteristics]

A --> A1[Sampling Rate & Bit Depth]
A --> A2[Noise Level & Room Acoustics]
A --> A3[Speakers & Accents]
A --> A4[Text & Phoneme Coverage]
A --> A5[Prosody & Emotion Diversity]

C --> C1[Clarity]
C --> C2[Naturalness]
C --> C3[Accent & Pronunciation]
C --> C4[Pitch & Timbre]
C --> C5[Emotional Expressiveness]


This diagram conceptually links dataset design choices (left) to the latent representation learned by a TTS model and finally to perceived voice qualities (right). [web:104][web:110][web:111]

---

## 6. Relationship to Piper TTS

Piper TTS typically expects training data in formats similar to LJSpeech (e.g., WAV files with a metadata file of audio–text pairs). [web:19][web:112] The datasets described above provide different trade-offs in terms of speaker diversity, quality, and prosody, which directly influence how a Piper-trained voice sounds:

- Using LJSpeech-like data yields a stable, single English female voice with good clarity but limited accent and emotional variation. [web:99][web:102]  
- Multi-speaker datasets like VCTK, LibriTTS, Hi-Fi, and HUI enable training Piper models that can support multiple voices, accents, or languages, at the cost of more complex training and balancing. [web:108][web:104][web:110][web:111]

When building personalized or multi-profile voices on top of Piper, following the guidelines in Section 4 helps select or construct datasets that match desired voice characteristics while maintaining high clarity and naturalness. [web:19][web:104]
