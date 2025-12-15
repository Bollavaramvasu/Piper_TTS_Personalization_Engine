import time
import parselmouth
import numpy as np
from logger import get_logger

log = get_logger(__name__)

def extract_prosody(wav_path: str):
    start = time.perf_counter()
    log.info(f"Starting prosody extraction from {wav_path}")

    snd = parselmouth.Sound(wav_path)
    duration = snd.get_total_duration()

    # Pitch
    pitch = snd.to_pitch()
    f0 = pitch.selected_array["frequency"]
    f0 = f0[f0 > 0]  # voiced only

    if f0.size > 0:
        mean_f0 = float(np.mean(f0))
        std_f0 = float(np.std(f0))
    else:
        mean_f0 = 0.0
        std_f0 = 0.0

    # Intensity / energy
    intensity = snd.to_intensity()
    energy = intensity.values[0]
    mean_energy = float(np.mean(energy))
    std_energy = float(np.std(energy))

    # Simple pause / rhythm estimation from energy changes
    diff_energy = np.diff(energy)
    pause_events = np.where(diff_energy < -3.0)[0]
    num_pauses = int(len(pause_events))
    pause_rate = num_pauses / duration if duration > 0 else 0.0

    speech_events = np.where(diff_energy > 3.0)[0]
    speech_event_rate = len(speech_events) / duration if duration > 0 else 0.0

    profile = {
        "duration": duration,
        "mean_f0": mean_f0,
        "std_f0": std_f0,
        "mean_energy": mean_energy,
        "std_energy": std_energy,
        "num_pauses": num_pauses,
        "pause_rate": pause_rate,
        "speech_event_rate": speech_event_rate,
    }

    elapsed = time.perf_counter() - start
    log.info(
        f"Prosody features extracted from {wav_path}: {profile} "
        f"(f0_len={len(f0)}, energy_len={len(energy)}, time={elapsed:.3f}s)"
    )

    
    return profile

if __name__ == "__main__":
    p = extract_prosody("user_clean.wav")
    print(p)
