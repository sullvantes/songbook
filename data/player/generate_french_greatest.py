"""Generate data/player/french_greatest.json. Run: python data/player/generate_french_greatest.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID = {
    c["name"]
    for c in json.loads((ROOT / "data/club/clubs.json").read_text())
    + json.loads((ROOT / "data/club/world_cup_teams.json").read_text())
}
FR = "France"

# name, position, years_active, clubs (excluding France), extra_tags
ENTRIES = [
    ("Michel Platini", "Forward", "1972–1987", ["Juventus"], ["legend", "goat", "1970s", "1980s"]),
    ("Zinedine Zidane", "Midfielder", "1988–2006", ["Juventus", "Real Madrid"], ["legend", "goat", "1990s", "2000s"]),
    ("Thierry Henry", "Forward", "1994–2014", ["AS Monaco", "Arsenal FC", "FC Barcelona"], ["legend", "goat", "1990s", "2000s", "2010s"]),
    ("Raymond Kopa", "Forward", "1949–1967", ["Real Madrid"], ["legend", "1950s", "1960s"]),
    ("Just Fontaine", "Forward", "1950–1962", ["OGC Nice"], ["legend", "1950s", "1960s"]),
    ("Lilian Thuram", "Defender", "1990–2008", ["AS Monaco", "Juventus", "FC Barcelona"], ["legend", "1990s", "2000s"]),
    ("Marcel Desailly", "Defender", "1986–2006", ["Olympique Marseille", "AC Milan", "Chelsea FC"], ["legend", "1980s", "1990s", "2000s"]),
    ("Laurent Blanc", "Defender", "1983–2003", ["AS Saint-Etienne", "Olympique Marseille", "AS Roma", "Inter Milan", "Manchester United"], ["legend", "1980s", "1990s", "2000s"]),
    ("Emmanuel Petit", "Midfielder", "1988–2005", ["AS Monaco", "Arsenal FC", "FC Barcelona", "Chelsea FC"], ["legend", "1990s", "2000s"]),
    ("Patrick Vieira", "Midfielder", "1993–2011", ["AS Monaco", "Arsenal FC", "Inter Milan", "Manchester City"], ["legend", "1990s", "2000s", "2010s"]),
    ("Robert Pires", "Midfielder", "1992–2014", ["AS Saint-Etienne", "Olympique Marseille", "Arsenal FC", "Villarreal CF"], ["legend", "1990s", "2000s", "2010s"]),
    ("Franck Ribery", "Forward", "2000–2023", ["Olympique Marseille", "Bayern Munich"], ["legend", "2000s", "2010s", "2020s"]),
    ("Karim Benzema", "Forward", "2004–present", ["Olympique Lyon", "Real Madrid", "Al Ittihad"], ["legend", "2000s", "2010s", "2020s"]),
    ("Kylian Mbappe", "Forward", "2015–present", ["AS Monaco", "Paris Saint-Germain", "Real Madrid"], ["legend", "2010s", "2020s"]),
    ("Antoine Griezmann", "Forward", "2009–present", ["Real Sociedad", "Atletico Madrid", "FC Barcelona"], ["legend", "2010s", "2020s"]),
    ("N'Golo Kante", "Midfielder", "2010–present", ["Leicester City", "Chelsea FC", "Al Ittihad"], ["legend", "2010s", "2020s"]),
    ("Hugo Lloris", "Goalkeeper", "2001–present", ["OGC Nice", "Tottenham Hotspur", "LA Galaxy"], ["legend", "2000s", "2010s", "2020s"]),
    ("Raphael Varane", "Defender", "2010–2024", ["Real Madrid", "Manchester United"], ["legend", "2010s", "2020s"]),
    ("Jean-Pierre Papin", "Forward", "1984–1998", ["Olympique Marseille", "AC Milan"], ["legend", "1980s", "1990s"]),
    ("Eric Cantona", "Forward", "1983–1997", ["Olympique Marseille", "Leeds United", "Manchester United"], ["legend", "1980s", "1990s"]),
    ("Didier Deschamps", "Midfielder", "1985–2003", ["Olympique Marseille", "Juventus", "Chelsea FC", "Valencia CF"], ["legend", "1980s", "1990s", "2000s"]),
    ("Fabien Barthez", "Goalkeeper", "1991–2007", ["AS Monaco", "Manchester United"], ["legend", "1990s", "2000s"]),
    ("Bixente Lizarazu", "Defender", "1988–2006", ["Bayern Munich", "Borussia Dortmund"], ["legend", "1980s", "1990s", "2000s"]),
    ("Youri Djorkaeff", "Forward", "1984–2006", ["AS Monaco", "Inter Milan"], ["legend", "1980s", "1990s", "2000s"]),
    ("David Trezeguet", "Forward", "1994–2014", ["AS Monaco", "Juventus"], ["legend", "1990s", "2000s", "2010s"]),
    ("Claude Makelele", "Midfielder", "1989–2011", ["Real Madrid", "Chelsea FC"], ["legend", "1990s", "2000s", "2010s"]),
    ("Sylvain Wiltord", "Forward", "1993–2012", ["Arsenal FC", "Olympique Lyon"], ["legend", "1990s", "2000s", "2010s"]),
    ("William Gallas", "Defender", "1997–2015", ["Chelsea FC", "Arsenal FC"], ["legend", "1990s", "2000s", "2010s"]),
    ("Samir Nasri", "Midfielder", "2004–2020", ["Olympique Marseille", "Arsenal FC", "Manchester City"], ["legend", "2000s", "2010s", "2020s"]),
    ("Nicolas Anelka", "Forward", "1996–2015", ["Arsenal FC", "Real Madrid", "Chelsea FC", "Manchester City"], ["legend", "1990s", "2000s", "2010s"]),
    ("Olivier Giroud", "Forward", "2005–present", ["Arsenal FC", "Chelsea FC", "AC Milan"], ["legend", "2000s", "2010s", "2020s"]),
    ("Paul Pogba", "Midfielder", "2011–present", ["Manchester United", "Juventus"], ["legend", "2010s", "2020s"]),
    ("Ousmane Dembele", "Forward", "2014–present", ["Borussia Dortmund", "FC Barcelona", "Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Nabil Fekir", "Forward", "2010–present", ["Olympique Lyon", "Real Betis"], ["2010s", "2020s"]),
    ("Kingsley Coman", "Forward", "2013–present", ["Paris Saint-Germain", "Juventus", "Bayern Munich"], ["2010s", "2020s"]),
    ("Adrien Rabiot", "Midfielder", "2012–present", ["Paris Saint-Germain", "Juventus"], ["2010s", "2020s"]),
    ("Aurelien Tchouameni", "Midfielder", "2018–present", ["AS Monaco", "Real Madrid"], ["2010s", "2020s"]),
    ("Eduardo Camavinga", "Midfielder", "2018–present", ["Real Madrid"], ["2010s", "2020s"]),
    ("Jules Kounde", "Defender", "2016–present", ["Sevilla FC", "FC Barcelona"], ["2010s", "2020s"]),
    ("Dayot Upamecano", "Defender", "2015–present", ["RB Leipzig", "Bayern Munich"], ["2010s", "2020s"]),
    ("Theo Hernandez", "Defender", "2014–present", ["AC Milan", "Real Madrid"], ["2010s", "2020s"]),
    ("Lucas Hernandez", "Defender", "2014–present", ["Atletico Madrid", "Bayern Munich"], ["2010s", "2020s"]),
    ("Benjamin Pavard", "Defender", "2014–present", ["VfB Stuttgart", "Bayern Munich", "Inter Milan"], ["2010s", "2020s"]),
    ("Presnel Kimpembe", "Defender", "2014–present", ["Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Dimitri Payet", "Midfielder", "2000–present", ["Olympique Marseille", "West Ham United"], ["legend", "2000s", "2010s", "2020s"]),
    ("Steve Mandanda", "Goalkeeper", "2004–present", ["Olympique Marseille"], ["legend", "2000s", "2010s", "2020s"]),
    ("Mike Maignan", "Goalkeeper", "2015–present", ["Lille OSC", "AC Milan"], ["2010s", "2020s"]),
    ("Marius Tresor", "Defender", "1968–1983", ["Olympique Marseille"], ["legend", "1960s", "1970s", "1980s"]),
    ("Dominique Rocheteau", "Forward", "1972–1989", ["AS Saint-Etienne", "Paris Saint-Germain"], ["legend", "1970s", "1980s"]),
    ("Alain Giresse", "Midfielder", "1970–1988", [], ["legend", "1970s", "1980s"]),
    ("Jean Tigana", "Midfielder", "1975–1995", [], ["legend", "1970s", "1980s", "1990s"]),
    ("Luis Fernandez", "Midfielder", "1978–1997", [], ["legend", "1970s", "1980s", "1990s"]),
    ("Maxime Bossis", "Defender", "1969–1985", [], ["legend", "1960s", "1970s", "1980s"]),
    ("Roger Piantoni", "Forward", "1950–1966", [], ["legend", "1950s", "1960s"]),
    ("Maryan Wisnieski", "Forward", "1953–1968", [], ["legend", "1950s", "1960s"]),
    ("Robert Jonquet", "Defender", "1943–1960", [], ["legend", "1940s", "1950s", "1960s"]),
    ("Bernard Bosquier", "Defender", "1963–1978", [], ["legend", "1960s", "1970s"]),
    ("Michel Hidalgo", "Midfielder", "1952–1966", ["Olympique Lyon"], ["legend", "1950s", "1960s"]),
    ("Bruno Bellone", "Forward", "1977–1994", [], ["legend", "1970s", "1980s", "1990s"]),
    ("Hatem Ben Arfa", "Forward", "2004–present", ["Olympique Marseille", "Newcastle United"], ["2000s", "2010s", "2020s"]),
    ("Wissam Ben Yedder", "Forward", "2010–present", ["AS Monaco", "Sevilla FC"], ["2010s", "2020s"]),
    ("Lucas Digne", "Defender", "2011–present", ["Paris Saint-Germain", "Everton FC", "Aston Villa"], ["2010s", "2020s"]),
    ("Yohan Cabaye", "Midfielder", "2004–2019", ["Lille OSC", "Paris Saint-Germain", "Newcastle United"], ["2000s", "2010s"]),
    ("Blaise Matuidi", "Midfielder", "2004–2022", ["Paris Saint-Germain", "Juventus", "Inter Miami CF"], ["legend", "2000s", "2010s", "2020s"]),
    ("Jeremy Menez", "Forward", "2004–2020", ["AS Roma", "Paris Saint-Germain", "AC Milan"], ["2000s", "2010s", "2020s"]),
    ("Mathieu Flamini", "Midfielder", "2003–2019", ["Arsenal FC", "AC Milan"], ["2000s", "2010s"]),
    ("Alexandre Lacazette", "Forward", "2009–present", ["Olympique Lyon", "Arsenal FC"], ["2000s", "2010s", "2020s"]),
    ("Corentin Tolisso", "Midfielder", "2013–present", ["Olympique Lyon", "Bayern Munich"], ["2010s", "2020s"]),
    ("Ferland Mendy", "Defender", "2015–present", ["Olympique Lyon", "Real Madrid"], ["2010s", "2020s"]),
    ("Christopher Nkunku", "Forward", "2015–present", ["Paris Saint-Germain", "RB Leipzig", "Chelsea FC"], ["2010s", "2020s"]),
    ("Ibrahima Konate", "Defender", "2017–present", ["RB Leipzig", "Liverpool FC"], ["2010s", "2020s"]),
    ("Wesley Fofana", "Defender", "2018–present", ["Leicester City", "Chelsea FC"], ["2010s", "2020s"]),
    ("Kurt Zouma", "Defender", "2011–present", ["Chelsea FC", "West Ham United"], ["2010s", "2020s"]),
    ("Axel Disasi", "Defender", "2016–present", ["AS Monaco", "Chelsea FC"], ["2010s", "2020s"]),
    ("Djibril Cisse", "Forward", "1998–2015", ["Olympique Marseille", "Liverpool FC"], ["1990s", "2000s", "2010s"]),
    ("Sidney Govou", "Forward", "2000–2015", ["Olympique Lyon"], ["2000s", "2010s"]),
    ("Florent Malouda", "Midfielder", "1997–2018", ["Olympique Lyon", "Chelsea FC"], ["1990s", "2000s", "2010s"]),
    ("Johan Micoud", "Midfielder", "1990–2008", ["Werder Bremen", "Bayern Munich"], ["1990s", "2000s"]),
    ("Christian Karembeu", "Midfielder", "1988–2005", ["Olympique Marseille", "Real Madrid"], ["legend", "1980s", "1990s", "2000s"]),
    ("Frank Leboeuf", "Defender", "1988–2007", ["Olympique Marseille", "Chelsea FC"], ["legend", "1980s", "1990s", "2000s"]),
    ("Bernard Lama", "Goalkeeper", "1983–2001", ["Paris Saint-Germain"], ["legend", "1980s", "1990s", "2000s"]),
    ("Marcus Thuram", "Forward", "2015–present", ["Borussia Monchengladbach", "Inter Milan"], ["2010s", "2020s"]),
    ("Loic Remy", "Forward", "2005–2021", ["Chelsea FC", "Newcastle United"], ["2000s", "2010s", "2020s"]),
    ("Anthony Martial", "Forward", "2012–present", ["Manchester United"], ["2010s", "2020s"]),
    ("Tanguy Ndombele", "Midfielder", "2016–present", ["Tottenham Hotspur", "Olympique Lyon"], ["2010s", "2020s"]),
    ("Christophe Dugarry", "Forward", "1990–2008", ["FC Barcelona", "Olympique Marseille"], ["1990s", "2000s"]),
    ("Andre-Pierre Gignac", "Forward", "2004–present", ["Olympique Lyon", "Olympique Marseille"], ["2000s", "2010s", "2020s"]),
    ("Amine Gouiri", "Forward", "2017–present", ["OGC Nice", "Real Sociedad"], ["2010s", "2020s"]),
    ("Alphonse Areola", "Goalkeeper", "2012–present", ["Paris Saint-Germain", "Real Madrid"], ["2010s", "2020s"]),
    ("William Saliba", "Defender", "2018–present", ["Arsenal FC"], ["2010s", "2020s"]),
    ("Moussa Sissoko", "Midfielder", "2007–present", ["Newcastle United", "Tottenham Hotspur", "SSC Napoli"], ["2000s", "2010s", "2020s"]),
    ("Jean-Pierre Adams", "Defender", "1963–1976", [], ["legend", "1960s", "1970s"]),
    ("Wendie Renard", "Defender", "2007–present", ["Olympique Lyon"], ["legend", "2000s", "2010s", "2020s"]),
    ("Marie-Antoinette Katoto", "Forward", "2015–present", ["Paris Saint-Germain"], ["legend", "2010s", "2020s"]),
    ("Kadidiatou Diani", "Forward", "2011–present", ["Paris Saint-Germain"], ["legend", "2010s", "2020s"]),
    ("Amandine Henry", "Midfielder", "2004–present", ["Olympique Lyon", "Paris Saint-Germain"], ["legend", "2000s", "2010s", "2020s"]),
    ("Eugenie Le Sommer", "Forward", "2004–present", ["Olympique Lyon"], ["legend", "2000s", "2010s", "2020s"]),
    ("Sakina Karchaoui", "Defender", "2013–present", ["Paris Saint-Germain", "Manchester City"], ["2010s", "2020s"]),
    ("Grace Geyoro", "Midfielder", "2015–present", ["Paris Saint-Germain"], ["2010s", "2020s"]),
    ("Selma Bacha", "Defender", "2018–present", ["Olympique Lyon"], ["2010s", "2020s"]),
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
                "clubs": [*clubs, FR],
                "tags": ["french", *tags],
            }
        )

    out = ROOT / "data/player/french_greatest.json"
    out.write_text(json.dumps(players, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(players)} players to {out}")


if __name__ == "__main__":
    main()
