create database hackaton COLLATE Cyrillic_General_CI_AS;

use hackaton;

create table hackaton.dbo.msg_list (
    msg_id INT PRIMARY KEY IDENTITY (1, 1), 
    msg_head VARCHAR (50) NOT NULL,
    msg_body VARCHAR (255) NOT NULL);

insert into dbo.msg_list (msg_head, msg_body) values ('Выровняйте спину!', 'Во избежание проблем с осанкой рекомендуется сменить положение');
insert into dbo.msg_list (msg_head, msg_body) values ('Оторвитесь от монитора!', 'Вы устали. Почему бы не выпить чашку чая?');
insert into dbo.msg_list (msg_head, msg_body) values ('Улучшите освещение', 'Рекомендуется включить дополнительный источник освещения');
select * from dbo.msg_list

create table hackaton.dbo.screen_history (
    stime DATETIME NOT NULL DEFAULT GETDATE(), 
    sname VARCHAR (50) NOT NULL);

create table hackaton.dbo.alert_history (
    atime DATETIME NOT NULL DEFAULT GETDATE(), 
    aname VARCHAR (255) NOT NULL);

create table hackaton.dbo.alert_manager (
    msg_id INT PRIMARY KEY IDENTITY (1, 1),
    iter_count INT NOT NULL,
    send_status INT);


use hackaton;    	
ALTER TABLE dbo.alert_history
ADD val float NULL;