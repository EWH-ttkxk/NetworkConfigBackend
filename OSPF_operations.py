from TelnetClient import TelnetClient

RouterA_ip = '172.16.0.1'
RouterB_ip = '172.16.0.2'
RouterC_ip = '172.16.0.3'


class OSPF_operations:

    # 添加静态路由配置
    def add_OSPF(self, IPs, OSPFcommands):
        # commands = []
        routers = ['RouterA', 'RouterB', 'RouterC']
        router_ips = [RouterA_ip, RouterB_ip, RouterC_ip]
        for i in range(len(routers)):
            self.configSet(router_ips[i], 'CISCO', IPs[routers[i]], routers[i])
        for i in range(len(routers)):
            self.ospfSet(router_ips[i], 'CISCO', routers[i], OSPFcommands[routers[i]])
        return 'Set configure success'

    def ospfSet(self,host_ip, password, router, ospf_commands):
        client = TelnetClient()
        client.login_host(host_ip, password)
        commands = ['config terminal']
        commands.append("router ospf 1")
        for item in ospf_commands:
            commands.append(item)
        commands.append("end")

        for command in commands:
            client.execute_some_command(command)
        client.logout_host()

    def configSet(self, host_ip, password, port_ips, router):
        client = TelnetClient()
        client.login_host(host_ip, password)
        commands = ['config terminal']
        for port_ip in port_ips:
            commands.extend(['int ' + str(port_ip['port']),
                             "ip address " + str(port_ip['ip']) + ' ' + str(port_ip['subnetMask'])
                             ])
            if 's' in port_ip['port']:
                commands.append('no shutdown')
        commands.append("end")

        for command in commands:
            client.execute_some_command(command)
        client.logout_host()

    # 逐一清空每个路由器配置
    def remove_OSPF(self, IPs):
        routers = ['RouterA', 'RouterB', 'RouterC']
        router_ips = [RouterA_ip, RouterB_ip, RouterC_ip]
        for i in range(len(routers)):
            self.configRemove(router_ips[i], 'CISCO', IPs[routers[i]], routers[i])
        return 'Clear configure success!'

    def configRemove(self, host_ip, password, port_ips, router):
        client = TelnetClient()
        client.login_host(host_ip, password)
        commands = ['config terminal']
        # 清空端口配置
        for port_ip in port_ips:
            # 清空环路端口配置
            if 'l' in port_ip['port']:
                commands.append('no interface %s' % port_ip['port'])
            # 将s0/0/0和s0/0/1恢复为默认配置
            else:
                commands.append('default interface %s' % port_ip['port'])

        # 删除所有OSPF路由配置
        commands.append("no router ospf")
        commands.append("end")
        for command in commands:
            client.execute_some_command(command)
        client.logout_host()

        # for command in commands:
        #     client.execute_some_command(command)
        # client.logout_host()
    # def checkConfig(self, host_ip, username, loginPassword):
    #     try:
    #         client = TelnetClient()
    #         client.login_host(host_ip, username, loginPassword)
    #         commands = ["enable", "CISCO"]
    #         for command in commands:
    #             self.tn.execute_some_command(command)
    #         res = client.execute_some_command("show ip route")
    #         client.login_host()
    #         return res
    #     except Exception as e:
    #         return str(e)

    # def ping(self, ip1, ip2, username, loginPassword):
    #     try:
    #         client = TelnetClient()
    #         client.login_host(ip1, username, loginPassword)
    #         res = client.execute_some_command("ping " + ip2)
    #         client.logout_host()
    #         return res
    #     except Exception as e:
    #         return str(e)
