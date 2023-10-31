#import socket
from xmlrpc import client as xmlrpclib
#print(socket.getaddrinfo('localhiost',8069))

# url = "http://127.0.0.1:8069"
# db = "odooDB"
# user = "andrian.prabowo@itgroupinc.asia"
# password = "openpgpwd"

url = "https://bms.odoo.itgroup.id/web"
db = "odoobms"
user = "andrian.prabowo@itgroupinc.asia"
password = "Prabow123!@#"

common = xmlrpclib.ServerProxy(url+"/xmlrpc/common")
user = common.login(db,user,password)
print(f"user id is {user}");

model = "res.partner"
search = []
method = "search"

operation = xmlrpclib.ServerProxy(url+"/xmlrpc/object")
list_of_partner_ids = operation.execute(db,user,password,model,method,search)
# print(list_of_partner_ids)

method = "read"
list_of_partner_ids = operation.execute(db,user,password,model,method,list_of_partner_ids)
#print(list_of_partner_ids)
 

for customer in list_of_partner_ids:
 print(customer['id'], customer['name'], customer['phone'],customer['email'])
# print()


