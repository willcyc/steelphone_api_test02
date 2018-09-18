#coding:utf-8
import pytest
import requests

Url = "https://mysteelapi.steelphone.com/v4/gq/breedUnit.htm?&isPad="
def test_get_success():
	'''供求-单位'''
	r = requests.post(Url)
	#print(r)
	code = r.status_code
	assert code == 200
	result = r.json()
	#print(result)
	priceList = ['元/吨', '元/千克', '元/个', '元/卷', '元/米', '元/平米']
	numList = ['吨', '千克', '个', '卷', '米', '平米']
	assert result['priceList'] == priceList
	assert result['numList'] == numList

if __name__ == '__main__':
	pytest.main(["-s", "gq_danwei_test.py"])