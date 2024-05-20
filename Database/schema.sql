DROP TABLE IF EXISTS Routes;
CREATE TABLE Routes (
    RouteName VARCHAR(70),
    Location VARCHAR(200) NOT NULL,
    Region VARCHAR(50) NOT NULL,
    URL VARCHAR(100),
    AVG_STARS Decimal(2,1),
    RouteType VARCHAR(40),
    Difficulty_Rating VARCHAR(10),
    Difficulty INTEGER NOT NULL,
    Latitude Decimal(7,5),
    Longitude Decimal(7,5),
    PRIMARY KEY(RouteName, Latitude)
);
-- CREATE TABLE Climbers (
--     ClimberId INTEGER PRIMARY KEY AUTOINCREMENT,
--     ClimberName VARCHAR(75) NOT NULL,
--     DOB DATE NOT NULL
-- );

-- CREATE TABLE Ticks (
--     ClimberName VARCHAR(75) NOT NULL,
--     RouteName VARCHAR(70) NOT NULL,
--     ClimbDate DATE NOT NULL,
--     ClimbStars Decimal(2,1),
--     AscentStyle VARCHAR(50),
--     LeadStyle VARCHAR(50),
--     AscentNotes VARCHAR(1000),
--     PRIMARY KEY(ClimberName, RouteName, ClimbDate),
--     FOREIGN KEY (ClimberName) REFERENCES Climbers(ClimberId),
--     FOREIGN KEY (RouteName) REFERENCES Routes(RouteName)
-- );
-- CREATE TABLE Developed_Routes (
--     DeveloperName VARCHAR(75) NOT NULL,
--     RouteName VARCHAR(70) NOT NULL,
--     DateDeveloped DATE NOT NULL,
--     PRIMARY KEY(DeveloperName, RouteName),
--     FOREIGN KEY (DeveloperName) REFERENCES Climbers(ClimberId),
--     FOREIGN KEY (RouteName) REFERENCES Routes(RouteName)
-- );
-- CREATE TABLE Climbing_equipment (
--     ProductName VARCHAR(200) NOT NULL,
--     Brand VARCHAR(100) NOT NULL,
--     Weight Decimal (5,1),
--     URL VARCHAR(1000),
--     PRIMARY KEY(ProductName, Brand)
-- );
-- CREATE TABLE Equipment_used (
--     ProductName VARCHAR(200) NOT NULL,
--     RouteName VARCHAR(70) NOT NULL,
--     PRIMARY KEY(ProductName, RouteName),
--     FOREIGN KEY (ProductName) REFERENCES Climbing_equipment(ProductName),
--     FOREIGN KEY (RouteName) REFERENCES Routes(RouteName)
-- );
-- DROP TABLE IF EXISTS Regions;
-- CREATE TABLE Regions (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- Region VARCHAR(75),
-- Country VARCHAR(75),
-- Continent VARCHAR(75)
-- );
--  DROP TABLE IF EXISTS Common_geologies;
-- CREATE TABLE Common_geologies (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- Region VARCHAR(75),
-- MainGeology VARCHAR(200)
-- );
