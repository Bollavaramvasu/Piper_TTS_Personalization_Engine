

def prosody_to_piper_params(profile: dict, emotion: str) -> dict:
    speech_rate = profile["speech_event_rate"]
    std_f0 = profile["std_f0"]

    # default
    length_scale = 1.0
    noise_scale = 0.67
    noise_w = 0.8

    # speed from speech rate
    if speech_rate > 4:
        length_scale = 0.9
    elif speech_rate < 2:
        length_scale = 1.1

    # expressiveness from pitch variation
    if std_f0 > 40:
        noise_scale = 0.8
        noise_w = 1.0
    else:
        noise_scale = 0.6
        noise_w = 0.7

    # emotion tweak
    if emotion == "excited":
        length_scale *= 0.95
        noise_scale *= 1.1
    elif emotion == "sad":
        length_scale *= 1.1
        noise_scale *= 0.9
    elif emotion == "happy":
        noise_scale *= 1.05

    return {
        "length_scale": length_scale,
        "noise_scale": noise_scale,
        "noise_w": noise_w,
        "emotion": emotion,
    }

