#coding:utf-8
import pytest
import requests
'''价格页面-添加定制'''
Url = "https://mysteelapi.steelphone.com/v4/market/sub/create.htm?&isPad="
def test_create_success():
	param = {'key1':'高线Ф6.5-10HPB300申特,螺纹钢Ф10HRB400申特,高线Ф6.5HPB235萍钢,'}
	headers = {
				'X-Tingyun-Id':'uGv7Tc5NyIw;c=2;r=1786430670;u=33c4eb74e06546e4b45c102139b0305e::4C34FFE3352222AA',
				'Content-Type':'application/x-www-form-urlencoded',
				'Content-Length':'JSON.stringify(param).length',  #定制内容字符串长度
				#'Content-Length':'240',
				'Host':'mysteelapi.steelphone.com',
				'Connection':'Keep-Alive',
				'Accept-Encoding':'gzip',
				'User-Agent':'okhttp/3.8.1'
				}
	
	body = {
			'tableId':'15278',
			'userId':'566453',
			"unionKey":param['key1'],
			#'unionKey':'螺纹钢Ф10HRB400申特,',
			'machineCode':'90526B160362A7A4FECA22411080F8CF',
			'name':'上海建筑钢材市场行情'
			}
			
	result = requests.post(Url,headers = headers,data = body).json()
	#print(result)
	assert result['result'] == 'true'

if __name__ == '__main__':
	pytest.main(["-s", "Price_subcreate_test.py"])