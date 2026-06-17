"""Generate data/player/portuguese_greatest.json. Run: python data/player/generate_portuguese_greatest.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID = {
    c["name"]
    for c in json.loads((ROOT / "data/club/clubs.json").read_text())
    + json.loads((ROOT / "data/club/world_cup_teams.json").read_text())
}
PT = "Portugal"

# name, position, years_active, clubs (excluding Portugal), extra_tags
ENTRIES = [
    ("Eusebio", "Forward", "1957–1975", ["SL Benfica"], ["legend", "goat", "1960s"]),
    ("Cristiano Ronaldo", "Forward", "2002–present", ["Sporting CP", "Manchester United", "Real Madrid", "Juventus"], ["legend", "goat", "2000s", "2010s", "2020s"]),
    ("Luis Figo", "Forward", "1989–2009", ["Sporting CP", "FC Barcelona", "Real Madrid", "Inter Milan"], ["legend", "goat", "1990s", "2000s"]),
    ("Rui Costa", "Midfielder", "1991–2008", ["SL Benfica", "ACF Fiorentina", "AC Milan"], ["legend", "1990s", "2000s"]),
    ("Deco", "Midfielder", "1997–2013", ["FC Porto", "FC Barcelona", "Chelsea FC"], ["legend", "2000s", "2010s"]),
    ("Pauleta", "Forward", "1990–2008", ["FC Porto", "Paris Saint-Germain", "SL Benfica"], ["legend", "1990s", "2000s"]),
    ("Pepe", "Defender", "2001–present", ["FC Porto", "Real Madrid", "Besiktas"], ["legend", "2000s", "2010s", "2020s"]),
    ("Bruno Fernandes", "Midfielder", "2012–present", ["Sporting CP", "Manchester United"], ["2010s", "2020s"]),
    ("Bernardo Silva", "Midfielder", "2014–present", ["SL Benfica", "AS Monaco", "Manchester City"], ["2010s", "2020s"]),
    ("Ruben Dias", "Defender", "2015–present", ["SL Benfica", "Manchester City"], ["2010s", "2020s"]),
    ("Joao Cancelo", "Defender", "2012–present", ["SL Benfica", "Valencia CF", "Juventus", "Manchester City", "Bayern Munich"], ["2010s", "2020s"]),
    ("Ruben Neves", "Midfielder", "2014–present", ["FC Porto", "Wolverhampton Wanderers"], ["2010s", "2020s"]),
    ("Nuno Gomes", "Forward", "1994–2015", ["SL Benfica"], ["legend", "1990s", "2000s", "2010s"]),
    ("Eder", "Forward", "2002–2021", ["Sporting CP", "Lille OSC"], ["legend", "2000s", "2010s", "2020s"]),
    ("Nani", "Midfielder", "2005–present", ["Sporting CP", "Manchester United"], ["2000s", "2010s", "2020s"]),
    ("Joao Moutinho", "Midfielder", "2004–present", ["Sporting CP", "AS Monaco", "FC Porto"], ["2000s", "2010s", "2020s"]),
    ("Ricardo Carvalho", "Defender", "1998–2017", ["FC Porto", "Chelsea FC"], ["legend", "2000s", "2010s"]),
    ("Vitor Baia", "Goalkeeper", "1986–2007", ["FC Porto", "FC Barcelona"], ["legend", "1990s", "2000s"]),
    ("Rui Patricio", "Goalkeeper", "2006–present", ["Sporting CP", "AS Roma", "Wolverhampton Wanderers"], ["2000s", "2010s", "2020s"]),
    ("Joao Felix", "Forward", "2018–present", ["SL Benfica", "Atletico Madrid", "Chelsea FC"], ["2010s", "2020s"]),
    ("Diogo Jota", "Forward", "2014–present", ["FC Porto", "Wolverhampton Wanderers", "Liverpool FC"], ["2010s", "2020s"]),
    ("Goncalo Ramos", "Forward", "2019–present", ["SL Benfica", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Simao Sabrosa", "Forward", "1994–2016", ["Sporting CP", "FC Barcelona", "Atletico Madrid", "Besiktas"], ["legend", "1990s", "2000s", "2010s"]),
    ("Ricardo Quaresma", "Forward", "2001–2021", ["Sporting CP", "FC Porto", "Besiktas"], ["2000s", "2010s", "2020s"]),
    ("Maniche", "Midfielder", "1996–2014", ["FC Porto", "Chelsea FC", "Inter Milan"], ["legend", "2000s", "2010s"]),
    ("Tiago Mendes", "Midfielder", "1999–2020", ["SL Benfica", "Chelsea FC", "Atletico Madrid", "Juventus"], ["2000s", "2010s", "2020s"]),
    ("Paulo Futre", "Forward", "1983–1999", ["FC Porto", "Atletico Madrid", "AC Milan"], ["legend", "1980s", "1990s"]),
    ("Fernando Chalana", "Forward", "1976–1991", ["SL Benfica"], ["legend", "1970s", "1980s"]),
    ("Mario Coluna", "Midfielder", "1954–1971", ["SL Benfica"], ["legend", "1960s"]),
    ("Jaime Graca", "Forward", "1968–1983", ["SL Benfica"], ["legend", "1960s", "1970s"]),
    ("Jose Aguas", "Forward", "1950–1963", ["SL Benfica"], ["legend", "1950s", "1960s"]),
    ("Humberto Coelho", "Defender", "1965–1985", ["SL Benfica"], ["legend", "1960s", "1970s", "1980s"]),
    ("Antonio Simoes", "Midfielder", "1960–1979", ["SL Benfica", "ACF Fiorentina"], ["legend", "1960s", "1970s"]),
    ("Joao Pinto", "Forward", "1990–2013", ["FC Porto", "SL Benfica"], ["legend", "1990s", "2000s", "2010s"]),
    ("Jorge Costa", "Defender", "1988–2008", ["FC Porto"], ["legend", "1990s", "2000s"]),
    ("Helder Postiga", "Forward", "1999–2018", ["FC Porto", "Tottenham Hotspur", "Valencia CF"], ["2000s", "2010s"]),
    ("Hugo Almeida", "Forward", "2001–2018", ["FC Porto", "Besiktas"], ["2000s", "2010s"]),
    ("Danny", "Midfielder", "2001–2023", ["Sporting CP", "Zenit Saint Petersburg"], ["2000s", "2010s", "2020s"]),
    ("Renato Sanches", "Midfielder", "2014–present", ["SL Benfica", "Bayern Munich", "Lille OSC"], ["2010s", "2020s"]),
    ("Vitinha", "Midfielder", "2019–present", ["FC Porto", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Joao Palhinha", "Midfielder", "2016–present", ["Sporting CP", "Bayern Munich"], ["2010s", "2020s"]),
    ("Nuno Mendes", "Defender", "2020–present", ["Sporting CP", "Paris Saint-Germain"], ["2020s"]),
    ("William Carvalho", "Midfielder", "2011–present", ["Sporting CP", "FC Porto", "Real Betis"], ["2010s", "2020s"]),
    ("Andre Silva", "Forward", "2015–present", ["FC Porto", "AC Milan", "RB Leipzig"], ["2010s", "2020s"]),
    ("Goncalo Guedes", "Forward", "2014–present", ["SL Benfica", "Valencia CF", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Rafa Silva", "Forward", "2013–present", ["SL Benfica"], ["2010s", "2020s"]),
    ("Jose Fonte", "Defender", "2006–present", ["Sporting CP", "Southampton FC", "Lille OSC"], ["2010s", "2020s"]),
    ("Fabio Coentrao", "Defender", "2005–2019", ["Sporting CP", "Real Madrid"], ["2000s", "2010s"]),
    ("Jose Bosingwa", "Defender", "2003–2013", ["FC Porto", "Chelsea FC"], ["2000s", "2010s"]),
    ("Miguel", "Defender", "2000–2014", ["SL Benfica", "Valencia CF"], ["2000s", "2010s"]),
    ("Nuno Valente", "Defender", "1993–2008", ["FC Porto"], ["legend", "1990s", "2000s"]),
    ("Costinha", "Midfielder", "1991–2008", ["FC Porto"], ["legend", "1990s", "2000s"]),
    ("Jorge Andrade", "Defender", "1995–2009", ["FC Porto", "Juventus"], ["1990s", "2000s"]),
    ("Abel Xavier", "Defender", "1993–2008", ["FC Porto", "Liverpool FC"], ["1990s", "2000s"]),
    ("Fernando Couto", "Defender", "1988–2004", ["FC Porto", "FC Barcelona"], ["legend", "1990s", "2000s"]),
    ("Carlos Secretario", "Defender", "1988–1999", ["Sporting CP", "Real Madrid"], ["legend", "1990s"]),
    ("Anthony Lopes", "Goalkeeper", "2010–present", ["FC Porto", "Olympique Lyon"], ["2010s", "2020s"]),
    ("Beto", "Goalkeeper", "2009–present", ["FC Porto", "Sevilla FC"], ["2010s", "2020s"]),
    ("Ricardo", "Goalkeeper", "1990–2009", ["Sporting CP"], ["legend", "1990s", "2000s"]),
    ("Quim", "Goalkeeper", "1995–2013", ["SL Benfica"], ["1990s", "2000s", "2010s"]),
    ("Andre Gomes", "Midfielder", "2012–present", ["SL Benfica", "Valencia CF", "FC Barcelona", "Everton FC"], ["2010s", "2020s"]),
    ("Joao Mario", "Midfielder", "2011–present", ["Sporting CP", "Inter Milan"], ["2010s", "2020s"]),
    ("Otavio", "Midfielder", "2010–present", ["FC Porto"], ["2010s", "2020s"]),
    ("Sergio Oliveira", "Midfielder", "2011–present", ["FC Porto"], ["2010s", "2020s"]),
    ("Pizzi", "Midfielder", "2007–present", ["SL Benfica"], ["2000s", "2010s", "2020s"]),
    ("Danilo Pereira", "Midfielder", "2012–present", ["FC Porto", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Nelson Oliveira", "Forward", "2010–present", ["SL Benfica", "Nottingham Forest"], ["2010s", "2020s"]),
    ("Silvestre Varela", "Forward", "2006–2020", ["FC Porto", "Sporting CP"], ["2000s", "2010s", "2020s"]),
    ("Domingos", "Forward", "1991–2008", ["SL Benfica"], ["1990s", "2000s"]),
    ("Capucho", "Forward", "1993–2012", ["FC Porto", "Rangers FC"], ["1990s", "2000s", "2010s"]),
    ("Pedro Mendes", "Forward", "1998–2016", ["Sporting CP", "Tottenham Hotspur", "Rangers FC"], ["1990s", "2000s", "2010s"]),
    ("Nelson Semedo", "Defender", "2015–present", ["SL Benfica", "FC Barcelona", "Wolverhampton Wanderers"], ["2010s", "2020s"]),
    ("Antonio Silva", "Defender", "2018–present", ["SL Benfica"], ["2010s", "2020s"]),
    ("Cedric Soares", "Defender", "2008–present", ["Sporting CP", "Southampton FC", "Arsenal FC"], ["2010s", "2020s"]),
    ("Neto", "Defender", "2012–present", ["FC Porto", "Valencia CF"], ["2010s", "2020s"]),
    ("Tiago Djalo", "Defender", "2019–present", ["Lille OSC"], ["2010s", "2020s"]),
    ("Paulo Sousa", "Midfielder", "1985–2002", ["FC Porto", "Juventus", "Inter Milan"], ["legend", "1980s", "1990s", "2000s"]),
    ("Jose Torres", "Forward", "1958–1969", ["SL Benfica"], ["legend", "1950s", "1960s"]),
    ("Bento", "Goalkeeper", "1968–1985", ["SL Benfica"], ["legend", "1970s", "1980s"]),
    ("Derlei", "Forward", "1998–2010", ["FC Porto"], ["2000s"]),
    ("Eliseu", "Defender", "2004–2020", ["SL Benfica"], ["2000s", "2010s", "2020s"]),
    ("Pedro Goncalves", "Forward", "2015–present", ["Sporting CP"], ["2010s", "2020s"]),
    ("Matheus Nunes", "Midfielder", "2018–present", ["Sporting CP", "Wolverhampton Wanderers", "Manchester City"], ["2010s", "2020s"]),
    ("Goncalo Inacio", "Defender", "2020–present", ["Sporting CP"], ["2020s"]),
    ("Rafael Leao", "Forward", "2017–present", ["Sporting CP", "AC Milan"], ["2010s", "2020s"]),
    ("Jessica Silva", "Forward", "2006–present", ["SL Benfica", "Paris Saint-Germain"], ["legend", "2000s", "2010s", "2020s"]),
    ("Ana Borges", "Forward", "2003–present", ["SL Benfica"], ["legend", "2000s", "2010s", "2020s"]),
    ("Claudia Neto", "Midfielder", "2003–present", ["SL Benfica"], ["legend", "2000s", "2010s", "2020s"]),
    ("Dolores Silva", "Midfielder", "2007–present", ["Sporting CP", "Atletico Madrid"], ["2000s", "2010s", "2020s"]),
    ("Carole Costa", "Defender", "2005–present", ["SL Benfica"], ["legend", "2000s", "2010s", "2020s"]),
    ("Andreia Jacinto", "Midfielder", "2016–present", ["Sporting CP"], ["2010s", "2020s"]),
    ("Telma Encarnacao", "Forward", "2011–present", ["Sporting CP", "SL Benfica"], ["2010s", "2020s"]),
    ("Sara Carvalho", "Midfielder", "2005–present", ["Sporting CP"], ["2010s", "2020s"]),
    ("Venancio", "Forward", "1960–1973", ["SL Benfica"], ["legend", "1960s", "1970s"]),
    ("Artur Jorge", "Forward", "1964–1978", ["SL Benfica"], ["legend", "1960s", "1970s"]),
    ("Jorge Cadete", "Forward", "1985–2000", ["Sporting CP", "Celtic FC"], ["1980s", "1990s"]),
    ("Vitorino", "Forward", "1968–1982", ["SL Benfica"], ["legend", "1960s", "1970s", "1980s"]),
    ("Rui Barros", "Midfielder", "1984–2000", ["FC Porto", "Juventus", "AS Monaco"], ["1980s", "1990s"]),
    ("Bruno Alves", "Defender", "2000–2021", ["FC Porto", "Rangers FC"], ["2000s", "2010s", "2020s"]),
    ("Ricardo Sa Pinto", "Forward", "1991–2008", ["Sporting CP"], ["1990s", "2000s"]),
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
                "clubs": [*clubs, PT],
                "tags": ["portuguese", *tags],
            }
        )

    out = ROOT / "data/player/portuguese_greatest.json"
    out.write_text(json.dumps(players, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(players)} players to {out}")


if __name__ == "__main__":
    main()
