"""Generate data/song/chicago_fire_chants.json. Run: python data/song/generate_chicago_fire_chants.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLUB = "Chicago Fire FC"
VALID_CLUBS = {
    c["name"]
    for c in json.loads((ROOT / "data/club/clubs.json").read_text())
    + json.loads((ROOT / "data/club/world_cup_teams.json").read_text())
    + json.loads((ROOT / "data/club/mls_teams.json").read_text())
}

# title, lyrics, description, tags
CHANTS = [
    (
        "For Chicago For Chicago Fire",
        "For Chicago, for Chicago Fire,\nFor Chicago, for Chicago Fire,\nWe will follow you wherever you go!",
        "Classic Chicago Fire supporter chant — one of the club's most recognizable terrace songs.",
        ["anthem", "classic", "supporters"],
    ),
    (
        "Chicago Fire Till I Die",
        "Chicago Fire till I die, on this I do rely,\nWe will love you Chicago Fire, till the day we die.",
        "Terrace pledge of lifelong support for the Fire.",
        ["fan-chant", "classic"],
    ),
    (
        "We Are the Fire",
        "We are the Fire, the mighty Fire,\nWe are the Fire, from Chicago!",
        "Identity chant for the club's Fire nickname.",
        ["fan-chant", "identity"],
    ),
    (
        "Burn Burn Burn",
        "Burn, burn, burn, Chicago Fire burn,\nBurn, burn, burn, till the league is overturned!",
        "High-energy chant built around the Fire name.",
        ["fan-chant", "identity"],
    ),
    (
        "Section 8 Is Here",
        "Section 8 is here, Section 8 is here,\nLoudest section in MLS, Section 8 is here!",
        "Chant for Section 8, the independent Chicago Fire supporters group.",
        ["fan-chant", "supporters", "section-8"],
    ),
    (
        "Let Your Light Shine",
        "Let your light shine, let your light shine,\nChicago Fire, let your light shine!",
        "Chant inspired by the club's 'Let Your Light Shine' motto.",
        ["fan-chant", "motto"],
    ),
    (
        "Chicago Fire Ole Ole Ole",
        "Ole, ole, ole ole! Ole, ole!\nChicago Fire, ole, ole!",
        "Victory chant adapted from the universal Ole Ole Ole.",
        ["fan-chant", "victory"],
    ),
    (
        "Fire Away",
        "Fire away, fire away, Chicago Fire away,\nFire away, fire away, every single day!",
        "Simple repetitive terrace chant.",
        ["fan-chant"],
    ),
    (
        "Chicago Fire Allez Allez",
        "Allez, allez, allez,\nWe are Chicago Fire, super Chicago Fire,\nAllez, allez, allez!",
        "Adapted allez-allez chant popular across global soccer.",
        ["fan-chant", "modern"],
    ),
    (
        "MLS Original",
        "Ninety-eight we won it all, Chicago Fire standing tall,\nMLS original, the first of them all!",
        "Chant celebrating the Fire's 1998 MLS Cup as an original MLS club.",
        ["fan-chant", "history", "mls-cup"],
    ),
    (
        "1998 MLS Cup Champions",
        "Nineteen ninety-eight, we were great,\nChicago Fire, MLS Cup champions of the league!",
        "Historical chant for the club's inaugural MLS Cup triumph.",
        ["fan-chant", "history", "mls-cup"],
    ),
    (
        "Double in 98",
        "Double in ninety-eight, double in ninety-eight,\nOpen Cup and MLS Cup, Chicago Fire was great!",
        "Chant referencing the 1998 domestic double (MLS Cup and US Open Cup).",
        ["fan-chant", "history", "trophy"],
    ),
    (
        "Soldier Field Belongs to Us",
        "Soldier Field belongs to us,\nSoldier Field belongs to us,\nEverywhere we go, the people want to know,\nWho we are, so we tell them.",
        "Home end chant at Soldier Field.",
        ["fan-chant", "stadium"],
    ),
    (
        "Bridgeview Days",
        "Bridgeview days, Bridgeview days,\nToyota Park memories never fade away!",
        "Nostalgic chant referencing the club's former stadium in Bridgeview.",
        ["fan-chant", "history", "stadium"],
    ),
    (
        "Chicago Fire Anthem",
        "Chicago Fire, burning bright,\nRed and white through day and night,\nFrom the lakefront to the west,\nChicago Fire, you're the best!",
        "Original-style fan anthem for the club.",
        ["anthem", "fan-song"],
    ),
    (
        "Windy City Fire",
        "Windy City Fire, Windy City Fire,\nChicago Fire, taking us higher!",
        "Chant linking the club to Chicago's Windy City nickname.",
        ["fan-chant", "city"],
    ),
    (
        "Midwest Soccer Pride",
        "Midwest soccer pride, Midwest soccer pride,\nChicago Fire, side by side!",
        "Regional identity chant for Midwest soccer culture.",
        ["fan-chant", "midwest"],
    ),
    (
        "Polish Triangle Fire",
        "Polish Triangle, Polish Triangle,\nChicago Fire, we all mingle!",
        "Chant referencing Chicago's historic Polish Triangle neighborhood and fan culture.",
        ["fan-chant", "city", "culture"],
    ),
    (
        "Over Land and Sea and Chicago",
        "We all follow Chicago Fire, over land and sea and Chicago,\nWe all follow Chicago Fire, on to victory!",
        "Away-support chant adapted from English terrace traditions.",
        ["fan-chant", "away"],
    ),
    (
        "Chicago Fire We Love You",
        "Chicago Fire, we love you, we do,\nChicago Fire, we love you, we do,\nChicago Fire, we love you, we do,\nAnd Soldier Field is our home!",
        "Simple love song for the club and stadium.",
        ["fan-chant"],
    ),
    (
        "Red and White Army",
        "Red and white army, red and white army,\nChicago Fire, the red and white army!",
        "Terrace identity chant for the club's colors.",
        ["fan-chant", "identity"],
    ),
    (
        "Fire on a Saturday",
        "Fire on a Saturday, we're going out today,\nFor a game of football with the Chicago Fire!",
        "Matchday terrace song for Saturday kickoffs.",
        ["fan-song", "matchday"],
    ),
    (
        "La La La Chicago Fire",
        "La la la la la, la la la la la,\nLa la la la la la la, Chicago Fire!",
        "Simple la-la-la terrace chant used during matches.",
        ["fan-chant"],
    ),
    (
        "Cuauhtémoc Blanco Song",
        "Cuauhtémoc Blanco, magic on the pitch,\nCuauhtémoc Blanco, Chicago Fire's witch!",
        "Player tribute for Mexican legend Cuauhtémoc Blanco.",
        ["player-tribute", "blanco", "legend"],
    ),
    (
        "Blanco La Ola",
        "Blanco, Blanco, running with the ball,\nBlanco, Blanco, best of them all!",
        "Chant celebrating Cuauhtémoc Blanco's flair at Chicago Fire.",
        ["player-tribute", "blanco"],
    ),
    (
        "Hristo Stoichkov Song",
        "Hristo, Hristo Stoichkov, Bulgarian king,\nHristo, Hristo Stoichkov, hear the Fire sing!",
        "Tribute to Bulgarian legend Hristo Stoichkov.",
        ["player-tribute", "stoichkov", "legend"],
    ),
    (
        "Bastian Schweinsteiger Chant",
        "Schweinsteiger, Schweinsteiger, World Cup winner here,\nSchweinsteiger, Schweinsteiger, Fire legend we revere!",
        "Chant for German World Cup winner Bastian Schweinsteiger.",
        ["player-tribute", "schweinsteiger", "legend"],
    ),
    (
        "Brian McBride Song",
        "McBride, McBride, heading in the goal,\nMcBride, McBride, Fire in his soul!",
        "Tribute to American legend and former captain Brian McBride.",
        ["player-tribute", "mcbride", "legend"],
    ),
    (
        "Chris Armas Chant",
        "Chris Armas, Chris Armas, engine of the team,\nChris Armas, Chris Armas, Fire's midfield dream!",
        "Player tribute for former midfielder Chris Armas.",
        ["player-tribute", "armas"],
    ),
    (
        "CJ Sapong Song",
        "Sapong, Sapong, scoring for the Fire,\nSapong, Sapong, taking us higher!",
        "Chant for forward CJ Sapong.",
        ["player-tribute"],
    ),
    (
        "Xherdan Shaqiri Chant",
        "Shaqiri, Shaqiri, left foot like a whip,\nShaqiri, Shaqiri, Chicago Fire's chip!",
        "Player tribute for Swiss star Xherdan Shaqiri.",
        ["player-tribute", "shaqiri"],
    ),
    (
        "Chris Mueller Song",
        "Mueller, Mueller, running down the wing,\nMueller, Mueller, hear the Fire sing!",
        "Chant for winger Chris Mueller.",
        ["player-tribute"],
    ),
    (
        "Gabriel Slonina Chant",
        "Slonina, Slonina, standing in the goal,\nSlonina, Slonina, Chicago Fire's soul!",
        "Goalkeeper tribute for Gabriel Slonina.",
        ["player-tribute", "goalkeeper"],
    ),
    (
        "Fire Goal Celebration",
        "Score a goal, fire celebration,\nChicago Fire all across the nation!",
        "Post-goal terrace chant.",
        ["fan-chant", "goal"],
    ),
    (
        "Beat the Crew",
        "Beat the Crew, beat the Crew, beat the Crew today,\nHell is real, but the Fire's here to stay!",
        "Rivalry chant against Columbus Crew.",
        ["fan-chant", "derby", "columbus"],
    ),
    (
        "Beat Sporting KC",
        "Beat Sporting, beat Sporting, beat Sporting today,\nHeartland rivalry, Fire all the way!",
        "Rivalry chant against Sporting Kansas City.",
        ["fan-chant", "derby", "sporting-kc"],
    ),
    (
        "Beat St Louis City",
        "Beat St Louis, beat St Louis, beat St Louis today,\nMidwest derby, Fire all the way!",
        "Regional rivalry chant against St. Louis CITY SC.",
        ["fan-chant", "derby", "st-louis"],
    ),
    (
        "Playoffs Fire",
        "Playoffs fire, playoffs fire,\nChicago Fire marching on!",
        "Playoff push chant for late-season matches.",
        ["fan-chant", "playoffs"],
    ),
    (
        "Fire Drums",
        "Beat the drums, beat the drums, Fire drums are here,\nChicago Fire supporters, loudest in the atmosphere!",
        "Chant for the supporter drumming sections.",
        ["fan-chant", "supporters"],
    ),
    (
        "Smoke and Flares",
        "Smoke and flares, smoke and flares,\nChicago Fire filling the air!",
        "Tifo and smoke celebration chant.",
        ["fan-chant", "tifo"],
    ),
    (
        "Fire Away Days",
        "Fire away days, Fire away days,\nFollowing Chicago every mile!",
        "Dedicated travelling supporters chant.",
        ["fan-chant", "away"],
    ),
    (
        "I Will Follow You Into the Fire",
        "I will follow you into the Fire,\nI will follow you into the Fire,\nChicago Fire, wherever you go!",
        "Terrace song play on the club name inspired by supporter culture.",
        ["fan-song", "classic"],
    ),
    (
        "Chicago Till I Die",
        "Chicago till I die, on this I do rely,\nWe will love you Chicago Fire, till the day we die.",
        "City-focused variant of the till-I-die pledge.",
        ["fan-chant"],
    ),
    (
        "Original 10 Pride",
        "Original ten pride, original ten pride,\nChicago Fire, MLS since ninety-five!",
        "Chant celebrating the Fire as one of MLS's original ten clubs.",
        ["fan-chant", "history", "mls-original"],
    ),
    (
        "Lamar Hunt Open Cup",
        "Open Cup champions, Open Cup champions,\nChicago Fire, trophy hunters!",
        "Chant celebrating multiple US Open Cup wins.",
        ["fan-chant", "history", "open-cup"],
    ),
    (
        "Fire Night",
        "Fire night, fire night, everything's alright,\nChicago Fire under the Soldier Field lights!",
        "Evening kickoff atmosphere chant.",
        ["fan-chant", "night-match"],
    ),
    (
        "Jump Around Soldier Field",
        "Jump around! Jump around! Jump around!\nChicago Fire, Soldier Field, jump around!",
        "Stadium hype chant inspired by jump-around traditions.",
        ["fan-chant", "stadium"],
    ),
    (
        "Chicago Fire Forever",
        "Chicago Fire forever, whatever the weather,\nRed and white together, now and forever!",
        "Closing terrace song affirming long-term loyalty.",
        ["fan-song", "classic"],
    ),
    (
        "Fuego Fuego",
        "Fuego, fuego, Chicago Fire fuego,\nFuego, fuego, burning through the league-o!",
        "Bilingual fire-themed terrace chant.",
        ["fan-chant", "bilingual"],
    ),
    (
        "Lakefront to the Loop",
        "From the lakefront to the Loop,\nChicago Fire, we follow you!",
        "Geographic chant referencing Chicago neighborhoods.",
        ["fan-chant", "city"],
    ),
]


def main():
    if CLUB not in VALID_CLUBS:
        raise SystemExit(f"{CLUB!r} not found in club data. Import MLS teams first.")

    titles = [c[0] for c in CHANTS]
    if len(titles) != len(set(titles)):
        dupes = {t for t in titles if titles.count(t) > 1}
        raise SystemExit(f"Duplicate titles: {dupes}")

    songs = []
    for title, lyrics, description, tags in CHANTS:
        songs.append(
            {
                "title": title,
                "lyrics": lyrics,
                "description": description,
                "is_fan_chant": True,
                "accepted": True,
                "clubs": [CLUB],
                "tags": ["chant", "chicago-fire", "mls", *tags],
            }
        )

    out = ROOT / "data/song/chicago_fire_chants.json"
    out.write_text(json.dumps(songs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(songs)} Chicago Fire chants to {out}")


if __name__ == "__main__":
    main()
