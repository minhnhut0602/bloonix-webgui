CREATE TABLE `service` (
    `id`                        BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `host_id`                   BIGINT NOT NULL,
    `service_parameter_id`      BIGINT NOT NULL,
    `active`                    CHAR(1) NOT NULL DEFAULT 1,
    `acknowledged`              CHAR(1) NOT NULL DEFAULT 0,
    `notification`              CHAR(1) NOT NULL DEFAULT 1,
    `agent_version`             VARCHAR(10) NOT NULL DEFAULT '0',
    `subkeys`                   TEXT,
    `active_comment`            VARCHAR(400) DEFAULT 'no comment',
    `acknowledged_comment`      VARCHAR(400) DEFAULT 'no comment',
    `notification_comment`      VARCHAR(400) DEFAULT 'no comment',
    `volatile_comment`          VARCHAR(400) DEFAULT 'no comment',
    `attempt_counter`           SMALLINT NOT NULL DEFAULT 1,
    `last_notification_1`       BIGINT NOT NULL DEFAULT 0,
    `last_notification_2`       BIGINT NOT NULL DEFAULT 0,
    `last_check`                BIGINT NOT NULL DEFAULT 0,
    `highest_attempt_status`    VARCHAR(10) NOT NULL DEFAULT 'OK',
    `flapping`                  CHAR(1) NOT NULL DEFAULT 0,
    `scheduled`                 CHAR(1) NOT NULL DEFAULT 0,
    `agent_dead`                CHAR(1) NOT NULL DEFAULT 0,
    `next_check`                BIGINT NOT NULL DEFAULT 0,
    `next_timeout`              BIGINT NOT NULL DEFAULT 0,
    `last_event`                BIGINT NOT NULL DEFAULT 0,
    `status_since`              BIGINT NOT NULL DEFAULT 0,
    `status_nok_since`          BIGINT NOT NULL DEFAULT 0,
    `status_dependency_matched` BIGINT NOT NULL DEFAULT 0,
    `volatile_status`           CHAR(1) NOT NULL DEFAULT 0,
    `volatile_since`            BIGINT NOT NULL DEFAULT 0,
    `status`                    VARCHAR(10) NOT NULL DEFAULT 'INFO',
    `result`                    TEXT NULL,
    `debug`                     TEXT NULL,
    `message`                   TEXT NOT NULL,
    `creation_time`             TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated`                   CHAR(1) DEFAULT '0',
    `last_status`               VARCHAR(10) DEFAULT 'INFO',
    `force_check`               CHAR(1) DEFAULT '0',
    `force_event`               CHAR(1) DEFAULT '0',
    FOREIGN KEY (`host_id`) REFERENCES `host`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`service_parameter_id`) REFERENCES `service_parameter`(`ref_id`) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE INDEX `service_id_index` ON `service` (`id`);
CREATE INDEX `service_host_id_index` ON `service` (`host_id`);
