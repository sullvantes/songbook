"""Generate data/player/english_greatest.json. Run: python data/player/generate_english_greatest.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID = {
    c["name"]
    for c in json.loads((ROOT / "data/club/clubs.json").read_text())
    + json.loads((ROOT / "data/club/world_cup_teams.json").read_text())
}
EN = "England"

# name, position, years_active, clubs (excluding England), extra_tags
ENTRIES = [
    ("Bobby Charlton", "Forward", "1956–1974", ["Manchester United"], ["legend", "1950s", "1960s", "1970s"]),
    ("Bobby Moore", "Defender", "1958–1978", ["West Ham United"], ["legend", "1960s", "1970s"]),
    ("Gordon Banks", "Goalkeeper", "1958–1978", ["Leicester City"], ["legend", "1960s", "1970s"]),
    ("Geoff Hurst", "Forward", "1959–1977", ["West Ham United"], ["legend", "1960s", "1970s"]),
    ("Jimmy Greaves", "Forward", "1957–1980", ["Tottenham Hotspur", "AC Milan"], ["legend", "1960s", "1970s"]),
    ("Tom Finney", "Forward", "1946–1960", [], ["legend", "1940s", "1950s"]),
    ("Stanley Matthews", "Forward", "1932–1965", [], ["legend", "goat", "1930s", "1940s", "1950s"]),
    ("Duncan Edwards", "Midfielder", "1953–1958", ["Manchester United"], ["legend", "1950s"]),
    ("Roger Hunt", "Forward", "1958–1972", ["Liverpool FC"], ["legend", "1960s", "1970s"]),
    ("Nobby Stiles", "Midfielder", "1960–1975", ["Manchester United"], ["legend", "1960s", "1970s"]),
    ("Martin Peters", "Midfielder", "1959–1981", ["West Ham United", "Tottenham Hotspur"], ["legend", "1960s", "1970s"]),
    ("Billy Wright", "Defender", "1939–1959", ["Wolverhampton Wanderers"], ["legend", "1940s", "1950s"]),
    ("Nat Lofthouse", "Forward", "1942–1960", [], ["legend", "1940s", "1950s"]),
    ("Colin Bell", "Midfielder", "1963–1979", ["Manchester City"], ["legend", "1960s", "1970s"]),
    ("Francis Lee", "Forward", "1960–1976", ["Manchester City"], ["legend", "1960s", "1970s"]),
    ("Gary Lineker", "Forward", "1978–1994", ["Leicester City", "Everton FC", "FC Barcelona"], ["legend", "1980s", "1990s"]),
    ("Peter Shilton", "Goalkeeper", "1966–1997", ["Nottingham Forest", "Southampton FC"], ["legend", "1970s", "1980s", "1990s"]),
    ("Paul Gascoigne", "Midfielder", "1985–2004", ["Newcastle United", "Tottenham Hotspur", "SS Lazio", "Rangers FC"], ["legend", "1980s", "1990s"]),
    ("Bryan Robson", "Midfielder", "1975–1997", ["Manchester United"], ["legend", "1980s", "1990s"]),
    ("Alan Shearer", "Forward", "1988–2006", ["Southampton FC", "Newcastle United"], ["legend", "1990s", "2000s"]),
    ("David Beckham", "Midfielder", "1992–2013", ["Manchester United", "Real Madrid", "LA Galaxy", "Paris Saint-Germain"], ["legend", "1990s", "2000s", "2010s"]),
    ("Michael Owen", "Forward", "1996–2013", ["Liverpool FC", "Real Madrid", "Newcastle United"], ["legend", "1990s", "2000s", "2010s"]),
    ("Steven Gerrard", "Midfielder", "1998–2016", ["Liverpool FC", "LA Galaxy"], ["legend", "1990s", "2000s", "2010s"]),
    ("Frank Lampard", "Midfielder", "1995–2017", ["Chelsea FC", "Manchester City"], ["legend", "1990s", "2000s", "2010s"]),
    ("Wayne Rooney", "Forward", "2002–2021", ["Everton FC", "Manchester United"], ["legend", "2000s", "2010s", "2020s"]),
    ("Rio Ferdinand", "Defender", "1996–2015", ["West Ham United", "Leeds United", "Manchester United"], ["legend", "1990s", "2000s", "2010s"]),
    ("John Terry", "Defender", "1998–2017", ["Chelsea FC"], ["legend", "1990s", "2000s", "2010s"]),
    ("Ashley Cole", "Defender", "1999–2019", ["Arsenal FC", "Chelsea FC"], ["legend", "1990s", "2000s", "2010s"]),
    ("Sol Campbell", "Defender", "1992–2012", ["Tottenham Hotspur", "Arsenal FC"], ["legend", "1990s", "2000s", "2010s"]),
    ("David Seaman", "Goalkeeper", "1981–2004", ["Arsenal FC", "Manchester City"], ["legend", "1980s", "1990s", "2000s"]),
    ("Teddy Sheringham", "Forward", "1983–2008", ["Nottingham Forest", "Tottenham Hotspur", "Manchester United"], ["legend", "1980s", "1990s", "2000s"]),
    ("Paul Scholes", "Midfielder", "1994–2013", ["Manchester United"], ["legend", "1990s", "2000s", "2010s"]),
    ("Ryan Giggs", "Midfielder", "1991–2014", ["Manchester United"], ["legend", "1990s", "2000s", "2010s"]),
    ("Kevin Keegan", "Forward", "1968–1984", ["Liverpool FC", "Hamburger SV"], ["legend", "1970s", "1980s"]),
    ("Glenn Hoddle", "Midfielder", "1975–1998", ["Tottenham Hotspur"], ["legend", "1970s", "1980s", "1990s"]),
    ("Chris Waddle", "Forward", "1978–1999", ["Newcastle United", "Tottenham Hotspur", "Olympique Marseille"], ["legend", "1980s", "1990s"]),
    ("Viv Anderson", "Defender", "1974–1995", ["Nottingham Forest", "Arsenal FC"], ["legend", "1970s", "1980s", "1990s"]),
    ("Tony Adams", "Defender", "1983–2002", ["Arsenal FC"], ["legend", "1980s", "1990s", "2000s"]),
    ("Stuart Pearce", "Defender", "1978–2002", ["Nottingham Forest", "Manchester City"], ["legend", "1980s", "1990s", "2000s"]),
    ("Trevor Brooking", "Midfielder", "1967–1988", ["West Ham United"], ["legend", "1970s", "1980s"]),
    ("Ray Wilkins", "Midfielder", "1973–1997", ["Chelsea FC", "AC Milan", "Paris Saint-Germain"], ["legend", "1970s", "1980s", "1990s"]),
    ("Ray Clemence", "Goalkeeper", "1965–1988", ["Liverpool FC", "Tottenham Hotspur"], ["legend", "1960s", "1970s", "1980s"]),
    ("Peter Reid", "Midfielder", "1974–1994", ["Everton FC"], ["legend", "1970s", "1980s", "1990s"]),
    ("Jamie Carragher", "Defender", "1996–2013", ["Liverpool FC"], ["legend", "1990s", "2000s", "2010s"]),
    ("Michael Carrick", "Midfielder", "1995–2018", ["West Ham United", "Tottenham Hotspur", "Manchester United"], ["1990s", "2000s", "2010s"]),
    ("Dennis Wise", "Midfielder", "1985–2006", ["Chelsea FC", "Leicester City"], ["1990s", "2000s"]),
    ("Emile Heskey", "Forward", "1995–2013", ["Leicester City", "Liverpool FC"], ["1990s", "2000s", "2010s"]),
    ("Peter Crouch", "Forward", "1998–2019", ["Liverpool FC", "Tottenham Hotspur"], ["2000s", "2010s"]),
    ("David James", "Goalkeeper", "1988–2014", ["Liverpool FC", "Aston Villa"], ["1990s", "2000s", "2010s"]),
    ("Jermain Defoe", "Forward", "1999–2022", ["Tottenham Hotspur", "West Ham United"], ["2000s", "2010s", "2020s"]),
    ("James Milner", "Midfielder", "2002–present", ["Leeds United", "Newcastle United", "Aston Villa", "Manchester City", "Liverpool FC"], ["2000s", "2010s", "2020s"]),
    ("Jordan Henderson", "Midfielder", "2004–2024", ["Liverpool FC", "Ajax"], ["2000s", "2010s", "2020s"]),
    ("Joe Cole", "Midfielder", "1999–2018", ["West Ham United", "Chelsea FC", "Liverpool FC"], ["2000s", "2010s"]),
    ("Dele Alli", "Midfielder", "2013–present", ["Tottenham Hotspur", "Everton FC"], ["2010s", "2020s"]),
    ("Ross Barkley", "Midfielder", "2010–present", ["Everton FC", "Chelsea FC"], ["2010s", "2020s"]),
    ("Kevin Phillips", "Forward", "1992–2014", ["Southampton FC", "Aston Villa"], ["1990s", "2000s", "2010s"]),
    ("Dion Dublin", "Forward", "1988–2008", ["Manchester United", "Aston Villa", "Celtic FC"], ["1990s", "2000s"]),
    ("Theo Walcott", "Forward", "2006–2023", ["Arsenal FC", "Everton FC"], ["2000s", "2010s", "2020s"]),
    ("Leighton Baines", "Defender", "2002–2020", ["Everton FC"], ["2000s", "2010s"]),
    ("Fabian Delph", "Midfielder", "2006–2022", ["Aston Villa", "Manchester City", "Everton FC"], ["2000s", "2010s", "2020s"]),
    ("Gary Cahill", "Defender", "2004–2021", ["Chelsea FC", "Aston Villa"], ["2000s", "2010s", "2020s"]),
    ("Jamie Vardy", "Forward", "2011–present", ["Leicester City"], ["2010s", "2020s"]),
    ("Harry Maguire", "Defender", "2011–present", ["Leicester City", "Manchester United"], ["2010s", "2020s"]),
    ("Dominic Calvert-Lewin", "Forward", "2015–present", ["Everton FC"], ["2010s", "2020s"]),
    ("Harry Kane", "Forward", "2009–present", ["Tottenham Hotspur", "Bayern Munich"], ["legend", "2010s", "2020s"]),
    ("Jude Bellingham", "Midfielder", "2019–present", ["Borussia Dortmund", "Real Madrid"], ["2010s", "2020s"]),
    ("Bukayo Saka", "Forward", "2018–present", ["Arsenal FC"], ["2010s", "2020s"]),
    ("Phil Foden", "Midfielder", "2017–present", ["Manchester City"], ["2010s", "2020s"]),
    ("Raheem Sterling", "Forward", "2012–present", ["Liverpool FC", "Manchester City", "Chelsea FC"], ["2010s", "2020s"]),
    ("Marcus Rashford", "Forward", "2016–present", ["Manchester United"], ["2010s", "2020s"]),
    ("Jack Grealish", "Midfielder", "2013–present", ["Aston Villa", "Manchester City"], ["2010s", "2020s"]),
    ("Jordan Pickford", "Goalkeeper", "2011–present", ["Everton FC"], ["2010s", "2020s"]),
    ("Declan Rice", "Midfielder", "2015–present", ["West Ham United", "Arsenal FC"], ["2010s", "2020s"]),
    ("Trent Alexander-Arnold", "Defender", "2016–present", ["Liverpool FC"], ["2010s", "2020s"]),
    ("Kyle Walker", "Defender", "2008–present", ["Tottenham Hotspur", "Manchester City"], ["2000s", "2010s", "2020s"]),
    ("John Stones", "Defender", "2011–present", ["Everton FC", "Manchester City"], ["2010s", "2020s"]),
    ("Mason Mount", "Midfielder", "2016–present", ["Chelsea FC", "Manchester United"], ["2010s", "2020s"]),
    ("James Maddison", "Midfielder", "2015–present", ["Leicester City", "Tottenham Hotspur"], ["2010s", "2020s"]),
    ("Tammy Abraham", "Forward", "2016–present", ["Chelsea FC", "AS Roma"], ["2010s", "2020s"]),
    ("Kalvin Phillips", "Midfielder", "2014–present", ["Leeds United", "Manchester City"], ["2010s", "2020s"]),
    ("Ellen White", "Forward", "2005–2022", ["Arsenal FC", "Manchester City"], ["legend", "2000s", "2010s", "2020s"]),
    ("Jill Scott", "Midfielder", "2004–2022", ["Manchester City", "Everton FC"], ["legend", "2000s", "2010s", "2020s"]),
    ("Lucy Bronze", "Defender", "2010–present", ["Liverpool FC", "Olympique Lyon", "Manchester City", "FC Barcelona"], ["legend", "2010s", "2020s"]),
    ("Kelly Smith", "Forward", "1996–2017", ["Arsenal FC"], ["legend", "1990s", "2000s", "2010s"]),
    ("Lauren James", "Forward", "2017–present", ["Chelsea FC"], ["2010s", "2020s"]),
    ("Beth Mead", "Forward", "2011–present", ["Arsenal FC"], ["2010s", "2020s"]),
    ("Georgia Stanway", "Midfielder", "2015–present", ["Manchester City", "Bayern Munich"], ["2010s", "2020s"]),
    ("Rachel Daly", "Forward", "2010–present", ["West Ham United", "Aston Villa"], ["2010s", "2020s"]),
    ("Millie Bright", "Defender", "2011–present", ["Chelsea FC"], ["2010s", "2020s"]),
    ("Leah Williamson", "Defender", "2011–present", ["Arsenal FC"], ["2010s", "2020s"]),
    ("Keira Walsh", "Midfielder", "2014–present", ["Manchester City", "FC Barcelona"], ["2010s", "2020s"]),
    ("Steph Houghton", "Defender", "2003–2021", ["Arsenal FC", "Manchester City"], ["legend", "2000s", "2010s", "2020s"]),
    ("Fara Williams", "Midfielder", "2001–2019", ["Liverpool FC", "Everton FC", "Arsenal FC"], ["legend", "2000s", "2010s"]),
    ("Alex Greenwood", "Defender", "2011–present", ["Everton FC", "Olympique Lyon", "Manchester City"], ["2010s", "2020s"]),
    ("Nikita Parris", "Forward", "2012–present", ["Liverpool FC", "Olympique Lyon", "Arsenal FC"], ["2010s", "2020s"]),
    ("Fran Kirby", "Forward", "2012–present", ["Chelsea FC"], ["2010s", "2020s"]),
    ("Chloe Kelly", "Forward", "2015–present", ["Manchester City", "Arsenal FC"], ["2010s", "2020s"]),
    ("Mary Earps", "Goalkeeper", "2013–present", ["Manchester United", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Alessia Russo", "Forward", "2018–present", ["Manchester United", "Arsenal FC"], ["2010s", "2020s"]),
    ("Toni Duggan", "Forward", "2007–2023", ["Everton FC", "Manchester City", "Atletico Madrid"], ["2000s", "2010s", "2020s"]),
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
                "clubs": [*clubs, EN],
                "tags": ["english", *tags],
            }
        )

    out = ROOT / "data/player/english_greatest.json"
    out.write_text(json.dumps(players, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(players)} players to {out}")


if __name__ == "__main__":
    main()
