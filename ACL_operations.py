from TelnetClient import TelnetClient

RouterA_ip = '172.16.0.1'
RouterB_ip = '172.16.0.2'
RouterC_ip = '172.16.0.3'


class ACL_operations:

    loginIp = {'RouterA': '172.16.0.1',
               'RouterB': '172.16.0.2',
               'RouterC': '172.16.0.3'}

    # 添加ACL条目
    def addACL(self, ACLOptions):
        client = TelnetClient()
        client.login_host(self.loginIp[ACLOptions['source']], 'CISCO')
        commands = []
        if ACLOptions["way"] == "deny":
            commands = ["config terminal",
                        "access-list " + str(ACLOptions["ACLId"]) + " deny " + self.loginIp[ACLOptions['target']] + " 255.255.255.0",
                        "access-list " + str(ACLOptions["ACLId"]) + " permit any",
                        "int " + ACLOptions["settingInterface"],
                        "ip access-group " + str(ACLOptions["ACLId"]) + " " + str(ACLOptions["direction"]),
                        "end"]
        else:
            commands = ["config terminal",
                        "no access-list " + str(ACLOptions["ACLId"]),
                        "end"]
        for command in commands:
            client.execute_some_command(command)
        res = client.execute_some_command("show ip access-list")
        client.logout_host()
        return res

    # 清空路由器的ACL配置
    def removeACL(self, ACLOptions):
        client = TelnetClient()
        client.login_host(self.loginIp[ACLOptions['source']], 'CISCO')
        commands = ["config terminal",
                    "no access-list " + str(ACLOptions["ACLId"]),
                    "end"]
        for command in commands:
            client.execute_some_command(command)
        res = client.execute_some_command("show ip access-list")
        client.logout_host()
        return res

    # def configIp(loginIp, username, loginPassword, managerPassword, settingInterface, settingIp):
    #     client = TelnetClient()
    #     client.login_host(loginIp, username, loginPassword)
    #     commands = ["enable",
    #                 managerPassword,
    #                 "config t",
    #                 "int " + settingInterface,
    #                 "ip add " + settingIp + " 255.255.255.0",
    #                 "no shutdown",
    #                 "end"]
    #     for command in commands:
    #         client.execute_some_command(command)
    #
    # def deny(ACLId, denyIp):
    #     client = TelnetClient()
    #     client.login_host("1.1.1.2", "root", "123456")
    #     commands = ["enable",
    #                 "123456",
    #                 "config t",
    #                 "access-list " + str(ACLId) + " deny " + denyIp + " 255.255.255.0",
    #                 "access-list " + str(ACLId) + " permit any",
    #                 "int " + PC1Interface,
    #                 "ip access-group " + str(ACLId) + " out",
    #                 "end"]
    #     for command in commands:
    #         client.execute_some_command(command)
    #     res = client.execute_some_command("show ip access-list")
    #     client.logout_host()
    #     return res
    #
    # def permit(ACLId):
    #     client = TelnetClient()
    #     client.login_host("1.1.1.2", "root", "123456")
    #     commands = ["enable",
    #                 "123456",
    #                 "config t",
    #                 "no access-list " + str(ACLId),
    #                 "end"]
    #     for command in commands:
    #         client.execute_some_command(command)
    #     res = client.execute_some_command("show ip access-list")
    #     client.logout_host()
    #     return res
    #
    # def denyPC2():
    #     return deny(PC2ACLId, PC2Ip)
    #     # client = TelnetClient()
    #     # client.login_host("1.1.1.2","root","123456")
    #     # commands = [ "enable",
    #     #              "123456",
    #     #              "config",
    #     #              "access-list 10 deny 2.2.2.1 255.255.255.0",
    #     #              "access-list 10 permit any",
    #     #              "int f0/0",
    #     #              "ip access-group 10 out",
    #     #              "exit"]
    #     # for command in commands:
    #     #     client.execute_some_command( command )
    #     # client.logout_host()
    #
    # def permitPC2():
    #     return permit(PC2ACLId)
    #     # client = TelnetClient()
    #     # client.login_host("1.1.1.2", "root", "123456")
    #     # commands = ["enable",
    #     #             "123456",
    #     #             "config",
    #     #             "no access-list 10",
    #     #             "exit"]
    #     # for command in commands:
    #     #     client.execute_some_command(command)
    #     # client.logout_host()
    #
    # def denyPC3():
    #     return deny(PC3ACLId, PC3Ip)
    #     # client = TelnetClient()
    #     # client.login_host("1.1.1.2","root","123456")
    #     # commands = [ "enable",
    #     #              "123456",
    #     #              "config",
    #     #              "access-list 20 deny 3.3.3.1 255.255.255.0",
    #     #              "access-list 20 permit any",
    #     #              "int f0/0",
    #     #              "ip access-group 20 out",
    #     #              "exit"]
    #     # for command in commands:
    #     #     client.execute_some_command( command )
    #     # client.logout_host()
    #
    # def permitPC3():
    #     return permit(PC3ACLId)
    #     # client = TelnetClient()
    #     # client.login_host("1.1.1.2", "root", "123456")
    #     # commands = ["enable",
    #     #             "123456",
    #     #             "config",
    #     #             "no access-list 20",
    #     #             "exit"]
    #     # for command in commands:
    #     #     client.execute_some_command(command)
    #     # client.logout_host()
    #
    # def ping(ip1, ip2, username, loginPassword):
    #     try:
    #         client = TelnetClient()
    #         client.login_host(ip1, username, loginPassword)
    #         res = client.execute_some_command("ping " + ip2)
    #         client.logout_host()
    #         return res
    #     except Exception as e:
    #         return str(e)
