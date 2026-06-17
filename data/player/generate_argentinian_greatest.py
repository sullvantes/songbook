"""Generate data/player/argentinian_greatest.json. Run: python data/player/generate_argentinian_greatest.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID = {
    c["name"]
    for c in json.loads((ROOT / "data/club/clubs.json").read_text())
    + json.loads((ROOT / "data/club/world_cup_teams.json").read_text())
}
AR = "Argentina"

# name, position, years_active, clubs (excluding Argentina), extra_tags
ENTRIES = [
    ("Lionel Messi", "Forward", "2004–present", ["FC Barcelona", "Paris Saint-Germain", "Inter Miami CF"], ["legend", "goat", "2000s", "2010s", "2020s"]),
    ("Diego Maradona", "Forward", "1976–1997", ["Boca Juniors", "FC Barcelona", "SSC Napoli"], ["legend", "goat", "1970s", "1980s", "1990s"]),
    ("Alfredo Di Stefano", "Forward", "1945–1966", ["Real Madrid"], ["legend", "goat", "1950s", "1960s"]),
    ("Mario Kempes", "Forward", "1970–1991", ["Valencia CF"], ["legend", "1970s", "1980s"]),
    ("Gabriel Batistuta", "Forward", "1988–2005", ["ACF Fiorentina", "AS Roma"], ["legend", "1990s", "2000s"]),
    ("Carlos Tevez", "Forward", "2001–2021", ["Boca Juniors", "West Ham United", "Manchester United", "Manchester City", "Juventus"], ["legend", "2000s", "2010s"]),
    ("Sergio Aguero", "Forward", "2003–2021", ["Club Atletico Independiente", "Atletico Madrid", "Manchester City"], ["legend", "2000s", "2010s", "2020s"]),
    ("Angel Di Maria", "Forward", "2005–present", ["SL Benfica", "Real Madrid", "Manchester United", "Paris Saint-Germain", "Juventus"], ["legend", "2000s", "2010s", "2020s"]),
    ("Javier Mascherano", "Midfielder", "2003–2020", ["River Plate", "Liverpool FC", "FC Barcelona"], ["legend", "2000s", "2010s"]),
    ("Javier Zanetti", "Defender", "1992–2014", ["Inter Milan"], ["legend", "1990s", "2000s", "2010s"]),
    ("Diego Simeone", "Midfielder", "1987–2006", ["Atletico Madrid", "Inter Milan", "SS Lazio"], ["legend", "1990s", "2000s"]),
    ("Juan Roman Riquelme", "Midfielder", "1994–2015", ["Boca Juniors", "Villarreal CF", "Racing Club"], ["legend", "1990s", "2000s", "2010s"]),
    ("Hernan Crespo", "Forward", "1993–2012", ["SS Lazio", "Inter Milan", "Chelsea FC", "AC Milan"], ["legend", "1990s", "2000s", "2010s"]),
    ("Gonzalo Higuain", "Forward", "2005–2022", ["Real Madrid", "Juventus", "Chelsea FC"], ["2000s", "2010s", "2020s"]),
    ("Emiliano Martinez", "Goalkeeper", "2012–present", ["Arsenal FC", "Aston Villa"], ["2010s", "2020s"]),
    ("Lautaro Martinez", "Forward", "2015–present", ["Inter Milan"], ["2010s", "2020s"]),
    ("Paulo Dybala", "Forward", "2011–present", ["Juventus", "AS Roma"], ["2010s", "2020s"]),
    ("Nicolas Otamendi", "Defender", "2007–present", ["FC Porto", "Manchester City", "SL Benfica"], ["2010s", "2020s"]),
    ("Enzo Fernandez", "Midfielder", "2019–present", ["River Plate", "SL Benfica", "Chelsea FC"], ["2010s", "2020s"]),
    ("Alexis Mac Allister", "Midfielder", "2016–present", ["Brighton & Hove Albion", "Liverpool FC"], ["2010s", "2020s"]),
    ("Julian Alvarez", "Forward", "2018–present", ["River Plate", "Manchester City", "Atletico Madrid"], ["2010s", "2020s"]),
    ("Gonzalo Montiel", "Defender", "2016–present", ["River Plate", "Sevilla FC", "Nottingham Forest"], ["2010s", "2020s"]),
    ("Nahuel Molina", "Defender", "2016–present", ["Atletico Madrid"], ["2010s", "2020s"]),
    ("Nicolas Tagliafico", "Defender", "2011–present", ["Ajax", "Olympique Lyon"], ["2010s", "2020s"]),
    ("Cristian Romero", "Defender", "2016–present", ["Atalanta BC", "Tottenham Hotspur"], ["2010s", "2020s"]),
    ("Rodrigo De Paul", "Midfielder", "2012–present", ["Valencia CF", "Atletico Madrid"], ["2010s", "2020s"]),
    ("Leandro Paredes", "Midfielder", "2010–present", ["AS Roma", "Paris Saint-Germain", "Juventus"], ["2010s", "2020s"]),
    ("Guido Rodriguez", "Midfielder", "2014–present", ["Club America", "Real Betis"], ["2010s", "2020s"]),
    ("Lisandro Martinez", "Defender", "2017–present", ["Ajax", "Manchester United"], ["2010s", "2020s"]),
    ("Juan Sebastian Veron", "Midfielder", "1993–2010", ["SS Lazio", "Manchester United", "Chelsea FC", "Inter Milan"], ["legend", "1990s", "2000s"]),
    ("Pablo Aimar", "Midfielder", "1995–2015", ["Valencia CF", "SL Benfica", "River Plate"], ["legend", "1990s", "2000s", "2010s"]),
    ("Esteban Cambiasso", "Midfielder", "1995–2015", ["Real Madrid", "Inter Milan", "Leicester City", "Olympiacos"], ["legend", "1990s", "2000s", "2010s"]),
    ("Fernando Redondo", "Midfielder", "1985–2004", ["Real Madrid", "Inter Milan"], ["legend", "1990s", "2000s"]),
    ("Gabriel Heinze", "Defender", "1996–2012", ["Paris Saint-Germain", "Manchester United", "Real Madrid", "Olympique Marseille"], ["1990s", "2000s", "2010s"]),
    ("Roberto Ayala", "Defender", "1991–2010", ["Valencia CF", "Newcastle United"], ["legend", "1990s", "2000s"]),
    ("Walter Samuel", "Defender", "1995–2014", ["AS Roma", "Inter Milan"], ["1990s", "2000s", "2010s"]),
    ("Nicolas Burdisso", "Defender", "1999–2014", ["AS Roma", "Inter Milan"], ["2000s", "2010s"]),
    ("Pablo Zabaleta", "Defender", "2002–2020", ["Manchester City", "West Ham United"], ["2000s", "2010s", "2020s"]),
    ("Ever Banega", "Midfielder", "2004–2023", ["Valencia CF", "Sevilla FC", "Inter Milan"], ["2000s", "2010s", "2020s"]),
    ("Javier Pastore", "Midfielder", "2007–2021", ["Paris Saint-Germain", "AS Roma"], ["2000s", "2010s", "2020s"]),
    ("Erik Lamela", "Forward", "2010–present", ["AS Roma", "Tottenham Hotspur"], ["2010s", "2020s"]),
    ("Mauro Icardi", "Forward", "2012–present", ["Inter Milan", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Lucas Biglia", "Midfielder", "2002–2021", ["RSC Anderlecht", "SS Lazio", "AC Milan"], ["2000s", "2010s", "2020s"]),
    ("Giovani Lo Celso", "Midfielder", "2015–present", ["Real Betis", "Tottenham Hotspur", "Villarreal CF"], ["2010s", "2020s"]),
    ("Exequiel Palacios", "Midfielder", "2015–present", ["River Plate", "Bayer Leverkusen"], ["2010s", "2020s"]),
    ("Angel Correa", "Forward", "2013–present", ["Atletico Madrid"], ["2010s", "2020s"]),
    ("Lucas Alario", "Forward", "2013–present", ["River Plate", "Bayer Leverkusen"], ["2010s", "2020s"]),
    ("Franco Armani", "Goalkeeper", "2009–present", ["River Plate"], ["2010s", "2020s"]),
    ("Sergio Romero", "Goalkeeper", "2004–present", ["Manchester United", "AS Monaco"], ["2000s", "2010s", "2020s"]),
    ("Wilfredo Caballero", "Goalkeeper", "1998–2020", ["Manchester City", "Chelsea FC"], ["2000s", "2010s", "2020s"]),
    ("Ubaldo Fillol", "Goalkeeper", "1969–1987", [], ["legend", "1970s", "1980s"]),
    ("Nery Pumpido", "Goalkeeper", "1977–1997", ["Racing Club"], ["legend", "1980s", "1990s"]),
    ("Daniel Passarella", "Defender", "1971–1989", [], ["legend", "1970s", "1980s"]),
    ("Osvaldo Ardiles", "Midfielder", "1973–1991", ["Tottenham Hotspur"], ["legend", "1970s", "1980s", "1990s"]),
    ("Ricardo Bochini", "Midfielder", "1972–1991", ["Club Atletico Independiente"], ["legend", "1970s", "1980s", "1990s"]),
    ("Jorge Burruchaga", "Midfielder", "1982–1998", ["Club Atletico Independiente"], ["legend", "1980s", "1990s"]),
    ("Oscar Ruggeri", "Defender", "1982–1997", ["Real Madrid", "River Plate"], ["legend", "1980s", "1990s"]),
    ("Claudio Caniggia", "Forward", "1985–2004", ["Atalanta BC", "AS Roma", "Boca Juniors", "Rangers FC"], ["legend", "1980s", "1990s", "2000s"]),
    ("Sergio Goycochea", "Goalkeeper", "1983–1998", ["Racing Club"], ["legend", "1980s", "1990s"]),
    ("Ariel Ortega", "Forward", "1991–2012", ["Valencia CF", "River Plate", "Boca Juniors"], ["legend", "1990s", "2000s", "2010s"]),
    ("Juan Pablo Sorin", "Defender", "1995–2009", ["Paris Saint-Germain", "Juventus", "Villarreal CF", "Cruz Azul"], ["1990s", "2000s"]),
    ("Roberto Sensini", "Defender", "1986–2009", ["SS Lazio"], ["1990s", "2000s"]),
    ("Matias Almeyda", "Midfielder", "1991–2007", ["Sevilla FC", "Inter Milan"], ["1990s", "2000s"]),
    ("Marcelo Gallardo", "Midfielder", "1993–2009", ["River Plate", "AS Monaco", "Paris Saint-Germain"], ["legend", "1990s", "2000s"]),
    ("Andres D'Alessandro", "Midfielder", "1998–2022", ["Boca Juniors", "Werder Bremen", "FC Porto"], ["2000s", "2010s", "2020s"]),
    ("Martin Demichelis", "Defender", "2001–2016", ["Bayern Munich", "Manchester City"], ["2000s", "2010s"]),
    ("Fabricio Coloccini", "Defender", "1998–2016", ["Newcastle United", "Atletico Madrid"], ["2000s", "2010s"]),
    ("Gabriel Mercado", "Defender", "2006–2021", ["River Plate", "Sevilla FC", "Cruz Azul"], ["2000s", "2010s", "2020s"]),
    ("Marcos Acuna", "Defender", "2011–present", ["Sevilla FC", "AS Roma"], ["2010s", "2020s"]),
    ("German Pezzella", "Defender", "2011–present", ["ACF Fiorentina", "Real Betis"], ["2010s", "2020s"]),
    ("Emiliano Buendia", "Midfielder", "2014–present", ["Aston Villa", "Brighton & Hove Albion"], ["2010s", "2020s"]),
    ("Giovanni Simeone", "Forward", "2013–present", ["ACF Fiorentina", "SSC Napoli", "Atletico Madrid"], ["2010s", "2020s"]),
    ("Martin Palermo", "Forward", "1992–2011", ["Boca Juniors", "Real Betis"], ["legend", "1990s", "2000s", "2010s"]),
    ("Guillermo Barros Schelotto", "Midfielder", "1992–2007", ["Boca Juniors"], ["legend", "1990s", "2000s"]),
    ("Cesar Delgado", "Forward", "1998–2016", ["Cruz Azul", "Chivas Guadalajara"], ["2000s", "2010s"]),
    ("Maxi Rodriguez", "Midfielder", "1997–2017", ["Atletico Madrid", "Liverpool FC"], ["legend", "1990s", "2000s", "2010s"]),
    ("Javier Saviola", "Forward", "1998–2015", ["FC Barcelona", "AS Monaco", "SL Benfica", "River Plate", "Olympique Marseille"], ["2000s", "2010s"]),
    ("Ezequiel Lavezzi", "Forward", "2003–2019", ["SSC Napoli", "Paris Saint-Germain"], ["2000s", "2010s"]),
    ("Franco Di Santo", "Forward", "2006–2019", ["Chelsea FC", "Werder Bremen"], ["2000s", "2010s"]),
    ("Fernando Gago", "Midfielder", "2004–2018", ["Real Madrid", "AS Roma", "Boca Juniors"], ["2000s", "2010s"]),
    ("Jonas Gutierrez", "Midfielder", "2004–2016", ["Newcastle United"], ["2000s", "2010s"]),
    ("Roberto Pereyra", "Midfielder", "2008–present", ["Juventus"], ["2010s", "2020s"]),
    ("Lucas Pratto", "Forward", "2007–present", ["River Plate", "Sevilla FC"], ["2010s", "2020s"]),
    ("Franco Vazquez", "Forward", "2007–present", ["Sevilla FC", "ACF Fiorentina"], ["2010s", "2020s"]),
    ("Daniel Bertoni", "Forward", "1973–1986", ["Club Atletico Independiente"], ["legend", "1970s", "1980s"]),
    ("Ricardo Villa", "Midfielder", "1972–1984", ["Nottingham Forest"], ["legend", "1970s", "1980s"]),
    ("Alberto Tarantini", "Defender", "1975–1989", ["Juventus", "River Plate"], ["legend", "1970s", "1980s"]),
    ("Antonio Rattin", "Midfielder", "1956–1970", ["Boca Juniors"], ["legend", "1960s"]),
    ("Silvio Marzolini", "Defender", "1959–1972", ["Boca Juniors"], ["legend", "1960s", "1970s"]),
    ("Norberto Alonso", "Midfielder", "1971–1987", ["River Plate"], ["legend", "1970s", "1980s"]),
    ("Jorge Valdano", "Forward", "1975–1988", ["Real Madrid"], ["legend", "1970s", "1980s"]),
    ("Pedro Pasculli", "Forward", "1980–1996", [], ["legend", "1980s", "1990s"]),
    ("Dario Cvitanich", "Forward", "2005–2021", ["Ajax", "Paris Saint-Germain"], ["2000s", "2010s", "2020s"]),
    ("Claudio Reyna", "Midfielder", "1994–2007", ["Rangers FC", "Manchester City", "VfL Wolfsburg"], ["legend", "1990s", "2000s"]),
    ("Leopoldo Luque", "Forward", "1972–1989", [], ["legend", "1970s", "1980s"]),
    ("Eliana Stabile", "Forward", "2017–present", [], ["legend", "2010s", "2020s"]),
    ("Estefania Banini", "Forward", "2012–present", [], ["legend", "2010s", "2020s"]),
    ("Yamila Rodriguez", "Forward", "2016–present", [], ["2010s", "2020s"]),
    ("Macarena Sanchez", "Forward", "2015–present", [], ["2010s", "2020s"]),
    ("Maria Potassa", "Forward", "2006–present", [], ["legend", "2000s", "2010s", "2020s"]),
]


def main():
    names = [entry[0] for entry in ENTRIES]
    if len(names) != len(set(names)):
        dupes = {name for name in names if names.count(name) > 1}
        raise SystemExit(f"Duplicate players: {dupes}")
    if len(ENTRIES) != 100:
        raise SystemExit(f"Expected 100 players, got {len(ENTRIES)}")

    players = []
    for name, position, years, clubs, tags in ENTRIES:
        for club in clubs:
            if club not in VALID:
                raise SystemExit(f"{name}: unknown club {club!r}")
        players.append(
            {
                "name": name,
                "position": position,
                "years_active": years,
                "clubs": [*clubs, AR],
                "tags": ["argentinian", *tags],
            }
        )

    out = ROOT / "data/player/argentinian_greatest.json"
    out.write_text(json.dumps(players, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(players)} players to {out}")


if __name__ == "__main__":
    main()
