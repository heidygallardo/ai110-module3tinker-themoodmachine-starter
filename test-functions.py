from mood_analyzer import MoodAnalyzer

m = MoodAnalyzer() 

print(m.preprocess('Hello, World!')) # expected output: ['hello', 'world']
print(m.preprocess("don't stop")) # expected output: ['don't', 'stop']
print(m.preprocess('happy,sad')) # expected output: ['happy,sad']
print(m.preprocess('!!! :) ???')) # expected output: []

print(m.score_text('I love this')) # expected output: 1
print(m.score_text('not happy')) # expected output: -1
print(m.score_text('not bad')) # expected output: 1
print(m.score_text('not very happy')) # expected output: -1
print(m.score_text('happy happy')) # expected output: 2
print(m.score_text('this is fine')) # expected output: 0

print(m.explain('I love this!!')) # 'love' should now count