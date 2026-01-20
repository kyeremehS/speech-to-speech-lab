import os
import sys
from typing import Tuple


def asr_transcribe(audio_path: str) -> str:
    if not os.path.isfile(audio_path):
        raise FileNotFoundError(audio_path)
    if not audio_path.lower().endswith(".txt"):
        raise ValueError("Only .txt input supported for ASR in this minimal pipeline")
    print(f"[ASR] reading {audio_path}")
    with open(audio_path, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.strip()
    print(f"[ASR] text='{text}'")
    return text


def llm_respond(prompt: str) -> str:
    print(f"[LLM] prompt='{prompt}'")
    response = f"Assistant: {prompt}"
    print(f"[LLM] response='{response}'")
    return response


def tts_speak(text: str, output_path: str) -> str:
    if not output_path.lower().endswith(".txt"):
        raise ValueError("Only .txt output supported for TTS in this minimal pipeline")
    out_dir = os.path.dirname(output_path) or "."
    os.makedirs(out_dir, exist_ok=True)
    print(f"[TTS] writing to {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"[TTS] done")
    return output_path


def run_pipeline(input_path: str, output_path: str) -> Tuple[str, str]:
    print("[Pipeline] start")
    text = asr_transcribe(input_path)
    reply = llm_respond(text)
    result_path = tts_speak(reply, output_path)
    print(f"[Pipeline] end -> {result_path}")
    return reply, result_path


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python simple_pipeline.py <input.txt> <output.txt>")
        sys.exit(1)
    in_path = sys.argv[1]
    out_path = sys.argv[2]
    run_pipeline(in_path, out_path)

