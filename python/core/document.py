class Document:
	def __init__(self, doc_id, name, contents):
		self.doc_id = doc_id
		self.name = name
		self.contents = contents

	def __repr__(self):
		return 'Document ({}, \'{}\')'.format(self.doc_id, self.name)
