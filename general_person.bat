call python xls_deploy_tool.py PERSON xls/person.xls
call protoc proto/tnt_deploy_person.proto --descriptor_set_out=desc/person.protodesc
call ProtoGen\protogen -i:desc/person.protodesc -o:cs/person.cs
pause