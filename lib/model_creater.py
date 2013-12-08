import json
class ModelCreator(object):
	def __init__(self, occ, data_set, data_counts, item_type = 'dp'):
		self.occ = occ
		self.data_set = data_set
		self.item_type = self.item_type
		self.data_counts = data_counts
		if occ == 0:
			self.save()

	def save(self):
		f = open('../model/data.json', 'w')
		f.write(self.data_counts)
		f.close()

	def create(self):
		for cat,count in self.data_counts.iteritems():
			model = {}
			for i in len(self.data_set[cat]):
				if i not in range(self.occ/10*count, (self.occ+1)/10*count):
					if item_type == 'dp':
						dp = json.loads(self.data_set[cat][i][4])	#Use D patterns
						self.update_occurence(model, dp)
					elif item_type == 'word':
						sents = json.loads(self.data_set[cat][i][3])	#Use Words
						self.update_occurences_word(model, sents)

			f = open('../model/'+cat.lower()+'.json', 'w')
			f.write(model])
			f.close()

	def update_occurences_word(self, model, sents):
		for words in sents:
			for word in words:
				try:
					model[word] += 1
				except:
					model[word] = 1
		return model

	def update_occurences(self, cat, dp):
	    for k,v in dp.iteritems():
	        try:
	            cat[k] += v
	        except:
	            cat[k] = v
	    return cat
