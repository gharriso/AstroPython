SELECT b.main_id,b.otype,b.rvz_redshift ,d.*
  FROM basic b
  JOIN mesDistance d ON b.oid=d.oidref


select b.otype,o.label,count(*)
from otypedef o join basic b on b.otype=o.otype  group by b.otype,o.label order by 3 desc

select b.main_id,b.rvz_redshift,b.sp_type ,d.dist,d.unit ,f.flux
  from basic b
  join mesDistance d on b.oid=d.oidref
  join flux f on b.oid=f.oidref
 where b.otype='*' and b.sp_type is not null
