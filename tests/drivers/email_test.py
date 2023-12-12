from zbase.drivers.email import SMTP, newSMTPEnv



# client = newSMTPEnv()

# # a = client.sendTpl("daqian.zhang@core42.ai" , "hello" , "<h1>hello {name}</h1>" , {"name":"zhangdaqian"})
# a = client.sendBatch("hello {name}" , "<h1>hello {name}</h1>" , [{"to":"daqian.zhang1@core42.ai1" , "name":"zhangdaqian"},{"to":"daqian.zhang@core42.ai" , "name":"zhangdaqian"}])
# print(a)