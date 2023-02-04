DROP TABLE IF EXISTS `workouts`;

CREATE TABLE IF NOT EXISTS `workouts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `exercise` varchar(255) NOT NULL,
  `reps` INT NOT NULL,
  `weight` INT NOT NULL,
  `duration` INT NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 AUTO_INCREMENT=1 ;

INSERT INTO `workouts` (`username`, `exercise`, `reps`, `weight`, `duration`) VALUES
('user1', 'bicep curls', 15, 40, 40),
('user1', 'bicep curls', 14, 40, 41),
('user1', 'bicep curls', 13, 40, 42),
('user1', 'bicep curls', 12, 40, 43);

SELECT * FROM workouts;

SELECT * FROM workouts WHERE username = 'user1' AND DATE(created_at) = '2023-02-03';