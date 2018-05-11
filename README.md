# tsoha-sauna

### Aihe 

Ohjelmani on saunavuorojen varausjärjestelmä, jossa taloyhtiön asukkaat voivat varata taloudelle saunavuoron. Asukkaat voivat rekisteröityä järjestelmään ja valita, mihin talouteen he kuuluvat. Kirjautuneena asukas pystyy tekemään varauksia taloudelleen ja tarkastelemaan talouden varauksia, menneitä ja tulevia. Asukas pystyy myös poistamaan oman varauksensa sekä tekemään siihen muutoksia. Taloyhtiön isännöitsijä on järjestelmän admin. Tarkoituksena olisi, että admin näkee listauksen kaikista varauksista ja pystyy tekemään niihin muutoksia. 

### Tietokannan rakenne

Tietokanta koostuu tauluista käyttäjä, talous, saunavuoro.

Taulujen liitokset tulevat alustavasti olemaan: 

Käyttäjä x--1 Talous,

Talous 1--x Saunavuoro,

### Käyttöohje

Mene sovelluksen [sivulle](https://tsoha-sauna.herokuapp.com/) tai kloonaa repositorio githubista ja käynnistä sovellus komennolla `python3 run.py`. 

Rekisteröitymään pääsee sivun oikeasta yläkulmasta kohdasta **Rekisteröidy** ja rekisteröitymisen jälkeen asukas kirjataan automaattisesti sivuille. Jatkossa asukas pääsee kirjautumaan luomillaan tunnuksilla sivun oikeasta yläkulmasta kohdastaa **Kirjaudu**. Asukkaan ollessa kirjautunut, pystyy hän tekemään uuden varauksen etusivulta. Etusivulle pääsee painamalla sivun vasemmasta ylälaidasta kohtaa **Saunavuoron varaus**. Asukas pystyy tarkastelemaan taloutensa varauksia painamalla yläpalkista kohtaa **Varaukset**. Asukas pystyy muokkaamaan taloutensa varauksia painamalla kynää ja poistamaan taloutensa varauksia painamalla roskakoria.

Asukas pääsee kirjautumaan ulos oikeasta yläkulmasta kohdasta **Hei 'asukkaan nimi' -- Kirjaudu ulos**.

### Rajoitteet

Kirjautunut asukas näkee listauksen vain oman taloutensa varauksista ja pystyy niitä poistamaan ja muokkaamaan. Asukas ei siis näe listausta muiden talouksien varauksista, eikä siten pysty niitä muokkaamaan tai poistamaan. 

### Puutokset

Admin ei näe listausta kaikista varauksista eikä näin ollen pysty muokkaamaan ja poistamaan muita kuin oman taloutensa varauksia. Menneitä aikoja kuluvalta päivältä pystyy varaamaan ja varauksen muokkauksesta tai poistamisesta ei tule mitään ilmoitusta. 

### Linkit

[Linkki sovellukseen](https://tsoha-sauna.herokuapp.com/)

[User storyt](https://github.com/selinale/tsoha-sauna/blob/master/documentation/userstories.md)

[Tietokantakaavio](https://github.com/selinale/tsoha-sauna/blob/master/documentation/DBtable.pdf)
