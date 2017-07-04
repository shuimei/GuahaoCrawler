#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from PageTemplate import HospitalList
from rules import hospitals_list
import pandas as pd
reload(sys)
sys.setdefaultencoding("utf-8")

def main():
	url_head = "https://www.guahao.com/hospital/areahospitals"
	pi = "all"
	p = "全国"
	hospital_num = 7892
	pageNos = range(1, hospital_num/10+2)
	data = pd.DataFrame()
	for pageNo in pageNos:
		hospitals = HospitalList(url_head, pi, p, pageNo)
		content = hospitals.get_response(hospitals["fields"])
		name = content['name']
		page = content['page_link']
		rank = content['rank']
		tel = content['tel']
		addr = content['address']
		order = content['order']
		t = pd.DataFrame(content)
		data = data.append(t)
		print pageNo
	data.to_csv("%s_hospitals.csv"%p)


if __name__ == '__main__':
	main()
