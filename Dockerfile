FROM python:3.9

WORKDIR /PhraseCounter

COPY PhraseCounter.py TestPhraseCounter.py ./

COPY testFiles testFiles/

RUN python3 TestPhraseCounter.py

ENTRYPOINT [ "python", "./PhraseCounter.py" ]