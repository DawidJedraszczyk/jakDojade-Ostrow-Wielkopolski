addBusList = [
['busNr1', 1, 45],
['busNr2', 2, 26],
['busNr4', 4, 22],
['busNr5', 5, 36],
['busNr6', 6, 36],
['busNr7', 7, 38],
['busNr8', 8, 23],
['busNr9', 9, 25],
['busNr10', 10, 29],
['busNr11', 11, 36],
['busNr12', 12, 31],
['busNr13', 13, 28],
['busNr14', 14, 39],
['busNr15', 15, 37],
['busNr16', 16, 34],
['busNr18', 18, 43],
['busNr20', 20, 42],
['busNr21', 21, 22],
['busNr22', 22, 42],
['busNr25', 25, 29]
]

dictionaries = [
    'busNr1 kierunek: Topola Wielka' ,
    'busNr1 kierunek: Dwernickiego' ,
    'busNr2 kierunek: Topola Osiedle' ,
    'busNr2 kierunek: Pruślin' ,
    'busNr4 kierunek: Smardów' ,
    'busNr4 kierunek: Wańkowicza',
    'busNr5 kierunek: Janków Zaleśny' ,
    'busNr5 kierunek: Nowa Krępa piekarnia' ,
    'busNr6 kierunek: Wielowieś' ,
    'busNr6 kierunek: Lotnicza Poznańska' ,
    'busNr7 kierunek: Wtórek wieś' ,
    'busNr7 kierunek: Lotnicza Poznańska' ,
    'busNr8 kierunek: Bema Cmentarz',
    'busNr8 kierunek: Komuny Paryskiej' ,
    'busNr9 kierunek: Pruślin' ,
    'busNr9 kierunek: Zacharzew' ,
    'busNr10 kierunek: Dwernickiego' ,
    'busNr10 kierunek: Komuny Paryskiej' ,
    'busNr11 kierunek: Gorzyce Wielkie' ,
    'busNr11 kierunek: Nowa Krępa piekarnia' ,
    'busNr12 kierunek: Topola Wielka' ,
    'busNr12 kierunek: Bema Cmentarz' ,
    'busNr13 kierunek: Zacharzew' ,
    'busNr13 kierunek: Janków Dw.PKP' ,
    'busNr14 kierunek: Ociąż' ,
    'busNr14 kierunek: Przeskok' ,
    'busNr15 kierunek: Chruszczyny' ,
    'busNr15 kierunek: Kuźnia' ,
    'busNr16 kierunek: Janków Przygodzki szkoła' ,
    'busNr16 kierunek: Centrum przesiadkowe' ,
    'busNr18 kierunek: Zamość wieś' ,
    'busNr18 kierunek: Lotnicza Poznańska' ,
    'busNr20 kierunek: N. Skalmierzyce Rynek' ,
    'busNr20 kierunek: Lotnicza Poznańska' ,
    'busNr21 kierunek: Gałązki Wielkie' ,
    'busNr21 kierunek: Lotnicza Poznańska' ,
    'busNr22 kierunek: Zacharzew' ,
    'busNr22 kierunek: Przeskok' ,
    'busNr25 kierunek: Zacharzew',
    'busNr25 kierunek: Komuny Paryskiej',
]

addStopsList = [
    # 1
    ['Dwernickiego', 'Żniwna III', 'Żniwna II', 'Żniwna I', 'Kłosowa', 'Zacharzew', 'Krotoszynska I', 'Batorego szkoła', 'Bema Cmentarz', 'Orzechowa I', 'Orzechowa', 'Radłowska I', 'Radłowska Sporna', 'Poznańska Lotnicza', 'Krotoszyńska ZAP', 'Centrum przesiadkowe', 'Raszkowska kościół', 'Plac 23 Stycznia II', 'Partyzancka', 'Głogowska', 'Kościuszki Armii Krajowej', 'Mylna I', 'Mylna II', 'Zębcowska I', 'Zębcowska II', 'Siewna II', 'Siewna I', 'Staroprzygodzka szkoła', 'Staroprzygodzka dyskoteka', 'Staroprzygodzka - sortownia', 'Sosnowa II', 'Sosnowa I', 'Sosnowa', 'Janków Dw.PKP', 'Janków Przyg. Sp. Chem. II', 'Janków Przygodzki Sp. Chem.', 'Janków Przygodzki cmentarz', 'Janków Przygodzki kościół', 'Janków Przygodzki wieś', 'Topola Wielka wieś IV', 'Topola Wielka wieś III','Topola Wielka wieś II n.ż.', 'Topola Wielka I', 'Topola Wielka skrzyżowanie', 'Topola Wielka'],
    # 2
    ['Pruślin', 'Grabowska Pruślin I', 'Grabowska Pruślińska', 'Grabowska Piaskowa', 'Grabowska Witosa', 'Grabowska szkoła', 'Kaliska Biedronka', 'Kaliska Bank','Gimnazjalna', 'Plac Bankowy', 'Partyzancka', 'Odolanowska I', 'Odolanowska Komenda', 'Odolanowska Bratnia', 'Odolanowska IV', 'Odolanowska Długa','Odolanowska VI', 'Odolanowska granica', 'Topola Mała I', 'Topola Mała II', 'Topola Osiedle skrzyżowanie', 'Topola Osiedle Dw. PKP', 'Topola Osiedle RSP', 'Topola Osiedle I n.ż.','Topola Osiedle nż', 'Topola Osiedle'],
    # 4
    ['Wańkowicza', 'Wańkowicza Zielona', 'Wodna', 'Spichrzowa II', 'Spichrzowa I', 'Centrum przesiadkowe', 'Raszkowska kościół', 'Wolności','Partyzancka', 'Głogowska', 'Wysocka ZUS', 'Wysocka Langiewicza', 'Nowa Hala', 'Kamienna', 'Kamienna Wiśniowa', 'Kamienna Łączność','Kamienna Południowa', 'Wysocko Małe I', 'Wysocko Małe pawilon', 'Smardów II', 'Smardów I', 'Smardów'],
    # 5
    ['Nowa Krępa piekarnia', 'Nowa Krępa I', 'Nowa Krępa II', 'Kaliska Spomasz', 'Kaliska Bank', 'Gimnazjalna', 'Plac Bankowy', 'Sienkiewicza', 'Wojska Polskiego', 'Krotoszyńska ZAP - wiadukt', 'Poznańska Krotoszyńska', 'Poznańska Lotnicza', 'Radłowska Sporna', 'Radłowska I','Radłowska II','Radłów I n/ż', 'Radłów szkoła', 'Radłów bar', 'Radłów', 'Radłów II n.ż.', 'Jaskółki PKS', 'Przybysławice I', 'Przybysławice bar', 'Raszków CPN', 'Raszków', 'Raszków CPN', 'Przybysławice staw', 'Pogrzybów I','Pogrzybów II', 'Walentynów I', 'Walentynów', 'Niemojewiec n.ż.', 'Niemojewiec I', 'Sulisław', 'Janków Zaleśny sklep', 'Janków Zaleśny'],
    # 6
    ['Lotnicza Poznańska','Poznańska Lotnicza', 'Krotoszyńska ZAP', 'Centrum przesiadkowe', 'Raszkowska kościół', 'Plac 23 Stycznia II', 'Partyzancka', 'Głogowska', 'Al. Powstańców Wlkp.', 'Kaliska Bank', 'Kaliska Biedronka', 'Grabowska szkoła', 'Grabowska Witosa', 'Grabowska Piaskowa', 'Grabowska Pruślińska', 'Grabowska - Jastrzębia', 'Grabowska Pruślin I', 'Pruślin', 'Wtórek PKS', 'Wtórek Sadowie', 'Parczew II', 'Parczew I n.ż.', 'Parczew Zmyślona', 'Sieroszewice III', 'Sieroszewice II', 'Sieroszewice I', 'Sieroszewice', 'Rososzyca cmentarz', 'Rososzyca','Rososzyca I n.ż.', 'Ołobok - granica', 'Ołobok', 'Masanów - sklep', 'Masanów - wieś', 'Masanów wieś II', 'Wielowieś'],
    # 7
    ['Lotnicza Poznańska','Poznańska Lotnicza', 'Krotoszyńska ZAP', 'Centrum przesiadkowe', 'Raszkowska kościół', 'Plac 23 Stycznia II', 'Partyzancka', 'Głogowska', 'Kompałły', 'Waryńskiego', 'Śmigielskiego I', 'Śmigielskiego', 'Paderewskiego I', 'Strzelecka II', 'Strzelecka I','Klasztorna I', 'Kamienna', 'Kamienna Wiśniowa', 'Kamienna Łączność', 'Kamienna Południowa', 'Wysocko Małe I', 'Wysocko Małe pawilon', 'Wysocko Małe szkoła', 'Wysocko Wielkie pawilon', 'Wysocko Wielkie remiza', 'Wysocko Wielkie kościół', 'Wysocko Wielkie n.ż.', 'Olendry Smardowskie n.ż.', 'Olendry Smardowskie','Olendry Smardowskie II n.ż.', 'Sadowie sklep', 'Sadowie', 'Sadowie Klasztor', 'Sadowie n/ż', 'Wtórek Sadowie', 'Wtórek wieś II', 'Wtórek wieś I', 'Wtórek wieś'],
    # 8
    ['Komuny Paryskiej', 'Komuny Paryskiej I', 'Komuny Paryskiej II', 'Komuny Paryskiej III', 'Strzelecka', 'Paderewskiego I', 'Paderewskiego II', 'Paderewskiego III', 'Piłsudskiego', 'Kaliska Bank', 'Gimnazjalna', 'Plac Bankowy', 'Sienkiewicza', 'Wojska Polskiego', 'Krotoszyńska ZAP - wiadukt','Poznańska Krotoszyńska', 'Poznańska Lotnicza', 'Radłowska Sporna', 'Radłowska I', 'Orzechowa', 'Orzechowa I', 'Bema cmentarz I', 'Bema Cmentarz'],
    # 9
    ['Zacharzew','Spacerowa I', 'Spacerowa II', 'Spacerowa III', 'Przymiejska I', 'Przymiejska II', 'Bema cmentarz I', 'Bema Cmentarz', 'Batorego ZAP', 'Krotoszyńska ZAP', 'Centrum przesiadkowe', 'Raszkowska kościół', 'M.Konopnickiej pawilon', 'M.Konopnickiej Sklejki', 'Reymonta','Limanowskiego cmentarz', 'Limanowskiego szpital', 'Kaliska Biedronka', 'Grabowska szkoła', 'Grabowska Witosa', 'Grabowska Piaskowa', 'Grabowska Pruślińska', 'Grabowska - Jastrzębia', 'Grabowska Pruślin I', 'Pruślin'],
    # 10
    ['Komuny Paryskiej','Komuny Paryskiej I', 'Komuny Paryskiej II', 'Komuny Paryskiej III', 'Strzelecka', 'Paderewskiego I', 'Paderewskiego II', 'Śmigielskiego I', 'Śmigielskiego II', 'Ks.Kar.Ledóchowskiego II', 'Limanowskiego MiniMal', 'Limanowskiego szpital', 'Limanowskiego cmentarz', 'Reymonta', 'M.Konopnickiej Sklejki','M.Konopnickiej pawilon', 'Raszkowska kościół', 'Centrum przesiadkowe', 'Krotoszyńska ZAP - wiadukt', 'Krotoszyńska Sowińskiego', 'Traugutta Czwartaków', 'Traugutta Skorupki', 'Traugutta Czarnieckiego', 'Traugutta Kordeckiego', 'Kordeckiego szkoła', 'Kordeckiego Urząd Skarbowy', 'Chłapowskiego I', 'Rejtana Prefabet', 'Dwernickiego'],
    # 11
    ['Nowa Krępa piekarnia','Nowa Krępa I', 'Nowa Krępa II', 'Witosa targowisko', 'Grabowska Witosa', 'Grabowska szkoła', 'Kaliska Spomasz', 'Bracka III', 'Bracka II', 'Bracka I', 'Grunwaldzka II', 'Grunwaldzka I', 'Limanowskiego Żeromskiego', 'Limanowskiego cmentarz', 'Limanowskiego szpital','Al. Słowackiego-Limanowskiego', 'M.Konopnickiej pawilon', 'Plac 23 Stycznia II', 'Partyzancka', 'Centrum przesiadkowe', 'Ostrów Wlkp - Dworzec PKP', 'Odolanowska I', 'Gorzycka Odolanowska', 'Gorzycka piekarnia', 'Gorzycka', 'Gorzycka Długa', 'Gorzycka Swobodna', 'Gorzycka V', 'Gorzycka Topolowa','Gorzyce Wielkie I', 'Gorzyce Wielkie II n.ż.', 'Gorzyce Wielkie III', 'Gorzyce Wielkie kościół', 'Gorzyce Wielkie V n.ż.', 'Gorzyce Wielkie Spokojna', 'Gorzyce Wielkie'],
    # 12
    ['Bema Cmentarz','Lotnicza Poznańska', 'Poznańska Lotnicza', 'Krotoszyńska ZAP', 'Centrum przesiadkowe', 'Raszkowska kościół', 'Plac 23 Stycznia II', 'Partyzancka', 'Głogowska', 'Armii Krajowej I', 'Armii Krajowej II', '3-go Maja - Żwirki', 'Wrocławska Miła', 'Wrocławska Kuźnia', 'Wrocławska Południowa','Wrocławska Osiedle', 'Wrocławska Janków Dw.PKP', 'Przygodzice cegielnia', 'Przygodzice osiedle', 'Przygodzice szkoła', 'Przygodzice', 'Przygodzice cmentarz', 'Pardalin', 'Janków Przygodzki szkoła', 'Janków Przygodzki wieś', 'Topola Wielka wieś IV', 'Topola Wielka wieś III', 'Topola Wielka wieś II n.ż.', 'Topola Wielka I','Topola Wielka skrzyżowanie', 'Topola Wielka'],
    # 13
    ['Janków Dw.PKP','Wrocławska Osiedle', 'Południowa III', 'Południowa II', 'Południowa I', 'Kamienna Łączność', 'Kamienna Wiśniowa', 'Kamienna', 'Klasztorna I', 'Strzelecka I', 'Strzelecka', 'Paderewskiego I', 'Paderewskiego II', 'Śmigielskiego I', 'Śmigielskiego II','Ks.Kar.Ledóchowskiego II', 'Kaliska Bank', 'Gimnazjalna', 'Plac Bankowy', 'Partyzancka', 'Plac 23 Stycznia I', 'Raszkowska kościół', 'Centrum przesiadkowe', 'Krotoszyńska ZAP - wiadukt', 'Krotoszyńska Sowińskiego', 'Krotoszyńska Bema', 'Krotoszynska I', 'Zacharzew'],
    # 14
    ['Przeskok','Gwarna', 'Krańcowa', 'Odskok II', 'Odskok I', 'Staroprzygodzka szkoła', 'Staroprzygodzka Siewna', 'Staroprzygodzka RDP', 'Budowlanych', 'Mylna II', 'Mylna I', 'Armii Krajowej II', 'Armii Krajowej I', 'Wrocławska szkoła', 'Sienkiewicza','Wojska Polskiego', 'Raszkowska kościół', 'M.Konopnickiej pawilon', 'Limanowskiego szpital', 'Limanowskiego cmentarz', 'Limanowskiego Żeromskiego', 'Limanowskiego Osadnicza', 'Limanowskiego Wenecja', 'Limanowskiego Piaski', 'Karski n.ż.', 'Karski', 'Kołątajew n.ż.', 'Kołątajew skrzyżowanie', 'Kołątajew Dw. PKP','Lewków cmentarz', 'Lewków park', 'Lewków SKR', 'Kwiatków II', 'Kwiatków I szkoła', 'Kwiatków', 'Kwiatków n.ż.', 'Fabianów II', 'Fabianów I', 'Ociąż'],
    # 15
    ['Kuźnia','3-go Maja szpital', '3-go Maja - Żwirki', 'Kościuszki Armii Krajowej', 'Kościuszki Bank', 'Sienkiewicza', 'Wojska Polskiego', 'Krotoszyńska ZAP - wiadukt', 'Krotoszyńska Sowińskiego', 'Krotoszyńska Bema', 'Krotoszynska I', 'Zacharzew', 'Zacharzew n.ż.', 'Lamki I', 'Lamki II','Lamki III', 'Lamki Świeligów', 'Lamki szkoła 1', 'Świeligów pawilon', 'Lamki szkoła 2', 'Lamki Świeligów', 'Lamki Zalesie', 'Lamki pętla', 'Lamki las n.ż.', 'Łąkociny I n.ż.', 'Łąkociny I', 'Łakociny Dw. PKP', 'Łakociny n.ż.', 'Daniszyn Ośrodek Zdrowia','Daniszyn wieś', 'Daniszyn SKR n.ż.', 'Mazury las', 'Cegły n.ż.', 'Cegły', 'Cegły n.ż.', 'Mazury las', 'Chruszczyny'],
    # 16
    ['Centrum przesiadkowe','Raszkowska kościół', 'Plac 23 Stycznia II', 'Partyzancka', 'Odolanowska I', 'Odolanowska Komenda', 'Odolanowska Bratnia', 'Odolanowska IV', 'Odolanowska Długa', 'Odolanowska VI', 'Odolanowska granica', 'Topola Mała I', 'Topola Mała II', 'Topola Osiedle skrzyżowanie', 'Topola Osiedle Dw. PKP','Topola Osiedle VI', 'Topola Osiedle V', 'Topola Osiedle', 'Topola Osiedle nż', 'Topola Osiedle I n.ż.', 'Topola Osiedle III n.ż.', 'Topola Osiedle II n.ż.', 'Topola Wielka szkoła', 'Topola Wielka wieś II n.ż.', 'Topola Wielka I', 'Topola Wielka skrzyżowanie', 'Topola Wielka', 'Topola Wielka skrzyżowanie', 'Topola Wielka I','Topola Wielka wieś II n.ż.', 'Topola Wielka wieś III', 'Topola Wielka wieś IV', 'Janków Przygodzki wieś', 'Janków Przygodzki szkoła'],
    # 18
    ['Lotnicza Poznańska','Poznańska Lotnicza', 'Krotoszyńska ZAP', 'Centrum przesiadkowe', 'Raszkowska kościół', 'Plac 23 Stycznia II', 'Partyzancka', 'Głogowska', 'Al. Powstańców Wlkp.', 'Kaliska Bank', 'Kaliska Biedronka', 'Grabowska szkoła', 'Grabowska Witosa', 'Grabowska Piaskowa', 'Grabowska Pruślińska','Grabowska - Jastrzębia', 'Grabowska Pruślin I', 'Pruślin', 'Wtórek PKS', 'Wtórek Sadowie', 'Parczew II', 'Parczew I n.ż.', 'Parczew Zmyślona', 'Sieroszewice III', 'Sieroszewice II', 'Latowice I', 'Sieroszewice I', 'Sieroszewice', 'Rososzyca cmentarz','Rososzyca bar', 'Psary', 'Sławin I', 'Sławin II', 'Sławin III', 'Ołobok', 'Masanów - sklep', 'Masanów - wieś', 'Masanów wieś II', 'Wielowieś', 'Wielowieś I las', 'Zamość I', 'Zamość II', 'Zamość wieś'],
    # 20
    ['Lotnicza Poznańska','Poznańska Lotnicza', 'Krotoszyńska ZAP', 'Centrum przesiadkowe', 'Ostrów Wlkp - Dworzec PKP', 'Głogowska', 'Kompałły', 'Kaliska Spomasz', 'Galeria Ostrovia -Serwańskiego', 'Czekanów', 'Fabianów', 'Biskupice Ociąż', 'Biskupice SKR', 'Biskupice cmentarz', 'Biskupice sklep','Biskupice', 'Biskupice sklep', 'Biskupice Ołoboczne n.ż.', 'Bilczew', 'Psary I', 'Psary II', 'Psary n.ż', 'Leziona', 'Leziona III', 'Leziona II szkoła', 'Leziona I', 'Leziona skrzyżowanie', 'Leziona PKS', 'Gostyczyna skrzyżowanie','Śmiłów II', 'Śmiłów I', 'Osiek II', 'Osiek I', 'Osiek n.ż.', 'Gostyczyna poczta', 'Strzegowa II sklep', 'Strzegowa I', 'Śliwniki II', 'Śliwniki I', 'Skalmierzyce kościół', 'Nowe Skalmierzyce Ośrodek Zdro', 'N. Skalmierzyce Rynek'],
    # 21
    ['Lotnicza Poznańska','Poznańska Lotnicza', 'Krotoszyńska ZAP', 'Centrum przesiadkowe', 'Ostrów Wlkp - Dworzec PKP', 'Głogowska', 'Kompałły', 'Kaliska Spomasz', 'Czekanów', 'Fabianów', 'Fabianów wieś I', 'Fabianów II', 'Fabianów I', 'Ociąż - Morawskiego 2', 'Kościuszków I','Kościuszków II', 'Kurów', 'Droszew', 'Droszew cmentarz', 'Kotowiecko', 'Pawłów', 'Gałązki Wielkie'],
    # 22
    ['Przeskok','Przeskok I', 'Przeskok II', 'Przeskok - Graniczna', 'Staroprzygodzka szkoła', 'Staroprzygodzka Siewna', 'Staroprzygodzka RDP', 'Budowlanych', 'Zębcowska I', 'Zębcowska II', 'Długa II', 'Odolanowska Długa', 'Odolanowska VI', 'Odolanowska granica', 'Topola Mała I','Topola Mała II', 'Topola Mała wieś skrzyżowanie', 'Topola Mała wieś n.ż.', 'Topola Mała remiza', 'Topola Mała wieś II', 'Topola Mała Gorzycka', 'Gorzyce Wielkie I', 'Gorzyce Wielkie II n.ż.', 'Gorzyce Wielkie III', 'Gorzyce Wielkie kościół', 'Gorzyce Wielkie III', 'Gorzyce Wielkie II n.ż.', 'Gorzyce Wielkie I', 'Gorzycka Topolowa','Gorzycka V', 'Gorzycka Swobodna', 'Gorzycka Długa', 'Gorzycka', 'Chłapowskiego I', 'Chłapowskiego Urząd Skarbowy', 'Kordeckiego szkoła', 'Traugutta Kordeckiego', 'Traugutta Czarnieckiego', 'Traugutta Skorupki', 'Krotoszyńska Bema', 'Krotoszynska I', 'Zacharzew'],
    # 25
    ['Komuny Paryskiej', 'Komuny Paryskiej I', 'Komuny Paryskiej II', 'Komuny Paryskiej III', 'Strzelecka', 'Paderewskiego I', 'Paderewskiego II', 'Paderewskiego III', 'Piłsudskiego', 'Limanowskiego MiniMal', 'Limanowskiego szpital', 'Limanowskiego cmentarz', 'Reymonta', 'M.Konopnickiej Sklejki', 'M.Konopnickiej pawilon','Wolności', 'Partyzancka', 'Centrum przesiadkowe', 'Ostrów Wlkp - Dworzec PKP', 'Odolanowska I', 'Kwiatowa', 'Okólna', 'Kordeckiego I', 'Kordeckiego szkoła', 'Kordeckiego Urząd Skarbowy', 'Chłapowskiego II', 'Wybickiego', 'Krotoszynska I', 'Zacharzew']
]

addHours = [
    ['busNr1', "Dwernickiego", [[8,10], [9,15], [10, 15], [11,15], [13, 5], [14, 10], [15, 10], [16, 10], [17, 30]]],
]