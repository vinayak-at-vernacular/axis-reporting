CREATE ROLE postgres WITH PASSWORD postgres;
CREATE DATABASE data;
GRANT ALL PRIVILEGES ON data TO postgres;


CREATE TABLE call (
    caller_number BIGINT
    ,call_id INT
    ,conv_id INT
    ,hour INT
    ,minute INT
    ,second INT
)

CREATE TABLE call_log (
    ani BIGINT
    ,call_id INT
    ,conv_id INT
    ,hour INT
)