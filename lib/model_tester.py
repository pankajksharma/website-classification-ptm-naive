import json

MODEL_DIR = '../model/'

class ModelTester(object):
	def __init__(self, occ, data_set, data_counts, type='dp'):
		self.occ = occ
		self.type = type
		self.data_set = data_set
		self.data_counts = data_counts
		self.cat_counts = json.load(open(MODEL_DIR+"data.json"))
		self.total_words = sum(self.cat_counts)
		self.category_counts = {
                u'entertain'  :json.load(open(MODEL_DIR+"entertain.json")),
                u'politics'   :json.load(open(MODEL_DIR+"politics.json")),
                u'econonics'  :json.load(open(MODEL_DIR+"econonics.json")),
                u'sports'     :json.load(open(MODEL_DIR+"sports.json")),
                u'education'  :json.load(open(MODEL_DIR+"education.json")),
                u'religion'   :json.load(open(MODEL_DIR+"religion.json")),
                u'health'     :json.load(open(MODEL_DIR+"health.json")),

        }
        self.categories = [u'entertain',u'politics',u'econonics',u'sports',u'education',u'religion',u'health']

	def test(self):
		true_cases = 0
		for cat, count in self.data_counts.iteritems():
			for row in self.data_set[cat][self.occ/10*count, (self.occ+1)/10*count]:
				cat = json.loads(row[2])[0]
				sents = json.loads(row[3])
				dp = json.loads(row[4])
				if self.type == 'dp':
					if cat == self.get_probable_category_dp(dp):
						true_cases += 1
				elif self.type == 'word':
					if cat == self.get_probable_category_word(sents):
						true_cases += 1
		return true_cases

	def get_probable_category_dp(self, dp):
		pc = {u'entertain':1.0,u'politics':1.0,u'econonics':1.0,u'sports':1.0,u'education':1.0,u'religion':1.0,u'health':1.0}
		for cat in categories:
			words_in_category = sum([word_count for  word_count in self.category_counts[cat]])
			words_count = self.total_words + words_in_category
			for w in dp:
				word = str(w)
                if word not in category_counts[category]:
                    pc[category]=pc[category]*Decimal((1.0/(n+v)))
                else:
                    pc[category]=pc[category]*Decimal(((1.0+category_counts[category][word])/(n+v)))
      category = max(pc, key=pc.get)
      return category

	def get_probable_category_dp(self, sents):
		pc = {u'entertain':1.0,u'politics':1.0,u'econonics':1.0,u'sports':1.0,u'education':1.0,u'religion':1.0,u'health':1.0}
		for cat in categories:
			words_in_category = sum([word_count for  word_count in self.category_counts[cat]])
			words_count = self.total_words + words_in_category
			for words in sents:
				for w in words:
					word = str(w)
	                if word not in category_counts[category]:
	                    pc[category]=pc[category]*Decimal((1.0/(n+v)))
	                else:
	                    pc[category]=pc[category]*Decimal(((1.0+category_counts[category][word])/(n+v)))
      category = max(pc, key=pc.get)
      return category
