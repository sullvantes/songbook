"""Generate data/player/german_greatest.json. Run: python data/player/generate_german_greatest.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID = {
    c["name"]
    for c in json.loads((ROOT / "data/club/clubs.json").read_text())
    + json.loads((ROOT / "data/club/world_cup_teams.json").read_text())
}
DE = "Germany"

# name, position, years_active, clubs (excluding Germany), extra_tags
ENTRIES = [
    ("Franz Beckenbauer", "Defender", "1964–1983", ["Bayern Munich", "Hamburger SV"], ["legend", "goat", "1960s", "1970s"]),
    ("Gerd Muller", "Forward", "1964–1981", ["Bayern Munich"], ["legend", "goat", "1960s", "1970s"]),
    ("Lothar Matthaus", "Midfielder", "1979–2000", ["Borussia Monchengladbach", "Bayern Munich", "Inter Milan"], ["legend", "goat", "1980s", "1990s"]),
    ("Fritz Walter", "Forward", "1940–1959", [], ["legend", "goat", "1940s", "1950s"]),
    ("Uwe Seeler", "Forward", "1953–1978", ["Hamburger SV"], ["legend", "goat", "1950s", "1960s", "1970s"]),
    ("Sepp Maier", "Goalkeeper", "1962–1979", ["Bayern Munich"], ["legend", "1960s", "1970s"]),
    ("Paul Breitner", "Midfielder", "1970–1983", ["Bayern Munich", "Real Madrid"], ["legend", "1970s", "1980s"]),
    ("Karl-Heinz Rummenigge", "Forward", "1974–1989", ["Borussia Monchengladbach", "Inter Milan"], ["legend", "goat", "1970s", "1980s"]),
    ("Gunter Netzer", "Midfielder", "1965–1975", ["Borussia Monchengladbach", "Real Madrid"], ["legend", "1960s", "1970s"]),
    ("Berti Vogts", "Defender", "1965–1979", ["Borussia Monchengladbach"], ["legend", "1960s", "1970s"]),
    ("Wolfgang Overath", "Midfielder", "1963–1977", [], ["legend", "1960s", "1970s"]),
    ("Pierre Littbarski", "Midfielder", "1972–1990", [], ["legend", "1970s", "1980s"]),
    ("Andreas Brehme", "Defender", "1980–1998", ["Bayern Munich", "Inter Milan", "VfB Stuttgart"], ["legend", "1980s", "1990s"]),
    ("Jurgen Klinsmann", "Forward", "1982–1998", ["VfB Stuttgart", "Inter Milan", "Tottenham Hotspur", "Bayern Munich"], ["legend", "goat", "1980s", "1990s"]),
    ("Rudi Voller", "Forward", "1976–1996", ["Werder Bremen", "AS Roma", "Bayer Leverkusen", "Olympique Marseille"], ["legend", "1980s", "1990s"]),
    ("Andreas Moller", "Midfielder", "1985–2008", ["Borussia Dortmund", "Juventus", "Borussia Monchengladbach"], ["legend", "1980s", "1990s", "2000s"]),
    ("Jurgen Kohler", "Defender", "1983–2002", ["Borussia Dortmund", "Juventus", "Bayer Leverkusen"], ["legend", "1980s", "1990s", "2000s"]),
    ("Matthias Sammer", "Midfielder", "1990–1998", ["Borussia Dortmund", "Inter Milan"], ["legend", "1990s"]),
    ("Oliver Bierhoff", "Forward", "1987–2003", ["Eintracht Frankfurt", "AC Milan", "AS Roma"], ["legend", "1990s", "2000s"]),
    ("Mehmet Scholl", "Midfielder", "1987–2007", ["Bayern Munich"], ["legend", "1990s", "2000s"]),
    ("Michael Ballack", "Midfielder", "1995–2012", ["FC Schalke 04", "Bayer Leverkusen", "Bayern Munich", "Chelsea FC"], ["legend", "goat", "1990s", "2000s", "2010s"]),
    ("Oliver Kahn", "Goalkeeper", "1987–2008", ["Bayern Munich"], ["legend", "goat", "1990s", "2000s"]),
    ("Jens Lehmann", "Goalkeeper", "1988–2011", ["Borussia Dortmund", "Arsenal FC"], ["legend", "1990s", "2000s", "2010s"]),
    ("Philipp Lahm", "Defender", "2002–2017", ["Bayern Munich", "VfB Stuttgart"], ["legend", "goat", "2000s", "2010s"]),
    ("Bastian Schweinsteiger", "Midfielder", "2002–2019", ["Bayern Munich", "Manchester United"], ["legend", "goat", "2000s", "2010s"]),
    ("Manuel Neuer", "Goalkeeper", "2004–present", ["FC Schalke 04", "Bayern Munich"], ["legend", "goat", "2000s", "2010s", "2020s"]),
    ("Toni Kroos", "Midfielder", "2007–2024", ["Bayern Munich", "Bayer Leverkusen", "Real Madrid"], ["legend", "goat", "2000s", "2010s", "2020s"]),
    ("Mesut Ozil", "Midfielder", "2006–2023", ["Werder Bremen", "Real Madrid", "Arsenal FC"], ["legend", "2000s", "2010s", "2020s"]),
    ("Miroslav Klose", "Forward", "1998–2016", ["FC Schalke 04", "Werder Bremen", "Bayern Munich", "SS Lazio"], ["legend", "goat", "1990s", "2000s", "2010s"]),
    ("Thomas Muller", "Forward", "2008–present", ["Bayern Munich"], ["legend", "2000s", "2010s", "2020s"]),
    ("Mario Gotze", "Midfielder", "2009–2020", ["Borussia Dortmund", "Bayern Munich", "Eintracht Frankfurt"], ["legend", "2000s", "2010s"]),
    ("Marco Reus", "Forward", "2009–2024", ["Borussia Dortmund"], ["legend", "2000s", "2010s", "2020s"]),
    ("Kai Havertz", "Forward", "2015–present", ["Bayer Leverkusen", "Chelsea FC", "Arsenal FC"], ["2010s", "2020s"]),
    ("Jamal Musiala", "Midfielder", "2019–present", ["Bayern Munich"], ["2010s", "2020s"]),
    ("Joshua Kimmich", "Midfielder", "2013–present", ["RB Leipzig", "Bayern Munich"], ["2010s", "2020s"]),
    ("Leon Goretzka", "Midfielder", "2013–present", ["VfL Wolfsburg", "FC Schalke 04", "Bayern Munich"], ["2010s", "2020s"]),
    ("Ilkay Gundogan", "Midfielder", "2009–present", ["Borussia Dortmund", "Manchester City", "FC Barcelona"], ["2010s", "2020s"]),
    ("Leroy Sane", "Forward", "2014–present", ["FC Schalke 04", "Manchester City", "Bayern Munich"], ["2010s", "2020s"]),
    ("Serge Gnabry", "Forward", "2011–present", ["Arsenal FC", "Werder Bremen", "Bayern Munich"], ["2010s", "2020s"]),
    ("Florian Wirtz", "Midfielder", "2020–present", ["Bayer Leverkusen"], ["2020s"]),
    ("Antonio Rudiger", "Defender", "2011–present", ["VfB Stuttgart", "AS Roma", "Chelsea FC", "Real Madrid"], ["2010s", "2020s"]),
    ("Mats Hummels", "Defender", "2006–present", ["Bayern Munich", "Borussia Dortmund"], ["2000s", "2010s", "2020s"]),
    ("Jerome Boateng", "Defender", "2006–2023", ["Hamburger SV", "Manchester City", "Bayern Munich", "Olympique Lyon"], ["2000s", "2010s", "2020s"]),
    ("Sami Khedira", "Midfielder", "2004–2021", ["VfB Stuttgart", "Real Madrid", "Juventus"], ["2000s", "2010s", "2020s"]),
    ("Per Mertesacker", "Defender", "2003–2018", ["Werder Bremen", "Arsenal FC"], ["2000s", "2010s"]),
    ("Lukas Podolski", "Forward", "2003–2021", ["Bayern Munich", "Arsenal FC", "Galatasaray"], ["2000s", "2010s", "2020s"]),
    ("Julian Draxler", "Midfielder", "2011–2024", ["FC Schalke 04", "VfL Wolfsburg", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Andre Schurrle", "Forward", "2009–2020", ["Bayer Leverkusen", "Chelsea FC", "Borussia Dortmund", "VfL Wolfsburg"], ["2000s", "2010s", "2020s"]),
    ("Mario Gomez", "Forward", "2003–2020", ["VfB Stuttgart", "Bayern Munich", "AC Milan", "VfL Wolfsburg"], ["2000s", "2010s", "2020s"]),
    ("Stefan Effenberg", "Midfielder", "1987–2002", ["Borussia Monchengladbach", "Bayern Munich", "ACF Fiorentina"], ["legend", "1990s", "2000s"]),
    ("Christian Ziege", "Defender", "1990–2006", ["Bayern Munich", "AC Milan", "Tottenham Hotspur", "Borussia Monchengladbach"], ["1990s", "2000s"]),
    ("Markus Babbel", "Defender", "1988–2007", ["Bayern Munich", "Liverpool FC", "VfB Stuttgart"], ["1990s", "2000s"]),
    ("Bodo Illgner", "Goalkeeper", "1983–1999", ["Borussia Monchengladbach", "Real Madrid"], ["1980s", "1990s"]),
    ("Dietmar Hamann", "Midfielder", "1993–2011", ["Bayern Munich", "Newcastle United", "Manchester City", "Liverpool FC"], ["1990s", "2000s", "2010s"]),
    ("Christoph Kramer", "Midfielder", "2011–present", ["Borussia Monchengladbach", "Bayer Leverkusen", "Borussia Dortmund"], ["2010s", "2020s"]),
    ("Timo Werner", "Forward", "2013–present", ["VfB Stuttgart", "RB Leipzig", "Chelsea FC"], ["2010s", "2020s"]),
    ("Niklas Sule", "Defender", "2013–present", ["Bayern Munich", "Borussia Dortmund"], ["2010s", "2020s"]),
    ("Bernd Leno", "Goalkeeper", "2009–present", ["VfB Stuttgart", "Bayer Leverkusen", "Arsenal FC"], ["2010s", "2020s"]),
    ("Marc-Andre ter Stegen", "Goalkeeper", "2009–present", ["Borussia Monchengladbach", "FC Barcelona"], ["2010s", "2020s"]),
    ("Kevin Trapp", "Goalkeeper", "2008–present", ["Eintracht Frankfurt", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Emre Can", "Midfielder", "2011–present", ["Bayer Leverkusen", "Liverpool FC", "Juventus", "Borussia Dortmund"], ["2010s", "2020s"]),
    ("Julian Brandt", "Midfielder", "2012–present", ["Bayer Leverkusen", "Borussia Dortmund"], ["2010s", "2020s"]),
    ("Robin Gosens", "Defender", "2014–present", ["Atalanta BC", "Inter Milan"], ["2010s", "2020s"]),
    ("Jonathan Tah", "Defender", "2013–present", ["Bayer Leverkusen", "Bayern Munich"], ["2010s", "2020s"]),
    ("Karim Bellarabi", "Forward", "2011–2023", ["Bayer Leverkusen"], ["2010s", "2020s"]),
    ("Julian Weigl", "Midfielder", "2014–2023", ["Borussia Dortmund", "SL Benfica"], ["2010s", "2020s"]),
    ("Max Kruse", "Forward", "2006–2024", ["Werder Bremen", "VfL Wolfsburg"], ["2000s", "2010s", "2020s"]),
    ("Stefan Kiessling", "Forward", "2003–2018", ["Bayer Leverkusen"], ["2000s", "2010s"]),
    ("Kevin-Prince Boateng", "Midfielder", "2004–2023", ["Tottenham Hotspur", "AC Milan", "Eintracht Frankfurt"], ["2000s", "2010s", "2020s"]),
    ("Sandro Wagner", "Forward", "2006–2020", ["Werder Bremen", "Bayern Munich"], ["2000s", "2010s", "2020s"]),
    ("Niclas Fullkrug", "Forward", "2013–present", ["Werder Bremen", "Borussia Dortmund"], ["2010s", "2020s"]),
    ("Thomas Hassler", "Midfielder", "1984–2000", ["AS Roma"], ["1980s", "1990s"]),
    ("Horst Hrubesch", "Forward", "1972–1988", [], ["legend", "1970s", "1980s"]),
    ("Klaus Fischer", "Forward", "1968–1988", [], ["legend", "1960s", "1970s", "1980s"]),
    ("Karl-Heinz Foerster", "Defender", "1976–1991", [], ["legend", "1970s", "1980s"]),
    ("Helmut Rahn", "Forward", "1946–1965", [], ["legend", "1940s", "1950s", "1960s"]),
    ("Max Morlock", "Forward", "1948–1964", [], ["legend", "1940s", "1950s", "1960s"]),
    ("Bernd Schuster", "Midfielder", "1978–1990", ["Real Madrid", "FC Barcelona", "Atletico Madrid"], ["legend", "1970s", "1980s"]),
    ("Thomas Helmer", "Defender", "1986–2000", ["Bayern Munich"], ["1990s", "2000s"]),
    ("Carsten Jancker", "Forward", "1993–2009", ["Bayern Munich", "AS Roma"], ["1990s", "2000s"]),
    ("Fredi Bobic", "Forward", "1988–2005", ["VfB Stuttgart", "Werder Bremen", "Eintracht Frankfurt"], ["1980s", "1990s", "2000s"]),
    ("Gerald Asamoah", "Forward", "1997–2014", ["FC Schalke 04"], ["1990s", "2000s", "2010s"]),
    ("Christoph Metzelder", "Defender", "1996–2013", ["Borussia Dortmund", "Real Madrid"], ["1990s", "2000s", "2010s"]),
    ("Marcel Schmelzer", "Defender", "2005–2020", ["Borussia Dortmund"], ["2000s", "2010s", "2020s"]),
    ("Neven Subotic", "Defender", "2006–2022", ["Borussia Dortmund", "AS Saint-Etienne"], ["2000s", "2010s", "2020s"]),
    ("Shkodran Mustafi", "Defender", "2009–2023", ["Everton FC", "Valencia CF", "Arsenal FC"], ["2010s", "2020s"]),
    ("Timo Hildebrand", "Goalkeeper", "1999–2014", ["VfB Stuttgart", "Valencia CF"], ["1990s", "2000s", "2010s"]),
    ("Rene Adler", "Goalkeeper", "2002–2019", ["Hamburger SV", "VfB Stuttgart"], ["2000s", "2010s"]),
    ("Cacau", "Forward", "1999–2015", ["VfB Stuttgart", "Werder Bremen"], ["1990s", "2000s", "2010s"]),
    ("Hans-Georg Schwarzenbeck", "Defender", "1966–1981", ["Bayern Munich"], ["legend", "1960s", "1970s", "1980s"]),
    ("Karl-Heinz Schnellinger", "Defender", "1958–1974", ["AC Milan", "Tottenham Hotspur"], ["legend", "1950s", "1960s", "1970s"]),
    ("Uli Stielike", "Midfielder", "1972–1988", ["Real Madrid"], ["legend", "1970s", "1980s"]),
    ("Bert Trautmann", "Goalkeeper", "1949–1964", ["Manchester City"], ["legend", "1940s", "1950s", "1960s"]),
    ("Birgit Prinz", "Forward", "1995–2011", [], ["legend", "goat", "1990s", "2000s", "2010s"]),
    ("Nadine Angerer", "Goalkeeper", "1995–2015", [], ["legend", "1990s", "2000s", "2010s"]),
    ("Alexandra Popp", "Forward", "2008–present", ["VfL Wolfsburg"], ["legend", "2000s", "2010s", "2020s"]),
    ("Dzsenifer Marozsan", "Midfielder", "2006–present", ["Olympique Lyon"], ["legend", "2000s", "2010s", "2020s"]),
    ("Lena Oberdorf", "Midfielder", "2015–present", ["VfL Wolfsburg"], ["2010s", "2020s"]),
    ("Lea Schuller", "Forward", "2015–present", ["Bayern Munich"], ["2010s", "2020s"]),
    ("Sara Dabritz", "Midfielder", "2012–present", ["Bayern Munich", "Paris Saint-Germain"], ["2010s", "2020s"]),
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
                "clubs": [*clubs, DE],
                "tags": ["german", *tags],
            }
        )

    out = ROOT / "data/player/german_greatest.json"
    out.write_text(json.dumps(players, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(players)} players to {out}")


if __name__ == "__main__":
    main()
