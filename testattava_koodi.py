#***************************************************** 
# T1_2_2.py kaytetaan luvun parillisuuden tarkistamiseen.
# @author tekija: Victoria
# @since pvm: (versio pvm 18.4.2023) 
# @version versio: (versionumero 1.0) 
# muutos: (nimikirjaimet omat nimikirjaimet) 
#*****************************************************/

#KOODAA SEURAAVA OHJELMA, MITA KOODI TULOSTAA?
#Koodaa seuraava Python- ohjelma kayttaen tyoasemalle asennettua Python ohjelmaa.
#Esittele koodaamasi ohjelma opettajalle ja vastaa kysymyksiin. Pida koodaamasi ohjelma tallessa esim. github:ssa myohempaa tarkastelua varten.

#Yksikkotestausvaiheet:
#1.luo kansio koodille tai lataa github:sta opettajan tehtavan repositori ja avaa kansio seka luo python file kansioon
#(kansion polussa ei saa olla skandeja joten ala kayta onedrivea koska kulun nimessa on skandeja)
#2.lisaa koodin header alkuun mallin mukaan ja lisaa pvm seka omat nimikirjaimet
#3. poista koodista kaikki skandit
#4.muokataan koodi funktiomuotoon (nimea fuktio)
#5.importoidaan yksikkotestikirjasto
#6.lisataan runtest- muuttuja.
#7.jos runtest==0 niin ohjelma kutsuu em. luotua funktiota ja ohjelma toimii normaalisti
#  testaa etta koodi toimii normaalisti kun runtest==0
#8.lisataan testauksessa tarvittavat fuktioparametrit ja vertailut
# (kun runtest==1 niin blokataan mahdolliset kayttoliittymainputit yms. pois koodista)
# -> em. blokatut muuttujat syotetaan funktioparametreina testattavaan funktioon#
#9.testaa etta peruskoodi tulostaa testattavaa numeroa vastaavan testiarvon
#kun peruskoodi tulostaaa oikeita arvoja syottoparametreilla niin lisataan testiluokka seka return lauseke 
#peruskoodiin
#10.lisataan testiluokka ja testifuktiot
#11.ajetaan yksikkotestit terminaalista ja dokumentoidaan koodi (github)
#12.palauta yksikkotestattu koodi githubin "fork"- toiminnolla opettajalle opettajan repositoriin 

import unittest
runtest = 1

def counter(num):
    for counter in range(1, num + 1):
        if (counter % 2) == 0:
            print(counter)
            palautusarvo = "on parillinen"
            print(palautusarvo)
        else:
            print(counter)
            palautusarvo = "on pariton"
            print(palautusarvo)
    if runtest == 1:
        return palautusarvo

if runtest == 0:
    counter(2)

# python -m unittest parillinen_pariton_looppi.py
class parillinen_pariton_looppi(unittest.TestCase):
    def test_count_parillinen(self):
        actual = str(counter(4))
        expected = 'on parillinen'
        try: 
            assert actual == expected
        except:  
            print('Virhe parittomuuden tarkistamisessa')

    def test_count_pariton(self):
        actual = str(counter(3))
        expected = 'on pariton'
        try: 
            assert actual == expected
        except:  
            print('Virhe parittomuuden tarkistamisessa')
            

#- TULOS -#

# 1
# on pariton
# 2
# on parillinen
# 3
# on pariton
# 4
# on parillinen
# .1
# on pariton
# 2
# on parillinen
# 3
# on pariton
# .
# ----------------------------------------------------------------------
# Ran 2 tests in 0.004s

# OK