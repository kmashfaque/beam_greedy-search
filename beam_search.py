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

# And:

# 𝑃("improves"∣"AI") = 0.7

# 𝑃("optimizes"∣"AI") =0.3


def beam_search_debug(beam_width=3):
    beam = [([], "<s>", 0.0)]
    step = 0

    while True:
        # print(f"\n--- Step {step} ---")
        # print("Current Beam:")
        # for seq, last_word, score in beam:
        #     print(f"  Sequence: {' '.join(seq)} | Last word: {last_word} | Score: {score:.4f}")

        candidates = []

        for seq, last_word, score in beam:
            if last_word == "</s>":
                candidates.append((seq, last_word, score))
                continue

            for next_word, prob in bigram_probs[last_word].items():
                new_seq = seq.copy()
                if next_word != "</s>":
                    new_seq.append(next_word)

                new_score = score + math.log(prob)
                candidates.append((new_seq, next_word, new_score))

                # print(f"    Expanded: {' '.join(new_seq)} | Next: {next_word} | Score: {new_score:.4f}")

        candidates.sort(key=lambda x: x[2], reverse=True)

        # print("\nCandidates after sorting:")
        # for seq, last_word, score in candidates:
        #     print(f"  {' '.join(seq)} | Last word: {last_word} | Score: {score:.4f}")

        beam = candidates[:beam_width]

        # print("\nBeam after pruning:")
        # for seq, last_word, score in beam:
        #     print(f"  {' '.join(seq)} | Last word: {last_word} | Score: {score:.4f}")

        if all(last_word == "</s>" for _, last_word, _ in beam):
            break

        step += 1

    best_sequence = max(beam, key=lambda x: x[2])
    return best_sequence[0], best_sequence[2]

result, score = beam_search_debug(beam_width=3)
print("\nFinal Result:", " ".join(result))
print("Final Score:", score)
