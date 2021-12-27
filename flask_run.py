from flask import Flask, request

from ACL_operations import ACL_operations
from OSPF_operations import OSPF_operations
from service_com import service_com
from static_operations import static_operations

app = Flask(__name__)  # __name__当前文件


# 添加ACL配置
@app.route('/ACL_add', methods=['POST'])
def acl_add():
    data = request.get_json()
    acl = ACL_operations()
    result = acl.addACL(data['ACLOptions'])
    return result


# 去除ACL配置
@app.route('/ACL_remove', methods=['POST'])
def acl_remove():
    data = request.get_json()
    acl = ACL_operations()
    result = acl.removeACL(data['ACLOptions'])
    return result


# 添加static路由配置
@app.route('/static_add', methods=['POST'])
def static_add():
    data = request.get_json()
    static = static_operations()
    result = static.add_static(data["IPs"], data["ipRoutes"])
    return result


# 清空static路由配置
@app.route('/static_remove', methods=['POST'])
def static_remove():
    data = request.get_json()
    static = static_operations()
    result = static.remove_static(data["IPs"], data["ipRoutes"])
    return result


# 添加OSPF路由配置
@app.route('/OSPF_add', methods=['POST'])
def OSPF_add():
    data = request.get_json()
    OSPF = OSPF_operations()
    result = OSPF.add_OSPF(data["IPs"], data["OSPFcommands"])
    return result


# 清空OSPF路由配置
@app.route('/OSPF_remove', methods=['POST'])
def OSPF_remove():
    data = request.get_json()
    OSPF = OSPF_operations()
    result = OSPF.remove_OSPF(data["IPs"])
    return result


# 检查配置是否成功
@app.route('/config_check', methods=['POST'])
def config_check():
    data = request.get_json()
    service = service_com()
    result = service.verifyTopology(data)
    return result


# 单个路由器执行命令
@app.route('/command_exe', methods=['POST'])
def command_exe():
    data = request.get_json()
    service = service_com()
    res = service.exe_com(data['router'], ['command'])
    return res


# 返回单个路由器信息
@app.route('/router_information', methods=['POST'])
def show_information():
    data = request.get_json()
    service = service_com()
    res = service.show_information(data['router'])
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
