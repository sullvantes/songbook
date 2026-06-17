"""Generate data/song/austin_fc_chants.json. Run: python data/song/generate_austin_fc_chants.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLUB = "Austin FC"
VALID_CLUBS = {
    c["name"]
    for c in json.loads((ROOT / "data/club/clubs.json").read_text())
    + json.loads((ROOT / "data/club/world_cup_teams.json").read_text())
    + json.loads((ROOT / "data/club/mls_teams.json").read_text())
}

# title, lyrics, description, tags
CHANTS = [
    (
        "Verde Listos",
        "Verde listos! Verde listos!\nAustin FC, we're ready to go!\nVerde listos! Verde listos!\nQ2 Stadium, let the green flag flow!",
        "Austin FC's official motto chant — 'Green, Ready' — sung by supporters at Q2 Stadium.",
        ["anthem", "motto", "pre-match"],
    ),
    (
        "Verde Till I Die",
        "Verde till I die, on this I do rely,\nWe will love you Austin FC, till the day we die.",
        "Terrace pledge of lifelong support for the Verde and Black.",
        ["fan-chant", "classic"],
    ),
    (
        "We Are Austin",
        "We are Austin, super Austin,\nWe are Austin, from the capital city!",
        "Call-and-response chant celebrating Austin as Texas's capital.",
        ["fan-chant", "city"],
    ),
    (
        "Austin FC Ole Ole Ole",
        "Ole, ole, ole ole! Ole, ole!\nAustin FC, ole, ole!",
        "Victory chant adapted from the universal Ole Ole Ole.",
        ["fan-chant", "victory"],
    ),
    (
        "Verde Verde Verde",
        "Verde, verde, verde!\nAustin FC! Austin FC!\nVerde, verde, verde!",
        "Simple repetitive chant for the club's green identity.",
        ["fan-chant", "identity"],
    ),
    (
        "Capital City Boys",
        "We're the capital city boys, making all the noise,\nAustin FC, Austin FC, we're the capital city boys!",
        "Chant linking the club to Austin's status as capital of Texas.",
        ["fan-chant", "city"],
    ),
    (
        "ATX Till I Die",
        "ATX till I die, on this I do rely,\nWe will love you Austin FC, till the day we die.",
        "Variant terrace song using the city's ATX abbreviation.",
        ["fan-chant"],
    ),
    (
        "Q2 Stadium Belongs to Us",
        "Q2 Stadium belongs to us,\nQ2 Stadium belongs to us,\nEverywhere we go, the people want to know,\nWho we are, so we tell them.",
        "Home end chant asserting Q2 Stadium as Austin FC territory.",
        ["fan-chant", "stadium"],
    ),
    (
        "Listos Verdes",
        "Listos verdes, listos verdes,\nAustin FC on the march again!",
        "Spanish-English hybrid chant using the club's green-ready identity.",
        ["fan-chant", "bilingual"],
    ),
    (
        "Keep Austin Verde",
        "Keep Austin verde, keep Austin verde,\nKeep Austin verde, Austin FC!",
        "Play on Austin's 'Keep Austin Weird' slogan adapted for the club.",
        ["fan-chant", "city"],
    ),
    (
        "Lone Star Greens",
        "Lone Star greens, Lone Star greens,\nAustin FC, the finest team you've seen!",
        "Chant referencing Texas as the Lone Star State.",
        ["fan-chant", "texas"],
    ),
    (
        "March to Q2",
        "March to Q2, march to Q2,\nAustin FC, we're marching through!",
        "Pre-match march chant as supporters head to the stadium.",
        ["fan-chant", "pre-match", "stadium"],
    ),
    (
        "Austin FC Anthem",
        "Austin FC, the capital's team,\nVerde and black is all we need,\nFrom the Hill Country to the coast,\nAustin FC, we love you most!",
        "Original-style fan anthem for the club.",
        ["anthem", "fan-song"],
    ),
    (
        "La La La Austin FC",
        "La la la la la, la la la la la,\nLa la la la la la la, Austin FC!",
        "Simple la-la-la terrace chant used during matches.",
        ["fan-chant"],
    ),
    (
        "Green and Black Army",
        "Green and black army, green and black army,\nAustin FC, the green and black army!",
        "Terrace identity chant for the Verde and Black supporters.",
        ["fan-chant", "identity"],
    ),
    (
        "Over Land and Sea and ATX",
        "We all follow Austin FC, over land and sea and ATX,\nWe all follow Austin FC, on to victory!",
        "Away-support chant adapted from English terrace traditions.",
        ["fan-chant", "away"],
    ),
    (
        "Verde on a Saturday",
        "Verde on a Saturday, we're going out today,\nFor a game of football with the Austin FC!",
        "Matchday terrace song for Saturday kickoffs.",
        ["fan-song", "matchday"],
    ),
    (
        "Austin FC We Love You",
        "Austin FC, we love you, we do,\nAustin FC, we love you, we do,\nAustin FC, we love you, we do,\nAnd Q2 is our home!",
        "Simple love song for the club and stadium.",
        ["fan-chant"],
    ),
    (
        "Texas Soccer Town",
        "Austin, Texas, soccer town,\nVerde and black we're world renowned!",
        "Chant positioning Austin as a growing American soccer city.",
        ["fan-chant", "city", "texas"],
    ),
    (
        "Section Verde",
        "Section Verde, Section Verde,\nLoudest section in the league!",
        "Chant for the loudest supporter sections at Q2 Stadium.",
        ["fan-chant", "supporters"],
    ),
    (
        "Austin FC Allez Allez",
        "Allez, allez, allez,\nWe are Austin FC, super Austin FC,\nAllez, allez, allez!",
        "Adapted allez-allez chant popular across global soccer.",
        ["fan-chant", "modern"],
    ),
    (
        "Verde Wave",
        "Do the verde wave, do the verde wave,\nAustin FC, Austin FC, do the verde wave!",
        "Stadium participation chant encouraging the wave.",
        ["fan-chant", "stadium"],
    ),
    (
        "ATX FC On Tour",
        "ATX FC on tour, ATX FC on tour,\nEverywhere we go, people want to know,\nWho we are, where we come from.",
        "Away-day chant for travelling Austin FC supporters.",
        ["fan-chant", "away"],
    ),
    (
        "Green Flag High",
        "Keep the green flag flying high, in the Texas sky,\nAustin FC forever, till the day we die!",
        "Terrace song about flying the club's green flag.",
        ["fan-song", "identity"],
    ),
    (
        "Sebastian Driussi Song",
        "Seba, Seba, Seba Driussi,\nAustin FC number ten, he's the best you'll ever see!",
        "Player chant for Argentine forward Sebastian Driussi.",
        ["player-tribute", "driussi"],
    ),
    (
        "Driussi Is His Name",
        "His name is Seba Driussi, he plays for Austin FC,\nHis name is Seba Driussi, he's better than Messi!",
        "Humorous player tribute comparing Driussi to Lionel Messi.",
        ["player-tribute", "driussi"],
    ),
    (
        "Diego Fagundez Song",
        "Diego, Diego Fagundez, running down the wing,\nDiego, Diego Fagundez, Austin FC king!",
        "Chant for longtime MLS winger Diego Fagundez.",
        ["player-tribute", "fagundez"],
    ),
    (
        "Alex Ring Song",
        "Alex Ring, Alex Ring, leading from the back,\nAlex Ring, Alex Ring, captain of the pack!",
        "Tribute to Danish captain and defender Alex Ring.",
        ["player-tribute", "ring"],
    ),
    (
        "Rodrigo Bentancur Chant",
        "Bentancur, Bentancur, running through the middle,\nBentancur, Bentancur, Austin FC's riddle!",
        "Chant for Uruguayan midfielder Rodrigo Bentancur at Austin FC.",
        ["player-tribute"],
    ),
    (
        "Nick Lima Song",
        "Nick Lima, Nick Lima, overlapping down the right,\nNick Lima, Nick Lima, green and black delight!",
        "Full-back tribute for Nick Lima.",
        ["player-tribute", "lima"],
    ),
    (
        "Cascante in the Middle",
        "Cascante in the middle, Cascante in the middle,\nRunning the show, running the show!",
        "Chant for Costa Rican midfielder Diego Cascante.",
        ["player-tribute", "cascante"],
    ),
    (
        "Brad Stuver Song",
        "Brad Stuver, Brad Stuver, standing tall in goal,\nBrad Stuver, Brad Stuver, keeping a clean sheet whole!",
        "Goalkeeper tribute for Brad Stuver.",
        ["player-tribute", "goalkeeper"],
    ),
    (
        "Pochettino Chant",
        "Pochettino, Pochettino, scoring for the green,\nPochettino, Pochettino, best we've ever seen!",
        "Chant for Austin FC forward Brandon Pochettino.",
        ["player-tribute"],
    ),
    (
        "Emiliano Rigoni Song",
        "Rigoni, Rigoni, magic on the ball,\nRigoni, Rigoni, best of them all!",
        "Player tribute for Argentine winger Emiliano Rigoni.",
        ["player-tribute", "rigoni"],
    ),
    (
        "Verde Goal Celebration",
        "Score a goal, verde celebration,\nAustin FC all across the nation!",
        "Post-goal terrace chant.",
        ["fan-chant", "goal"],
    ),
    (
        "MLS Expansion Pride",
        "Twenty twenty-one we arrived, Austin FC came alive,\nMLS expansion, verde and black, we thrive!",
        "Chant referencing Austin FC's 2021 MLS expansion debut.",
        ["fan-chant", "history", "expansion"],
    ),
    (
        "First Match at Q2",
        "First match at Q2, history was made,\nVerde and black, a new parade!",
        "Chant commemorating the inaugural match at Q2 Stadium.",
        ["fan-chant", "history", "stadium"],
    ),
    (
        "Playoffs Verde",
        "Playoffs verde, playoffs verde,\nAustin FC marching on!",
        "Playoff push chant for late-season matches.",
        ["fan-chant", "playoffs"],
    ),
    (
        "Beat Houston",
        "Beat Houston, beat Houston, beat Houston today,\nTexas derby, verde all the way!",
        "Texas derby chant against Houston Dynamo FC.",
        ["fan-chant", "derby", "houston"],
    ),
    (
        "Beat FC Dallas",
        "Beat Dallas, beat Dallas, beat Dallas today,\nCopa Tejas on the line, verde all the way!",
        "Copa Tejas rivalry chant against FC Dallas.",
        ["fan-chant", "derby", "dallas"],
    ),
    (
        "Copa Tejas Champions",
        "Copa Tejas champions, Copa Tejas champions,\nAustin FC, the best in Texas!",
        "Chant celebrating the Copa Tejas in-state trophy.",
        ["fan-chant", "derby", "trophy"],
    ),
    (
        "Verde Night",
        "Verde night, verde night, everything's alright,\nAustin FC under the Q2 lights!",
        "Evening kickoff atmosphere chant.",
        ["fan-chant", "night-match"],
    ),
    (
        "Jump Around Q2",
        "Jump around! Jump around! Jump around!\nAustin FC, Q2 Stadium, jump around!",
        "Stadium hype chant inspired by jump-around traditions.",
        ["fan-chant", "stadium"],
    ),
    (
        "Verde Drums",
        "Beat the drums, beat the drums, verde drums are here,\nAustin FC supporters, loudest in the atmosphere!",
        "Chant for the supporter drumming sections.",
        ["fan-chant", "supporters"],
    ),
    (
        "Austin FC Forever",
        "Austin FC forever, whatever the weather,\nVerde and black together, now and forever!",
        "Closing terrace song affirming long-term loyalty.",
        ["fan-song", "classic"],
    ),
    (
        "Green Smoke Rise",
        "Green smoke rise, green smoke rise,\nAustin FC, open your eyes!",
        "Tifo and smoke celebration chant.",
        ["fan-chant", "tifo"],
    ),
    (
        "Verde Away Days",
        "Verde away days, verde away days,\nFollowing Austin every mile!",
        "Dedicated travelling supporters chant.",
        ["fan-chant", "away"],
    ),
    (
        "Listos for Glory",
        "Listos for glory, listos for glory,\nAustin FC writing history!",
        "Ambitious terrace chant for silverware.",
        ["fan-chant", "ambition"],
    ),
    (
        "Hill Country to Q2",
        "From the Hill Country to Q2,\nAustin FC, we follow you!",
        "Geographic chant referencing the Texas Hill Country around Austin.",
        ["fan-chant", "city", "texas"],
    ),
    (
        "Verde Heartbeat",
        "Feel the verde heartbeat, feel the verde heartbeat,\nAustin FC, can't be beat!",
        "Rhythmic clapping chant in the stands.",
        ["fan-chant", "rhythm"],
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
                "tags": ["chant", "austin-fc", "mls", *tags],
            }
        )

    out = ROOT / "data/song/austin_fc_chants.json"
    out.write_text(json.dumps(songs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(songs)} Austin FC chants to {out}")


if __name__ == "__main__":
    main()
