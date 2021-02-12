# deepspeech-hot-words-booster
Testing of different boost values for hot-words in Mozilla's STT: DeepSpeech.

# How to use?
Run using `python 3.9`, while having a `deepspeech` installed.

Put files: `model.pbmm` and `scorer.scorer` in the same directory so this script can load up the model and the scorer correctly.

This works from version 0.9.0 since it was the version that added this feature.
Example of usage:
```
hotwords_adjusting.py --model model.pbmm --scorer.scorer --audio audio/filename.wav --min -100.0 --max 100.0 --steps 3 --hot_words hot,cold
```
This tests combinations of hot-words: 'hot' and 'cold' on audiofile 'filename.wav'
Using prios/boost values from range [-100;100] by doing 3 steps: [-100, 0, 100]
You can add up as many hot-words as you want. '?' is used as a end of an hot-words input.

There are default test cases prepared from which conclusions below were taken in file: `testcases.txt`
These test cases are different from files used in original docs (see link below), but the conclusions from those test cases are the same.

Those audio files are used according to the "Fair use" law: for nonprofit educational and scientific usage.

# Analysis

## Original post

This script was used in analyzing current state of hot-words feature in Mozilla's STT. 
Original post on Mozilla's Forum: ![here](https://discourse.mozilla.org/t/practical-tests-of-hot-word-feature-and-default-models-accuracy/73855/4)

The feature itself is still a small mystery for the DeepSpeech community. The exploratory testing was made in order to create an overall strategy in using hot-words in practice.

## Conclusions (19.01.2021, Deepspeech 0.9.3)

- Adding hot-word that has a space, like: “another one” doesn’t change behavior. Probably because it doesn’t appear in word detection mechanism and is not modified.

- Use hot-words if you need to detect one word and you can ignore everything else that comes after that word, because of letter splitting bug. Example: “listen”.

- You can use negative priority for words no to occur in the output, but be careful of this word to appear as a splitted one: “another” -> “an other” or as a word of similar sound: “gold” -> ”god”.

- Usage hot-words for calibrating accuracy is not the perfect one but add a very small priority and it could work. The value is dependant on your audio, it could be big or small to see a difference, but no intuitive way of determining accuracy gain was found.

- Nonexistent words cause no change in the transcription.

- Words that share no similarity to the given hot-word cause no change if the audio doesn’t include the sound of that word. 

- No change in transcription was found while a hot-words were an "extension" of a transcribed word. E.g.: 'knowledge' as hot-word didn't change 'know' to any other word in the transcription. Closer similarity may change it though. Change is more noticable on words that share similarity on their prefix rather than suffix.

- No software related errors caused by adding, removing, clearing hot-words were detected.

## Documentation

Those findings would be soon added to the official DeepSpeech documentation.

