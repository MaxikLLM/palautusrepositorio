Olen tehnyt tällä viikolla tekoälyagentin kanssa TDD-mallin mukaisia testejä. Testit 1–7 tehtiin niin, että kirjoitin itse testin, varmistin sen epäonnistuvan ja pyysin sitten agenttia toteuttamaan mahdollisimman pienen muutoksen, jolla testi menee läpi. Mielestäni agentti tuotti melko laadukasta koodia.

Tehtävissä 8–15 agentti kirjoitti myös testit. Ne olivat kunnossa, mutta mielestäni niiden tarkistuksissa olisi voinut olla muutama tarkistus vähemmän. Esimerkiksi ostoskorista poistamista testaavassa testissä olisi ehkä riittänyt tarkistaa ostoslistan pituus ja tuotteiden määrä ilman hinnan tarkistamista. Testit olivat siis hieman liian yksityiskohtaisia.

A-kohdassa minimitoteutuksen kanssa oli paljon ongelmia, koska agentti yritti useita kertoja toteuttaa yleisen toiminnallisuuden niin, että kaikki samankaltaiset testit menisivät läpi. Tämän vuoksi jouduin ohjeistamaan sitä useasti, jotta se toimisi kulloisenkin tarpeen mukaan. Hyvää oli se, ettei agentti yrittänyt muuttaa testejä.

En voi sanoa, että agentti olisi yrittänyt huijata. Ensimmäisen testin kohdalla minimitoteutus kuitenkin perustui kovakoodattuihin arvoihin. Agentti teki näin pyynnöstäni.

Jos valitsisin A- ja B-vaihtoehdon työnjaon välillä, pitäisin enemmän A-vaihtoehdosta. Silloin voin kirjoittaa testit itse ja minulla on jo odotus siitä, miten toiminnallisuuden pitäisi toimia. B-vaihtoehto on kuitenkin myös hyvä, jos esimerkiksi aikaa on vähän.