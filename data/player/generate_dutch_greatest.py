"""Generate data/player/dutch_greatest.json. Run: python data/player/generate_dutch_greatest.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID = {
    c["name"]
    for c in json.loads((ROOT / "data/club/clubs.json").read_text())
    + json.loads((ROOT / "data/club/world_cup_teams.json").read_text())
}
NL = "Netherlands"

# name, position, years_active, clubs (excluding Netherlands), extra_tags
ENTRIES = [
    ("Johan Cruyff", "Forward", "1964–1984", ["Ajax", "FC Barcelona"], ["legend", "goat", "1960s", "1970s"]),
    ("Marco van Basten", "Forward", "1982–1993", ["Ajax", "AC Milan"], ["legend", "goat", "1980s", "1990s"]),
    ("Ruud Gullit", "Midfielder", "1979–1998", ["Feyenoord", "AC Milan", "Chelsea FC"], ["legend", "goat", "1980s", "1990s"]),
    ("Frank Rijkaard", "Midfielder", "1980–1995", ["Ajax", "AC Milan", "Feyenoord"], ["legend", "goat", "1980s", "1990s"]),
    ("Dennis Bergkamp", "Forward", "1986–2006", ["Ajax", "Inter Milan", "Arsenal FC"], ["legend", "goat", "1990s", "2000s"]),
    ("Johan Neeskens", "Midfielder", "1968–1984", ["Ajax", "FC Barcelona"], ["legend", "1970s", "1980s"]),
    ("Rob Rensenbrink", "Forward", "1969–1987", ["RSC Anderlecht"], ["legend", "1970s", "1980s"]),
    ("Ruud Krol", "Defender", "1968–1986", ["Ajax", "SSC Napoli"], ["legend", "1970s", "1980s"]),
    ("Ronald Koeman", "Defender", "1980–1997", ["Ajax", "PSV Eindhoven", "FC Barcelona"], ["legend", "1980s", "1990s"]),
    ("Willem van Hanegem", "Midfielder", "1965–1983", ["Feyenoord"], ["legend", "1970s", "1980s"]),
    ("Piet Keizer", "Forward", "1961–1974", ["Ajax"], ["legend", "1960s", "1970s"]),
    ("Sjaak Swart", "Forward", "1956–1973", ["Ajax"], ["legend", "1960s", "1970s"]),
    ("Arie Haan", "Midfielder", "1969–1983", ["Ajax", "AC Milan"], ["legend", "1970s", "1980s"]),
    ("Wim Suurbier", "Defender", "1964–1982", ["Ajax"], ["legend", "1960s", "1970s", "1980s"]),
    ("Edwin van der Sar", "Goalkeeper", "1990–2011", ["Ajax", "Juventus", "Manchester United"], ["legend", "1990s", "2000s", "2010s"]),
    ("Jaap Stam", "Defender", "1992–2008", ["PSV Eindhoven", "Manchester United", "AC Milan"], ["legend", "1990s", "2000s"]),
    ("Patrick Kluivert", "Forward", "1991–2007", ["Ajax", "AC Milan", "FC Barcelona"], ["legend", "1990s", "2000s"]),
    ("Marc Overmars", "Forward", "1990–2009", ["Ajax", "Arsenal FC", "FC Barcelona"], ["legend", "1990s", "2000s"]),
    ("Edgar Davids", "Midfielder", "1991–2014", ["Ajax", "AC Milan", "Juventus", "Tottenham Hotspur"], ["legend", "1990s", "2000s", "2010s"]),
    ("Clarence Seedorf", "Midfielder", "1992–2014", ["Ajax", "Real Madrid", "Inter Milan", "AC Milan"], ["legend", "1990s", "2000s", "2010s"]),
    ("Giovanni van Bronckhorst", "Defender", "1993–2010", ["Feyenoord", "Arsenal FC", "FC Barcelona"], ["legend", "1990s", "2000s", "2010s"]),
    ("Frank de Boer", "Defender", "1988–2006", ["Ajax", "FC Barcelona", "Galatasaray"], ["legend", "1990s", "2000s"]),
    ("Ronald de Boer", "Midfielder", "1988–2008", ["Ajax", "FC Barcelona", "Rangers FC"], ["legend", "1990s", "2000s"]),
    ("Arjen Robben", "Forward", "2000–2023", ["PSV Eindhoven", "Chelsea FC", "Real Madrid", "Bayern Munich"], ["legend", "2000s", "2010s", "2020s"]),
    ("Wesley Sneijder", "Midfielder", "2002–2020", ["Ajax", "Real Madrid", "Inter Milan", "Galatasaray"], ["legend", "2000s", "2010s", "2020s"]),
    ("Robin van Persie", "Forward", "2001–2019", ["Feyenoord", "Arsenal FC", "Manchester United", "Fenerbahce"], ["legend", "2000s", "2010s"]),
    ("Ruud van Nistelrooy", "Forward", "1993–2012", ["PSV Eindhoven", "Manchester United", "Real Madrid"], ["legend", "1990s", "2000s", "2010s"]),
    ("Rafael van der Vaart", "Midfielder", "2000–2018", ["Ajax", "Real Madrid", "Tottenham Hotspur"], ["2000s", "2010s"]),
    ("Dirk Kuyt", "Forward", "1998–2017", ["Feyenoord", "Liverpool FC", "Fenerbahce"], ["2000s", "2010s"]),
    ("Pierre van Hooijdonk", "Forward", "1989–2007", ["Feyenoord", "Nottingham Forest", "Celtic FC"], ["1990s", "2000s"]),
    ("Jimmy Floyd Hasselbaink", "Forward", "1991–2008", ["Leeds United", "Atletico Madrid", "Chelsea FC"], ["1990s", "2000s"]),
    ("Roy Makaay", "Forward", "1993–2010", ["Bayern Munich"], ["1990s", "2000s", "2010s"]),
    ("Klaas-Jan Huntelaar", "Forward", "2000–2021", ["Ajax", "Real Madrid", "FC Schalke 04"], ["2000s", "2010s", "2020s"]),
    ("Virgil van Dijk", "Defender", "2011–present", ["Celtic FC", "Southampton FC", "Liverpool FC"], ["legend", "2010s", "2020s"]),
    ("Matthijs de Ligt", "Defender", "2016–present", ["Ajax", "Juventus", "Bayern Munich"], ["2010s", "2020s"]),
    ("Frenkie de Jong", "Midfielder", "2016–present", ["Ajax", "FC Barcelona"], ["2010s", "2020s"]),
    ("Memphis Depay", "Forward", "2011–present", ["PSV Eindhoven", "Manchester United", "Olympique Lyon", "FC Barcelona"], ["2010s", "2020s"]),
    ("Georginio Wijnaldum", "Midfielder", "2007–2024", ["PSV Eindhoven", "Newcastle United", "Liverpool FC", "AS Roma"], ["2000s", "2010s", "2020s"]),
    ("Stefan de Vrij", "Defender", "2009–present", ["Feyenoord", "SS Lazio", "Inter Milan"], ["2010s", "2020s"]),
    ("Daley Blind", "Defender", "2008–2023", ["Ajax", "Manchester United"], ["2010s", "2020s"]),
    ("Nathan Ake", "Defender", "2011–present", ["Chelsea FC", "Manchester City"], ["2010s", "2020s"]),
    ("Denzel Dumfries", "Defender", "2014–present", ["PSV Eindhoven", "Inter Milan"], ["2010s", "2020s"]),
    ("Cody Gakpo", "Forward", "2016–present", ["PSV Eindhoven", "Liverpool FC"], ["2010s", "2020s"]),
    ("Steven Bergwijn", "Forward", "2011–present", ["PSV Eindhoven", "Tottenham Hotspur", "Ajax"], ["2010s", "2020s"]),
    ("Luuk de Jong", "Forward", "2007–present", ["PSV Eindhoven", "Sevilla FC", "FC Barcelona"], ["2000s", "2010s", "2020s"]),
    ("Wout Weghorst", "Forward", "2011–present", ["VfL Wolfsburg", "Manchester United"], ["2010s", "2020s"]),
    ("Xavi Simons", "Midfielder", "2019–present", ["PSV Eindhoven", "RB Leipzig"], ["2010s", "2020s"]),
    ("Jeremie Frimpong", "Defender", "2019–present", ["Celtic FC", "Bayer Leverkusen"], ["2010s", "2020s"]),
    ("Ryan Babel", "Forward", "2002–2020", ["Ajax", "Liverpool FC", "Besiktas"], ["2000s", "2010s", "2020s"]),
    ("Phillip Cocu", "Midfielder", "1985–2008", ["PSV Eindhoven", "FC Barcelona"], ["1980s", "1990s", "2000s"]),
    ("Mark van Bommel", "Midfielder", "1992–2012", ["PSV Eindhoven", "FC Barcelona", "Bayern Munich", "AC Milan"], ["1990s", "2000s", "2010s"]),
    ("Nigel de Jong", "Midfielder", "2002–2018", ["Ajax", "Manchester City", "AC Milan"], ["2000s", "2010s"]),
    ("Jan Wouters", "Midfielder", "1980–1994", ["Ajax", "Bayern Munich"], ["1980s", "1990s"]),
    ("Arnold Muhren", "Midfielder", "1973–1990", ["Ajax", "Manchester United"], ["1970s", "1980s"]),
    ("Gerald Vanenburg", "Midfielder", "1980–2000", ["Ajax", "PSV Eindhoven"], ["1980s", "1990s", "2000s"]),
    ("Gregory van der Wiel", "Defender", "2006–2020", ["Ajax", "Paris Saint-Germain"], ["2000s", "2010s", "2020s"]),
    ("John Heitinga", "Defender", "2001–2016", ["Ajax", "Everton FC", "Atletico Madrid"], ["2000s", "2010s"]),
    ("Joris Mathijsen", "Defender", "1999–2017", ["Ajax", "Feyenoord"], ["2000s", "2010s"]),
    ("Khalid Boulahrouz", "Defender", "2001–2012", ["Chelsea FC", "VfB Stuttgart"], ["2000s", "2010s"]),
    ("Wilfred Bouma", "Defender", "1994–2012", ["PSV Eindhoven", "Aston Villa"], ["1990s", "2000s", "2010s"]),
    ("John Metgod", "Defender", "1979–1995", ["Nottingham Forest", "Tottenham Hotspur"], ["1970s", "1980s", "1990s"]),
    ("Andre Ooijer", "Defender", "1996–2011", ["PSV Eindhoven"], ["1990s", "2000s", "2010s"]),
    ("Maarten Stekelenburg", "Goalkeeper", "1999–2020", ["Ajax", "AS Roma", "Everton FC"], ["2000s", "2010s", "2020s"]),
    ("Jasper Cillessen", "Goalkeeper", "2010–2023", ["Ajax", "FC Barcelona", "Valencia CF"], ["2010s", "2020s"]),
    ("Michel Vorm", "Goalkeeper", "2005–2020", ["Tottenham Hotspur"], ["2000s", "2010s", "2020s"]),
    ("Tim Krul", "Goalkeeper", "2004–2023", ["Newcastle United"], ["2000s", "2010s", "2020s"]),
    ("Jan Jongbloed", "Goalkeeper", "1962–1981", ["Feyenoord"], ["legend", "1960s", "1970s", "1980s"]),
    ("Piet Schrijvers", "Goalkeeper", "1971–1985", ["Feyenoord"], ["1970s", "1980s"]),
    ("Wim Kieft", "Forward", "1980–1999", ["PSV Eindhoven", "FC Porto", "Olympique Marseille"], ["1980s", "1990s"]),
    ("Regi Blinker", "Forward", "1987–2006", ["Feyenoord", "Leeds United"], ["1980s", "1990s", "2000s"]),
    ("Bryan Roy", "Forward", "1987–2000", ["Feyenoord", "Nottingham Forest", "AC Milan"], ["1980s", "1990s"]),
    ("Gaston Taument", "Forward", "1989–2003", ["Feyenoord"], ["1980s", "1990s", "2000s"]),
    ("Eljero Elia", "Forward", "2004–2022", ["Feyenoord", "Juventus", "Southampton FC"], ["2000s", "2010s", "2020s"]),
    ("Luciano Narsingh", "Forward", "2008–2022", ["PSV Eindhoven"], ["2000s", "2010s", "2020s"]),
    ("Tonny Vilhena", "Midfielder", "2010–2023", ["Feyenoord"], ["2010s", "2020s"]),
    ("Davy Klaassen", "Midfielder", "2011–2024", ["Ajax", "Everton FC", "Werder Bremen"], ["2010s", "2020s"]),
    ("Jan Vennegoor of Hesselink", "Forward", "1995–2012", ["PSV Eindhoven", "Celtic FC"], ["1990s", "2000s", "2010s"]),
    ("Quincy Promes", "Forward", "2008–2024", ["Ajax", "Sevilla FC"], ["2000s", "2010s", "2020s"]),
    ("Donny van de Beek", "Midfielder", "2015–present", ["Ajax", "Manchester United"], ["2010s", "2020s"]),
    ("Ibrahim Afellay", "Midfielder", "2004–2021", ["PSV Eindhoven", "FC Barcelona", "Olympique Marseille"], ["2000s", "2010s", "2020s"]),
    ("Barry van Galen", "Midfielder", "1989–2006", ["Feyenoord", "Ajax"], ["1980s", "1990s", "2000s"]),
    ("Henk Timmer", "Goalkeeper", "1985–2009", ["Feyenoord"], ["1980s", "1990s", "2000s"]),
    ("Vivianne Miedema", "Forward", "2013–present", ["Bayern Munich", "Manchester City"], ["legend", "2010s", "2020s"]),
    ("Lieke Martens", "Midfielder", "2009–present", ["FC Barcelona"], ["legend", "2010s", "2020s"]),
    ("Sari van Veenendaal", "Goalkeeper", "2006–2023", ["Arsenal FC"], ["legend", "2000s", "2010s", "2020s"]),
    ("Danielle van de Donk", "Midfielder", "2008–present", ["Arsenal FC"], ["2010s", "2020s"]),
    ("Jill Roord", "Midfielder", "2010–present", ["Bayern Munich", "Manchester City"], ["2010s", "2020s"]),
    ("Sherida Spitse", "Midfielder", "2005–present", [], ["legend", "2000s", "2010s", "2020s"]),
    ("Stefanie van der Gragt", "Defender", "2010–2024", ["FC Barcelona"], ["2010s", "2020s"]),
    ("Jackie Groenen", "Midfielder", "2010–present", ["Manchester United", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Lineth Beerensteyn", "Forward", "2013–present", ["Bayern Munich"], ["2010s", "2020s"]),
    ("Anouk Dekker", "Defender", "2005–2020", [], ["2000s", "2010s", "2020s"]),
    ("Renate Jansen", "Forward", "2006–2023", [], ["2000s", "2010s", "2020s"]),
    ("Dominique Janssen", "Defender", "2013–present", ["Arsenal FC", "VfL Wolfsburg"], ["2010s", "2020s"]),
    ("Daphne van Domselaar", "Goalkeeper", "2016–present", ["Ajax"], ["2010s", "2020s"]),
    ("Victoria Pel", "Forward", "2014–present", ["Ajax"], ["2010s", "2020s"]),
    ("Esmee Brugts", "Forward", "2018–present", ["PSV Eindhoven"], ["2010s", "2020s"]),
    ("Tessel Middag", "Midfielder", "2010–2022", ["Ajax"], ["2010s", "2020s"]),
    ("Merel van Dongen", "Defender", "2011–present", ["Ajax"], ["2010s", "2020s"]),
    ("Romee Leuchter", "Forward", "2017–present", ["Ajax"], ["2010s", "2020s"]),
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
                "clubs": [*clubs, NL],
                "tags": ["dutch", *tags],
            }
        )

    out = ROOT / "data/player/dutch_greatest.json"
    out.write_text(json.dumps(players, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(players)} players to {out}")


if __name__ == "__main__":
    main()
