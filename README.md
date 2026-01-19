## ASR -> LLM -> TTS learning pipeline(V0)

## Goal
Build a stupid-but-correct, synchronous speech-to-speech pipeline to train architectural judgment. This is not a product.

## Non-Goals
- No streaming
- No batching
- No async
- No performance optimizations
- No production readiness
- No UI

## Success Criteria
- One audion input produces one audio ouput
- All features are visible
- Code is readable and maintainable

## Model Choices
- ASR: Faster Whisper (small)
- LLM: Qwen3-1.7b 
- TTS: Chatterbox Turbo

## Architectural Note
- All components are synchronous
- All components are treated as black boxes
- Failures surface immediately


