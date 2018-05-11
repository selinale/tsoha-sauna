# SQL-kyselyt

```sql
SELECT Account.id, Account.username FROM Account
LEFT JOIN Reservation ON Reservation.account_id = Account.id
GROUP BY Account.id
HAVING COUNT(Reservation.id) = 0

SELECT reservation.hour, account.household
FROM Reservation
LEFT JOIN account ON reservation.account_id=account.id
WHERE date = :reserved

SELECT reservation.id, account.household, reservation.hour, reservation.date
FROM account
LEFT JOIN reservation ON reservation.account_id=account.id

SELECT date, hour, id FROM reservation
WHERE account_id IN
  (SELECT id FROM account
  WHERE household = :household)
ORDER BY hour ASC
