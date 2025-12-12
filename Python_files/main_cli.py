import argparse
import json
import subprocess
from pathlib import Path
from logger import get_logger
from profile_builder import build_profile

log = get_logger(__name__)


PIPER_EXE = r"C:\piper\piper\piper"  # or C:\wherever-your-working-piper-is\piper
MODEL = r"C:\piper\piper\en_US-kathleen-low.onnx"


def synth_with_profile(text: str, profile_path: str, out_path: str):
    profile = json.loads(Path(profile_path).read_text(encoding="utf-8"))
    params = profile["piper_runtime_params"]

    # Build the same command you run manually in PowerShell
    cmd = (
        f'"{PIPER_EXE}" '
        f'--model "{MODEL}" '
        f'--length_scale {params["length_scale"]} '
        f'--noise_scale {params["noise_scale"]} '
        f'--noise_w {params["noise_w"]} '
        f'--output_file "{out_path}"'
    )
    print("Running command string:", cmd)

    # Use shell=True so Windows loads piper the same way as from PS
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True,
    )
    stdout, stderr = proc.communicate(text)
    print("Piper stdout:", stdout)
    print("Piper stderr:", stderr)
    if proc.returncode != 0:
        raise RuntimeError("Piper failed with code " + str(proc.returncode))

def main():
    parser = argparse.ArgumentParser(
        description="Piper personalization engine CLI"
    )
    parser.add_argument(
        "--train-profile",
        action="store_true",
        help="Analyze user_clean.wav and build voice_profile.json",
    )
    parser.add_argument(
        "--profile",
        type=str,
        default="voice_profile.json",
        help="Path to profile JSON",
    )
    parser.add_argument(
        "--text",
        type=str,
        help="Text to synthesize",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="personalized.wav",
        help="Output WAV file",
    )
    args = parser.parse_args()

    if args.train_profile:
    	log.info("Building profile from user_clean.wav ...")
    	profile = build_profile()
    	log.info("Profile saved to voice_profile.json")
    	print(json.dumps(profile, indent=2))

    if args.text:
    	log.info(f"Synthesizing with profile {args.profile} ...")
    	synth_with_profile(args.text, args.profile, args.output)
    	log.info(f"Saved synthesized audio to {args.output}")
    	print(f"Saved synthesized audio to {args.output}")


if __name__ == "__main__":
    main()
