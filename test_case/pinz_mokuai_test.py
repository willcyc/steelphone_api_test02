#coding:utf-8
import requests
import pytest
'''建筑钢材首页模块'''
def test_get_success():	
	url = "https://mysteelapi.steelphone.com/v4/channel/breedIndex.htm?&isPad="
	body = {'userId':'503879','machineCode':'90526B160362A7A4FECA22411080F8CF','breedId':'010101','protocolVersion':'4.7.2'}
	result = requests.post(url,data = body).json()
	#print(result)
	na = ['价格','钢厂','成交','库存','调研','报告','汇总','产品']
	for i in range (0,8):
		assert result['modules'][i]['name'] == na[i]
	assert result['articleChannels'][0]['name'] == '直播'
	assert result['articleChannels'][1]['name'] == '热点资讯'

if __name__ == '__main__':
	pytest.main(["-s", "pinz_mokuai_test.py"])