"""Generate data/song/chelsea_chants.json. Run: python data/song/generate_chelsea_chants.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLUB = "Chelsea FC"

# title, lyrics, description, tags
CHANTS = [
    (
        "Carefree",
        "Carefree, wherever we may be,\nWe are the famous CFC,\nStrongly we will follow,\nWherever they may be,\nWe will not be moved,\nFrom our old familiar home on the banks of the River Thames.",
        "Chelsea's best-known terrace song, sung home and away to declare loyalty to the club.",
        ["fan-song", "classic", "anthem"],
    ),
    (
        "Blue is the Colour",
        "Blue is the colour, football is the game,\nWe're all together and winning is our aim,\nSo cheer us on through the sun and rain,\n'Cause Chelsea, Chelsea is our name.\nSo cheer us on through the sun and rain,\n'Cause Chelsea, Chelsea is our name.",
        "Official Chelsea club song written by Daniel O'Donnell; played before home matches at Stamford Bridge.",
        ["anthem", "classic", "pre-match"],
    ),
    (
        "Celery",
        "Celery, celery,\nIf she don't come I'll stalk her,\nUp to the shed,\nStand her on her head,\nKeep the dampers down,\nThe blue flag flying, we're all off to Stamford Bridge.",
        "Historic Chelsea terrace chant; supporters often throw celery (now banned) during the song.",
        ["fan-chant", "historic", "shed-end"],
    ),
    (
        "Ten Men Went to Mow",
        "Ten men went to mow, went to mow a meadow,\nHeigh ho! The derry-o, ten men went to mow.\nNine men went to mow, went to mow a meadow,\nHeigh ho! The derry-o, nine men went to mow.\nEight men went to mow, went to mow a meadow,\nHeigh ho! The derry-o, eight men went to mow.",
        "Traditional counting song sung in the Shed End; counts down from ten men to one.",
        ["fan-chant", "classic", "shed-end"],
    ),
    (
        "Keep the Blue Flag Flying High",
        "Keep the blue flag flying high,\nHigh up in the sky,\nKeep the blue flag flying high,\nFor Chelsea, for Chelsea.",
        "Classic Chelsea terrace song celebrating the club's blue colours and identity.",
        ["fan-song", "classic"],
    ),
    (
        "We All Follow Chelsea",
        "We all follow Chelsea,\nOver land and sea and Leicester,\nWe all follow Chelsea,\nOn to victory.",
        "Core Chelsea call-and-response chant declaring support home and away.",
        ["fan-chant", "classic"],
    ),
    (
        "London is Blue",
        "London is blue, London is blue,\nTottenham Hotspur, you're in Division Two,\nOh London is blue, London is blue,\nArsenal go to pieces, QPR are shite.",
        "Terrace song asserting Chelsea's dominance in London and taunting local rivals.",
        ["fan-chant", "classic", "rivalry", "london"],
    ),
    (
        "Allez Allez Allez",
        "Allez, allez, allez,\nWe are Chelsea, super Chelsea,\nAllez, allez, allez.",
        "Adapted terrace chant popular at Stamford Bridge during European and domestic campaigns.",
        ["fan-chant", "modern", "european"],
    ),
    (
        "Chelsea Chelsea",
        "Chelsea, Chelsea, Chelsea, Chelsea,\nChelsea, Chelsea, Chelsea, Chelsea.",
        "Simple repetitive call chant used throughout Stamford Bridge.",
        ["fan-chant"],
    ),
    (
        "We Are Chelsea, Tra La La",
        "We are Chelsea, tra la la la la,\nWe are Chelsea, tra la la la la la la la.",
        "Simple call-and-response chant used around the ground.",
        ["fan-chant"],
    ),
    (
        "This Is Stamford Bridge",
        "This is Stamford Bridge,\nThis is Stamford Bridge,\nNo one wants to be here.",
        "Chant referencing Chelsea's home ground, echoing the famous Anfield tunnel sign.",
        ["fan-chant", "stamford-bridge"],
    ),
    (
        "Stamford Bridge Is Falling Down",
        "Stamford Bridge is falling down, falling down, falling down,\nStamford Bridge is falling down, my fair lady.",
        "Terrace adaptation of the nursery rhyme, sung during big home nights.",
        ["fan-chant", "stamford-bridge"],
    ),
    (
        "Shed End Chant",
        "We're the Shed End boys, we're the Shed End boys,\nWe're the Shed End boys, and we're going to make a noise.",
        "Chant from the historic Shed End stand, Chelsea's traditional home end.",
        ["fan-chant", "shed-end", "stadium"],
    ),
    (
        "We'll Never Be Mastered",
        "We'll never be mastered, never be mastered,\nWe'll never be mastered by you.",
        "Defiant terrace chant sung by Chelsea supporters home and away.",
        ["fan-chant", "classic"],
    ),
    (
        "One Club One Flag",
        "One club, one flag, one dream,\nChelsea, Chelsea, Chelsea.",
        "Modern identity chant celebrating unity among Chelsea supporters.",
        ["fan-chant", "modern"],
    ),
    (
        "Jose Mourinho Chant",
        "Jose Mourinho, Jose Mourinho,\nJose Mourinho, Jose Mourinho,\nOh, Jose Mourinho.",
        "Iconic chant for Jose Mourinho during his two trophy-laden spells as Chelsea manager.",
        ["manager-tribute", "mourinho", "legend"],
    ),
    (
        "The Special One",
        "The Special One, la la la la la,\nThe Special One, la la la la la la la.",
        "Chant referencing Mourinho's famous 'Special One' self-description at his Chelsea unveiling.",
        ["manager-tribute", "mourinho", "legend"],
    ),
    (
        "Antonio Conte Chant",
        "Antonio Conte, la la la la la,\nAntonio Conte, he leads the Blues.",
        "Tribute to Antonio Conte, who won the Premier League in his first season at Chelsea (2016-17).",
        ["manager-tribute", "conte"],
    ),
    (
        "Thomas Tuchel Chant",
        "Thomas Tuchel, he leads the Blues,\nThomas Tuchel, he leads the Blues.",
        "Chant for Thomas Tuchel, Chelsea manager during the 2021 Champions League triumph.",
        ["manager-tribute", "tuchel", "modern", "european"],
    ),
    (
        "Gianfranco Zola",
        "There's only one Gianfranco Zola, one Gianfranco Zola,\nThere's only one Gianfranco Zola.",
        "Tribute to Gianfranco Zola, beloved Chelsea forward and later assistant manager.",
        ["player-tribute", "legend", "zola"],
    ),
    (
        "Didier Drogba Is His Name",
        "His name is Didier Drogba, he plays for Chelsea,\nHe scores the goals, he makes the Shed End sing,\nHe plays on the left, he plays on the right,\nThat boy Drogba makes defenders look shite.",
        "Terrace tribute to Didier Drogba, Chelsea's greatest big-game striker.",
        ["player-tribute", "legend", "drogba"],
    ),
    (
        "Drogba La La La",
        "Drogba, la la la la la la,\nDidier Drogba, la la la la la la.",
        "Simple melody chant for Didier Drogba during his two Chelsea spells.",
        ["player-tribute", "legend", "drogba"],
    ),
    (
        "Super Frank Lampard",
        "Super Frank Lampard, la la la la la,\nSuper Frank Lampard, la la la la la la la.",
        "Iconic chant for Frank Lampard, Chelsea's all-time leading goalscorer from midfield.",
        ["player-tribute", "legend", "lampard"],
    ),
    (
        "There's Only One Frank Lampard",
        "There's only one Frank Lampard, one Frank Lampard,\nThere's only one Frank Lampard.",
        "Call-and-response tribute to Frank Lampard, later Chelsea manager.",
        ["player-tribute", "legend", "lampard"],
    ),
    (
        "John Terry Leader of the Blues",
        "John Terry, leader of the Blues,\nJohn Terry, leader of the Blues.",
        "Shed End chant honouring John Terry's captaincy and Chelsea loyalty.",
        ["player-tribute", "legend", "terry", "captain"],
    ),
    (
        "There's Only One John Terry",
        "There's only one John Terry, one John Terry,\nThere's only one John Terry.",
        "Direct terrace tribute to defender and captain John Terry.",
        ["player-tribute", "legend", "terry", "captain"],
    ),
    (
        "Eden Hazard Chant",
        "Hazard, Hazard, Hazard Hazard Hazard,\nEden Hazard, Hazard Hazard Hazard.",
        "Repetitive chant for Eden Hazard, Chelsea's talisman during the 2010s.",
        ["player-tribute", "legend", "hazard"],
    ),
    (
        "Hazard La La La",
        "Hazard, la la la la la la,\nEden Hazard, la la la la la la.",
        "Melody chant for Belgian winger Eden Hazard.",
        ["player-tribute", "legend", "hazard"],
    ),
    (
        "N'Golo Kante Chant",
        "N'Golo Kante, he sits in midfield,\nN'Golo Kante, he plays for Chelsea.",
        "Terrace tribute to N'Golo Kante, midfield engine of two Premier League titles.",
        ["player-tribute", "legend", "kante"],
    ),
    (
        "Kante He Runs All Day",
        "Kante, Kante, N'Golo Kante,\nHe runs all day, he runs all day.",
        "Chant celebrating Kante's extraordinary stamina and ball-winning ability.",
        ["player-tribute", "legend", "kante"],
    ),
    (
        "Cole Palmer Chant",
        "Cole Palmer, he plays for Chelsea,\nCole Palmer, he scores the goals.",
        "Tribute to Cole Palmer, academy graduate and key figure in Chelsea's modern era.",
        ["player-tribute", "palmer", "modern", "academy"],
    ),
    (
        "Cold Palmer",
        "Cold Palmer, Cold Palmer,\nCole Palmer, Cold Palmer.",
        "Playful nickname chant for Cole Palmer, a pun on his name and composure.",
        ["player-tribute", "palmer", "modern"],
    ),
    (
        "Ashley Cole Chant",
        "Ashley Cole, Ashley Cole,\nAshley Cole, Ashley Cole.",
        "Chant for Ashley Cole, one of the greatest left-backs in Premier League history.",
        ["player-tribute", "legend", "cole"],
    ),
    (
        "Petr Cech Chant",
        "Petr Cech, la la la la la la la la la,\nThe best goalkeeper in the world.",
        "Goalkeeper chant for Petr Cech, Chelsea's legendary number one.",
        ["player-tribute", "legend", "cech", "goalkeeper"],
    ),
    (
        "Joe Cole Chant",
        "Joe Cole, Joe Cole, running down the wing,\nJoe Cole, Joe Cole, running down the wing.",
        "Terrace song for winger Joe Cole during his Chelsea years.",
        ["player-tribute", "cole"],
    ),
    (
        "Claude Makelele",
        "Makelele, Makelele, Claude Makelele,\nMakelele, Makelele, Claude Makelele.",
        "Tribute to Claude Makelele, whose holding role was so influential it was named after him.",
        ["player-tribute", "legend", "makelele"],
    ),
    (
        "Michael Essien",
        "Michael Essien, he plays in midfield,\nMichael Essien, he plays for Chelsea.",
        "Chant for Ghanaian midfielder Michael Essien, known as 'The Bison'.",
        ["player-tribute", "essien"],
    ),
    (
        "Fernando Torres",
        "Fernando Torres, he plays for Chelsea,\nFernando Torres, he scores the goals.",
        "Chant for Fernando Torres, including his famous semi-final goal against Barcelona in 2012.",
        ["player-tribute", "torres", "european"],
    ),
    (
        "Thiago Silva Chant",
        "Thiago Silva, he plays at the back,\nThiago Silva, he plays for Chelsea.",
        "Chant for Brazilian centre-back Thiago Silva during his Chelsea spell.",
        ["player-tribute", "thiago-silva", "modern"],
    ),
    (
        "Mason Mount Chant",
        "Mason Mount, he wears the number ten,\nMason Mount, he plays for Chelsea.",
        "Tribute to academy graduate Mason Mount, key player in the 2021 Champions League win.",
        ["player-tribute", "mount", "modern", "academy"],
    ),
    (
        "Reece James Chant",
        "Reece James, he plays right-back,\nReece James, he plays for Chelsea.",
        "Chant for homegrown captain Reece James.",
        ["player-tribute", "james", "modern", "academy", "captain"],
    ),
    (
        "Munich 2012 Chant",
        "Munich, Munich, we won it all in Munich,\nMunich, Munich, we won it all in Munich.",
        "Chant celebrating Chelsea's first Champions League title, won in Munich in 2012.",
        ["fan-chant", "european", "2012", "champions-league"],
    ),
    (
        "Kings of Europe 2012",
        "We're the kings of Europe, kings of Europe,\nChelsea FC, we're the kings of Europe.",
        "Celebration chant for Chelsea's 2012 Champions League triumph over Bayern Munich.",
        ["fan-chant", "european", "2012", "champions-league"],
    ),
    (
        "Drogba Penalty Munich",
        "Drogba, Drogba, he scored in Munich,\nDrogba, Drogba, he scored in Munich.",
        "Chant immortalising Didier Drogba's winning penalty in the 2012 Champions League final.",
        ["player-tribute", "drogba", "european", "2012", "legend"],
    ),
    (
        "Champions of Europe",
        "Champions of Europe, champions of Europe,\nChelsea FC, champions of Europe.",
        "General European celebration chant sung after 2012 and 2021 triumphs.",
        ["fan-chant", "european", "champions-league"],
    ),
    (
        "Arsenal Taunt",
        "We hate Tottenham Hotspur, we hate Tottenham Hotspur,\nWe hate Tottenham Hotspur, but Arsenal are shite.",
        "Classic Chelsea rivalry chant mocking both North London clubs.",
        ["fan-chant", "rivalry", "arsenal", "banter"],
    ),
    (
        "Tottenham Taunt",
        "What a load of shite, what a load of shite,\nTottenham Hotspur, what a load of shite.",
        "Terrace taunt directed at Chelsea's North London rivals Tottenham Hotspur.",
        ["fan-chant", "rivalry", "tottenham", "banter"],
    ),
    (
        "Liverpool Taunt (2008)",
        "We won it twice at Anfield, we won it twice at Anfield,\nChelsea FC, we won it twice at Anfield.",
        "Banter chant referencing Chelsea's Champions League knockouts of Liverpool at Anfield.",
        ["fan-chant", "rivalry", "liverpool", "banter", "european"],
    ),
    (
        "Manchester United Taunt",
        "You're not singing anymore, you're not singing anymore,\nYou're not singing anymore, you're not singing anymore.",
        "Generic taunt often directed at Manchester United at Stamford Bridge.",
        ["fan-chant", "rivalry", "banter"],
    ),
    (
        "Who Are Ya",
        "Who are ya? Who are ya? Who are ya?",
        "Generic terrace taunt used by Chelsea fans toward opposition supporters.",
        ["fan-chant", "away", "banter"],
    ),
    (
        "You're Not Singing Anymore",
        "You're not singing anymore, you're not singing anymore,\nYou're not singing anymore, you're not singing anymore.",
        "Taunt sung when silencing an away end at Stamford Bridge.",
        ["fan-chant", "banter", "stadium"],
    ),
    (
        "Roman Abramovich Song",
        "Roman Abramovich, he eats his lunch in a solid gold bath,\nRoman Abramovich, he eats his lunch in a solid gold bath.",
        "Humorous terrace song about former owner Roman Abramovich during the trophy era.",
        ["fan-song", "legacy", "abramovich"],
    ),
]


def main():
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
                "tags": ["chant", "chelsea", *tags],
            }
        )

    out = ROOT / "data/song/chelsea_chants.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(songs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(songs)} Chelsea chants to {out}")


if __name__ == "__main__":
    main()
