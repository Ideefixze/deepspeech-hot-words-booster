import deepspeech
from deepspeech import Model, version
import numpy as np
import wave
import itertools

#Load the model and the scorer
DeepSpeech = Model("deepspeech-0.9.2-models.pbmm")
DeepSpeech.enableExternalScorer("deepspeech-0.9.2-models.scorer")

#Prints out a Cartesian product of hotwords and their prios
def test_file(filename, hotwords, min_prio, max_prio, prio_steps):

    fin = wave.open(filename, 'rb')
    audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)
    fin.close()

    prio_lists = np.linspace(min_prio, max_prio,prio_steps).tolist()

    prio_product = itertools.product(prio_lists, repeat=len(hotwords))
    for x in itertools.product(prio_lists, repeat=len(hotwords)):
        DeepSpeech.clearHotWords()
        for y in enumerate(hotwords):
            DeepSpeech.addHotWord(hotwords[y[0]], x[y[0]])
        
        print(f"{hotwords} = {x} :: [{DeepSpeech.stt(audio)}]")

# Example of a valid input:
# audio/filename.wav
# hot
# cold
# ?
# -100
# 100
# 3
#
# This tests combinations of hot-words: 'hot' and 'cold' on audiofile 'filename.wav'
# using prios from range [-100;100] by doing 3 steps: [-100, 0, 100]
# You can add up as many hot-words as you want. '?' is used as a end of an hot-words input.
if __name__ == '__main__':
    filename = input()
    hotwords = []
    p = input()
    while (p !="?"):
        hotwords.append(p)
        p = input()
    min_prio = float(input())
    max_prio = float(input())
    prio_steps = int(input())

    if(min_prio>=max_prio):
        print("Error: min_prio can't be bigger than max_prio.")
    else:
        test_file(filename, hotwords, min_prio, max_prio, prio_steps)