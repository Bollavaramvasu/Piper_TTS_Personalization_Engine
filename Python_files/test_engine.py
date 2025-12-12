from prosody_profile import extract_prosody
from emotion_model import infer_emotion
from style_mapping import prosody_to_piper_params

def test_prosody_basic():
    p = extract_prosody("user_clean.wav")
    assert "duration" in p
    assert "mean_f0" in p

def test_emotion_label():
    dummy = {"std_f0": 10, "std_energy": 2, "speech_event_rate": 1, "pause_rate": 0.2}
    e = infer_emotion(dummy)
    assert e in ["happy", "sad", "neutral", "excited"]
