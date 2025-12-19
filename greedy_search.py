import math

# Bigram probabilities P(next_word | current_word)
# A bigram language model assumes:

# The probability of the next word depends only on the previous word.

# This is a Markov assumption (order = 1).

bigram_probs = {
    "<s>": {"AI": 0.6, "Production": 0.4},
    "AI": {"improves": 0.3, "optimizes": 0.7},
    "Production": {"needs": 0.6, "uses": 0.4},
    "improves": {"efficiency": 0.6, "quality": 0.4},
    "optimizes": {"process": 1.0},
    "needs": {"optimization": 1.0},
    "uses": {"AI": 1.0},
    "efficiency": {"</s>": 1.0},
    "quality": {"</s>": 1.0},
    "process": {"</s>": 1.0},
    "optimization": {"</s>": 1.0}
}
# "AI": {"improves": 0.7, "optimizes": 0.3}

# It means:

# If the current word is “AI”, then:

# Probability of next word being “improves” is 0.7

# Probability of next word being “optimizes” is 0.3

# 𝑃("improves"∣"AI") = 0.7

# 𝑃("optimizes"∣"AI") =0.3



# GREEDY search

def greedy_search():
    current_word = "<s>"
    sentence = []
    score = 0.0

    while current_word != "</s>":
        next_words = bigram_probs[current_word]
        next_word = max(next_words,key=next_words.get)

        score += math.log(next_words[next_word])
        if next_word != "</s>":
            sentence.append(next_word)
        
        current_word = next_word
    
    return sentence, score

greedy_result, greedy_score = greedy_search()
print("Greedy result", " ".join(greedy_result))
print("Greedy Score", greedy_score)