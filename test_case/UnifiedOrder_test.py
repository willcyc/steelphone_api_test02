#coding:utf-8
import pytest
import requests

'''预支付下单'''
Url = "https://mysteelapi.steelphone.com/v4/finance/pay/unifiedOrder.htm?"
def test_creat_success():
	body = {'attach':'0|||0506-全品种-1200-|||1|||13839205941','coupon':'0','payFee':30000,'totalFee':30000,
	'userId':566453,'payType':0,'machineCode':'90526B160362A7A4FECA22411080F8CF','score':0,'deviceInfo':13839205941} 
	#attach:附加信息；coupon：使用抵用券 单位:分；payFee：实际支付金额，单位:分；totalFee：总金额，单位:分；payType：支付渠道 0-支付宝1-微信2-apple pay；score：使用积分
	r = requests.post(Url,data = body)
	code = r.status_code
	result = r.json()
	#print(code)
	#print(result)
	assert code == 200
	assert result['result'] == 'true'

if __name__ == '__main__':
	pytest.main(["-s", "UnifiedOrder_test.py"])