# deepspeech-hot-words-booster
Testing of different boost values for hot-words in Mozilla's STT: Deepspeech.

# How to use?
Run using python, while having a ```deepspeech``` installed. This works from version 0.9.0.
Example of an input after you run this script:
```
audio/filename.wav
hot
cold
?
-100
100
3
```
This tests combinations of hot-words: 'hot' and 'cold' on audiofile 'filename.wav'
Using prios/boost values from range [-100;100] by doing 3 steps: [-100, 0, 100]
You can add up as many hot-words as you want. '?' is used as a end of an hot-words input.

# Analysis

## Original post

This script was used in analyzing current state of hot-words feature in Mozilla's STT. 
Original post on Mozilla's Forum: ![here](https://discourse.mozilla.org/t/practical-tests-of-hot-word-feature-and-default-models-accuracy/73855/4)

## Conclusions

- Adding hot-word that has a space, like: “another one” doesn’t change behavior. Probably because it doesn’t appear in word detection mechanism and is not modified.

- Use hot-words if you need to detect one word and you can ignore everything else that comes after that word, because of letter splitting bug. Example: “listen”.

- You can use negative priority for words no to occur in the output, but be careful of this word to appear as a splitted one: “another” -> “an other” or as a word of similar sound: “gold” -> ”god”.

- Usage hot-words for calibrating accuracy is not the perfect one but add a very small priority and it could work. The value is dependant on your audio, it could be big or small to see a difference, but no intuitive way of determining accuracy gain was found.

- Nonexistent words as hot-words or words that share no similarity to the given hot-word cause no change if the audio doesn’t include the sound of that word.

- No software related errors caused by adding, removing, clearing hot-words were detected.

## Documentation

Those findings would be soon added to the official Deepspeech documentation.

