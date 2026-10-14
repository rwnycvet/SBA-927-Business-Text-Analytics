# SBA 927 Business Text Analytics

**Author:** Richard Watson Jr.  
**Course:** Per Scholas — SBA 927 Business Text Analytics  
**Repository:** https://github.com/rwnycvet/SBA-927-Business-Text-Analytics

This project analyzes 12 supplied passages about *I, Robot* using Python,
NLTK, and TextBlob. It demonstrates tokenization, preprocessing, stemming,
lemmatization, part-of-speech (POS) tagging, named entity recognition (NER),
and sentiment analysis. The report also documents prompt-based language-model
experiments performed during the assessment.

## Project files

| File | Purpose |
|---|---|
| `sba927_analysis.py` | Submitted Python analysis script |
| `SBA927.txt` | Required input dataset, with one passage per line |
| `SBA927_results.txt` | Saved preprocessing, stemming, lemmatization, POS, and NER output for all 12 passages |
| `SBA_927_Business_Text_Analytics_Report.docx` | Per Scholas formatted report, including the full results appendix |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Excludes local environments, caches, and credentials |

## Requirements

- Python 3 with pip
- Internet access on the first run to download the required NLTK resources
- A terminal opened in the project folder, where both the Python script and `SBA927.txt` are located

No API key is needed to run the Python script. The prompt-based language-model
experiments are documented in the report and are not executed by this script.

## Run on Windows with PowerShell

Download this repository using **Code → Download ZIP**, extract it, and open
the extracted folder in VS Code. Open a terminal in that folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe sba927_analysis.py
```

These commands use the virtual environment directly; activating it is optional.
If Python is available through `py` instead of `python`, use
`py -m venv .venv` for the first command.

## Run on macOS or Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python sba927_analysis.py
```

## What the script does

1. Reads the 12 lines of `SBA927.txt` from the current working directory.
2. Tokenizes and cleans the text, lowercases tokens, and removes stop words.
   It retains `no`, `not`, and `nor` and expands the dataset's `doesn't` to
   `does not` to preserve negation.
3. Applies Porter stemming and default noun-based WordNet lemmatization.
4. Performs POS tagging and NER on the original text.
5. Prints TextBlob sentiment polarity for passages 5, 8, and 12.
6. Writes the full token, stem, lemma, POS, and NER output to
   `SBA927_results.txt` in the current folder, replacing any existing copy.

NLTK downloads `punkt`, `punkt_tab`, `stopwords`, `wordnet`,
`averaged_perceptron_tagger_eng`, `maxent_ne_chunker_tab`, and `words` as needed.

## Observed results and interpretation

- The script processes 12 passages and preserves `not` in Sonny's statement.
- NER identifies Susan Calvin as `PERSON` but makes mistakes with the movie
  title, V.I.K.I., and Sonny. For example, Sonny is labeled `GPE` in passage 11.
- Default noun lemmatization can produce misleading forms, including
  `serves` → `serf` and `leaves` → `leaf`.
- The recorded TextBlob polarity scores are `0.200` for passage 5,
  `-0.033` for passage 8, and `0.000` for passage 12.
- Passage 5's positive numeric score conflicts with the passage's sinister
  turn, showing why automated sentiment scores require contextual review.

The supplied dataset has no reference sentiment labels. The report's model
comparisons are small, manually reviewed examples, not benchmark accuracy
measurements. No model was fine-tuned. Outputs can differ across library or
NLTK-resource versions; the committed results preserve the assessment run.

## Troubleshooting

- **`SBA927.txt` not found:** open the terminal in the project folder before
  running the script. Keep the dataset filename exactly `SBA927.txt`.
- **Missing Python module:** install `requirements.txt` using the same Python
  interpreter that runs the script.
- **NLTK resource error:** check internet access and download availability,
  then rerun the script. Keep NLTK resources outside the repository.

## Report and submission

Download the `.docx` report to view it in Word or another compatible reader.
Its Appendix D includes the complete 12-passage output. The report uses
transcribed console evidence; actual VS Code screenshots are not included.

The final Canvas submission should be the repository URL:

https://github.com/rwnycvet/SBA-927-Business-Text-Analytics
