

SQL1 = '''
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='宁波传输市本级华为SDH网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='杭州华为传输U2000网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='丽水华为SDH和DWDM网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='衢州华为SDH网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='金华华为SDH网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='湖州华为SDH网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='台州传输华为SDH网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='舟山传输华为SDH网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='温州华为SDH网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='绍兴华为SDH网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='杭州中兴传输U31网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='丽水中兴U31传输网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='金华中兴SDH网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='湖州中兴SDH和DWDM网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='嘉兴中兴SDH网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='省网管中兴OTN网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='衢州中兴SDHU31网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='台州中兴U31网管'
 union all 
select count(*) from t_channel where i_data_source=2 and i_channel_type=51 and s_subnetwork='省网管烽火OTN网管'
'''
SQL2 = '''
select count(*) from T_CHANNEL c where S_SUBNETWORK='宁波传输市本级华为SDH网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='杭州华为传输U2000网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='丽水华为SDH和DWDM网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='衢州华为SDH网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='金华华为SDH网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='湖州华为SDH网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='台州传输华为SDH网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='舟山传输华为SDH网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='温州华为SDH网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='绍兴华为SDH网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='杭州中兴传输U31网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='丽水中兴U31传输网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='金华中兴SDH网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='湖州中兴SDH和DWDM网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='嘉兴中兴SDH网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='省网管中兴OTN网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='衢州中兴SDHU31网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='台州中兴U31网管'and I_DATA_SOURCE=2
 union all 
select count(*) from T_CHANNEL c where S_SUBNETWORK='省网管烽火OTN网管'and I_DATA_SOURCE=2
'''
SQL3 = '''
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='宁波传输市本级华为SDH网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='宁波传输市本级华为SDH网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='杭州华为传输U2000网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='杭州华为传输U2000网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='丽水华为SDH和DWDM网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='丽水华为SDH和DWDM网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='衢州华为SDH网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='衢州华为SDH网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='金华华为SDH网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='金华华为SDH网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='湖州华为SDH网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='湖州华为SDH网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='台州传输华为SDH网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='台州传输华为SDH网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='舟山传输华为SDH网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='舟山传输华为SDH网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='温州华为SDH网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='温州华为SDH网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='绍兴华为SDH网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='绍兴华为SDH网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='杭州中兴传输U31网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='杭州中兴传输U31网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='丽水中兴U31传输网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='丽水中兴U31传输网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='金华中兴SDH网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='金华中兴SDH网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='湖州中兴SDH和DWDM网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='湖州中兴SDH和DWDM网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='嘉兴中兴SDH网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='嘉兴中兴SDH网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='省网管中兴OTN网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='省网管中兴OTN网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='衢州中兴SDHU31网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='衢州中兴SDHU31网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='台州中兴U31网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='台州中兴U31网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
union all
select isnull(a.s_subnetwork,b.fine_s_subnetwork) unit ,isnull(a.nubmer,0) nubmer ,isnull(b.fine_nubmer,0) fine_nubmer
 from (select count(*) as nubmer ,s_subnetwork from t_channel  where I_STATE  in(1,6,7)  and s_subnetwork='省网管烽火OTN网管' group by s_subnetwork) A FULL JOIN 
(select count(*) as fine_nubmer,s_subnetwork fine_s_subnetwork  from t_channel  where I_STATE not  in(1,6,7)  and s_subnetwork='省网管烽火OTN网管'  group by s_subnetwork) b on a.s_subnetwork=b.fine_s_subnetwork
'''
wg_sql = 'SELECT AUTO_ID,REQUEST_TIME,OP_FLAG,SYNC_FLAG FROM CCIC_OP_EXE_LOG WHERE auto_id=(SELECT  MAX(AUTO_ID) FROM CCIC_OP_EXE_LOG)'



