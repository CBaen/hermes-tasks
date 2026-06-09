# Evidence

This folder stores compact evidence for capability use, upvotes, downvotes,
failures, fixes, promotions, deprecations, retests, watch status, and rollback
or revalidation events.

Use `capability-evidence.jsonl` when evidence exists. Each line should be one
small JSON object. Do not store secrets, private conversation text, raw client
data, or long logs here.

Evidence should answer:

- What capability was used?
- Where was it used?
- Did it achieve the intended result?
- What verification was done?
- What confidence level applies now?
- What rollback or revalidation path exists if the change fails?
- Did it create any known regression or privacy risk?
