
# Schema

```sql
CREATE TABLE household (
        id VARCHAR NOT NULL,
        PRIMARY KEY (id)
);
CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        household VARCHAR(2),
        role VARCHAR(10),
        PRIMARY KEY (id),
        FOREIGN KEY(household) REFERENCES household (id)
);
CREATE TABLE reservation (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        date DATE NOT NULL,
        hour INTEGER NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
);
```
