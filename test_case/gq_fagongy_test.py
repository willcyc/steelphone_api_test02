#coding:utf-8
import pytest
import requests

Url = "https://mysteelapi.steelphone.com/v4/gq/create.htm?"
def test_get_success():
	'''供应-发布成功'''
	body = {'breedAttr':'2472-规格-sSpecification-A00;2473-产地/牌号-sFactory-西南铝','breedId':'849','breedName':'铝锭','city':'曲靖','detailInfo':'',
	'gqImgUrl':'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/gq/1530618361609.jpg','id':'0','machineCode':'90526B160362A7A4FECA22411080F8CF','price':'',
	'prodNum':'','province':'云南','supplyType':'1','unit':'元/吨','userId':'744408'}
	r = requests.post(Url,data = body)
	code = r.status_code
	assert code == 200

if __name__ == '__main__':
	pytest.main(["-s", "gq_fagongy_test.py"])