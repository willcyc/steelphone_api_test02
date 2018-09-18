#coding:utf-8
import pytest
import requests

'''价格板块根据条件筛选'''
Url = "http://mysteelapi.steelphone.com/v4/market/filter.htm?&isPad="

def test_breedName_null():
	sx = '螺纹钢,高线_Ф12,Ф14_HRB500E,HRB400E_敬业,新兴铸管'
	body = {'tableId':'12911','userId':'566453','vals':sx,'heads':'breed_spec_material_place','isSub':'0','marketId':'30170423'}
	result = requests.post(Url,data = body).json()
	#print(result)
	if result['markets'] != []:
		for i in range(0,len(result['markets'])):
			#print(result['markets'][i])
			assert result['markets'][i]['spec'] in sx
			assert result['markets'][i]['breed'] in sx
			assert result['markets'][i]['place'] in sx
			assert result['markets'][i]['material'] in sx
	else:
		print("请重新选择筛选项")

if __name__ == '__main__':
	pytest.main(["-s", "Price_shaixuan_test.py"])