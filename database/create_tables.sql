CREATE TABLE `users` (
  `id` CHAR(36) NOT NULL,
  `username` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `firstname` VARCHAR(255) NOT NULL,
  `lastname` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_username` (`username`)
);

CREATE TABLE `stocks` (
    `id` CHAR(36) NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `unique_name` (`name`)
);

CREATE TABLE `user_stocks`(
    `stock_id` CHAR(36) NOT NULL,
    `user_id` CHAR(36) NOT NULL,
    PRIMARY KEY (`stock_id`, `user_id`),
    FOREIGN KEY (`stock_id`) REFERENCES `stocks`(`id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)
);
