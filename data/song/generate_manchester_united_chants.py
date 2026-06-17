"""Generate data/song/manchester_united_chants.json. Run: python data/song/generate_manchester_united_chants.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLUB = "Manchester United"

# title, lyrics, description, tags
CHANTS = [
    (
        "Glory Glory Man United",
        "Glory, glory, Man United,\nGlory, glory, Man United,\nGlory, glory, Man United,\nAs the Reds go marching on, on, on.",
        "Manchester United's signature anthem, sung throughout Old Trafford and on away trips.",
        ["anthem", "classic"],
    ),
    (
        "United Road",
        "United Road take me home,\nTo the place I belong,\nTo Old Trafford, to see United,\nUnited Road take me home.",
        "Fan song sung to the tune of Country Roads, celebrating the journey to Old Trafford.",
        ["fan-song", "classic", "old-trafford"],
    ),
    (
        "Sit Down Sit Down",
        "If you hate Man United stand up,\nIf you hate Man United stand up,\nIf you hate Man United, if you hate Man United,\nIf you hate Man United stand up.",
        "Terrace baiting chant sung to the tune of Blue Moon; invites rival fans to stand if they hate United.",
        ["fan-chant", "classic", "terrace"],
    ),
    (
        "Red Army",
        "We are the Red Army,\nMarching along,\nSinging our song,\nShouting together,\nWe are the Red Army.",
        "Identity chant for United's travelling support, known as the Red Army.",
        ["fan-chant", "classic", "away"],
    ),
    (
        "20 Times Champions",
        "20 times, 20 times, Man United,\n20 times I tell you, 20 times,\n20 times, 20 times, Man United,\nWe've won the League 20 times.",
        "Chant celebrating Manchester United's record 20 English league titles.",
        ["fan-chant", "classic", "trophy"],
    ),
    (
        "Theatre of Dreams",
        "This is the Theatre of Dreams,\nThis is the Theatre of Dreams,\nThis is the Theatre of Dreams,\nAnd we're gonna win today.",
        "Chant referencing Old Trafford's famous nickname, coined by Bobby Charlton.",
        ["fan-chant", "old-trafford", "classic"],
    ),
    (
        "Stretford End",
        "We're the Stretford End,\nWe're the Stretford End,\nWe're the Stretford End,\nAnd we're gonna sing our song.",
        "Chant from the Stretford End, United's historic home terrace at Old Trafford.",
        ["fan-chant", "old-trafford", "stretford-end"],
    ),
    (
        "We Are the Red Devils",
        "We are the Red Devils,\nMighty, mighty Red Devils,\nWe are the Red Devils,\nAnd we follow United.",
        "Terrace identity chant for Manchester United's Red Devils nickname.",
        ["fan-chant", "classic"],
    ),
    (
        "Manchester Is Red",
        "Manchester is red, Manchester is red,\nWe hate City, we hate Liverpool,\nManchester is red.",
        "Chant asserting United's dominance in Manchester and rivalry with City and Liverpool.",
        ["fan-chant", "rivalry", "classic"],
    ),
    (
        "George Best (The Belfast Boy)",
        "Georgie Best, Georgie Best,\nThe Belfast Boy,\nGeorgie Best, Georgie Best,\nThe greatest of them all.",
        "Tribute to George Best, United's dazzling 1960s winger and Ballon d'Or winner.",
        ["player-tribute", "legend", "best"],
    ),
    (
        "Ooh Aah Cantona",
        "Ooh aah Cantona,\nOoh aah Cantona,\nOoh aah Cantona,\nOoh aah Cantona.",
        "Iconic Eric Cantona chant from the 1990s; one of United's most enduring terrace songs.",
        ["player-tribute", "legend", "cantona"],
    ),
    (
        "Ryan Giggs Will Tear You Apart",
        "Ryan Giggs, Ryan Giggs,\nWill tear you apart again.",
        "Chant for Ryan Giggs sung to the tune of Joy Division's Love Will Tear Us Apart.",
        ["player-tribute", "legend", "giggs"],
    ),
    (
        "Paul Scholes From Fifty Yards",
        "Paul Scholes, he'll score you goals,\nPaul Scholes, from 50 yards.",
        "Terrace tribute celebrating Paul Scholes's long-range shooting and midfield mastery.",
        ["player-tribute", "legend", "scholes"],
    ),
    (
        "David Beckham",
        "Posh and Becks, Posh and Becks,\nDavid Beckham, he's the best,\nPosh and Becks, Posh and Becks,\nDavid Beckham, he's the best.",
        "1990s chant for David Beckham, United's iconic right midfielder and free-kick specialist.",
        ["player-tribute", "legend", "beckham"],
    ),
    (
        "Wayne Rooney (Running Down the Wing)",
        "Rooney, Rooney,\nRunning down the wing,\nRooney, Rooney,\nRunning down the wing.",
        "Terrace song for Wayne Rooney, United's record goalscorer.",
        ["player-tribute", "legend", "rooney"],
    ),
    (
        "Viva Ronaldo",
        "Viva Ronaldo,\nViva Ronaldo,\nViva Ronaldo,\nViva Ronaldo.",
        "Chant for Cristiano Ronaldo during his first spell at Old Trafford (2003-2009).",
        ["player-tribute", "legend", "ronaldo"],
    ),
    (
        "Stand Up If You Love Roy Keane",
        "Stand up if you love Roy Keane,\nStand up if you love Roy Keane,\nStand up if you love Roy Keane,\nStand up, stand up.",
        "Call-and-response tribute to captain Roy Keane, the heart of United's midfield dynasty.",
        ["player-tribute", "legend", "keane"],
    ),
    (
        "Sir Alex Ferguson",
        "There's only one Alex Ferguson,\nOne Alex Ferguson,\nThere's only one Alex Ferguson.",
        "Tribute to Sir Alex Ferguson, manager of United's 26-year trophy-laden era.",
        ["manager-tribute", "legend", "ferguson"],
    ),
    (
        "Marcus Rashford",
        "Rashford, la la la la la la la,\nRashford, la la la la la la la,\nIf he's good enough for you, he's good enough for me,\nIf he scores another few, then I'll be Mancunian too.",
        "Modern terrace chant for Marcus Rashford, adapted from the Mo Salah melody.",
        ["player-tribute", "rashford", "modern"],
    ),
    (
        "Bruno Fernandes",
        "Bruno, Bruno, Bruno Fernandes,\nFrom Sporting to United,\nBruno, Bruno, Bruno Fernandes,\nHe's our Portuguese jewel.",
        "Chant for Bruno Fernandes, United's creative midfield talisman since 2020.",
        ["player-tribute", "bruno-fernandes", "modern"],
    ),
    (
        "1999 Treble",
        "We've won the treble,\nWe've won the treble,\nManchester United,\nWe've won the treble.",
        "Celebration chant for United's historic 1998-99 treble of Premier League, FA Cup, and Champions League.",
        ["fan-chant", "treble", "1999", "classic"],
    ),
    (
        "One Nil to United (Solskjaer)",
        "One nil to United, one nil to United,\nOle Gunnar Solskjaer, one nil to United.",
        "Chant immortalising Ole Gunnar Solskjaer's injury-time winner in the 1999 Champions League final.",
        ["player-tribute", "solskjaer", "1999", "treble", "european"],
    ),
    (
        "Manchester City Taunt (Blue Moon)",
        "Blue Moon, you saw me standing alone,\nWithout a dream in my heart,\nWithout a trophy of my own.",
        "Rivalry taunt sung to Manchester City's Blue Moon anthem, mocking their trophy drought.",
        ["fan-chant", "rivalry", "manchester-city", "banter"],
    ),
    (
        "Bertie's Got a City",
        "Bertie's got a City, City, City,\nBertie's got a City on his head.",
        "Classic Manchester derby taunt referencing City's perceived inferiority to United.",
        ["fan-chant", "rivalry", "manchester-city", "derby", "banter"],
    ),
    (
        "Going Down Liverpool",
        "Going down, going down, so are Liverpool,\nGoing down, going down, so are Liverpool,\nIf you hate Liverpool, clap your hands.",
        "Rivalry chant directed at Liverpool, often sung during title races or relegation battles.",
        ["fan-chant", "rivalry", "liverpool", "banter"],
    ),
    (
        "Arsenal Taunt (What Were You Thinking)",
        "What were you thinking, what were you thinking,\nSigning Emmanuel Adebayor?",
        "Banter chant aimed at Arsenal, referencing Adebayor's move to Manchester City.",
        ["fan-chant", "rivalry", "arsenal", "banter"],
    ),
    (
        "Leeds United Taunt",
        "We all hate Leeds Scum, we all hate Leeds Scum,\nWe all hate Leeds Scum.",
        "Rivalry chant against Leeds United, one of English football's fiercest historic rivalries.",
        ["fan-chant", "rivalry", "leeds", "banter"],
    ),
    (
        "We're Man United Sing What We Want",
        "We're Man United, we'll sing what we want,\nWe're Man United, we'll sing what we want.",
        "Defiant away-end chant asserting United fans' right to sing anywhere.",
        ["fan-chant", "away", "classic"],
    ),
    (
        "You're Not Singing Anymore",
        "You're not singing anymore, you're not singing anymore,\nYour team's going home, your team's going home.",
        "Generic terrace taunt used by United fans when silencing opposition supporters.",
        ["fan-chant", "away", "banter"],
    ),
    (
        "Who Are Ya",
        "Who are ya? Who are ya? Who are ya?",
        "Standard away-end taunt directed at opposition fans whose team is losing.",
        ["fan-chant", "away", "banter"],
    ),
    (
        "Bobby Charlton",
        "Bobby Charlton, Bobby Charlton,\nThe greatest Red of all,\nBobby Charlton, Bobby Charlton,\nHe never took a fall.",
        "Tribute to Sir Bobby Charlton, 1968 European Cup winner and England World Cup hero.",
        ["player-tribute", "legend", "charlton"],
    ),
    (
        "Bryan Robson (Captain Marvel)",
        "Captain Marvel, Captain Marvel,\nBryan Robson, Captain Marvel.",
        "Chant for Bryan Robson, United's inspirational captain through the 1980s and early 1990s.",
        ["player-tribute", "legend", "robson"],
    ),
    (
        "Denis Law (The King)",
        "Denis Law, Denis Law,\nThe King of Old Trafford,\nDenis Law, Denis Law,\nThe King of Old Trafford.",
        "Tribute to Denis Law, the Lawman, one of United's greatest strikers of the 1960s.",
        ["player-tribute", "legend", "law"],
    ),
    (
        "Ole Gunnar Solskjaer (Baby-Faced Assassin)",
        "Ole, Ole, Ole Gunnar Solskjaer,\nOle, Ole, Ole Gunnar Solskjaer.",
        "Celebratory chant for Ole Gunnar Solskjaer, super-sub and 1999 Champions League hero.",
        ["player-tribute", "solskjaer", "1999", "legend"],
    ),
    (
        "Peter Schmeichel",
        "Schmeichel, Schmeichel,\nStanding on the wall,\nSchmeichel, Schmeichel,\nHe's the best of all.",
        "Tribute to Peter Schmeichel, United's legendary Danish goalkeeper of the 1990s dynasty.",
        ["player-tribute", "legend", "schmeichel", "goalkeeper"],
    ),
    (
        "Rio Ferdinand",
        "Rio Ferdinand, he plays at the back,\nRio Ferdinand, he's the best in the land.",
        "Chant for Rio Ferdinand, commanding centre-back of the Ferguson era.",
        ["player-tribute", "ferdinand", "modern"],
    ),
    (
        "Nemanja Vidic",
        "Vidic, Vidic, Nemanja Vidic,\nVidic, Vidic, he'll break your legs.",
        "Terrace tribute to Nemanja Vidic, United's fearsome Serbian centre-back.",
        ["player-tribute", "vidic", "modern"],
    ),
    (
        "Rio and Vida (Defence Partnership)",
        "Rio and Vida, Rio and Vida,\nRio and Vida, the best in the land.",
        "Chant celebrating the Rio Ferdinand and Nemanja Vidic centre-back partnership.",
        ["player-tribute", "ferdinand", "vidic", "modern"],
    ),
    (
        "Patrice Evra",
        "Patrice Evra, he plays left-back,\nPatrice Evra, he plays for United.",
        "Chant for French left-back Patrice Evra, a key member of multiple title-winning sides.",
        ["player-tribute", "evra", "modern"],
    ),
    (
        "Park Ji-sung",
        "Park Ji-sung, he runs all day,\nPark Ji-sung, he runs all day.",
        "Tribute to Park Ji-sung, the tireless South Korean midfielder beloved at Old Trafford.",
        ["player-tribute", "park-ji-sung", "modern"],
    ),
    (
        "Edwin van der Sar",
        "Edwin van der Sar, the goalkeeper,\nEdwin van der Sar, the best in the world.",
        "Chant for Dutch goalkeeper Edwin van der Sar, United's No. 1 from 2005 to 2011.",
        ["player-tribute", "van-der-sar", "modern", "goalkeeper"],
    ),
    (
        "Dwight Yorke",
        "Dwight Yorke, he scores the goals,\nDwight Yorke, he plays for United.",
        "Tribute to Dwight Yorke, prolific striker and key figure in the 1999 treble season.",
        ["player-tribute", "yorke", "1999", "treble"],
    ),
    (
        "Faith in Youth",
        "Faith, faith in youth,\nUnited have got faith in youth,\nFaith, faith in youth,\nUnited have got faith in youth.",
        "Chant celebrating United's tradition of developing young players through the academy.",
        ["fan-chant", "academy", "classic"],
    ),
    (
        "The Busby Babes",
        "The Busby Babes were glorious,\nThe Busby Babes were glorious,\nThe Busby Babes were glorious,\nAnd they never will be forgotten.",
        "Remembrance chant for the Busby Babes, United's young team tragically lost in the 1958 Munich air disaster.",
        ["remembrance", "busby-babes", "classic"],
    ),
    (
        "Flowers of Manchester",
        "The flowers of Manchester lay sleeping,\nIn the cold, dark earth, in the rain,\nAnd the flowers of Manchester united,\nWill bloom and bloom again.",
        "Solemn song commemorating the Munich air disaster of 6 February 1958.",
        ["remembrance", "busby-babes", "folk"],
    ),
    (
        "Three European Cups",
        "We've won it three times, we've won it three times,\nManchester United, we've won it three times.",
        "Chant celebrating United's three European Cup/Champions League titles before 2008.",
        ["fan-chant", "european", "classic"],
    ),
    (
        "Champions of Europe (1968)",
        "Champions of Europe, champions of Europe,\nManchester United, champions of Europe.",
        "Celebration of United's first European Cup triumph at Wembley in 1968 under Matt Busby.",
        ["fan-chant", "european", "1968", "classic"],
    ),
    (
        "Follow Follow Man United",
        "Follow, follow, follow,\nFollow Man United,\nFollow, follow, follow,\nOn to victory.",
        "Core call-and-response chant declaring support for United home and away.",
        ["fan-chant", "classic", "away"],
    ),
    (
        "Come On You Reds",
        "Come on you Reds, come on you Reds,\nCome on you Reds, come on you Reds.",
        "Simple repetitive terrace chant urging United on during matches.",
        ["fan-chant", "classic"],
    ),
    (
        "We Love United",
        "We love United, we do,\nOh United we love you, we do,\nOh United we love you, we do,\nAnd we follow United through and through.",
        "Terrace song affirming lifelong support for Manchester United.",
        ["fan-chant", "classic"],
    ),
    (
        "Old Trafford Bound",
        "We're going up to Old Trafford,\nWe're going up to Old Trafford,\nWe're going up to Old Trafford,\nTo see United win.",
        "Matchday chant sung by fans heading to the Theatre of Dreams.",
        ["fan-chant", "old-trafford", "matchday"],
    ),
    (
        "Everywhere We Go",
        "Everywhere we go,\nPeople want to know,\nWho we are,\nSo we tell them,\nWe are United, mighty mighty United.",
        "Away-day chant introducing United's travelling support to rival grounds.",
        ["fan-chant", "away", "classic"],
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
                "tags": ["chant", "manchester-united", *tags],
            }
        )

    out = ROOT / "data/song/manchester_united_chants.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(songs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(songs)} Manchester United chants to {out}")


if __name__ == "__main__":
    main()
