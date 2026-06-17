"""Generate data/song/arsenal_chants.json. Run: python data/song/generate_arsenal_chants.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLUB = "Arsenal FC"

# title, lyrics, description, tags
CHANTS = [
    (
        "Good Old Arsenal",
        "Good old Arsenal is proud to say,\nThat we are the best team the world has ever seen,\nWe are the best team the world has ever seen,\nAnd it's Arsenal, Arsenal FC,\nWe're by far the greatest team the world has ever seen.",
        "Arsenal's official club song, released in 1971 and still sung before home matches.",
        ["anthem", "classic", "pre-match"],
    ),
    (
        "One Nil to the Arsenal",
        "One nil to the Arsenal, one nil to the Arsenal,\nOne nil to the Arsenal, one nil to the Arsenal.",
        "Iconic terrace chant sung to the tune of Go West; celebrates Arsenal's reputation for 1-0 wins.",
        ["fan-chant", "classic", "terrace"],
    ),
    (
        "Hot Stuff",
        "Hot stuff baby this evening,\nBaby needs a goal, and I'm in need of a win,\nHot stuff baby this evening,\nGonna get my way, gonna get a win.",
        "Donna Summer adaptation sung on the terraces, especially during tense matches.",
        ["fan-chant", "classic", "terrace", "pop"],
    ),
    (
        "We Are the Gooners",
        "We are the Gooners, the mighty mighty Gooners,\nWe are the Gooners, from Highbury.",
        "Core identity chant for Arsenal supporters, referencing the Gooner nickname and old ground.",
        ["fan-chant", "classic", "gooners"],
    ),
    (
        "North London Forever",
        "North London forever, whatever the weather,\nThese colours must never fade,\nNo matter the reason, no matter the season,\nThese colours must never fade.",
        "Modern Arsenal anthem celebrating North London identity and the red-and-white colours.",
        ["anthem", "modern", "north-london"],
    ),
    (
        "Victoria Concordia Crescit",
        "Victoria Concordia Crescit,\nVictory through harmony.",
        "Chant referencing Arsenal's Latin motto, meaning 'Victory Through Harmony'.",
        ["fan-chant", "classic", "motto"],
    ),
    (
        "49 Unbeaten",
        "Forty-nine, forty-nine unbeaten,\nForty-nine, forty-nine unbeaten,\nWe won the league without losing.",
        "Chant celebrating the Invincibles' 49-match unbeaten run in the 2003-04 title season.",
        ["fan-chant", "classic", "invincibles"],
    ),
    (
        "The Invincibles",
        "We are the Invincibles, the mighty mighty Invincibles,\nWe are the Invincibles, from Highbury.",
        "Terrace song honouring the unbeaten 2003-04 Premier League champions.",
        ["fan-chant", "classic", "invincibles"],
    ),
    (
        "Thierry Henry Is His Name",
        "His name is Thierry Henry, Thierry Henry,\nHis name is Thierry Henry, he plays for Arsenal.",
        "Classic terrace tribute to Thierry Henry, Arsenal's all-time leading goalscorer.",
        ["player-tribute", "legend", "henry"],
    ),
    (
        "Thierry Henry (Va Va Voom)",
        "Thierry Henry, Thierry Henry, Thierry Henry,\nVa va voom, va va voom.",
        "Celebratory chant for Thierry Henry, referencing his famous 'va va voom' catchphrase.",
        ["player-tribute", "legend", "henry"],
    ),
    (
        "Dennis Bergkamp",
        "Dennis Bergkamp, Dennis Bergkamp, Dennis Bergkamp,\nNumber ten, number ten.",
        "Tribute to Dutch forward Dennis Bergkamp, one of Arsenal's greatest ever players.",
        ["player-tribute", "legend", "bergkamp"],
    ),
    (
        "There's Only One Tony Adams",
        "There's only one Tony Adams, one Tony Adams,\nThere's only one Tony Adams.",
        "Terrace chant for captain Tony Adams, leader of the famous back four.",
        ["player-tribute", "legend", "adams"],
    ),
    (
        "Ian Wright",
        "Wrighty, Wrighty, Wrighty, Wrighty,\nIan Wright, Ian Wright.",
        "Kop-end style chant for striker Ian Wright, Arsenal legend and club record holder before Henry.",
        ["player-tribute", "legend", "wright"],
    ),
    (
        "Patrick Vieira",
        "Vieira, Vieira, Vieira, Vieira,\nPatrick Vieira, Patrick Vieira.",
        "Midfield general chant for Patrick Vieira, captain of the Wenger era's greatest teams.",
        ["player-tribute", "legend", "vieira"],
    ),
    (
        "Bukayo Saka",
        "Bukayo Saka, he plays on the right,\nBukayo Saka, his future's looking bright.",
        "Modern homegrown hero chant for Bukayo Saka, academy graduate and England star.",
        ["player-tribute", "saka", "modern", "academy"],
    ),
    (
        "Martin Odegaard",
        "Martin Odegaard, he's our Norwegian prince,\nMartin Odegaard, he plays for Arsenal.",
        "Chant for captain Martin Odegaard, Arsenal's creative midfield leader.",
        ["player-tribute", "odegaard", "modern"],
    ),
    (
        "Declan Rice",
        "Declan Rice, Declan Rice, Declan Rice,\nHe sits in midfield, he sits in midfield.",
        "Terrace song for England midfielder Declan Rice, signed from West Ham in 2023.",
        ["player-tribute", "rice", "modern"],
    ),
    (
        "There's Only One Arsene Wenger",
        "There's only one Arsene Wenger, one Arsene Wenger,\nThere's only one Arsene Wenger.",
        "Tribute to legendary manager Arsene Wenger, who managed Arsenal for 22 years.",
        ["manager-tribute", "legend", "wenger"],
    ),
    (
        "Arsene Wenger (One Arsene Wenger)",
        "One Arsene Wenger, there's only one Arsene Wenger,\nOne Arsene Wenger, there's only one Arsene Wenger.",
        "Alternative Wenger chant sung during his long reign at Highbury and the Emirates.",
        ["manager-tribute", "legend", "wenger"],
    ),
    (
        "What Do You Think of Tottenham?",
        "What do you think of Tottenham? Shit!\nWhat do you think of Tottenham? Shit!\nWhat do you think of Tottenham? Shit!\nWhat do you think of Tottenham? Shit!",
        "Classic North London derby call-and-response chant directed at Tottenham Hotspur.",
        ["fan-chant", "derby", "tottenham", "north-london"],
    ),
    (
        "Stand Up If You Love the Arsenal",
        "Stand up if you love the Arsenal,\nStand up if you love the Arsenal.",
        "Simple terrace call chant used to rouse the home support at the Emirates.",
        ["fan-chant", "classic", "terrace"],
    ),
    (
        "Arsenal Till I Die",
        "Arsenal till I die, I know I am,\nI'm Arsenal till I die, I know I am, I know I am.",
        "Loyalty chant sung to the tune of Bread of Heaven, declaring lifelong support.",
        ["fan-chant", "classic"],
    ),
    (
        "Red and White Army",
        "We are the Red and White Army, the mighty mighty Red and White Army,\nWe are the Red and White Army, from Highbury.",
        "Identity chant celebrating Arsenal's red and white colours.",
        ["fan-chant", "classic"],
    ),
    (
        "Over Land and Sea and Tottenham",
        "We all follow Arsenal, over land and sea and Tottenham,\nWe all follow Arsenal, on to victory.",
        "Core support chant declaring allegiance home, away, and over local rivals.",
        ["fan-chant", "classic", "tottenham"],
    ),
    (
        "We Hate Tottenham",
        "We hate Tottenham, we hate Tottenham,\nWe hate Tottenham, and we hate Tottenham.",
        "North London derby chant expressing the long-standing rivalry with Spurs.",
        ["fan-chant", "derby", "tottenham", "north-london"],
    ),
    (
        "Where's Your European Cup?",
        "Where's your European Cup? Where's your European Cup?\nWhere's your European Cup? Where's your European Cup?",
        "Derby taunt referencing Tottenham's lack of a European Cup/Champions League title.",
        ["fan-chant", "derby", "tottenham", "banter"],
    ),
    (
        "Spurs Are on Their Way to Wembley",
        "Spurs are on their way to Wembley, Spurs are on their way to Wembley,\nThey've won it twice, they've won it twice, and the Emirates is shite.",
        "Banter chant mocking Tottenham's temporary Wembley spell and trophy record.",
        ["fan-chant", "derby", "tottenham", "banter"],
    ),
    (
        "Highbury",
        "Highbury, Highbury, Highbury,\nWe will never forget you.",
        "Nostalgic chant for Arsenal's former home, Highbury, closed in 2006.",
        ["fan-chant", "classic", "highbury"],
    ),
    (
        "The Clock End",
        "The Clock End, the Clock End, the Clock End,\nWe are the Clock End army.",
        "Chant referencing the famous Clock End stand at Highbury, now echoed at the Emirates.",
        ["fan-chant", "classic", "highbury"],
    ),
    (
        "North Bank",
        "North Bank, la la la la la,\nNorth Bank, la la la la la.",
        "Chant for the North Bank, the vocal heart of the Highbury and Emirates support.",
        ["fan-chant", "classic", "highbury"],
    ),
    (
        "Emirates Stadium",
        "This is the Emirates, this is the Emirates,\nNo one wants to be here.",
        "Chant referencing the Emirates Stadium, parodying the intimidating home atmosphere.",
        ["fan-chant", "emirates", "modern"],
    ),
    (
        "We Love You Arsenal",
        "We love you Arsenal, we do,\nWe love you Arsenal, we do,\nWe love you Arsenal, we do,\nAnd the North Bank loves you too.",
        "Simple terrace song affirming support for the club and the North Bank faithful.",
        ["fan-chant", "classic"],
    ),
    (
        "We've Got the Whole World in Our Hands",
        "We've got the whole world in our hands,\nWe've got the whole wide world in our hands.",
        "Spiritual adapted as an Arsenal celebration chant during title challenges.",
        ["fan-song", "classic", "terrace"],
    ),
    (
        "She Wears a Red and White Shirt",
        "She wears a red and white shirt, red and white shirt,\nRed and white shirt, she wears a red and white shirt,\nAnd she knows her Arsenal.",
        "Terrace song celebrating female Arsenal supporters and club colours.",
        ["fan-song", "classic"],
    ),
    (
        "Keep the Faith",
        "Keep the faith, keep the faith, keep the faith,\nWe are Arsenal.",
        "Encouraging chant sung during difficult periods, urging supporters to stay loyal.",
        ["fan-chant", "classic"],
    ),
    (
        "We're the North London Side",
        "We're the North London side, the Emirates side,\nWe're the North London side, the Emirates side.",
        "Identity chant asserting Arsenal's North London roots at the Emirates Stadium.",
        ["fan-chant", "north-london", "emirates"],
    ),
    (
        "Robert Pires",
        "Robert Pires, Robert Pires, Robert Pires,\nRunning down the wing.",
        "Tribute to French winger Robert Pires, key member of the Invincibles.",
        ["player-tribute", "legend", "pires", "invincibles"],
    ),
    (
        "Freddie Ljungberg",
        "Freddie Ljungberg, he wears red hair,\nFreddie Ljungberg, he plays for Arsenal.",
        "Chant for Swedish winger Freddie Ljungberg, known for his distinctive red hair.",
        ["player-tribute", "legend", "ljungberg", "invincibles"],
    ),
    (
        "Sol Campbell",
        "Sol Campbell, Sol Campbell, Sol Campbell,\nHe left Tottenham for Arsenal.",
        "Controversial tribute to Sol Campbell, who crossed the North London divide in 2001.",
        ["player-tribute", "legend", "campbell", "north-london"],
    ),
    (
        "David Seaman",
        "David Seaman, David Seaman, David Seaman,\nThe best goalkeeper in the land.",
        "Chant for goalkeeper David Seaman, Arsenal's number one through the 1990s and early 2000s.",
        ["player-tribute", "legend", "seaman", "goalkeeper"],
    ),
    (
        "Lee Dixon",
        "Lee Dixon, Lee Dixon, Lee Dixon,\nRight-back, right-back.",
        "Tribute to full-back Lee Dixon, part of Arsenal's famous defensive unit.",
        ["player-tribute", "legend", "dixon"],
    ),
    (
        "Nigel Winterburn",
        "Nigel Winterburn, Nigel Winterburn,\nLeft-back, left-back.",
        "Chant for left-back Nigel Winterburn, a mainstay of the Wenger revolution.",
        ["player-tribute", "legend", "winterburn"],
    ),
    (
        "Ray Parlour",
        "Ray Parlour, Ray Parlour, Ray Parlour,\nThe Romford Pele.",
        "Tribute to midfielder Ray Parlour, nicknamed the Romford Pele for his work rate.",
        ["player-tribute", "legend", "parlour"],
    ),
    (
        "Robin van Persie",
        "Robin van Persie, he scores the goals,\nRobin van Persie, he plays for Arsenal.",
        "Chant for Dutch striker Robin van Persie during his prolific Arsenal years.",
        ["player-tribute", "van-persie"],
    ),
    (
        "Cesc Fabregas",
        "Cesc Fabregas, he plays in midfield,\nCesc Fabregas, he plays for Arsenal.",
        "Tribute to Spanish midfielder Cesc Fabregas, academy graduate and future captain.",
        ["player-tribute", "fabregas", "academy"],
    ),
    (
        "Jack Wilshere",
        "Jack Wilshere, Jack Wilshere, Jack Wilshere,\nHe's one of our own.",
        "Homegrown midfielder chant for Jack Wilshere, Hale End academy product.",
        ["player-tribute", "wilshere", "academy"],
    ),
    (
        "Alexis Sanchez",
        "Alexis Sanchez, he plays on the left,\nAlexis Sanchez, he's the best.",
        "Chant for Chilean forward Alexis Sanchez during his prolific 2014-2018 spell.",
        ["player-tribute", "sanchez"],
    ),
    (
        "Pierre-Emerick Aubameyang",
        "Aubameyang, Aubameyang, Aubameyang,\nHe scores the goals.",
        "Terrace song for striker Pierre-Emerick Aubameyang, Golden Boot winner.",
        ["player-tribute", "aubameyang"],
    ),
    (
        "Gabriel Jesus",
        "Gabriel Jesus, he plays for Arsenal,\nGabriel Jesus, he scores the goals.",
        "Chant for Brazilian striker Gabriel Jesus, signed from Manchester City.",
        ["player-tribute", "jesus", "modern"],
    ),
    (
        "Gabriel Magalhaes",
        "Gabriel, Gabriel, Gabriel Magalhaes,\nHe plays at the back.",
        "Chant for Brazilian centre-back Gabriel Magalhaes.",
        ["player-tribute", "gabriel", "modern"],
    ),
    (
        "William Saliba",
        "William Saliba, he plays at the back,\nWilliam Saliba, he's the best in France.",
        "Tribute to French centre-back William Saliba, Hale End graduate.",
        ["player-tribute", "saliba", "modern", "academy"],
    ),
    (
        "Kai Havertz",
        "Kai Havertz, he plays for Arsenal,\nKai Havertz, he scores the goals.",
        "Chant for German forward Kai Havertz, signed from Chelsea in 2023.",
        ["player-tribute", "havertz", "modern"],
    ),
    (
        "Mikel Arteta Chant",
        "Mikel Arteta, he leads the team,\nMikel Arteta, he plays the Arsenal way.",
        "Chant for manager Mikel Arteta, former captain and Invincibles midfielder.",
        ["manager-tribute", "arteta", "modern"],
    ),
    (
        "Double Winners 1971",
        "Nineteen seventy-one, we won the Double,\nNineteen seventy-one, we won the Double.",
        "Chant celebrating Arsenal's first league and FA Cup double in 1970-71.",
        ["fan-chant", "classic", "history"],
    ),
    (
        "FA Cup Kings",
        "Fourteen times we've won the FA Cup,\nFourteen times we've won the FA Cup.",
        "Chant celebrating Arsenal's record FA Cup haul.",
        ["fan-chant", "classic", "fa-cup"],
    ),
    (
        "Wenger Out (Irony)",
        "We want Wenger out, we want Wenger out,\nWe want Wenger out, and then we want him back.",
        "Ironic terrace song from the later Wenger years, sung affectionately by supporters.",
        ["fan-chant", "banter", "wenger"],
    ),
    (
        "Fields of Highbury",
        "Low lie the fields of Highbury,\nWhere once we watched the great Arsene Wenger.",
        "Fan song sung to the tune of Fields of Athenry, nostalgic for the old ground.",
        ["fan-song", "classic", "highbury"],
    ),
    (
        "Allez Allez Allez (Arsenal)",
        "Allez, allez, allez,\nWe are Arsenal, super Arsenal,\nAllez, allez, allez.",
        "European-style terrace chant adopted by Arsenal fans during European campaigns.",
        ["fan-chant", "modern", "european"],
    ),
    (
        "Who Are Ya",
        "Who are ya? Who are ya? Who are ya?",
        "Generic terrace taunt used by Arsenal fans toward opposition supporters.",
        ["fan-chant", "away", "banter"],
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
                "tags": ["chant", "arsenal", *tags],
            }
        )

    out = ROOT / "data/song/arsenal_chants.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(songs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(songs)} Arsenal chants to {out}")


if __name__ == "__main__":
    main()
