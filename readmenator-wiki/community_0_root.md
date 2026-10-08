# root

*Community 0 | 1 files | cohesion 1.00*

## Definition

This community groups 1 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `ToneGenerator`, `__init__`, `generate_waveform`, `play_tone`, `save_tone`, `wheelEvent`. Core file: `main.py` (6 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `main.py` | py | utility | 6 | no |

## Key Symbols

- `wheelEvent` (function, `main.py:17`) `def wheelEvent(event)`
- `ToneGenerator` (class, `main.py:25`) `class ToneGenerator(QWidget)`
- `__init__` (method, `main.py:26`) `def __init__(self)`
- `play_tone` (method, `main.py:62`) `def play_tone(self)`
- `save_tone` (method, `main.py:98`) `def save_tone(self)`
- `generate_waveform` (method, `main.py:126`) `def generate_waveform(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- [dataflow UNCHECKED_ALLOC] `main.py:81` `play_tone` `stream`: Result of allocator stored in `stream` is never checked against NULL.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `main.py`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `main.py`
