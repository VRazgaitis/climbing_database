CREATE TABLE Routes (
    RouteName VARCHAR(40),
    Location VARCHAR(40) NOT NULL,
    URL VARCHAR(40),
    AVG_STARS Decimal(2,1),
    RouteType VARCHAR(40),
    Difficulty_Rating VARCHAR(40),
    PRIMARY KEY(RouteName)
);