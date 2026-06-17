"""Generate data/player/usa_greatest.json. Run: python data/player/generate_usa_greatest.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID = {
    c["name"]
    for c in json.loads((ROOT / "data/club/clubs.json").read_text())
    + json.loads((ROOT / "data/club/world_cup_teams.json").read_text())
}
US = "United States"

# name, position, years_active, clubs (excluding United States), extra_tags
ENTRIES = [
    ("Christian Pulisic", "Forward", "2016–present", ["Borussia Dortmund", "Chelsea FC", "AC Milan"], ["2010s", "2020s"]),
    ("Landon Donovan", "Forward", "1999–2016", ["LA Galaxy", "Bayer Leverkusen"], ["legend", "2000s", "2010s"]),
    ("Clint Dempsey", "Forward", "2004–2018", ["Tottenham Hotspur", "Everton FC"], ["legend", "2000s", "2010s"]),
    ("Tim Howard", "Goalkeeper", "1997–2019", ["Manchester United", "Everton FC"], ["legend", "2000s", "2010s"]),
    ("Claudio Reyna", "Midfielder", "1994–2008", ["Manchester City", "Rangers FC"], ["legend", "1990s", "2000s"]),
    ("Weston McKennie", "Midfielder", "2017–present", ["FC Schalke 04", "Juventus"], ["2010s", "2020s"]),
    ("Tyler Adams", "Midfielder", "2016–present", ["RB Leipzig", "Leeds United"], ["2010s", "2020s"]),
    ("Sergino Dest", "Defender", "2018–present", ["Ajax", "FC Barcelona", "AC Milan"], ["2010s", "2020s"]),
    ("Giovanni Reyna", "Midfielder", "2019–present", ["Borussia Dortmund"], ["2010s", "2020s"]),
    ("Brad Friedel", "Goalkeeper", "1994–2015", ["Liverpool FC", "Tottenham Hotspur"], ["2000s", "2010s"]),
    ("Kasey Keller", "Goalkeeper", "1989–2011", ["Leicester City", "Tottenham Hotspur"], ["1990s", "2000s", "2010s"]),
    ("Tony Meola", "Goalkeeper", "1988–2006", [], ["legend", "1990s", "2000s"]),
    ("Cobi Jones", "Midfielder", "1992–2007", ["LA Galaxy"], ["1990s", "2000s"]),
    ("Brian McBride", "Forward", "1996–2010", ["Everton FC", "VfL Wolfsburg"], ["1990s", "2000s"]),
    ("Eric Wynalda", "Forward", "1990–2000", [], ["legend", "1990s"]),
    ("Alexi Lalas", "Defender", "1992–2002", [], ["legend", "1990s", "2000s"]),
    ("John O'Brien", "Midfielder", "1997–2012", ["Ajax"], ["2000s"]),
    ("DaMarcus Beasley", "Midfielder", "1999–2019", ["PSV Eindhoven", "Rangers FC"], ["2000s", "2010s"]),
    ("Carlos Bocanegra", "Defender", "2002–2014", ["AS Saint-Etienne", "Rangers FC"], ["2000s", "2010s"]),
    ("Oguchi Onyewu", "Defender", "2002–2015", ["AC Milan", "Newcastle United"], ["2000s", "2010s"]),
    ("Michael Bradley", "Midfielder", "2004–2023", ["Borussia Monchengladbach", "AS Roma"], ["2000s", "2010s", "2020s"]),
    ("Jozy Altidore", "Forward", "2006–2022", ["Villarreal CF"], ["2000s", "2010s", "2020s"]),
    ("Eddie Pope", "Defender", "1996–2007", [], ["1990s", "2000s"]),
    ("Tab Ramos", "Midfielder", "1988–2002", ["Real Betis"], ["legend", "1990s", "2000s"]),
    ("John Harkes", "Midfielder", "1990–2000", [], ["1990s"]),
    ("Earnie Stewart", "Forward", "1988–2005", [], ["1990s", "2000s"]),
    ("Paul Caligiuri", "Midfielder", "1984–2001", [], ["legend", "1980s", "1990s", "2000s"]),
    ("Eddie Lewis", "Midfielder", "1996–2012", ["Leeds United"], ["1990s", "2000s", "2010s"]),
    ("Jermaine Jones", "Midfielder", "2000–2017", ["Bayer Leverkusen", "FC Schalke 04"], ["2000s", "2010s"]),
    ("Maurice Edu", "Midfielder", "2007–2015", ["Rangers FC"], ["2000s", "2010s"]),
    ("DeAndre Yedlin", "Defender", "2013–present", ["Tottenham Hotspur", "Newcastle United", "Inter Miami CF"], ["2010s", "2020s"]),
    ("John Brooks", "Defender", "2010–present", ["VfL Wolfsburg"], ["2010s", "2020s"]),
    ("Matt Turner", "Goalkeeper", "2013–present", ["Arsenal FC", "Nottingham Forest"], ["2010s", "2020s"]),
    ("Yunus Musah", "Midfielder", "2020–present", ["Valencia CF", "AC Milan"], ["2020s"]),
    ("Brenden Aaronson", "Midfielder", "2019–present", ["FC Red Bull Salzburg", "Leeds United"], ["2010s", "2020s"]),
    ("Antonee Robinson", "Defender", "2017–present", [], ["2010s", "2020s"]),
    ("Chris Richards", "Defender", "2018–present", ["Bayern Munich"], ["2010s", "2020s"]),
    ("Cameron Carter-Vickers", "Defender", "2014–present", ["Tottenham Hotspur", "Celtic FC"], ["2010s", "2020s"]),
    ("Matt Miazga", "Defender", "2013–present", ["Chelsea FC"], ["2010s", "2020s"]),
    ("Josh Sargent", "Forward", "2017–present", ["Werder Bremen"], ["2010s", "2020s"]),
    ("Julian Green", "Forward", "2013–2021", ["Bayern Munich", "VfB Stuttgart"], ["2010s", "2020s"]),
    ("Freddy Adu", "Forward", "2004–2020", ["SL Benfica"], ["2000s", "2010s"]),
    ("Sacha Kljestan", "Midfielder", "2005–2018", ["RSC Anderlecht"], ["2000s", "2010s"]),
    ("Aron Johannsson", "Forward", "2010–2020", ["Werder Bremen"], ["2010s", "2020s"]),
    ("Bobby Convey", "Midfielder", "2000–2013", ["Tottenham Hotspur"], ["2000s", "2010s"]),
    ("Brad Guzan", "Goalkeeper", "2002–present", ["Aston Villa"], ["2000s", "2010s", "2020s"]),
    ("Geoff Cameron", "Defender", "2008–2021", [], ["2000s", "2010s", "2020s"]),
    ("Graham Zusi", "Midfielder", "2009–2023", [], ["2000s", "2010s", "2020s"]),
    ("Nick Rimando", "Goalkeeper", "2000–2018", [], ["2000s", "2010s"]),
    ("Walker Zimmerman", "Defender", "2013–present", [], ["2010s", "2020s"]),
    ("Paul Arriola", "Midfielder", "2013–present", [], ["2010s", "2020s"]),
    ("Herculez Gomez", "Forward", "2002–2018", [], ["2000s", "2010s"]),
    ("Mix Diskerud", "Midfielder", "2010–2017", ["Manchester City"], ["2010s"]),
    ("Stuart Holden", "Midfielder", "2005–2014", [], ["2000s", "2010s"]),
    ("Kyle Beckerman", "Midfielder", "1998–2019", [], ["1990s", "2000s", "2010s"]),
    ("Frankie Hejduk", "Defender", "1996–2011", ["LA Galaxy"], ["1990s", "2000s", "2010s"]),
    ("Ben Olsen", "Midfielder", "1998–2009", [], ["1990s", "2000s"]),
    ("Brian Ching", "Forward", "2001–2013", [], ["2000s", "2010s"]),
    ("Charlie Davies", "Forward", "2006–2016", [], ["2000s", "2010s"]),
    ("Clint Mathis", "Forward", "1998–2010", [], ["1990s", "2000s"]),
    ("Gregg Berhalter", "Defender", "1995–2011", ["LA Galaxy"], ["1990s", "2000s", "2010s"]),
    ("Eddie Johnson", "Forward", "2001–2017", [], ["2000s", "2010s"]),
    ("Ricardo Clark", "Midfielder", "2003–2019", [], ["2000s", "2010s"]),
    ("Thomas Dooley", "Defender", "1984–1999", ["Bayer Leverkusen", "FC Schalke 04"], ["1980s", "1990s"]),
    ("Walter Bahr", "Midfielder", "1951–1965", [], ["legend", "1950s", "1960s"]),
    ("Mia Hamm", "Forward", "1987–2004", [], ["legend", "goat", "1990s", "2000s"]),
    ("Abby Wambach", "Forward", "2001–2015", [], ["legend", "2000s", "2010s"]),
    ("Alex Morgan", "Forward", "2009–present", ["Olympique Lyon", "Tottenham Hotspur"], ["2010s", "2020s"]),
    ("Megan Rapinoe", "Forward", "2006–2023", ["Olympique Lyon"], ["legend", "2000s", "2010s", "2020s"]),
    ("Carli Lloyd", "Midfielder", "2005–2021", ["Manchester City"], ["legend", "2000s", "2010s", "2020s"]),
    ("Hope Solo", "Goalkeeper", "2000–2016", [], ["legend", "2000s", "2010s"]),
    ("Kristine Lilly", "Midfielder", "1987–2010", [], ["legend", "1990s", "2000s", "2010s"]),
    ("Michelle Akers", "Forward", "1985–2000", [], ["legend", "goat", "1980s", "1990s", "2000s"]),
    ("Julie Foudy", "Midfielder", "1987–2004", [], ["legend", "1990s", "2000s"]),
    ("Brandi Chastain", "Defender", "1988–2004", [], ["legend", "1990s", "2000s"]),
    ("Shannon Boxx", "Midfielder", "2000–2015", [], ["2000s", "2010s"]),
    ("Tobin Heath", "Forward", "2009–2023", ["Paris Saint-Germain", "Manchester United"], ["2000s", "2010s", "2020s"]),
    ("Kelley O'Hara", "Defender", "2010–present", [], ["2010s", "2020s"]),
    ("Becky Sauerbrunn", "Defender", "2008–present", [], ["2000s", "2010s", "2020s"]),
    ("Julie Ertz", "Midfielder", "2013–2023", [], ["2010s", "2020s"]),
    ("Rose Lavelle", "Midfielder", "2017–present", ["Manchester City"], ["2010s", "2020s"]),
    ("Lindsey Horan", "Midfielder", "2013–present", ["Paris Saint-Germain", "Olympique Lyon"], ["2010s", "2020s"]),
    ("Christen Press", "Forward", "2013–2022", ["Manchester United"], ["2010s", "2020s"]),
    ("Alyssa Naeher", "Goalkeeper", "2009–present", [], ["2010s", "2020s"]),
    ("Crystal Dunn", "Forward", "2013–present", ["Chelsea FC"], ["2010s", "2020s"]),
    ("Emily Sonnett", "Defender", "2013–present", [], ["2010s", "2020s"]),
    ("Ali Krieger", "Defender", "2008–2023", [], ["2000s", "2010s", "2020s"]),
    ("Heather O'Reilly", "Midfielder", "2002–2016", ["Arsenal FC"], ["2000s", "2010s"]),
    ("Tierna Davidson", "Defender", "2018–present", [], ["2010s", "2020s"]),
    ("Naomi Girma", "Defender", "2020–present", [], ["2020s"]),
    ("Sophia Smith", "Forward", "2020–present", [], ["2020s"]),
    ("Trinity Rodman", "Forward", "2021–present", [], ["2020s"]),
    ("Andi Sullivan", "Midfielder", "2017–present", [], ["2010s", "2020s"]),
    ("Catarina Macario", "Forward", "2017–present", ["Olympique Lyon", "Chelsea FC"], ["2010s", "2020s"]),
    ("April Heinrichs", "Forward", "1986–1991", [], ["legend", "1980s", "1990s"]),
    ("Shannon MacMillan", "Forward", "1993–2006", [], ["1990s", "2000s"]),
    ("Tiffeny Milbrett", "Forward", "1991–2006", [], ["1990s", "2000s"]),
    ("Cindy Parlow", "Forward", "1995–2004", [], ["1990s", "2000s"]),
    ("Kate Markgraf", "Defender", "1997–2010", [], ["1990s", "2000s", "2010s"]),
    ("Tisha Venturini", "Midfielder", "1992–2000", [], ["1990s"]),
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
                "clubs": [*clubs, US],
                "tags": ["american", *tags],
            }
        )

    out = ROOT / "data/player/usa_greatest.json"
    out.write_text(json.dumps(players, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(players)} players to {out}")


if __name__ == "__main__":
    main()
