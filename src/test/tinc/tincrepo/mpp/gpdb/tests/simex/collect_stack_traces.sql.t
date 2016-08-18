insert into offenders(id,iteration,logtime,logsession,logmessage) 
select nextval('id_sequence'),%iteration%,logtime,logsession,logmessage from gp_toolkit.__gp_log_master_ext where logmessage like 'SimEx inject: class%' and logsession = 
(
select logsession from
(
(select logsession,logtime from gp_toolkit.__gp_log_segment_ext where logmessage like 'SimEx inject: class%' order by logtime desc limit 1) UNION ALL (select logsession,logtime from gp_toolkit.__gp_log_master_ext where logmessage like 'SimEx inject: class%' order by logtime desc limit 1) 
) FOO order by FOO.logtime desc limit 1
)
UNION ALL 
select nextval('id_sequence'),%iteration%,logtime,logsession,logmessage from gp_toolkit.__gp_log_segment_ext where logmessage like 'SimEx inject: class%' and logsession = 
(
select logsession from
(
(select logsession,logtime from gp_toolkit.__gp_log_segment_ext where logmessage like 'SimEx inject: class%' order by logtime desc limit 1) UNION ALL (select logsession,logtime from gp_toolkit.__gp_log_master_ext where logmessage like 'SimEx inject: class%' order by logtime desc limit 1) 
) FOO order by FOO.logtime desc limit 1
)
;
