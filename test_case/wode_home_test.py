#coding:utf-8
import pytest
import requests
'''我的-首页'''
Url = "https://mysteelapi.steelphone.com/v4/user/info/my.htm?"

def test_get_success():	
	payload = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF'}
	r = requests.post(Url,params = payload)
	result = r.json()
	#print(result)

	assert result['adminName'] == '岳宗平'
	assert result['inviteUrl'] == 'https://m.steelphone.com/v4/app/invite/qm/toIndex.ms?cellphone=ge2vsn22gi1dkpjwge'
	assert result['encCellphone'] == 'ge2vsn22gi1dkpjwge'
	assert result['registerTime'] == '2017-03-06'
	assert result['userType'] == '1'

if __name__ == '__main__':
	pytest.main(["-s", "wode_home_test.py"])