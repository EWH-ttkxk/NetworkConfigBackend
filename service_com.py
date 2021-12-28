from TelnetClient import TelnetClient
import telnetlib


class service_com:
    loginIp = {'RouterA': '172.16.0.1',
               'RouterB': '172.16.0.2',
               'RouterC': '172.16.0.3'}

    def verifyTopology(self, data):
        result = ''
        for key, value in data.items():
            router = value['router']
            input = value['input']
            exp_outputs = value['output']
            client = TelnetClient()
            client.login_host(self.loginIp[router], 'CISCO')
            real_output = client.execute_some_command(input)
            print(real_output)
            print(1)
            print(exp_outputs)
            res = ' pass!\n'
            for exp_output in exp_outputs:
                if exp_output in real_output:
                    continue
                else:
                    res = ' fail!\n'
                    break
            result = result + router + ' ' + key + res
            client.logout_host()
        return result

    # 某个路由器上执行命令
    def exe_com(self, router, com):
        client = TelnetClient()
        client.login_host(self.loginIp[router], 'CISCO')

        res = client.execute_some_command(com)
        client.logout_host()
        return res

    # 显示某个路由器信息
    def show_information(self, router):
        client = TelnetClient()
        client.login_host(self.loginIp[router], 'CISCO')
        res = client.execute_some_command('show ip route')
        client.logout_host()
        return res
