import requests
from lxml import etree


class HospitalList(object):
	"""docstring for HospitalList"""
	
	def __init__(self, url_head, pi, p, pageNo):
		super(HospitalList, self).__init__()
		self.url_head = url_head
		self.pi = pi
		self.p = p
		self.pageNo = pageNo
		self.request = self.make_request()

	def make_request(self):
		params = {
			'pi': self.pi,
			'p': self.p,
			'pageNo': self.pageNo
		}
		s = requests.Session()
		return s.get(self.url_head, params=params)

	def get_response(self, rules_dict):
		r = self.request
		content = r.content
		selector = etree.HTML(content)
		fields = rules_dict.keys()
		contents_dict = {}
		for field in fields:
			contents_dict[field] = selector.xpath(rules_dict[field])
		return contents_dict