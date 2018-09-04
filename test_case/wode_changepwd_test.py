#coding:utf-8
import pytest
import requests

'''我的-修改密码'''
Url = "https://mysteelapi.steelphone.com/v4/user/password/update.htm?"
def test_oldpwd_error():
	'''旧密码错误'''
	result = requests.post(Url,params = {'newPassword':'123456','userId':'566453','oldPassword':'12345','machineCode':'4B49B9A413D01B2EB2139C82782AF1FB'}).json()
	assert result['result'] == 'false'

def test_newpwd_error():
	'''新密码格式错误'''
	result = requests.post(Url,params = {'newPassword':'123456测试','userId':'566453','oldPassword':'123456','machineCode':'4B49B9A413D01B2EB2139C82782AF1FB'}).json()
	assert result['result'] == 'false'

def test_change_success():
	'''修改成功'''
	r = requests.post(Url,params = {'newPassword':'123456','userId':'566453','oldPassword':'123456','machineCode':'4B49B9A413D01B2EB2139C82782AF1FB'})
	result = r.json()
	code = r.status_code	
	assert code == 200
	assert result['result'] == 'true'
		
if __name__ == '__main__':
	pytest.main(["-s", "wode_changepwd_test.py"])