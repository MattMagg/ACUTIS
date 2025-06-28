# ACUTIS

ACUTIS is an early stage concept currently represented by a collection of project documents and a small Python codebase. This repository lays the groundwork for future development and organization of the idea.

## Available Documents

- **ACUTIS Main Proposal.rtf** – overview of the concept
- **ProvisionalPatent ACUTIS.rtf** – provisional patent paperwork

All documentation is provided as RTF files in the repository root. High-level
research findings live in `acutis_research.md` and ongoing plans are tracked in
`docs/roadmap.md`.

## Repository Structure

The following directories provide a starting framework:

- `docs/` – supplementary design notes and references
- `src/` – Python source code for simulations and algorithms
- `tests/` – unit tests for the Python modules
- `src/acutis/plugin.py` – example plugin interface for transducers

The current code offers simple abstractions for hardware, collar control, data acquisition, and signal processing. These pieces are intentionally lightweight and will evolve as the project matures.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for a brief guide on synchronizing your branch and resolving conflicts.

## License

This project is licensed under the [MIT License](LICENSE).
