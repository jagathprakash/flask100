SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Registration`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Registration` (
  `email` VARCHAR(20) NOT NULL,
  `FirstName` VARCHAR(20) NOT NULL,
  `FamilyName` VARCHAR(20) NOT NULL,
  `cost` INT NULL,
  `donation` INT NULL,
  `paid` TINYINT NOT NULL,
  `Address` VARCHAR(45) NULL,
  `State` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`email`),
  INDEX `email`(`email` ASC))
  ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Members`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Members` (
  `RegistrationEmail` VARCHAR(20) NULL,
  `MemberFName` VARCHAR(20) NULL,
  `MemberLName` VARCHAR(20) NULL,
  INDEX `RegistrationEmail_idx` (`RegistrationEmail` ASC),
  CONSTRAINT `RegistrationEmail`
  FOREIGN KEY (`RegistrationEmail`)
  REFERENCES `mydb`.`Registration` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
  ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
