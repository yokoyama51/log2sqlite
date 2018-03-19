
BEGIN;

CREATE TABLE `LOG` (
    `_id`     INTEGER PRIMARY KEY AUTOINCREMENT
  , `user`    TEXT NOT NULL
  , `fc`      INTEGER NOT NULL
  , `host`    TEXT NOT NULL
  , `date_s`  DATETIME NOT NULL
  , `res_s`   INTEGER NOT NULL
  , `res_t`   INTEGER NOT NULL
  , `status`  INTEGER NOT NULL
);

CREATE TABLE `LOG_PARAM` (
    `_id`     INTEGER
  , `key`     TEXT
  , `value`   TEXT
);

COMMIT;
