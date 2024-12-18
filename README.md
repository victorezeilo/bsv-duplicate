# Detection of Duplicates in Bibtex References

[![GitHub](https://img.shields.io/github/license/bth-dipt-teaching/bsv-duplicate)](./LICENSE)

This repository contains a toy system which detects duplicate entries from `.bib` files which contain a list of references to scientific articles.

> [!CAUTION]
> This is a toy system containing **seeded defects**! Do not use this code for production purposes.

## Repository Structure

The repository contains the following files.

```
├── data : directory containing data
│   └── references.bib : an exemplary data file in .bibtex format
├── doc : directory containing documentation files
│   ├── context-specification.md : context of the system, describing why the system needs to be realized
│   ├── requirements-specification.md : requirements of the system, describing what needs to be realized
│   └── system-specification.md : specification of the system, describing how the system will be realized
├── src : directory containing all source code
│   ├── util: supporting files for the main file
│   │   ├── detector.py : script implementing the duplicate detection
│   │   └── parser.py : script for parsing the raw text file into a list of Article objects
│   └── main.py: main file executing the functionality
└── test : directory containing all test files
```

## Usage

## Testing

## License

Copyright © 2024 by Julian Frattini. 
This work (source code) is available under the [MIT license](./LICENSE).
