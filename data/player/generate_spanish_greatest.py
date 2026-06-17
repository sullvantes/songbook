"""Generate data/player/spanish_greatest.json. Run: python data/player/generate_spanish_greatest.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID = {
    c["name"]
    for c in json.loads((ROOT / "data/club/clubs.json").read_text())
    + json.loads((ROOT / "data/club/world_cup_teams.json").read_text())
}
ES = "Spain"

# name, position, years_active, clubs (excluding Spain), extra_tags
ENTRIES = [
    ("Iker Casillas", "Goalkeeper", "1999–2020", ["Real Madrid", "FC Porto"], ["legend", "2000s", "2010s"]),
    ("Andoni Zubizarreta", "Goalkeeper", "1981–1998", ["Athletic Club", "FC Barcelona", "Valencia CF"], ["legend", "1980s", "1990s"]),
    ("Luis Arconada", "Goalkeeper", "1974–1988", ["Real Sociedad"], ["legend", "1970s", "1980s"]),
    ("Victor Valdes", "Goalkeeper", "2002–2018", ["FC Barcelona"], ["2000s", "2010s"]),
    ("David de Gea", "Goalkeeper", "2009–present", ["Atletico Madrid", "Manchester United"], ["2010s", "2020s"]),
    ("Pepe Reina", "Goalkeeper", "1999–2021", ["FC Barcelona", "Liverpool FC", "AC Milan", "SSC Napoli", "Villarreal CF"], ["2000s", "2010s", "2020s"]),
    ("Antoni Ramallets", "Goalkeeper", "1947–1964", ["FC Barcelona"], ["legend", "1950s", "1960s"]),
    ("Ricardo Zamora", "Goalkeeper", "1918–1938", ["Real Madrid"], ["legend", "1920s", "1930s"]),
    ("Unai Simon", "Goalkeeper", "2014–present", ["Athletic Club"], ["2010s", "2020s"]),
    ("Santiago Canizares", "Goalkeeper", "1987–2010", ["Real Madrid", "Valencia CF"], ["1990s", "2000s"]),
    ("Sergio Ramos", "Defender", "2003–2023", ["Sevilla FC", "Real Madrid", "Paris Saint-Germain"], ["legend", "2000s", "2010s", "2020s"]),
    ("Carles Puyol", "Defender", "1995–2014", ["FC Barcelona"], ["legend", "2000s", "2010s"]),
    ("Gerard Pique", "Defender", "2004–2023", ["Manchester United", "FC Barcelona"], ["legend", "2000s", "2010s", "2020s"]),
    ("Jordi Alba", "Defender", "2005–present", ["Valencia CF", "FC Barcelona", "Inter Miami CF"], ["2000s", "2010s", "2020s"]),
    ("Fernando Hierro", "Defender", "1987–2005", ["Real Madrid"], ["legend", "1980s", "1990s", "2000s"]),
    ("Dani Carvajal", "Defender", "2010–present", ["Bayer Leverkusen", "Real Madrid"], ["2010s", "2020s"]),
    ("Nacho", "Defender", "2011–present", ["Real Madrid"], ["2010s", "2020s"]),
    ("Alvaro Arbeloa", "Defender", "2004–2016", ["Real Madrid", "Liverpool FC", "West Ham United"], ["2000s", "2010s"]),
    ("Joan Capdevila", "Defender", "1995–2014", ["FC Barcelona", "Villarreal CF", "SL Benfica"], ["1990s", "2000s", "2010s"]),
    ("Marc Bartra", "Defender", "2010–present", ["FC Barcelona", "Borussia Dortmund", "Real Betis"], ["2010s", "2020s"]),
    ("Pau Torres", "Defender", "2016–present", ["Villarreal CF", "Aston Villa"], ["2010s", "2020s"]),
    ("Aymeric Laporte", "Defender", "2010–present", ["Athletic Club", "Manchester City"], ["2010s", "2020s"]),
    ("Cesar Azpilicueta", "Defender", "2008–present", ["Chelsea FC", "Atletico Madrid"], ["2000s", "2010s", "2020s"]),
    ("Alberto Moreno", "Defender", "2011–present", ["Sevilla FC", "Liverpool FC", "Villarreal CF"], ["2010s", "2020s"]),
    ("Jose Antonio Camacho", "Defender", "1973–1989", ["Real Madrid"], ["legend", "1970s", "1980s"]),
    ("Rafael Alkorta", "Defender", "1984–1997", ["Athletic Club", "Real Madrid"], ["legend", "1980s", "1990s"]),
    ("Miguel Angel Nadal", "Defender", "1986–1999", ["FC Barcelona"], ["legend", "1980s", "1990s"]),
    ("Jose Maria Pirri", "Defender", "1964–1982", ["Real Madrid"], ["legend", "1960s", "1970s", "1980s"]),
    ("Eric Garcia", "Defender", "2017–present", ["Manchester City", "FC Barcelona"], ["2010s", "2020s"]),
    ("Inigo Martinez", "Defender", "2011–present", ["Real Sociedad", "Atletico Madrid"], ["2010s", "2020s"]),
    ("Andoni Goikoetxea", "Defender", "1975–1990", ["Athletic Club"], ["legend", "1970s", "1980s"]),
    ("Irene Paredes", "Defender", "2008–present", ["Paris Saint-Germain", "FC Barcelona"], ["2010s", "2020s"]),
    ("Xavi", "Midfielder", "1998–2019", ["FC Barcelona"], ["legend", "goat", "1990s", "2000s", "2010s"]),
    ("Andres Iniesta", "Midfielder", "2002–2023", ["FC Barcelona"], ["legend", "goat", "2000s", "2010s", "2020s"]),
    ("Sergio Busquets", "Midfielder", "2008–present", ["FC Barcelona", "Inter Miami CF"], ["legend", "2000s", "2010s", "2020s"]),
    ("Cesc Fabregas", "Midfielder", "2003–2023", ["Arsenal FC", "FC Barcelona", "Chelsea FC", "AS Monaco"], ["legend", "2000s", "2010s", "2020s"]),
    ("David Silva", "Midfielder", "2003–2020", ["Valencia CF", "Manchester City", "Real Sociedad"], ["legend", "2000s", "2010s", "2020s"]),
    ("Xabi Alonso", "Midfielder", "1999–2017", ["Real Sociedad", "Liverpool FC", "Real Madrid", "Bayern Munich"], ["legend", "2000s", "2010s"]),
    ("Luis Enrique", "Midfielder", "1991–2004", ["Sporting CP", "Real Madrid", "FC Barcelona"], ["legend", "1990s", "2000s"]),
    ("Pep Guardiola", "Midfielder", "1988–2006", ["FC Barcelona"], ["legend", "1980s", "1990s", "2000s"]),
    ("Michel", "Midfielder", "1982–1990", ["Real Madrid"], ["legend", "1980s"]),
    ("Gaizka Mendieta", "Midfielder", "1992–2008", ["Valencia CF", "SS Lazio", "FC Barcelona"], ["legend", "1990s", "2000s"]),
    ("Marcos Senna", "Midfielder", "1995–2013", ["Villarreal CF"], ["legend", "2000s", "2010s"]),
    ("Santi Cazorla", "Midfielder", "2003–2020", ["Villarreal CF", "Arsenal FC"], ["legend", "2000s", "2010s", "2020s"]),
    ("Koke", "Midfielder", "2009–present", ["Atletico Madrid"], ["2010s", "2020s"]),
    ("Saul Niguez", "Midfielder", "2009–present", ["Atletico Madrid", "Chelsea FC"], ["2010s", "2020s"]),
    ("Isco", "Midfielder", "2010–2024", ["Real Madrid"], ["2010s", "2020s"]),
    ("Dani Ceballos", "Midfielder", "2014–present", ["Real Madrid", "Arsenal FC"], ["2010s", "2020s"]),
    ("Pedri", "Midfielder", "2020–present", ["FC Barcelona"], ["2020s"]),
    ("Gavi", "Midfielder", "2021–present", ["FC Barcelona"], ["2020s"]),
    ("Rodri", "Midfielder", "2013–present", ["Villarreal CF", "Atletico Madrid", "Manchester City"], ["2010s", "2020s"]),
    ("Mikel Merino", "Midfielder", "2014–present", ["Real Sociedad", "Newcastle United"], ["2010s", "2020s"]),
    ("Fabian Ruiz", "Midfielder", "2014–present", ["Real Betis", "SSC Napoli", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Thiago", "Midfielder", "2008–2023", ["FC Barcelona", "Bayern Munich", "Liverpool FC"], ["2000s", "2010s", "2020s"]),
    ("Pablo Fornals", "Midfielder", "2014–present", ["Villarreal CF", "West Ham United"], ["2010s", "2020s"]),
    ("Juan Mata", "Midfielder", "2007–2023", ["Valencia CF", "Chelsea FC", "Manchester United"], ["2000s", "2010s", "2020s"]),
    ("Dani Olmo", "Midfielder", "2014–present", ["GNK Dinamo Zagreb", "RB Leipzig", "FC Barcelona"], ["2010s", "2020s"]),
    ("Ruben Baraja", "Midfielder", "1993–2010", ["Valencia CF", "Atletico Madrid"], ["1990s", "2000s"]),
    ("Luis Milla", "Midfielder", "1986–2001", ["Real Madrid"], ["1980s", "1990s", "2000s"]),
    ("Rafael Gordillo", "Midfielder", "1977–1993", ["Real Madrid", "Atletico Madrid"], ["1970s", "1980s", "1990s"]),
    ("Jose Mari Bakero", "Midfielder", "1980–1997", ["FC Barcelona"], ["legend", "1980s", "1990s"]),
    ("Raul Garcia", "Midfielder", "2004–present", ["Atletico Madrid", "Athletic Club"], ["2000s", "2010s", "2020s"]),
    ("Albert Celades", "Midfielder", "1995–2010", ["Real Madrid"], ["1990s", "2000s"]),
    ("Aitana Bonmati", "Midfielder", "2012–present", ["FC Barcelona"], ["legend", "2010s", "2020s"]),
    ("Alexia Putellas", "Midfielder", "2011–present", ["FC Barcelona"], ["legend", "2010s", "2020s"]),
    ("Teresa Abelleira", "Midfielder", "2018–present", ["Real Madrid"], ["2010s", "2020s"]),
    ("Raul", "Forward", "1994–2015", ["Real Madrid", "FC Schalke 04"], ["legend", "goat", "1990s", "2000s", "2010s"]),
    ("Fernando Torres", "Forward", "2001–2019", ["Atletico Madrid", "Liverpool FC", "Chelsea FC", "AC Milan"], ["legend", "2000s", "2010s"]),
    ("David Villa", "Forward", "2001–2020", ["Valencia CF", "FC Barcelona", "Atletico Madrid"], ["legend", "2000s", "2010s"]),
    ("Fernando Morientes", "Forward", "1993–2010", ["Real Madrid", "AS Monaco", "Liverpool FC"], ["1990s", "2000s"]),
    ("Emilio Butragueno", "Forward", "1984–1998", ["Real Madrid"], ["legend", "1980s", "1990s"]),
    ("Luis Suarez", "Forward", "1940–1961", ["FC Barcelona", "Inter Milan"], ["legend", "1940s", "1950s"]),
    ("Telmo Zarra", "Forward", "1940–1955", ["Athletic Club"], ["legend", "1940s", "1950s"]),
    ("Quini", "Forward", "1970–1987", ["Sporting CP", "FC Barcelona"], ["legend", "1970s", "1980s"]),
    ("Alvaro Morata", "Forward", "2010–present", ["Real Madrid", "Juventus", "Chelsea FC", "Atletico Madrid"], ["2010s", "2020s"]),
    ("Ferran Torres", "Forward", "2016–present", ["Valencia CF", "Manchester City", "FC Barcelona"], ["2010s", "2020s"]),
    ("Marco Asensio", "Forward", "2014–present", ["Real Madrid", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Diego Costa", "Forward", "2006–2021", ["Atletico Madrid", "Chelsea FC"], ["2010s", "2020s"]),
    ("Josep Samitier", "Forward", "1919–1936", ["FC Barcelona"], ["legend", "1920s", "1930s"]),
    ("Paco Alcacer", "Forward", "2010–present", ["Valencia CF", "FC Barcelona", "Borussia Dortmund"], ["2010s", "2020s"]),
    ("Aritz Aduriz", "Forward", "2002–2020", ["Athletic Club"], ["2000s", "2010s", "2020s"]),
    ("Roberto Soldado", "Forward", "2005–2021", ["Real Madrid", "Valencia CF", "Tottenham Hotspur"], ["2000s", "2010s", "2020s"]),
    ("Julen Guerrero", "Forward", "1992–2006", ["Athletic Club"], ["legend", "1990s", "2000s"]),
    ("Lucas Vazquez", "Forward", "2008–present", ["Real Madrid"], ["2010s", "2020s"]),
    ("Pedro", "Forward", "2004–2021", ["FC Barcelona", "Chelsea FC"], ["2000s", "2010s", "2020s"]),
    ("Nico Williams", "Forward", "2021–present", ["Athletic Club"], ["2020s"]),
    ("Jenni Hermoso", "Forward", "2004–present", ["FC Barcelona", "Paris Saint-Germain"], ["legend", "2000s", "2010s", "2020s"]),
    ("Salma Paralluelo", "Forward", "2018–present", ["Villarreal CF", "FC Barcelona"], ["2020s"]),
    ("Santillana", "Forward", "1971–1988", ["Real Madrid"], ["legend", "1970s", "1980s"]),
    ("Amancio Amaro", "Forward", "1962–1976", ["Real Madrid"], ["legend", "1960s", "1970s"]),
    ("Ismael Urzaiz", "Forward", "1990–2007", ["Athletic Club"], ["1990s", "2000s"]),
    ("Dani Guiza", "Forward", "1996–2016", ["Valencia CF", "Fenerbahce"], ["2000s", "2010s"]),
    ("Alvaro Negredo", "Forward", "2003–2020", ["Sevilla FC", "Manchester City", "Valencia CF"], ["2000s", "2010s"]),
    ("Juanito", "Forward", "1973–1987", ["Real Madrid"], ["legend", "1970s", "1980s"]),
    ("Evariste", "Forward", "1981–1992", ["FC Barcelona"], ["legend", "1980s", "1990s"]),
    ("Carles Rexach", "Forward", "1969–1981", ["FC Barcelona"], ["legend", "1960s", "1970s", "1980s"]),
    ("Patri Guijarro", "Midfielder", "2012–present", ["FC Barcelona"], ["2010s", "2020s"]),
    ("Olga Carmona", "Defender", "2017–present", ["Real Madrid"], ["2020s"]),
    ("Joseba Etxeberria", "Forward", "1993–2010", ["Athletic Club"], ["1990s", "2000s"]),
    ("Mikel Oyarzabal", "Forward", "2014–present", ["Real Sociedad"], ["2010s", "2020s"]),
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
                "clubs": [*clubs, ES],
                "tags": ["spanish", *tags],
            }
        )

    out = ROOT / "data/player/spanish_greatest.json"
    out.write_text(json.dumps(players, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(players)} players to {out}")


if __name__ == "__main__":
    main()
