#coding:utf-8
import requests
import pytest
'''建筑钢材首页指数'''
def test_get_success():	
	url = "http://mysteelapi.steelphone.com/v4/xpic/breedXpicSides.htm?&isPad="
	body = {'userId':'503879','machineCode':'90526B160362A7A4FECA22411080F8CF','breedId':'010101'}
	result = requests.post(url,data = body).json()
	#print(result)
	'''左侧指数'''
	assert result['left'][0]['name'] == '钢材相对指数'
	assert result['left'][0]['url'] == 'https://m.steelphone.com/app/map/index.html?zsoption=gczh&UAlocal=1&zs=1#hqzs'
	assert result['left'][1]['name'] == '钢材综合指数'
	assert result['left'][1]['url'] == 'https://m.steelphone.com/app/map/index.html?zsoption=gczh_abs&UAlocal=1&zs=1#hqzs'
	assert result['left'][2]['name'] == '螺纹相对指数'
	assert result['left'][2]['url'] == 'https://m.steelphone.com/app/map/index.html?zsoption=lwgzs&UAlocal=1&zs=1#hqzs'
	assert result['left'][3]['name'] == '螺纹绝对指数'
	assert result['left'][3]['url'] == 'https://m.steelphone.com/app/map/index.html?zsoption=lwgzs_abs&UAlocal=1&zs=1#hqzs'
	assert result['left'][4]['name'] == '上海螺纹钢指数'
	assert result['left'][4]['url'] == 'https://m.steelphone.com/app/map/index.html?zsoption=shlwgzs&UAlocal=1&zs=1#hqzs'

	'''右侧指数'''
	assert result['right'][0]['name'] == '长材相对指数'
	assert result['right'][0]['url'] == 'https://m.steelphone.com/app/map/index.html?zsoption=cczs&UAlocal=1&zs=1#hqzs'
	assert result['right'][1]['name'] == '长材绝对指数'
	assert result['right'][1]['url'] == 'https://m.steelphone.com/app/map/index.html?zsoption=cczs_abs&UAlocal=1&zs=1#hqzs'
	assert result['right'][2]['name'] == '线材相对指数'
	assert result['right'][2]['url'] == 'https://m.steelphone.com/app/map/index.html?zsoption=xczs&UAlocal=1&zs=1#hqzs'
	assert result['right'][3]['name'] == '线材绝对指数'
	assert result['right'][3]['url'] == 'https://m.steelphone.com/app/map/index.html?zsoption=xczs_abs&UAlocal=1&zs=1#hqzs'
if __name__ == '__main__':
	pytest.main(["-s", "pinz_zhishu_test.py"])