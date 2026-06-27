"""
Quick checks for MoodAnalyzer.

Run with:
    python test_functions.py
"""

from mood_analyzer import MoodAnalyzer

m = MoodAnalyzer()

print("=== preprocess ===")
print(m.preprocess("I LOVE this!! :) "))   # expect ['i', 'love', 'this']
print(m.preprocess("don't stop"))          # expect ["don't", 'stop']
print(m.preprocess("!!! :) ???"))          # expect []

print("\n=== score_text ===")
print(m.score_text("I love this"))         # expect 1
print(m.score_text("not happy"))           # expect -1
print(m.score_text("not bad"))             # expect 1
print(m.score_text("not very happy"))      # expect -1
print(m.score_text("happy happy"))         # expect 2
print(m.score_text("this is fine"))        # expect 0

print("\n=== explain ===")
print(m.explain("I love this!!"))          # 'love' should now count
