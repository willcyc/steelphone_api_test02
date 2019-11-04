#coding:utf-8
import requests
import pytest
'''定制品种'''
def test_batch_Create():
	url = "http://mysteelapi.steelphone.com/v4/subBreedInfo/batchCreate.htm?"
	result = requests.post(url,params = {"userId":"1052762","breedIds":"01,08,02,07,03"})  #01-黑色金属 08-建筑材料 02-有色金属 07-农产品 03-能源化工
	code = result.status_code
	assert code == 200

if __name__ == '__main__':
	pytest.main(["-s", "dingzhi_batchCreate.py"])