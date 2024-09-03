
create table public.tasks (
    id SERIAL primary key,
    title varchar(255) not null,
    description text,
    completed boolean not null default false
);
