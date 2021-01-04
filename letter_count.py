
import collections
import matplotlib.pyplot as plt
import time

start_time = time.time()

hamlet = '''
	After escaping the musketeers, Don Quixote and Sancho ride to a nearby inn. Once again, Don Quixote imagines the inn is a castle, although Sancho is not quite convinced. Don Quixote is given a bed in a former hayloft, and Sancho sleeps on the rug next to the bed; they share the loft with a muleteer. When night comes, Don Quixote imagines the servant girl at the inn, Helen, to be a beautiful princess, and makes her sit on his bed with him, scaring her. Seeing what is happening, the muleteer attacks Don Quixote, breaking the fragile bed and leading to a large and chaotic fight in which Don Quixote and Sancho are once again badly hurt. Don Quixote's explanation for everything is that they fought with an enchanted Moor. He also believes that he can cure their wounds with a mixture he calls "the balm of Fierabras", which only makes them sick. Don Quixote and Sancho decide to leave the inn, but Quixote, following the example of the fictional knights, leaves without paying. Sancho, however, remains and ends up wrapped in a blanket and tossed up in the air (blanketed) by several mischievous guests at the inn, something that is often mentioned over the rest of the novel. After his release, he and Don Quixote continue their travels.

'''

# d1 = dict()

# for char in hamlet:
# 	if char in d1:
# 		d1[char] = d1[char] + 1
# 	else:
# 		d1[char] = 1
# print(d1)
# x1,y1 = zip(*d1.items())
# plt.bar(x1,y1)
# plt.show()

# d2 = {}
# for char in hamlet:
# 	d2[char] = d2.get(char, 0) + 1
# print(d2)
# plt.bar(d2.keys(),d2.values())
# plt.show()

count = collections.Counter(hamlet)
print(count)
plt.bar(count.keys(), count.values())
plt.show()

print('------%s seconds------' % (time.time() - start_time) )