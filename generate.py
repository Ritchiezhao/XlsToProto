import xls_deploy_tool
# key:sheetname  value: excelPath
configs = {"PERSON":"xls/person.xls",
		   "GOODS_INFO":"xls/goods_info.xls"
}

for k,v in configs.iteritems(): 
    print "###begin### convert xls %s sheet =" % v,k
    xls_deploy_tool._Convert(v,k)
    print "###end### convert xls %s sheet =" % v,k
