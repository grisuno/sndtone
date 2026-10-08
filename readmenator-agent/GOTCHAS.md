# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `main.py` (score: 0.60)

## Hotspots (complexity + centrality)

- `main.py` -- complexity: 1.0, centrality: 1.0, combined: 1.0

## Dataflow Issues (INFERRED, review each lead)

- `main.py:81` `play_tone` [UNCHECKED_ALLOC] `stream`: Result of allocator stored in `stream` is never checked against NULL.
