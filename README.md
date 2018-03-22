# tsoha-sauna

#### Aihe 

Tarkoituksenani on luoda saunavuorojen varausjärjestelmä, jossa taloyhtiön asukkaat voivat varata taloudelle saunavuoron. Asukkaat voivat kirjautua järjestelmään ja valita, mihin talouteen he kuuluvat. Saunavuorot varataan kunkin talouden nimissä. Taloyhtiön isännöitsijä on järjestelmän admin. Admin pystyy lisäämään tai poistamaan käyttäjiä, vaihtamaan salasanoja, poistamaan saunavuoroja ja muita hallinnollisia toimia, joita en ole vielä päättänyt. 

Lisäksi tiedostojen talletus toiminnallisuutta on pyydetty. Tiedostoja voi tallettaa ja ladata yksinkertaisesta tiedostopankista

#### Tietokannan rakenne

Tietokanta koostuu ainakin tauluista käyttäjä, talous, saunavuoro, tiedosto.

Taulujen liitokset tulevat alustavasti olemaan: 

Käyttäjä x--1 Talous,

Talous 1--x Saunavuoro,

Käyttäjä 1--x Tiedosto.

Nämä saattavat muuttua.

https://tsoha-sauna.herokuapp.com/
