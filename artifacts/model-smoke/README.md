# Wardenclyffe Hermes Model Smoke Artifacts

Canonical PASS artifact:

- `artifacts/model-smoke/wardenclyffe-nous-free-model-smoke-20260613.json`

Notes:

- Wardenclyffe Nous Portal auth is verified on the Free subscription.
- The configured default model `anthropic/claude-opus-4.6` is paid/credit-gated for this account and failed the first smoke attempt with a low-balance error.
- The successful smoke used explicit free model `stepfun/step-3.7-flash:free`.
- This proves local-only model execution only; it does not approve broad autonomous dispatch.
