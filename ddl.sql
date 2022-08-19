create table weather(
`station_id` varchar(15),
`date` date,
`max_temperature` int, 
`min_temperature` int, 
`precipitation` int,
primary key (`station_id`,`date`));

create table corn_yield(
`year` int,
`yield` int,
primary key (`year`));


create table data_statistics(
`station_id` varchar(15),
`year_from_date` int,
`avg_max_temp` int,
`avg_min_temp` int,
`total_precipitation` int,
primary key (`year_from_date`, `station_id`));
