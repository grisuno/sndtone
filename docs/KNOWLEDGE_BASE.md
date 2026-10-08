# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. 1 files, 6 symbols, 15 imports. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM, Ruby, Swift, Kotlin, Scala, Lua, Elixir.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Start here:** Statistics Dashboard for scope, God Nodes for blast radius, Architecture Reference for per-file API. Agents: prefer `readmenator-agent/INDEX.md` + `SYMBOLS.md`.

**Wiki:** prefer `readmenator-wiki/index.md` for progressive disclosure: one synthesis page per community, `connections.json` with EXTRACTED vs INFERRED confidence, `queries.md` log, `REPORT.md` audit.

**Confidence:** EXTRACTED = parsed from source, INFERRED = heuristic bridge, AMBIGUOUS = reported, never hidden. See `readmenator-wiki/REPORT.md`.

**Total Files Parsed:** 1 | **Total Symbols Extracted:** 6 | **Total Imports:** 15

<!-- ranking_model: v1.0 | weights: {ppr:0.45,auth:0.2,test:0.15,doc:0.1,fresh:0.1} | alpha:0.85 | commit:1e0fd0b | date:2026-07-18 -->


## Table of Contents

1. [Statistics Dashboard](#statistics-dashboard)
2. [Architectural Layers](#architectural-layers)
3. [Ranked Context](#ranked-context)
4. [God Nodes](#god-nodes)
5. [Suggested Questions](#suggested-questions)
6. [Hotspot Analysis](#hotspot-analysis)
7. [Change Impact Analysis](#change-impact-analysis)
8. [Suggested Linting Rules](#suggested-linting-rules)
9. [Dataflow Analysis](#dataflow-analysis)
10. [Orphans](#orphans)
11. [Query Recipes](#query-recipes)
12. [Structural Knowledge Map](#structural-knowledge-map)
13. [UML Class Diagram](#uml-class-diagram)
14. [Code Property Graph](#code-property-graph)
15. [Architecture Reference](#architecture-reference)
    - [PY (1 files)](#py-1-files)

---

## Statistics Dashboard

| Metric | Value |
|--------|-------|
| Total Files | 1 |
| Total Symbols | 6 |
| Total Imports | 15 |
| Call Edges | 130 |
| Inheritance Edges | 1 |
| Languages | 1 |
| Avg Symbols/File | 6.0 |
| Avg Imports/File | 15.0 |

### Top Files by Import Count (Fan-Out)

| File | Imports | Symbols | Language |
|------|---------|---------|----------|
| `main.py` | 15 | 6 | py |

---

## Architectural Layers

Auto-detected from path patterns, naming conventions, and imported frameworks.

| Layer | Files |
|-------|-------|
| utility | 1 |

### utility

- `main.py` (py, 6 symbols)

---

## Ranked Context

Files ranked by composite score for the current query context. The ranking combines Personalized PageRank (query relevance), global authority, test coverage, documentation coverage, and code freshness. Model: v1.0.

| Rank | File | Composite | PPR | Authority | Test | Doc |
|------|------|-----------|-----|-----------|------|-----|
| 1 | `main.py` | 0.0000 | 0.0000 | 0.0000 | 0.00 | 0.00 |

---

## God Nodes

Most architecturally central files ranked by combined import/export degree and symbol richness.

| File | Score | Connections | PageRank |
|------|-------|-------------|----------|
| `main.py` | 0.6 | | 0.0000 |

---

## Suggested Questions

Auto-generated exploration prompts based on graph structure:

- What does main.py depend on, and what depends on it? (0 connections)
- What is ToneGenerator in main.py and how is it used?
- What is the overall architecture of this codebase?

---

## Hotspot Analysis

Files ranked by combined complexity (symbol count) and centrality (connection count). High-scoring files are architecturally critical and may need refactoring attention.

| File | Complexity | Centrality | Combined | Symbols | Connections |
|------|-----------|------------|----------|---------|-------------|
| `main.py` | 1.000 | 1.000 | 1.000 | 6 | 15 |

---

## Dataflow Analysis

Procedural intra-function dataflow findings (zero tokens, regex-based heuristics, all INFERRED). Each lead is grounded at file:line for manual review.

**1 findings** (UNCHECKED_ALLOC: 1).

| File | Function | Line | Kind | Variable | Description |
|------|----------|------|------|----------|-------------|
| `main.py` | `play_tone` | 81 | `UNCHECKED_ALLOC` | `stream` | Result of allocator stored in `stream` is never checked against NULL. |

---

## Change Impact Analysis

Files sorted by how many other files would be affected if they changed. High-impact files should be changed with caution.

| File | Direct Dependents | Transitive Dependents | Total Impact |
|------|------------------|----------------------|--------------|
| `main.py` | 0 | 0 | 0 |

---

## Suggested Linting Rules

Automatically suggested linting and security rules based on patterns detected in the codebase. These can be exported as Semgrep rules using the `--export-rules` flag.

| Rule ID | Severity | Description | Language | Matches |
|---------|----------|-------------|----------|---------|
| `RM001` | info | Large number of functions in py: 5 total | py | 5 |

---

## Orphans

Files with no documentation or low connectivity. These are candidates for documentation investment or cleanup.

- `main.py` (6 symbols, no doc)

---

## Query Recipes

Example queries you can run against this knowledge base using the ranking engine:

```
# Find files most relevant to a concept
readmenator query "Where is the import resolver implemented?"

# Rank files by relevance to a topic
readmenator query "How does documentation generation work?"

# Explain why a file ranks highly
readmenator query "explain readmenator/_documentation.py"

# Trace dependency paths with ranked context
readmenator query "path from CLI to exporter"
```

The ranking model uses the following signals:

- **Personalized PageRank** (45% weight): query-specific relevance via seed propagation
- **Global Authority** (20% weight): structural importance via standard PageRank
- **Test Coverage** (15% weight): fraction of symbols referenced in test files
- **Doc Coverage** (10% weight): presence of docstrings and file-level docs
- **Freshness** (10% weight): recent modification activity

Results include score decomposition and justification paths for each ranked item.

---

## Structural Knowledge Map

```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    main_py["main.py (py)"]
    class main_py mod;
    main_py_wheelEvent["wheelEvent"]
    class main_py_wheelEvent fn;
    main_py --> main_py_wheelEvent
    main_py_ToneGenerator["ToneGenerator"]
    class main_py_ToneGenerator cls;
    main_py --> main_py_ToneGenerator
    main_py___init__["__init__"]
    class main_py___init__ fn;
    main_py --> main_py___init__
    main_py_play_tone["play_tone"]
    class main_py_play_tone fn;
    main_py --> main_py_play_tone
    main_py_save_tone["save_tone"]
    class main_py_save_tone fn;
    main_py --> main_py_save_tone
    ext_sys["sys"]
    class ext_sys ext;
    main_py -.->|imports| ext_sys
    ext_math["math"]
    class ext_math ext;
    main_py -.->|imports| ext_math
    ext_numpy["numpy"]
    class ext_numpy ext;
    main_py -.->|imports| ext_numpy
    ext_pygame["pygame"]
    class ext_pygame ext;
    main_py -.->|imports| ext_pygame
    ext_time["time"]
    class ext_time ext;
    main_py -.->|imports| ext_time
    ext_pyaudio["pyaudio"]
    class ext_pyaudio ext;
    main_py -.->|imports| ext_pyaudio
    ext_wave["wave"]
    class ext_wave ext;
    main_py -.->|imports| ext_wave
    ext_soundfile["soundfile"]
    class ext_soundfile ext;
    main_py -.->|imports| ext_soundfile
    ext_matplotlib_pyplot["matplotlib.pyplot"]
    class ext_matplotlib_pyplot ext;
    main_py -.->|imports| ext_matplotlib_pyplot
    ext_scipy_fft["scipy.fft"]
    class ext_scipy_fft ext;
    main_py -.->|imports| ext_scipy_fft
    ext_PyQt5_QtWidgets["PyQt5.QtWidgets"]
    class ext_PyQt5_QtWidgets ext;
    main_py -.->|imports| ext_PyQt5_QtWidgets
    ext_PyQt5_QtGui["PyQt5.QtGui"]
    class ext_PyQt5_QtGui ext;
    main_py -.->|imports| ext_PyQt5_QtGui
    ext_PyQt5["PyQt5"]
    class ext_PyQt5 ext;
    main_py -.->|imports| ext_PyQt5
    ext_PyQt5_QtCore["PyQt5.QtCore"]
    class ext_PyQt5_QtCore ext;
    main_py -.->|imports| ext_PyQt5_QtCore
    ext_mpl_toolkits_mplot3d["mpl_toolkits.mplot3d"]
    class ext_mpl_toolkits_mplot3d ext;
    main_py -.->|imports| ext_mpl_toolkits_mplot3d
```

---

## UML Class Diagram

Auto-generated Mermaid class diagram from parsed class-level symbols. Shows classes, structs, interfaces, traits, and their methods with inheritance and dependency relationships.

```mermaid
classDiagram
  class main_py_ToneGenerator {
    <<class>>
    +wheelEvent(event)
    +__init__(self)
    +play_tone(self)
    +save_tone(self)
    +generate_waveform(self)
  }
```

---

## Code Property Graph

Machine-readable Code Property Graph (CPG) in JSON-LD format. This block allows AI agents to parse the full structural graph without additional file reads. Compatible with GraphRAG pipelines.

```json
{"@context": "https://schema.org", "analysis": {"communities": [], "god_nodes": [{"node_id": "main.py", "score": 0.6}], "surprising_connections": []}, "edges": [{"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "sys"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "pygame"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "pyaudio"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "wave"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "soundfile"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "matplotlib.pyplot"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "scipy.fft"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "PyQt5.QtWidgets"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "PyQt5.QtGui"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "PyQt5"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "PyQt5.QtCore"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "main.py", "target": "mpl_toolkits.mplot3d"}], "generator": "readmenator", "metadata": {"edge_count": 146, "file_count": 1, "language_count": 1, "symbol_count": 6}, "nodes": [{"id": "main.py", "kind": "module", "label": "main.py", "language": "py", "sha256": "d7bdb20cce7cff53", "symbol_count": 6, "symbols": [{"kind": "function", "line": 17, "name": "wheelEvent", "signature": "def wheelEvent(event)"}, {"kind": "class", "line": 25, "name": "ToneGenerator", "signature": "class ToneGenerator(QWidget)"}, {"kind": "method", "line": 26, "name": "__init__", "signature": "def __init__(self)"}, {"kind": "method", "line": 62, "name": "play_tone", "signature": "def play_tone(self)"}, {"kind": "method", "line": 98, "name": "save_tone", "signature": "def save_tone(self)"}, {"kind": "method", "line": 126, "name": "generate_waveform", "signature": "def generate_waveform(self)"}]}], "type": "CodePropertyGraph", "version": "1.0"}
```

---

## Architecture Reference

### PY (1 files)

#### `main.py`
**Path:** `main.py`

**Classes:**
- `ToneGenerator` (line 25) `class ToneGenerator(QWidget)`

**Functions:**
- `wheelEvent` (line 17) `def wheelEvent(event)`

**Methods:**
- `__init__` (line 26) `def __init__(self)`
- `play_tone` (line 62) `def play_tone(self)`
- `save_tone` (line 98) `def save_tone(self)`
- `generate_waveform` (line 126) `def generate_waveform(self)`
