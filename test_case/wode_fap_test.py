#coding:utf-8
import pytest
import requests
'''查询、添加、修改、删除发票'''
Url = "https://mysteelapi.steelphone.com/v4/basicInfo/queryBill.htm?&isPad="

def test_chaxun_fapiao():
	payload = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF'} 
	r = requests.post(Url,params = payload)
	code = r.status_code
	result = r.json()
	assert code == 200
	assert result['result'] == 'true'
	#print(result)

	if result['bills'] == []:
		'''添加发票'''
		url01 = "https://mysteelapi.steelphone.com/v4/basicInfo/saveBill.htm?&isPad="
		body01 = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF','creditCode':'123456789012345','companyName':'测试123456','type':'0','classify':'1'}
		result01 = requests.post(url01,data = body01).json()
		assert result01['result'] == 'true'
		a = result01['id']
		#print(a)
		'''修改发票'''
		url02 = "https://mysteelapi.steelphone.com/v4/basicInfo/updateBill.htm?&isPad="
		body02 = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF','creditCode':'123456789012345','companyName':'测试123','id':a,'type':'0','classify':'1'}
		result02 = requests.post(url02,data = body02).json()
		assert result02['result'] == 'true'

		'''删除发票'''
		url03 = "https://mysteelapi.steelphone.com/v4/basicInfo/deleteBill.htm?&isPad="
		body03 = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF','id':a}
		result03 = requests.post(url03,data = body03).json()
		assert result03['result'] == 'true'
	else:
		'''修改发票'''
		b = result['bills'][0]['id']
		#print(b)
		url02 = "https://mysteelapi.steelphone.com/v4/basicInfo/updateBill.htm?&isPad="
		body02 = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF','creditCode':'123456789012345','companyName':'测试123','id':b,'type':0,'classify':1}
		result02 = requests.post(url02,data = body02).json()
		#print(result02)
		assert result02['result'] == 'true'

		'''删除发票'''
		url03 = "https://mysteelapi.steelphone.com/v4/basicInfo/deleteBill.htm?&isPad="
		body03 = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF','id':b}
		result03 = requests.post(url03,data = body03).json()
		assert result03['result'] == 'true'
	
if __name__ == '__main__':
	pytest.main(["-s", "wode_fap_test.py"])