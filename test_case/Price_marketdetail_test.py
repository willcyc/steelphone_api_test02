#coding:utf-8
import pytest
import requests

'''价格详情页'''
Url = "https://mysteelapi.steelphone.com/v4/market/detail.htm?"

def test_breedName_null():	
	body = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF','mId':'12488915','tId':'15278','code':'CN310000ST3605220208'}
	result = requests.post(Url,data = body).json()
	#print(result)
	assert result['shareInfo']['channelId'] == body['tId']
	assert result['shareInfo']['objectId'] == body['mId']

if __name__ == '__main__':
	pytest.main(["-s", "Price_marketdetail_test.py"])