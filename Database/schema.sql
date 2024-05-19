DROP TABLE IF EXISTS Routes;
CREATE TABLE Routes (
    RouteName VARCHAR(70),
    Location VARCHAR(200) NOT NULL,
    URL VARCHAR(100),
    AVG_STARS Decimal(2,1),
    RouteType VARCHAR(40),
    Difficulty_Rating VARCHAR(10),
    Latitude Decimal(7,5),
    Longitude Decimal(7,5),
    PRIMARY KEY(RouteName, Latitude)
);