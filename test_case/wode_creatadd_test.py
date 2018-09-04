#coding:utf-8
import pytest
import requests
from parameterized import parameterized
'''添加收件地址'''
Url = "https://mysteelapi.steelphone.com/v4/finance/address/create.htm?"

@parameterized.expand([
	('18790851702','南京路','北京市','566453','测试007','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','','昌平区','北京市','','',200,'result'),
	('18790851703','长安路','北京市','566453','测试008','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','','玄武区','北京市','','',200,'result'),
	('18790851704','中南海','北京市','566453','测试009','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','','崇文区','北京市','','',200,'result')
	#('18790851','中南海','北京市','566453','测试12345678901234567890123456','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','','崇文区','北京市','','',200,'result')
])

def test_creat_success(phone,address,province,userId,receiver,machineCode,id,area,city,postcode,isPad,status,ys):
	payload = {'linkPhone':phone,'address':address,'province':province,'userId':userId,'receiver':receiver,
		'machineCode':machineCode,'id':id,'area':area,'city':city,'postcode':postcode,'isPad':isPad}
	r = requests.post(Url,params = payload)
	code = r.status_code
	result = r.json()
	#print(code)
	#print(result)

	assert code == status
	assert result[ys] == 'true'

if __name__ == '__main__':
	pytest.main(["-s", "wode_creatadd_test.py"])