alter table Users add phone_number INT NOT NULL DEFAULT 0;
alter table Users alter column phone_number type VARCHAR(15);