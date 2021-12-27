from TelnetClient import TelnetClient


class check_config:
    loginIp = {'RouterA': '172.16.0.1',
               'RouterB': '172.16.0.2',
               'RouterC': '172.16.0.3'}

    def verifyTopology(self, data):
        result = ''
        for key, value in data.items():
            router = value['router']
            input = value['input']
            exp_output = value['output']
            client = TelnetClient()
            client.login_host(self.loginIp[router], 'CISCO')
            real_output = client.execute_some_command(input)
            print(real_output)
            print(1)
            print(exp_output)
            if exp_output in real_output:
                result = result + router + ' ' + key + ' pass!\n'
            else:
                result = result + router + ' ' + key + ' fail!\n'
            client.logout_host()
        return result
    # 登录路由器ping对应ip并返回输出信息
    # def ping_check(self, router, ip):
    #     try:
    #         client = TelnetClient()
    #         client.login_host(self.loginIp[router], 'root', 'CISCO')
    #         res = client.execute_some_command("ping " + ip)
    #         client.logout_host()
    #         return res
    #     except Exception as e:
    #         return str(e)
    #
    # def show_ip_check(self, router):
    #     try:
    #         client = TelnetClient()
    #         client.login_host(self.loginIp[router], 'root', 'CISCO')
    #         res = client.execute_some_command("show ip route")
    #         client.logout_host()
    #         return res
    #     except Exception as e:
    #         return str(e)
