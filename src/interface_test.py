import requests

class InterfaceTest:
    def interface_test(self,testMethods,testUrl,testParams,testCookies):
        # 方法是get
        if testMethods == "get":
            print("方法是：get")
            #print("链接是：",testUrl)
            #print("请求参数是：", testParams)
            if testCookies == "None":
                print("没有cookie:")
                r = requests.get(testUrl,params=testParams)
            else:
                r = requests.get(testUrl,params=testParams,cookie=testCookies)
            testStatus_code=r.status_code #返回状态码
            if testStatus_code==200:
                print("接口测试成功")
                result = r.json()
                return r.text
            else:
                print("接口访问失败")
                result = r.json()
                return r.text
        #方法是post
        elif testMethods == "post":
            print("方法是：post")
            #print("链接是：",testUrl)
            #print("请求参数是：", testParams)
            if testCookies == "None":
                print("没有cookie:")
                r = requests.post(testUrl,data=testParams)
            else:
                r = requests.post(testUrl,data=testParams,cookie=testCookies)
            testStatus_code=r.status_code
            if testStatus_code==200:
                print("接口测试成功")
                result = r.json()
                return r.text
            else:
                print("接口访问失败")
                result = r.json()
                return r.text

        else:
            print("暂时不支持该接口方法，如有需要，后续完善")






