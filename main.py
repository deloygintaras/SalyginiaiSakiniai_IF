# 6 tema
# 2.
# Liepkite vartotojui suvesti savo amžių. Patikrinkite ar amžius yra didesnis arba lygus 18-ai, jei taip -išveskite "jūs galite balsuoti".
import pathlib

# print("suveskite savo amziu")
# amzius = int(input())
# if amzius >= 18:
#     print("jus galite balsuoti")
# else:
#     print("jus negalite balsuoti")
# 3.
# Leiskite vartotojui suvesti norimą kiekį pažymių (pavyzdžiui, jūs nusimatote 3-is kintamuosius, tai leidžiate padaryti 3 įvedimus).
# Raskite šių pažymių vidurkį. Patikrinkite ar vidurkis teigiamas (daugiau arba lygu 5-iems), jei taip -išveskite "vidurkis teigiamas".

# print("suveskite norima kieki pazymiu")
# paz = []
# for i in range(3):
#     paz = float(input())
# if paz >= 5:
#     print("vidurkis teigiamas")
# else:
#     print("vidurkis neigiamas")

# 4.
# Susikurkite skaičiaus kintamąjį arba leiskite šį skaičių įvesti vartotojui. Atlikite šiuos patikrinimus ir veiksmus:
# 1.
# Jei skaičius dalinasi iš 5, tuomet išveskite šio skaičiaus daugybos lentelę nuo 1 iki 5.
# 2.
# Jei skaičius lyginis, tuomet išveskite šį skaičių, jo kvadratą ir jį padalintą iš 2.
# 3.
# Jei skaičius nesidalina iš 7, tuomet susikurkite antrąjį kintamąjį, išveskite šių dviejų skaičių sumą, skirtumą, sandaugą, dalmenį.

# print("iveskite viena skaiciaus kintamaji")
# kint = int(input())
# if kint % 5 == 0:
#     print(f"{kint} * 1 = {kint * 1}")
#     print(f"{kint} * 2 = {kint * 2}")
#     print(f"{kint} * 3 = {kint * 3}")
#     print(f"{kint} * 4 = {kint * 4}")
#     print(f"{kint} * 5 = {kint * 5}")
# else:
#     print("skaicius nesidalina is 5")

# print("iveskite viena skaiciaus kintamaji")
# kint = int(input())
# if kint % 2 == 0:
#     print(f"pasirinktas skaicius: {kint}")
#     print(f"skaiciaus kvadratas: {kint} **2 = {kint ** 2}")
#     print(f"skaicius padalintas is 2: {kint} / 2 = {kint / 2}")
# else:
#     print("skaicius nelyginis")

# print("iveskite viena skaiciaus kintamaji")
# kint = int(input())
# if kint % 7 != 0:
#     print("prasau iveskite kita skaiciu")
#     kint2 = int(input())
#     print(f"{kint} + {kint2} = {kint + kint2}")
#     print(f"{kint} - {kint2} = {kint - kint2}")
#     print(f"{kint} * {kint2} = {kint * kint2}")
#     print(f"{kint} / {kint2} = {kint / kint2}")
# else:
#     print("skacius dalinasi is 7")

# 5.
# Susikurkite tris skaièiu kintamuosius su norimomis reikšmemis, arba leiskite šiuos skaièius suvesti vartotojui.
# Patikrinkite šias s¹lygas (naudojant elif dalis):
# 1.
# Ar pirmas skaièius didesnis už antr¹?
# 2.
# Ar antras skaièius didesnis už treèi¹?
# 3.
# Ar treèias skaièius didesnis už pirm¹?

sk1 = 6
sk2 = 8
sk3 = 11

# if sk1 > sk2:
#     print("pirmas skaicius didesnis uz antraji")
# elif sk2 > sk3:
#     print("antras skaicius didesnis uz treciaji")
# elif sk3 > sk1:
#     print("trecias skaicius didesnis uz pirmaji")

# 6. Susikurkite tris skaičių kintamuosius su norimomis reikšmėmis, arba leiskite šiuos skaičius suvesti vartotojui.
# Patikrinkite šias sąlygas (naudojant elif dalis):
# 1.
# Ar pirmi du skaičiai yra lygūs?
# 2.
# Ar paskutiniai du skaičiai yra lygūs?
# 3.
# Ar pirmas skaičius yra lygus 0?
# 4.
# Ar antras skaičius neigiamas?
# 5.
# Ar trečias skaičius teigiamas?

# print("suveskite tris skaiciu kintamuosius")
# print ("skaicius 1")
# sk1 = int(input())
# print("skaicius 2")
# sk2 = int(input())
# print("skaicius 3")
# sk3 = int(input())
# if sk1 == sk2:
#     print("sk 1 lygus sk2")
# elif sk2 == sk3:
#     print("sk2 lygus sk3")
# elif sk1 == 0:
#     print("1 skaicius lygus 0")
# elif sk2 < 0:
#     print("antras skaicius neigiamas")
# elif sk3 > 0:
#     print("trecias skaicius teigiamas")

# 7. Susikurkite kintam¹ji egzamino pažymiui saugoti [0-10]. Naudojant elif dalis patikrinkite šias s¹lygas ir išveskite atitinkam¹ tekst¹:
# 1.
# Jei pažymys yra lygus 10 išvesti “puiku”.
# 2.
# Jei pažymys yra lygus arba didesnis nei 9 išvesti “labai gerai”.
# 3.
# Jei pažymys yra lygus arba didesnis nei 7 išvesti “gerai”.
# 4.
# Jei pažymys yra lygus arba didesnis nei 5 išvesti “patenkinamai”.
# 5.
# Jei pažymys mažesnis nei 5 išvesti “egzaminas neišlaikytas”.

# print("galutinis ivertinimas:")
# sk1 = 8
# if sk1 == 10:
#     print("puiku")
# elif sk1 >= 9:
#     print("labai gerai")
# elif sk1 >= 7:
#     print("gerai")
# elif sk1 >= 5:
#     print("patenkinamai")
# elif sk1 < 5:
#     print("egzaminas neislaikytas")

# 7.
# Leiskite vartotojui suvesti norimą skaičių. Patikrinkite ar jis yra lyginis, jei taip išveskite vieną informaciją, jei ne -kitą.

# print("suveskite norima skaciu")
# sk1 = int(input())
# if sk1 % 2 == 0:
#     print("skacius lyginis")
# else:
#     print("skacius nelyginis")

#
# 8.
# Leiskite vartotojui suvesti norim¹ skaièiu. Patikrinkite ar šis skaièius dalinasi iš 7, jei taip išveskite vien¹ tekst¹, jei ne -kit¹.
# print("iveskite norima skaiciu")
# sk1 = int(input())
# if sk1 % 7 == 0:
#     print("skaicius dalinasi is 7")
# else:
#     print("skacius nesidalina is 7")


# 9.
# Susikurkite kintam¹ji, kuriame nurodytumete keli¹ iki norimo failo.
# Patikrinkite ar šis failas yra .py tipo, jei taip išveskite vien¹ tekst¹, jei ne -kit¹.

# file_format = pathlib.Path("main.py").suffix
# if file_format == '.py':
#     print("failas .py")
# else:
#     print("failas ne .py")

# 10.
# Susikurkite skaièiui saugoti skirt¹ kintam¹ji, arba reikšmê leiskite suvesti vartotojui. Tikrinkite (naudojant visas if s¹lygos dalis):
# 1.
# Ar skaièius yra lyginis?
# 2.
# Ar dalinasi iš 5?
# 3.
# Ar skaièius lygus 3?
# 4.
# Jeigu nieko nepavyko rasti, išveskite klaidos pranešim¹.

# print("iveskite skaiciu")
# sk1 = int(input())
# if sk1 % 2 == 0:
#     print(f"{sk1} skaicius yra lyginis")
# elif sk1 % 5 == 0:
#     print(f"{sk1} dalinasi is 5")
# elif sk1 == 3:
#     print(f"{sk1} lygus 3")
# else:
#     print("ERROR 404")

# 11.
# Susikurkite tris skaièius arba leiskite visus skaièius suvesti vartotojui. Tikrinkite (naudojant visas if s¹lygos dalis):
# 1.
# Ar pirmi du skaièiai lygus?
# 2.
# Ar pirmas ir treèias skaièiai lygus?
# 3.
# Ar treèias skaièius didesnis už pirm¹?
# 4.
# Ar antras skaièius lygus dvigubai treèio skaièiaus reikšmei?
# 5.
# Ar pirmas skaièius dalinasi iš 3?
# 6.
# Jei nieko nepavyko rasti, išveskite klaidos pranešim¹.

# print("sukurkite 3 skaicius")
# print("skaicius 1")
# sk1 = int(input())
# print("skacius 2")
# sk2 = int(input())
# print("skacius 3")
# sk3 = int(input())
# if sk1 == sk2:
#     print("f{sk1}  1 lygus 2 {sk2}")
# elif sk1 == sk3:
#     print(f"{sk1} 1 lygus 3 {sk3}")
# elif sk3 > sk1:
#     print(f"{sk3} didesnis uz {sk1}")
# elif sk2 == sk3**2:
#     print(f"{sk2} lygus 3 skaicio dvigubai reiksmei")
# elif sk1 % 3 == 0:
#     print(f"{sk1} dalinasi is 3")
# else:
#     print("ERROR 404")

# 12.
# Leiskite vartotojui suvesti tris skaičius. Suraskite kuris iš šių skaičių yra didžiausias.
