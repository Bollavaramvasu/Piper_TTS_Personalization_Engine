# Logs

## Preprocessing

C:\Users\vasum\AppData\Local\Programs\Python\Python314\Lib\site-packages\pydub\utils.py:170: RuntimeWarning: Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work
  warn("Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work", RuntimeWarning)
2025-12-12 18:04:54,749 [INFO] __main__ - Preprocessing audio: user_raw.wav -> user_clean.wav
2025-12-12 18:04:54,764 [INFO] __main__ - Input channels=2, frame_rate=48000, sample_width=2
2025-12-12 18:04:54,912 [INFO] __main__ - Finished preprocessing
2025-12-12 18:04:54,912 [INFO] __main__ - Saved user_clean.wav

## Profile training

2025-12-12 18:04:55,561 [INFO] __main__ - Building profile from user_clean.wav ...
2025-12-12 18:04:55,774 [INFO] profile_builder - Built profile for default_user: emotion=neutral, params={'length_scale': 0.9, 'noise_scale': 0.6, 'noise_w': 0.7, 'emotion': 'neutral'}
2025-12-12 18:04:55,775 [INFO] __main__ - Profile saved to voice_profile.json
{
  "version": "1.0",
  "user_id": "default_user",
  "source_audio": "user_clean.wav",
  "prosody_features": {
    "duration": 74.41065759637188,
    "mean_f0": 114.63373132056799,
    "std_f0": 31.05928466296394,
    "mean_energy": 52.997669887010325,
    "std_energy": 33.493292616286794,
    "num_pauses": 766,
    "pause_rate": 10.294224305274097,
    "speech_event_rate": 10.253907499900961
  },
  "dominant_emotion": "neutral",
  "piper_runtime_params": {
    "length_scale": 0.9,
    "noise_scale": 0.6,
    "noise_w": 0.7
  }
}

## Personalized synthesis

2025-12-12 18:04:56,496 [INFO] __main__ - Synthesizing with profile voice_profile.json ...
Running command string: "C:\piper\piper\piper" --model "C:\piper\piper\en_US-kathleen-low.onnx" --length_scale 0.9 --noise_scale 0.6 --noise_w 0.7 --output_file "personalized.wav"
Piper stdout: personalized.wav

Piper stderr: [2025-12-12 18:04:57.327] [piper] [info] Loaded voice in 0.586704 second(s)
[2025-12-12 18:04:57.375] [piper] [info] Initialized piper
[2025-12-12 18:04:57.854] [piper] [info] Real-time factor: 0.19437634892086328 (infer=0.432293 sec, audio=2.224 sec)
[2025-12-12 18:04:57.855] [piper] [info] Terminated piper

2025-12-12 18:04:57,896 [INFO] __main__ - Saved synthesized audio to personalized.wav
Saved synthesized audio to personalized.wav

