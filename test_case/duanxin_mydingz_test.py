#coding:utf-8
import pytest
import requests
from parameterized import parameterized
import random

'''短信-我的定制页面'''
Url = "https://mysteelapi.steelphone.com/v4/sms/getMySmsPack.htm?"

'''判断用户是否登录'''
payload = {'cellphone':'13839205941','password':'e10adc3949ba59abbe56e057f20f883e','token':'1507bfd3f797e28773a','ostype':'1','machineInfo':'HUAWEI,PIC-AL00,26','softVersion':'4.7.3'}
r = requests.post("http://mysteelapi.steelphone.com/v4/user/login.htm?",params = payload)
denglu = r.json()
#print(denglu)

if denglu['result'] == 'true':
#====================================================================测试数据（异常情况）================================================================
	@parameterized.expand([
		#用例名称，参数：userId、machineCode，预期结果1，预期结果2
		("both_null",'','','传参异常！','false'),
		("userId_null",'','90526B160362A7A4FECA22411080F8CF','传参异常！','false'),
		#("machineCode_null",'566453','','该账户已在其他设备上登录，请联系管理员！','false'),
		("userId_error",'5664532','90526B160362A7A4FECA22411080F8CF','用户不存在','false'),
		("userId_notmatch",'744408','90526B160362A7A4FECA22411080F8CF','该账户已在其他设备上登录，请联系管理员！','false'),
		("machineCode_error",'5664532','90526B160362A7A4FECA22411080F8CF','用户不存在','false'),
		("both_error",'56645325','90526B160362A7A4FECA22411080F8CF','用户不存在','false')
	])

#====================================================================请求、断言===============================================================
	def test_case(_,type,id,a,c):
		body = {'userId':type,'machineCode':id}
		result = requests.post(Url,data = body).json()
		#print(result)
		assert result['errorstr'] ==a
		assert result['result'] == c

	def test_get_success():
		'''查询成功'''
		body = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF'}
		result = requests.post(Url,data = body).json()
		#print(result)
		assert result['result'] == 'true'

		dingzhi = []
		for dx in result['sms']:
			#print(dx['name'])
			dingzhi.append(dx['name'])
		#print (dingzhi)
		#========================将定制的行情名称放入本地TXT文件中========================
		f = open (r'E:\git\steelphone_api_test02\test_case\html.txt','w')
		print (dingzhi,file = f)
		f.close()

		idlist = []
		for dx in result['sms']:
			#print(dx['name'])
			idlist.append(dx['id'])
		#print (idlist)
		#print(len(idlist))
		b = random.sample(idlist, 5)
		global a
		a = ",".join(b)
		#print(a)

elif denglu['result'] == 'false':
		print("请退出账户：13839205941")

#======================================================短信排序==============================================================
url = "https://mysteelapi.steelphone.com/v4/sms/setSmsPackPriority.htm?&isPad="
def test_get_success01():
	body = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF','packIds':a}
	result01 = requests.post(url,data = body)
	#print(result01)
	code = result01.status_code
	assert code == 200

if __name__ == '__main__':
	pytest.main(["-s", "duanxin_mydingz_test.py"])