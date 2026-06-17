"""Generate data/player/italian_greatest.json. Run: python data/player/generate_italian_greatest.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID = {
    c["name"]
    for c in json.loads((ROOT / "data/club/clubs.json").read_text())
    + json.loads((ROOT / "data/club/world_cup_teams.json").read_text())
}
IT = "Italy"

# name, position, years_active, clubs (excluding Italy), extra_tags
ENTRIES = [
    ("Giuseppe Meazza", "Forward", "1929–1940", ["Inter Milan"], ["legend", "goat", "1930s"]),
    ("Silvio Piola", "Forward", "1929–1954", [], ["legend", "1930s", "1940s"]),
    ("Giacinto Facchetti", "Defender", "1960–1978", ["Inter Milan"], ["legend", "1960s", "1970s"]),
    ("Gianni Rivera", "Midfielder", "1959–1979", ["AC Milan"], ["legend", "1960s", "1970s"]),
    ("Sandro Mazzola", "Forward", "1960–1977", ["Inter Milan"], ["legend", "1960s", "1970s"]),
    ("Gaetano Scirea", "Defender", "1972–1988", ["Juventus"], ["legend", "1970s", "1980s"]),
    ("Dino Zoff", "Goalkeeper", "1961–1983", ["Juventus"], ["legend", "1970s", "1980s"]),
    ("Franco Baresi", "Defender", "1977–1997", ["AC Milan"], ["legend", "goat", "1980s", "1990s"]),
    ("Paolo Maldini", "Defender", "1984–2009", ["AC Milan"], ["legend", "goat", "1980s", "1990s", "2000s"]),
    ("Giuseppe Bergomi", "Defender", "1979–1999", ["Inter Milan"], ["legend", "1980s", "1990s"]),
    ("Roberto Baggio", "Forward", "1982–2004", ["ACF Fiorentina", "Juventus", "AC Milan", "Inter Milan", "AS Roma"], ["legend", "goat", "1980s", "1990s", "2000s"]),
    ("Paolo Rossi", "Forward", "1973–1987", ["Juventus", "Inter Milan"], ["legend", "1970s", "1980s"]),
    ("Marco Tardelli", "Midfielder", "1969–1988", ["Juventus", "Inter Milan"], ["legend", "1970s", "1980s"]),
    ("Antonio Cabrini", "Defender", "1973–1991", ["Juventus"], ["legend", "1970s", "1980s"]),
    ("Claudio Gentile", "Defender", "1972–1989", ["Juventus", "Inter Milan"], ["legend", "1970s", "1980s"]),
    ("Bruno Conti", "Midfielder", "1973–1998", ["AS Roma"], ["legend", "1970s", "1980s", "1990s"]),
    ("Giancarlo Antognoni", "Midfielder", "1972–1987", ["ACF Fiorentina"], ["legend", "1970s", "1980s"]),
    ("Francesco Totti", "Forward", "1992–2017", ["AS Roma"], ["legend", "1990s", "2000s", "2010s"]),
    ("Andrea Pirlo", "Midfielder", "1995–2017", ["AC Milan", "Juventus"], ["legend", "2000s", "2010s"]),
    ("Alessandro Del Piero", "Forward", "1991–2014", ["Juventus"], ["legend", "1990s", "2000s", "2010s"]),
    ("Filippo Inzaghi", "Forward", "1991–2012", ["Juventus", "AC Milan"], ["legend", "1990s", "2000s", "2010s"]),
    ("Gianluigi Buffon", "Goalkeeper", "1995–2023", ["Juventus", "Paris Saint-Germain"], ["legend", "goat", "1990s", "2000s", "2010s", "2020s"]),
    ("Fabio Cannavaro", "Defender", "1992–2011", ["SSC Napoli", "Inter Milan", "Juventus", "Real Madrid"], ["legend", "1990s", "2000s", "2010s"]),
    ("Roberto Donadoni", "Midfielder", "1982–2000", ["AC Milan", "AS Roma"], ["legend", "1980s", "1990s"]),
    ("Gianluca Vialli", "Forward", "1980–1999", ["Juventus", "Chelsea FC"], ["legend", "1980s", "1990s"]),
    ("Roberto Mancini", "Forward", "1981–2001", ["AC Milan", "Inter Milan", "SS Lazio"], ["legend", "1980s", "1990s"]),
    ("Christian Vieri", "Forward", "1991–2009", ["Juventus", "Atletico Madrid", "Inter Milan", "SS Lazio"], ["legend", "1990s", "2000s"]),
    ("Gianluca Zambrotta", "Defender", "1994–2012", ["Juventus", "FC Barcelona", "AC Milan"], ["legend", "1990s", "2000s", "2010s"]),
    ("Alessandro Nesta", "Defender", "1993–2012", ["SS Lazio", "AC Milan", "Chelsea FC"], ["legend", "1990s", "2000s", "2010s"]),
    ("Luca Toni", "Forward", "1996–2016", ["ACF Fiorentina", "Bayern Munich"], ["legend", "2000s", "2010s"]),
    ("Gianfranco Zola", "Forward", "1983–2005", ["SSC Napoli", "Chelsea FC"], ["legend", "1980s", "1990s", "2000s"]),
    ("Marco Materazzi", "Defender", "1990–2011", ["Inter Milan", "Everton FC"], ["legend", "1990s", "2000s", "2010s"]),
    ("Gennaro Gattuso", "Midfielder", "1995–2013", ["AC Milan"], ["legend", "1990s", "2000s", "2010s"]),
    ("Francesco Toldo", "Goalkeeper", "1991–2010", ["Inter Milan"], ["1990s", "2000s", "2010s"]),
    ("Walter Zenga", "Goalkeeper", "1980–2000", ["Inter Milan"], ["1980s", "1990s"]),
    ("Giuseppe Signori", "Forward", "1986–2005", ["SS Lazio"], ["1990s", "2000s"]),
    ("Antonio Cassano", "Forward", "1999–2017", ["AS Roma", "Real Madrid", "AC Milan"], ["2000s", "2010s"]),
    ("Alberto Gilardino", "Forward", "1999–2017", ["AC Milan", "ACF Fiorentina", "Juventus"], ["2000s", "2010s"]),
    ("Vincenzo Montella", "Forward", "1990–2010", ["AC Milan", "AS Roma", "ACF Fiorentina"], ["1990s", "2000s", "2010s"]),
    ("Salvatore Schillaci", "Forward", "1982–1999", ["Juventus", "Inter Milan"], ["legend", "1980s", "1990s"]),
    ("Daniele De Rossi", "Midfielder", "2001–2019", ["AS Roma"], ["2000s", "2010s"]),
    ("Claudio Marchisio", "Midfielder", "2005–2018", ["Juventus"], ["2000s", "2010s"]),
    ("Giorgio Chiellini", "Defender", "2000–2022", ["Juventus"], ["legend", "2000s", "2010s", "2020s"]),
    ("Leonardo Bonucci", "Defender", "2006–2023", ["Inter Milan", "Juventus", "AC Milan"], ["2000s", "2010s", "2020s"]),
    ("Andrea Barzagli", "Defender", "1998–2019", ["Juventus"], ["2000s", "2010s"]),
    ("Massimo Ambrosini", "Midfielder", "1995–2014", ["AC Milan"], ["1990s", "2000s", "2010s"]),
    ("Pietro Vierchowod", "Defender", "1972–1999", ["Juventus", "AS Roma"], ["1970s", "1980s", "1990s"]),
    ("Riccardo Boniperti", "Forward", "1946–1961", ["Juventus"], ["legend", "1940s", "1950s"]),
    ("Omar Sivori", "Forward", "1954–1969", ["Juventus"], ["legend", "1950s", "1960s"]),
    ("John Charles", "Forward", "1957–1970", ["Juventus"], ["legend", "1950s", "1960s"]),
    ("Demetrio Albertini", "Midfielder", "1988–2005", ["AC Milan", "Atletico Madrid"], ["1990s", "2000s"]),
    ("Gianluigi Lentini", "Forward", "1986–2008", ["AC Milan", "Atletico Madrid"], ["1990s"]),
    ("Franco Causio", "Midfielder", "1968–1983", ["Juventus", "Inter Milan"], ["legend", "1960s", "1970s", "1980s"]),
    ("Simone Inzaghi", "Forward", "1998–2010", ["Juventus", "SS Lazio"], ["1990s", "2000s"]),
    ("Alessandro Costacurta", "Defender", "1986–2007", ["AC Milan"], ["legend", "1980s", "1990s", "2000s"]),
    ("Christian Panucci", "Defender", "1987–2010", ["AC Milan", "Real Madrid", "AS Roma", "Chelsea FC"], ["1990s", "2000s"]),
    ("Angelo Di Livio", "Midfielder", "1985–2005", ["Juventus", "AS Roma"], ["1990s", "2000s"]),
    ("Fabio Grosso", "Defender", "1998–2015", ["Inter Milan", "Juventus"], ["2000s", "2010s"]),
    ("Enrico Chiesa", "Forward", "1988–2010", ["ACF Fiorentina", "Juventus"], ["1990s", "2000s"]),
    ("Antonio Conte", "Midfielder", "1985–2004", ["Juventus"], ["1990s", "2000s"]),
    ("Alessandro Florenzi", "Defender", "2011–present", ["AS Roma", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Gianluigi Donnarumma", "Goalkeeper", "2015–present", ["AC Milan", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Federico Chiesa", "Forward", "2016–present", ["ACF Fiorentina", "Juventus"], ["2010s", "2020s"]),
    ("Nicolo Barella", "Midfielder", "2015–present", ["Atalanta BC", "Inter Milan"], ["2010s", "2020s"]),
    ("Sandro Tonali", "Midfielder", "2017–present", ["AC Milan", "Inter Milan", "Newcastle United"], ["2010s", "2020s"]),
    ("Marco Verratti", "Midfielder", "2008–present", ["Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Jorginho", "Midfielder", "2010–present", ["SSC Napoli", "Chelsea FC", "Arsenal FC"], ["2010s", "2020s"]),
    ("Ciro Immobile", "Forward", "2009–present", ["Juventus", "Borussia Dortmund", "Sevilla FC", "SS Lazio"], ["2010s", "2020s"]),
    ("Lorenzo Insigne", "Forward", "2010–2022", ["SSC Napoli"], ["2010s", "2020s"]),
    ("Mario Balotelli", "Forward", "2006–2021", ["Inter Milan", "Manchester City", "Liverpool FC", "AC Milan"], ["2000s", "2010s", "2020s"]),
    ("Moise Kean", "Forward", "2016–present", ["Juventus", "Everton FC", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Giacomo Raspadori", "Forward", "2018–present", ["SSC Napoli"], ["2010s", "2020s"]),
    ("Manuel Locatelli", "Midfielder", "2016–present", ["AC Milan", "Juventus"], ["2010s", "2020s"]),
    ("Federico Bernardeschi", "Forward", "2014–present", ["ACF Fiorentina", "Juventus", "LA Galaxy"], ["2010s", "2020s"]),
    ("Alessio Romagnoli", "Defender", "2012–present", ["AC Milan", "SS Lazio"], ["2010s", "2020s"]),
    ("Emerson Palmieri", "Defender", "2011–present", ["AS Roma", "Chelsea FC", "West Ham United"], ["2010s", "2020s"]),
    ("Leonardo Spinazzola", "Defender", "2012–present", ["Atalanta BC", "AS Roma"], ["2010s", "2020s"]),
    ("Gianluca Mancini", "Defender", "2015–present", ["Atalanta BC", "AS Roma"], ["2010s", "2020s"]),
    ("Bryan Cristante", "Midfielder", "2013–present", ["Atalanta BC", "AS Roma"], ["2010s", "2020s"]),
    ("Patrick Cutrone", "Forward", "2017–present", ["AC Milan", "Wolverhampton Wanderers"], ["2010s", "2020s"]),
    ("Fabio Quagliarella", "Forward", "1999–2023", ["Juventus", "SSC Napoli", "AS Roma"], ["2000s", "2010s", "2020s"]),
    ("Matteo Politano", "Forward", "2013–present", ["SSC Napoli", "Inter Milan"], ["2010s", "2020s"]),
    ("Lorenzo Pellegrini", "Midfielder", "2014–present", ["AS Roma"], ["2010s", "2020s"]),
    ("Davide Zappacosta", "Defender", "2013–present", ["Atalanta BC", "Chelsea FC", "AS Roma"], ["2010s", "2020s"]),
    ("Federico Gatti", "Defender", "2018–present", ["Juventus"], ["2010s", "2020s"]),
    ("Nicolo Zaniolo", "Midfielder", "2016–present", ["Inter Milan", "AS Roma"], ["2010s", "2020s"]),
    ("Gianluca Scamacca", "Forward", "2016–present", ["Atalanta BC", "West Ham United"], ["2010s", "2020s"]),
    ("Matteo Darmian", "Defender", "2006–present", ["AC Milan", "Manchester United", "Inter Milan"], ["2000s", "2010s", "2020s"]),
    ("Francesco Acerbi", "Defender", "2007–present", ["SS Lazio", "Inter Milan"], ["2010s", "2020s"]),
    ("Alessandro Bastoni", "Defender", "2016–present", ["Atalanta BC", "Inter Milan"], ["2010s", "2020s"]),
    ("Barbara Bonansea", "Forward", "2000–present", ["Juventus"], ["legend", "2000s", "2010s", "2020s"]),
    ("Cristiana Girelli", "Forward", "2003–present", ["Juventus"], ["legend", "2000s", "2010s", "2020s"]),
    ("Sara Gama", "Defender", "2006–present", ["Juventus"], ["legend", "2000s", "2010s", "2020s"]),
    ("Laura Giuliani", "Goalkeeper", "2008–present", ["Atletico Madrid"], ["2010s", "2020s"]),
    ("Elisa Bartoli", "Defender", "2008–present", ["Juventus"], ["2010s", "2020s"]),
    ("Martina Rosucci", "Midfielder", "2008–present", ["Juventus"], ["2010s", "2020s"]),
    ("Valentina Bergamaschi", "Forward", "2004–present", ["AC Milan"], ["2000s", "2010s", "2020s"]),
    ("Daniela Sabatino", "Forward", "2001–present", ["AS Roma"], ["2000s", "2010s", "2020s"]),
    ("Alice Bergamino", "Defender", "2010–present", ["Juventus"], ["2010s", "2020s"]),
    ("Benedetta Glionna", "Defender", "2016–present", ["AS Roma"], ["2010s", "2020s"]),
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
                "clubs": [*clubs, IT],
                "tags": ["italian", *tags],
            }
        )

    out = ROOT / "data/player/italian_greatest.json"
    out.write_text(json.dumps(players, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(players)} players to {out}")


if __name__ == "__main__":
    main()
