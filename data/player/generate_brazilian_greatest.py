"""Generate data/player/brazilian_greatest.json. Run: python data/player/generate_brazilian_greatest.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID = {
    c["name"]
    for c in json.loads((ROOT / "data/club/clubs.json").read_text())
    + json.loads((ROOT / "data/club/world_cup_teams.json").read_text())
}
BR = "Brazil"

# name, position, years_active, clubs (excluding Brazil), extra_tags
ENTRIES = [
    ("Pele", "Forward", "1956–1977", ["Santos FC"], ["legend", "goat", "1950s", "1960s", "1970s"]),
    ("Garrincha", "Forward", "1953–1972", [], ["legend", "goat", "1960s"]),
    ("Zico", "Midfielder", "1971–1989", ["Flamengo"], ["legend", "1980s"]),
    ("Socrates", "Midfielder", "1974–1989", ["Corinthians"], ["legend", "1980s"]),
    ("Rivaldo", "Forward", "1991–2015", ["FC Barcelona", "AC Milan"], ["legend", "1990s", "2000s"]),
    ("Ronaldo", "Forward", "1993–2011", ["FC Barcelona", "Inter Milan", "Real Madrid", "Corinthians"], ["legend", "goat", "1990s", "2000s"]),
    ("Ronaldinho", "Forward", "1998–2015", ["Paris Saint-Germain", "FC Barcelona", "AC Milan"], ["legend", "2000s"]),
    ("Kaka", "Midfielder", "2001–2017", ["AC Milan", "Real Madrid"], ["legend", "2000s"]),
    ("Neymar", "Forward", "2009–present", ["Santos FC", "FC Barcelona", "Paris Saint-Germain"], ["legend", "2010s", "2020s"]),
    ("Romario", "Forward", "1985–2009", ["PSV Eindhoven", "FC Barcelona", "Flamengo"], ["legend", "1990s"]),
    ("Bebeto", "Forward", "1983–1999", [], ["legend", "1990s"]),
    ("Adriano", "Forward", "2000–2016", ["Inter Milan", "Sao Paulo FC"], ["legend", "2000s"]),
    ("Gabriel Jesus", "Forward", "2015–present", ["Manchester City", "Arsenal FC"], ["2010s", "2020s"]),
    ("Roberto Firmino", "Forward", "2011–2023", ["Liverpool FC"], ["2010s", "2020s"]),
    ("Vinicius Junior", "Forward", "2017–present", ["Real Madrid"], ["2010s", "2020s"]),
    ("Rodrygo", "Forward", "2018–present", ["Real Madrid"], ["2010s", "2020s"]),
    ("Richarlison", "Forward", "2015–present", ["Everton FC", "Tottenham Hotspur"], ["2010s", "2020s"]),
    ("Hulk", "Forward", "2006–present", ["Zenit Saint Petersburg"], ["2010s"]),
    ("Fred", "Forward", "2009–present", ["Manchester United", "FC Shakhtar Donetsk"], ["2010s", "2020s"]),
    ("Tostao", "Forward", "1963–1972", [], ["legend", "1960s", "1970s"]),
    ("Jairzinho", "Forward", "1965–1982", [], ["legend", "1960s", "1970s"]),
    ("Careca", "Forward", "1978–1997", ["SSC Napoli"], ["legend", "1980s", "1990s"]),
    ("Muller", "Forward", "1974–1992", ["Sao Paulo FC"], ["legend", "1980s", "1990s"]),
    ("Evaristo", "Forward", "1957–1968", ["FC Barcelona"], ["legend", "1950s", "1960s"]),
    ("Rivelino", "Midfielder", "1965–1981", ["Corinthians"], ["legend", "1970s"]),
    ("Gerson", "Midfielder", "1961–1974", [], ["legend", "1960s", "1970s"]),
    ("Didi", "Midfielder", "1945–1966", [], ["legend", "1950s", "1960s"]),
    ("Zizinho", "Midfielder", "1941–1967", [], ["legend", "1950s"]),
    ("Falcao", "Midfielder", "1972–1989", ["AS Roma"], ["legend", "1980s"]),
    ("Rai", "Midfielder", "1987–2000", ["Paris Saint-Germain", "Sao Paulo FC"], ["1990s"]),
    ("Leonardo", "Midfielder", "1987–2005", ["AC Milan", "Paris Saint-Germain"], ["1990s", "2000s"]),
    ("Juninho Pernambucano", "Midfielder", "1993–2013", ["Olympique Lyon", "Al Nassr"], ["1990s", "2000s", "2010s"]),
    ("Alex", "Midfielder", "1999–2014", ["Chelsea FC", "Fenerbahce"], ["2000s", "2010s"]),
    ("Paulinho", "Midfielder", "2008–2021", ["Tottenham Hotspur", "FC Barcelona"], ["2010s"]),
    ("Casemiro", "Midfielder", "2011–present", ["Real Madrid", "Manchester United"], ["2010s", "2020s"]),
    ("Fernandinho", "Midfielder", "2005–2022", ["Manchester City"], ["2010s", "2020s"]),
    ("Fabinho", "Midfielder", "2013–2023", ["Liverpool FC", "AS Monaco"], ["2010s", "2020s"]),
    ("Philippe Coutinho", "Midfielder", "2010–2022", ["Liverpool FC", "FC Barcelona"], ["2010s", "2020s"]),
    ("Lucas Moura", "Midfielder", "2010–present", ["Paris Saint-Germain", "Tottenham Hotspur"], ["2010s", "2020s"]),
    ("Willian", "Forward", "2007–2021", ["Chelsea FC", "Arsenal FC"], ["2010s", "2020s"]),
    ("Oscar", "Midfielder", "2008–2017", ["Chelsea FC"], ["2010s"]),
    ("Ramires", "Midfielder", "2009–2016", ["Chelsea FC"], ["2010s"]),
    ("Dunga", "Midfielder", "1982–1998", ["Inter Milan"], ["legend", "1980s", "1990s"]),
    ("Ze Roberto", "Midfielder", "1994–2012", ["Bayer Leverkusen", "Bayern Munich"], ["1990s", "2000s", "2010s"]),
    ("Gilberto Silva", "Midfielder", "1997–2013", ["Arsenal FC"], ["2000s", "2010s"]),
    ("Hernanes", "Midfielder", "2007–2017", ["SS Lazio", "Inter Milan", "Juventus"], ["2000s", "2010s"]),
    ("Anderson", "Midfielder", "2004–2015", ["Manchester United"], ["2000s", "2010s"]),
    ("Diego", "Midfielder", "2002–2016", ["FC Porto", "Werder Bremen", "Atletico Madrid", "Juventus"], ["2000s", "2010s"]),
    ("Ederson", "Goalkeeper", "2011–present", ["Manchester City"], ["2010s", "2020s"]),
    ("Alisson Becker", "Goalkeeper", "2016–present", ["Liverpool FC"], ["2010s", "2020s"]),
    ("Julio Cesar", "Goalkeeper", "1997–2015", ["Inter Milan", "Tottenham Hotspur"], ["2000s", "2010s"]),
    ("Dida", "Goalkeeper", "1991–2015", ["AC Milan"], ["1990s", "2000s", "2010s"]),
    ("Marcos", "Goalkeeper", "1992–2011", [], ["2000s"]),
    ("Taffarel", "Goalkeeper", "1985–2003", ["Atletico Madrid"], ["1980s", "1990s", "2000s"]),
    ("Rogerio Ceni", "Goalkeeper", "1990–2015", ["Sao Paulo FC"], ["1990s", "2000s", "2010s"]),
    ("Gilmar", "Goalkeeper", "1951–1969", ["Santos FC"], ["legend", "1950s", "1960s"]),
    ("Cafu", "Defender", "1988–2008", ["AS Roma", "AC Milan"], ["legend", "1990s", "2000s"]),
    ("Roberto Carlos", "Defender", "1991–2012", ["Real Madrid", "Inter Milan"], ["legend", "1990s", "2000s"]),
    ("Thiago Silva", "Defender", "2004–present", ["AC Milan", "Paris Saint-Germain", "Chelsea FC"], ["2000s", "2010s", "2020s"]),
    ("Lucio", "Defender", "1997–2016", ["Bayer Leverkusen", "Inter Milan", "Tottenham Hotspur"], ["2000s", "2010s"]),
    ("Dani Alves", "Defender", "2003–2023", ["FC Barcelona", "Paris Saint-Germain", "Sao Paulo FC"], ["2000s", "2010s", "2020s"]),
    ("Maicon", "Defender", "2001–2018", ["Inter Milan", "AS Roma"], ["2000s", "2010s"]),
    ("Marcelo", "Defender", "2005–2022", ["Real Madrid"], ["2000s", "2010s", "2020s"]),
    ("Aldair", "Defender", "1983–2000", ["AS Roma"], ["1980s", "1990s"]),
    ("Branco", "Defender", "1982–2002", ["ACF Fiorentina"], ["1980s", "1990s"]),
    ("Jorginho", "Defender", "1989–1995", [], ["1990s"]),
    ("Miranda", "Defender", "2006–2019", ["Atletico Madrid", "Inter Milan"], ["2010s"]),
    ("Juan", "Defender", "1999–2012", ["AS Roma", "Inter Milan"], ["2000s", "2010s"]),
    ("Edmilson", "Defender", "1994–2011", ["Olympique Lyon", "FC Barcelona"], ["1990s", "2000s", "2010s"]),
    ("Julio Belletti", "Defender", "1992–2010", ["FC Barcelona", "Chelsea FC"], ["1990s", "2000s", "2010s"]),
    ("Gabriel Magalhaes", "Defender", "2015–present", ["Arsenal FC"], ["2010s", "2020s"]),
    ("Marquinhos", "Defender", "2012–present", ["Paris Saint-Germain", "AS Roma"], ["2010s", "2020s"]),
    ("Danilo", "Defender", "2007–present", ["FC Porto", "Real Madrid", "Juventus", "Manchester City"], ["2000s", "2010s", "2020s"]),
    ("Carlos Alberto", "Defender", "1958–1982", ["Santos FC"], ["legend", "1960s", "1970s"]),
    ("Nilton Santos", "Defender", "1948–1964", [], ["legend", "1950s", "1960s"]),
    ("Djalma Santos", "Defender", "1948–1970", [], ["legend", "1950s", "1960s", "1970s"]),
    ("Clodoaldo", "Midfielder", "1965–1984", [], ["legend", "1970s", "1980s"]),
    ("Leao", "Goalkeeper", "1967–1986", [], ["legend", "1970s", "1980s"]),
    ("Robinho", "Forward", "2002–2020", ["Real Madrid", "Manchester City", "AC Milan"], ["2000s", "2010s"]),
    ("Denilson", "Midfielder", "1991–2006", ["Real Betis"], ["1990s", "2000s"]),
    ("Kleberson", "Midfielder", "1998–2013", ["Manchester United"], ["2000s"]),
    ("Luis Fabiano", "Forward", "1998–2016", ["Sevilla FC", "Sao Paulo FC"], ["2000s", "2010s"]),
    ("Elano", "Forward", "2001–2015", ["Manchester City"], ["2000s", "2010s"]),
    ("Grafite", "Forward", "2001–2016", ["VfL Wolfsburg"], ["2000s", "2010s"]),
    ("Gabriel Barbosa", "Forward", "2013–present", ["Inter Milan", "Flamengo"], ["2010s", "2020s"]),
    ("Raphinha", "Forward", "2014–present", ["Leeds United", "FC Barcelona"], ["2010s", "2020s"]),
    ("Martinelli", "Forward", "2019–present", ["Arsenal FC"], ["2010s", "2020s"]),
    ("Malcom", "Forward", "2014–present", ["FC Barcelona", "Zenit Saint Petersburg"], ["2010s", "2020s"]),
    ("Talisca", "Midfielder", "2013–present", ["SL Benfica", "Al Nassr"], ["2010s", "2020s"]),
    ("Luiz Gustavo", "Midfielder", "2007–2022", ["Bayern Munich", "VfL Wolfsburg"], ["2000s", "2010s", "2020s"]),
    ("Renato Gaucho", "Midfielder", "1983–2011", ["Flamengo"], ["1980s", "1990s", "2000s", "2010s"]),
    ("Edmundo", "Forward", "1991–2008", ["ACF Fiorentina", "Valencia CF"], ["1990s", "2000s"]),
    ("Viola", "Forward", "1985–2006", ["Corinthians", "Sao Paulo FC"], ["1980s", "1990s", "2000s"]),
    ("Vava", "Forward", "1951–1969", ["Atletico Madrid"], ["legend", "1950s", "1960s"]),
    ("Leonidas da Silva", "Forward", "1929–1950", [], ["legend", "1930s", "1940s"]),
    ("Formiga", "Midfielder", "1995–2021", [], ["legend", "1990s", "2000s", "2010s", "2020s"]),
    ("Marta", "Forward", "2000–2024", [], ["legend", "2000s", "2010s", "2020s"]),
    ("Cristiane", "Forward", "2000–2020", ["Paris Saint-Germain", "Olympique Lyon"], ["2000s", "2010s", "2020s"]),
    ("Pedro", "Forward", "2006–present", ["Chelsea FC", "Flamengo"], ["2000s", "2010s", "2020s"]),
    ("Arthur", "Midfielder", "2015–present", ["FC Barcelona", "Liverpool FC", "Juventus"], ["2010s", "2020s"]),
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
                "clubs": [*clubs, BR],
                "tags": ["brazilian", *tags],
            }
        )

    out = ROOT / "data/player/brazilian_greatest.json"
    out.write_text(json.dumps(players, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(players)} players to {out}")


if __name__ == "__main__":
    main()