select query,starttime,endtime, datediff(milliseconds,starttime, endtime) as "Total_Exec_Time(in milliseconds)" 
from stl_query 
order by "Total_Exec_Time(in milliseconds)" desc;
