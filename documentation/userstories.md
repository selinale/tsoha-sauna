# User stories

Käyttäjänä haluan...
  * rekisteröityä, että pääsen valitsemaan mihin talouteen kuulun
  * kirjautua sisään, että pääsen varaamaan saunavuoroja
  * kirjautua sisään, että pääsen muokkaamaan tai poistamaan talouteni saunavuoroja

# SQL-kyselyt

Alla listattuna käyttämäni SQL-kyselyt. 


Etsitään varatut tunnit:
```sql
SELECT reservation.hour, account.household
FROM Reservation
LEFT JOIN account ON reservation.account_id=account.id
WHERE date = :reserved
```

Etsitään varauksen tehnyt talous
```sql
SELECT date, hour, id FROM reservation
WHERE account_id IN
  (SELECT id FROM account
   WHERE household = :household)
ORDER BY hour ASC
```
