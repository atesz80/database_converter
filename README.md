# Adatbázis konverter alkalmazás

## Az alkalmazásról

Az alkalmazás segítségével könnyedén lementhetjük adatbázis tábláink tartalmát csv file-okba.
A program nagyon egyszerűen működik, csak ki kell választani a menteni kívánt táblát vagy táblákat és a "Save" gombra kattintva megtörténik a táblák tartalma csv file-okba mentése.

## Telepítése és elindítása

Töltse a repository-ból a szükséges file-okat

https://github.com/atesz80/database_converter.git

Futtatás előtt hozzon létre egy virtuális környezetet.
```bash
python3 -m venv env
```
Aktiválja a virtuális környezetet.
```bash
source env/bin/activate
```
Telepítse a függőségeket
```bash
pip3 install -r requirements.txt
```
Indítsa el az alkalmazást terminálból vagy parancssorból:
```bash
cd converter
python3.9 main.py
```
