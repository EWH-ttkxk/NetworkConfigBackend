import logging
import telnetlib
import time


class TelnetClient:

    def __init__(self):
        self.tn = telnetlib.Telnet()

    # 此函数实现telnet登录主机
    def login_host(self, host_ip, password):
        try:
            self.tn.open(host_ip)
        except:
            logging.warning('%s网络连接失败' % host_ip)
            return False
        # 等待Password出现后输入用户名，最多等待20秒
        self.tn.read_until(b'Password: ', timeout=20)
        self.tn.write(password.encode('ascii') + b'\n')
        # 延时两秒再收取返回结果，给服务端足够响应时间
        time.sleep(2)
        # 获取登录结果
        # read_very_eager()获取到的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode('ascii')
        # 登录成功后进入特权命令状态
        if 'Login incorrect' not in command_result:
            logging.warning('%s登录成功' % host_ip)
            self.tn.write('enable'.encode('ascii') + b'\n')
            self.tn.read_until(b'Password: ')
            self.tn.write(password.encode('ascii') + b'\n')
            return True
        else:
            logging.warning('%s登录失败，用户名或密码错误' % host_ip)
            return False

    # 此函数实现执行传过来的命令，并输出其执行结果
    def execute_some_command(self, command):
        # 执行命令
        self.tn.write(command.encode('ascii') + b'\n')
        time.sleep(2)
        # 获取命令结果
        command_result = self.tn.read_very_eager().decode('ascii')

        logging.warning('命令执行结果：\n%s' % command_result)

        return command_result

    # 退出telnet
    def logout_host(self):
        self.tn.write(b"exit\n")


tn = telnetlib.Telnet()
# # 测试telnet
# if __name__ == '__main__':
#     tc = TelnetClient()
#     tc.login_host('172.16.0.1', 'CISCO')
#     res = tc.execute_some_command('show running-config')
#     print(res)
#     tc.logout_host()
