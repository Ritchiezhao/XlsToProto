call python xls_deploy_tool.py GOODS_INFO xls/goods_info.xls
call protoc tnt_deploy_goods_info.proto --descriptor_set_out=goods_info.protodesc
call ProtoGen\protogen -i:goods_info.protodesc -o:goods_info.cs
pause