create sequence id_sequence increment 1;

create table offenders (id integer,iteration integer,logtime timestamp,logsession varchar,logmessage text,hash integer) distributed by(id);

