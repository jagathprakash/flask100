CREATE SCHEMA IF NOT EXISTS `Convention2017` DEFAULT CHARACTER SET utf8 ;
USE `Convention2017` ;

-- -----------------------------------------------------
-- Table `Convention2017`.`Registration`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Convention2017`.`Registration` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NOT NULL,
  `firstname` VARCHAR(45) NOT NULL,
  `familyname` VARCHAR(45) NULL,
  `cost` INT NOT NULL DEFAULT 120,
  `paid` TINYINT NOT NULL DEFAULT 0,
  `address` VARCHAR(250) NULL,
  `state` VARCHAR(45) NOT NULL,
  `travel` TINYINT NULL DEFAULT 0,
  `stay` TINYINT NULL DEFAULT 0,
  PRIMARY KEY (`email`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Convention2017`.`Member`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Convention2017`.`Member` (
  `Registration_email` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `child` TINYINT NOT NULL DEFAULT 0,
  INDEX `fk_Member_Registration_idx` (`Registration_email` ASC),
  CONSTRAINT `fk_Member_Registration`
    FOREIGN KEY (`Registration_email`)
    REFERENCES `Convention2017`.`Registration` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Convention2017`.`Donation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Convention2017`.`Donation` (
  `Registration_email` VARCHAR(45) NOT NULL,
  `amount` INT NULL,
  INDEX `fk_Donation_Registration1_idx` (`Registration_email` ASC),
  CONSTRAINT `fk_Donation_Registration1`
    FOREIGN KEY (`Registration_email`)
    REFERENCES `Convention2017`.`Registration` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;