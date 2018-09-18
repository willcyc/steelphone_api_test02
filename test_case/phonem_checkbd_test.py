#coding:utf-8
import pytest
import requests

Url = "http://mysteelapi.steelphone.com/v4/wxInfo/checkNumber.htm?&isPad="
def test_get_success():
	'''检查手机号是否已绑定过微信号'''
	body = {'number':'13839205941','machineCode':'90526B160362A7A4FECA22411080F8CF'}
	r = requests.post(Url,data=body)
	#print(r)
	code = r.status_code
	assert code == 200
	result = r.json()
	#print(result)
	if result['result']== 'true' and result['isConnect'] == 'yes':
		print("该手机号已绑定过微信号")
	elif result['result']== 'false' and result['errorstr'] == '该账户已在其他设备上登录，请联系管理员！':
		print("请清空机器码")
	else:
		print("该手机号未绑定过微信号")

if __name__ == '__main__':
	pytest.main(["-s", "phonem_checkbd_test.py"])