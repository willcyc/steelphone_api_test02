#coding:utf-8
import pytest
import requests
from parameterized import parameterized

'''首页广告-行情地图'''	
Url = "https://mysteelapi.steelphone.com/v4/getAdv.htm?"
@parameterized.expand([
	#用例名称，参数：type、id，实际结果，预期结果
	("both_null",'','','adv',[]),
	("id_null",6,'','adv',[]),
	("type_error_null",4,1,'adv',[]),
	("id_error",6,5,'adv',[]),
	("both_error_null",5,5,'adv',[])
])

def test_case(_,type,id,a,c):
	result = requests.post(Url,params = {'type':type,'id':id}).json()
	#print(result)
	assert result[a] == c
	#print(a)

def test_hqmap_type_null():
	'''参数type为空：启动页广告'''
	result = requests.post(Url,params = {'type':'','id':1}).json()
	#print(self.result)
	#self.assertEqual(self.result['adv'][0]['title'],"2018半年会--夏尊恩")

def test_hqmap_success():
	'''行情地图查询成功'''
	result = requests.get(Url,params = {'type':6,'id':1}).json()
	#print(result)
	
	for val in result['adv']:
		#print(val)
		pass
	#print(val['id'])
	assert val['id'] == '3685'     #广告id
	assert val['title'] == '我的钢铁行情地图'    #广告标题
	assert val['description'] == '6'   #广告位置
	assert val['src'] == 'https://m.steelphone.com/app/map/index.html?UAlocal=1&dt=1#hqmap'  #广告跳转地址
	assert val['type'] == '1'    #广告的频道id
	assert val['url'] == 'http://mfs.mysteelcdn.com/group1/M00/04/DB/rBL63lpe7E6AAR0pAAA1d-l94mQ951.png'   #广告图片路径	

if __name__ == '__main__':
	pytest.main(["-s", "Home_hqmap_test.py"])