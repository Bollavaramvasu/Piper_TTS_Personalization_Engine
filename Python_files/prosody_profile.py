# prosody_profile.py
import parselmouth
import numpy as np
from logger import get_logger

log = get_logger(__name__)


def extract_prosody(wav_path: str):
    snd = parselmouth.Sound(wav_path)
    duration = snd.get_total_duration()

    pitch = snd.to_pitch()
    f0 = pitch.selected_array["frequency"]
    f0 = f0[f0 > 0]
    mean_f0 = float(np.mean(f0)) if f0.size > 0 else 0.0
    std_f0 = float(np.std(f0)) if f0.size > 0 else 0.0

    intensity = snd.to_intensity()
    energy = intensity.values[0]
    mean_energy = float(np.mean(energy))
    std_energy = float(np.std(energy))

    diff_energy = np.diff(energy)
    pause_events = np.where(diff_energy < -3.0)[0]
    num_pauses = int(len(pause_events))
    pause_rate = num_pauses / duration if duration > 0 else 0.0

    speech_events = np.where(diff_energy > 3.0)[0]
    speech_event_rate = len(speech_events) / duration if duration > 0 else 0.0

    return {
        "duration": duration,
        "mean_f0": mean_f0,
        "std_f0": std_f0,
        "mean_energy": mean_energy,
        "std_energy": std_energy,
        "num_pauses": num_pauses,
        "pause_rate": pause_rate,
        "speech_event_rate": speech_event_rate,
    }

if __name__ == "__main__":
    profile = extract_prosody("user_clean.wav")
    log.info(f"Prosody features: {profile}")
    print(profile)
