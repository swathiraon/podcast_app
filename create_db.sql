create database bit;
use bit;
create table Announcements(id int primary key AUTO_INCREMENT,
                            title text,
                            adate date,
                            body text
                            );


create table documents(id int,
                        Did varchar(20),
                        constraint fkd foreign key(id) references Announcements(id),
                        constraint pkd primary key(id,did)
                        );

create table Faculty(id Numeric primary key,
					 FName text,
                     Designation text,
                     Qualification text,
                     Email text,
                     Dept text);