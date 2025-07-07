#tuples
top_scores = (100, 95, 92, 92, 88, 85)
print(top_scores[0])
print(top_scores[2])
print("the length of the tuple is:", len(top_scores))
#tuples are immutable
''' 
top_scores[0] = 99 
TypeError: 'tuple' object does not support item assignment
'''
#tuples methods
print(top_scores.count(92))
print(top_scores.index(85))