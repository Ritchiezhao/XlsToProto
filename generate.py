import xls_deploy_tool
import os,platform

# key:sheetname  value: excelPath
configs = {"PERSON":"xls/person.xls",
		   "GOODS_INFO":"xls/goods_info.xls"
}

def ModifiedTime(path):
    if platform.system() == "Windows":
        path = path.replace('/', '\\');
        path = path.decode("utf-8")
    
    if not os.path.isfile(path):
        return 0

    stat = os.stat(path)
    return stat.st_mtime


def CanGenerate(xlsPath,protoPath):
	if ModifiedTime(xlsPath) > ModifiedTime(protoPath):
		return 1
	return 0 

modifyConfigs = {}
for k,v in configs.iteritems(): 
	protoPath = "proto/game_deploy_"+k.lower()+".proto"
	if CanGenerate(v,protoPath):
		modifyConfigs[k] = v 
print modifyConfigs

for k,v in modifyConfigs.iteritems(): 
    print "###begin### convert xls %s sheet =" % v,k
    xls_deploy_tool._Convert(v,k)
    print "####end#### convert xls %s sheet =" % v,k

for k,v in modifyConfigs.iteritems():
	print "###begin### convert cs %s sheet =" % v,k
	command1 = "protoc proto/game_deploy_"+k.lower()+".proto " +"--descriptor_set_out=desc/"+k.lower()+".protodesc"
	os.system(command1)

	command2 = "ProtoGen\protogen -i:desc/"+k.lower()+".protodesc -o:cs/"+k.lower()+".cs"
	os.system(command2)
	print "####end#### convert cs %s sheet =" % v,k
