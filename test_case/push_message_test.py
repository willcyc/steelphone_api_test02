#coding:utf-8
import requests
import pytest
'''即时新闻'''
def test_get_success():	
	url = "http://mysteelapi.steelphone.com/v4/message/pushMessage/list.htm?&isPad="
	body = {'userId':'503879','machineCode':'90526B160362A7A4FECA22411080F8CF','page':'1','type':'1'}
	r = requests.post(url,data = body)
	code = r.status_code
	assert code == 200

if __name__ == '__main__':
	pytest.main(["-s", "push_message_test.py"])
