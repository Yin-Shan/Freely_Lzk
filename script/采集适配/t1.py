from program_dict import caiji,shipei
import IPy
import openpyxl
import os,sys
project_path = os.path.abspath(os.path.dirname(__file__))
print(os.path.join(project_path,'att',"SQL.py"))

#wb1 = openpyxl.load_workbook('程序清单.xlsx')
#ws2 = wb1["Sheet1"]
#for i in range(1,176):
#    #if i in (15, 39, 46, 47, 134, 149, 156):  # 删除的
#    #    pass
#    #else:
#    ws2['B'+str(i+1)] = caiji[i][0]
#    ws2['C' + str(i+1)] = caiji[i][1]
#    ws2['D' + str(i+1)] = caiji[i][2]
#    ws2['E' + str(i+1)] = caiji[i][3]
#wb1.save('采集程序清单.xlsx')
#wb1.close()

#for i in range(1,169):
#    if caiji[i][0] not in IPy.IP('172.22.0.0/24'):
#        print(caiji[i][0])
    #if shipei[i][0] not in IPy.IP('172.22.0.0/24'):
    #    print(i,shipei[i][0])


