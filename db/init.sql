CREATE SCHEMA IF NOT EXISTS vpn_admin AUTHORIZATION vpn_admin;
create table vpn_admin.usr(id SERIAL PRIMARY KEY,
telegram_id int,
fullname varchar(255),
nickname varchar(255)
);

create table IF NOT EXISTS vpn_admin.user_tokens(guid varchar(36) default uuid_generate_v4(), 
usr_id int references vpn_admin.usr(id) not null,
usr_token varchar(4000) not null,
enabled bool default True, 
createdete date default CURRENT_DATE
);