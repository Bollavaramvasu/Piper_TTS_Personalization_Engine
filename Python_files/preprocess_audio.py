from pydub import AudioSegment
from logger import get_logger

log = get_logger(__name__)
TARGET_SR = 22050

def to_mono_16bit_22050(in_path: str, out_path: str):
    log.info(f"Preprocessing audio: {in_path} -> {out_path}")
    audio = AudioSegment.from_file(in_path)
    log.info(f"Input channels={audio.channels}, frame_rate={audio.frame_rate}, sample_width={audio.sample_width}")
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(TARGET_SR)
    audio = audio.set_sample_width(2)
    audio.export(out_path, format="wav")
    log.info("Finished preprocessing")

if __name__ == "__main__":
    to_mono_16bit_22050("user_raw.wav", "user_clean.wav")
    log.info("Saved user_clean.wav")
