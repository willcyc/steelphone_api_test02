#coding:utf-8
import pytest
import requests

Url = "https://mysteelapi.steelphone.com/v4/gq/create.htm?"
def test_get_success():
	'''求购-发布成功'''
	body = {'breedAttr':'1-规格-sSpecification-∮10;2-材质-sMaterial-HRB335;3-产地/厂家-sFactory-申特','breedName':'二级螺纹钢','gqImgUrl':'','detailInfo':'',
	'province':'天津','userId':'744408','supplyType':'3','prodNum':'','machineCode':'90526B160362A7A4FECA22411080F8CF','id':'0','city':'天津','unit':'元/吨','price':'','breedId':'38'}
	r = requests.post(Url,data = body)
	#print(r)
	code = r.status_code
	assert code == 200

if __name__ == '__main__':
	pytest.main(["-s", "gq_faqiug_test.py"])