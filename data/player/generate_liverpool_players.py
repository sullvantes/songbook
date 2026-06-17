"""Generate data/player/liverpool_players.json. Run: python data/player/generate_liverpool_players.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID_CLUBS = {
    c["name"]
    for c in json.loads((ROOT / "data/club/clubs.json").read_text())
    + json.loads((ROOT / "data/club/world_cup_teams.json").read_text())
}
LIVERPOOL = "Liverpool FC"

# name, position, years_active, nationality (optional, must be in VALID_CLUBS), extra_tags
PLAYERS = [
    # Goalkeepers
    ("Alisson Becker", "Goalkeeper", "2018–present", "Brazil", ["current", "legend"]),
    ("Caoimhin Kelleher", "Goalkeeper", "2018–2024", "Republic of Ireland", ["academy"]),
    ("Vitezslav Jaros", "Goalkeeper", "2021–present", "Czech Republic", ["current", "academy"]),
    ("Adrian", "Goalkeeper", "2019–2024", "Spain", []),
    ("Simon Mignolet", "Goalkeeper", "2013–2018", "Belgium", []),
    ("Pepe Reina", "Goalkeeper", "2005–2013", "Spain", ["legend"]),
    ("Jerzy Dudek", "Goalkeeper", "2001–2007", "Poland", ["legend", "istanbul"]),
    ("David James", "Goalkeeper", "1992–1999", "England", []),
    ("Bruce Grobbelaar", "Goalkeeper", "1981–1994", "South Africa", ["legend", "1980s"]),
    ("Ray Clemence", "Goalkeeper", "1967–1981", "England", ["legend", "1970s"]),
    ("Loris Karius", "Goalkeeper", "2016–2018", "Germany", []),
    # Defenders
    ("Virgil van Dijk", "Defender", "2018–present", "Netherlands", ["current", "legend", "captain"]),
    ("Ibrahima Konate", "Defender", "2021–present", "France", ["current"]),
    ("Joe Gomez", "Defender", "2015–present", "England", ["current", "academy"]),
    ("Conor Bradley", "Defender", "2020–present", "Northern Ireland", ["current", "academy"]),
    ("Jarell Quansah", "Defender", "2021–present", "England", ["current", "academy"]),
    ("Andrew Robertson", "Defender", "2017–present", "Scotland", ["current", "legend"]),
    ("Trent Alexander-Arnold", "Defender", "2016–2025", "England", ["legend", "academy"]),
    ("Kostas Tsimikas", "Defender", "2020–present", "Greece", ["current"]),
    ("Jeremie Frimpong", "Defender", "2025–present", "Netherlands", ["current"]),
    ("Joel Matip", "Defender", "2016–2024", "Cameroon", ["legend"]),
    ("Dejan Lovren", "Defender", "2014–2021", "Croatia", []),
    ("Martin Skrtel", "Defender", "2008–2016", "Slovakia", []),
    ("Jamie Carragher", "Defender", "1996–2013", "England", ["legend", "academy", "captain"]),
    ("Sami Hyypia", "Defender", "1999–2009", "Finland", ["legend"]),
    ("John Arne Riise", "Defender", "2001–2008", "Norway", []),
    ("Daniel Agger", "Defender", "2006–2014", "Denmark", []),
    ("Steve Finnan", "Defender", "2003–2008", "Republic of Ireland", []),
    ("Mark Lawrenson", "Defender", "1983–1988", "England", ["1980s"]),
    ("Alan Hansen", "Defender", "1977–1991", "Scotland", ["legend", "1980s"]),
    ("Phil Neal", "Defender", "1974–1985", "England", ["legend", "1970s"]),
    ("Ron Yeats", "Defender", "1961–1971", "Scotland", ["legend", "1960s"]),
    ("Tommy Smith", "Defender", "1962–1978", "England", ["legend", "1970s"]),
    ("Emlyn Hughes", "Defender", "1967–1979", "England", ["legend", "1970s"]),
    ("Glen Johnson", "Defender", "2009–2015", "England", []),
    ("Fabio Aurelio", "Defender", "2006–2010", "Brazil", []),
    ("Mamadou Sakho", "Defender", "2013–2017", "France", []),
    ("Ragnar Klavan", "Defender", "2016–2018", "Estonia", []),
    # Midfielders
    ("Alexis Mac Allister", "Midfielder", "2023–present", "Argentina", ["current", "world-cup-winner"]),
    ("Dominik Szoboszlai", "Midfielder", "2023–present", "Hungary", ["current"]),
    ("Ryan Gravenberch", "Midfielder", "2023–present", "Netherlands", ["current"]),
    ("Wataru Endo", "Midfielder", "2023–present", "Japan", ["current", "captain"]),
    ("Curtis Jones", "Midfielder", "2019–present", "England", ["current", "academy"]),
    ("Harvey Elliott", "Midfielder", "2019–present", "England", ["current", "academy"]),
    ("Florian Wirtz", "Midfielder", "2025–present", "Germany", ["current"]),
    ("Steven Gerrard", "Midfielder", "1998–2015", "England", ["legend", "academy", "captain"]),
    ("Jordan Henderson", "Midfielder", "2011–2023", "England", ["legend", "captain"]),
    ("James Milner", "Midfielder", "2015–2023", "England", ["legend"]),
    ("Fabinho", "Midfielder", "2018–2023", "Brazil", ["legend"]),
    ("Gini Wijnaldum", "Midfielder", "2016–2021", "Netherlands", []),
    ("Naby Keita", "Midfielder", "2018–2023", None, []),
    ("Thiago Alcantara", "Midfielder", "2020–2024", "Spain", []),
    ("Xabi Alonso", "Midfielder", "2004–2009", "Spain", ["legend"]),
    ("Javier Mascherano", "Midfielder", "2007–2010", "Argentina", []),
    ("Lucas Leiva", "Midfielder", "2007–2017", "Brazil", []),
    ("Philippe Coutinho", "Midfielder", "2013–2018", "Brazil", []),
    ("Adam Lallana", "Midfielder", "2014–2020", "England", []),
    ("Emre Can", "Midfielder", "2014–2018", "Germany", []),
    ("Stefan Bajcetic", "Midfielder", "2022–present", "Spain", ["current", "academy"]),
    ("Giorgi Mamardashvili", "Goalkeeper", "2025–present", None, ["current"]),
    ("Raheem Sterling", "Forward", "2012–2015", "England", ["academy"]),
    ("Alberto Moreno", "Defender", "2014–2019", "Spain", []),
    ("Jose Enrique", "Defender", "2011–2014", "Spain", []),
    ("Ben Woodburn", "Midfielder", "2016–2022", "Wales", ["academy"]),
    ("Suso", "Midfielder", "2010–2013", "Spain", ["academy"]),
    ("Sebastian Coates", "Defender", "2011–2013", "Uruguay", []),
    ("Milan Jovanovic", "Forward", "2010–2011", "Serbia", []),
    ("Ian Callaghan", "Midfielder", "1960–1978", "England", ["legend", "1960s"]),
    ("Terry McDermott", "Midfielder", "1974–1980", "England", ["1970s"]),
    ("Graeme Souness", "Midfielder", "1978–1984", "Scotland", ["legend", "1980s", "captain"]),
    ("Steve McMahon", "Midfielder", "1985–1990", "England", ["1980s"]),
    ("John Barnes", "Midfielder", "1987–1997", "England", ["legend"]),
    ("Steve McManaman", "Midfielder", "1990–1999", "England", ["academy"]),
    ("Dietmar Hamann", "Midfielder", "1999–2006", "Germany", ["legend"]),
    ("Ray Kennedy", "Midfielder", "1974–1982", "England", ["1970s"]),
    ("Peter Beardsley", "Midfielder", "1987–1991", "England", []),
    ("Ronnie Whelan", "Midfielder", "1979–1994", "Republic of Ireland", ["1980s"]),
    ("Jimmy Case", "Midfielder", "1973–1981", "England", ["1970s"]),
    ("Takumi Minamino", "Midfielder", "2020–2024", "Japan", []),
    ("Arthur Melo", "Midfielder", "2022–2023", "Brazil", []),
    # Forwards
    ("Mohamed Salah", "Forward", "2017–present", "Egypt", ["current", "legend"]),
    ("Darwin Nunez", "Forward", "2022–present", "Uruguay", ["current"]),
    ("Luis Diaz", "Forward", "2022–present", "Colombia", ["current"]),
    ("Cody Gakpo", "Forward", "2023–present", "Netherlands", ["current"]),
    ("Hugo Ekitike", "Forward", "2025–present", "France", ["current"]),
    ("Federico Chiesa", "Forward", "2024–present", "Italy", ["current"]),
    ("Diogo Jota", "Forward", "2020–2024", "Portugal", ["legend", "remembrance"]),
    ("Roberto Firmino", "Forward", "2015–2023", "Brazil", ["legend"]),
    ("Sadio Mane", "Forward", "2016–2022", "Senegal", ["legend"]),
    ("Luis Suarez", "Forward", "2011–2014", "Uruguay", ["legend"]),
    ("Fernando Torres", "Forward", "2007–2011", "Spain", ["legend"]),
    ("Michael Owen", "Forward", "1996–2004", "England", ["legend", "academy"]),
    ("Robbie Fowler", "Forward", "1993–2001", "England", ["legend", "academy"]),
    ("Ian Rush", "Forward", "1980–1996", "Wales", ["legend"]),
    ("Kenny Dalglish", "Forward", "1977–1990", "Scotland", ["legend", "player-manager"]),
    ("Roger Hunt", "Forward", "1958–1969", "England", ["legend", "1960s"]),
    ("Ian St John", "Forward", "1961–1971", "Scotland", ["legend", "1960s"]),
    ("Kevin Keegan", "Forward", "1971–1977", "England", ["legend", "1970s"]),
    ("John Toshack", "Forward", "1970–1978", "Wales", ["1970s"]),
    ("Peter Crouch", "Forward", "2005–2010", "England", []),
    ("Dirk Kuyt", "Forward", "2006–2012", "Netherlands", []),
    ("Andy Carroll", "Forward", "2011–2013", "England", []),
    ("Daniel Sturridge", "Forward", "2013–2019", "England", []),
    ("Divock Origi", "Forward", "2014–2022", "Belgium", ["legend", "istanbul"]),
    ("Emile Heskey", "Forward", "1999–2004", "England", []),
    ("Stan Collymore", "Forward", "1995–1997", "England", []),
    ("Dean Saunders", "Forward", "1991–1992", "Wales", []),
    ("John Aldridge", "Forward", "1987–1991", "Republic of Ireland", ["1980s"]),
    ("Craig Bellamy", "Forward", "2007–2011", "Wales", []),
    ("Djibril Cisse", "Forward", "2004–2007", "France", []),
    ("Mario Balotelli", "Forward", "2014–2016", "Italy", []),
    ("Christian Benteke", "Forward", "2015–2016", "Belgium", []),
    ("Xherdan Shaqiri", "Forward", "2018–2021", "Switzerland", []),
    ("Luis Garcia", "Midfielder", "2005–2007", "Spain", ["legend", "istanbul"]),
    ("Vladimir Smicer", "Forward", "1999–2005", "Czech Republic", ["istanbul"]),
    ("Harry Kewell", "Forward", "2003–2008", "Australia", []),
    ("Florent Sinama-Pongolle", "Forward", "2003–2006", "France", []),
    ("Billy Liddell", "Forward", "1938–1961", "Scotland", ["legend", "1950s"]),
]

# Remove duplicates, invalid nationalities, and non-players like managers
SEEN = set()
CLEANED = []
for entry in PLAYERS:
    name = entry[0]
    if name in SEEN:
        continue
    SEEN.add(name)
    nationality = entry[3]
    if nationality and nationality not in VALID_CLUBS:
        # Drop nationality if not in import data (e.g. Finland, Estonia, Guinea)
        entry = (entry[0], entry[1], entry[2], None, entry[4])
    if entry[1] == "Manager":
        continue  # skip managers
    CLEANED.append(entry)
PLAYERS = CLEANED


def main():
    titles = [p[0] for p in PLAYERS]
    if len(titles) != len(set(titles)):
        dupes = {t for t in titles if titles.count(t) > 1}
        raise SystemExit(f"Duplicate names: {dupes}")

    if LIVERPOOL not in VALID_CLUBS:
        raise SystemExit(f"{LIVERPOOL!r} not found in club data.")

    players = []
    for name, position, years, nationality, tags in PLAYERS:
        clubs = [LIVERPOOL]
        if nationality:
            if nationality not in VALID_CLUBS:
                raise SystemExit(f"{name}: unknown nationality {nationality!r}")
            clubs.append(nationality)
        players.append(
            {
                "name": name,
                "position": position,
                "years_active": years,
                "clubs": clubs,
                "tags": ["liverpool", *tags],
            }
        )

    out = ROOT / "data/player/liverpool_players.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(players, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(players)} Liverpool players to {out}")


if __name__ == "__main__":
    main()
