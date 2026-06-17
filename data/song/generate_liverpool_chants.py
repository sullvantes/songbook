"""Generate data/song/liverpool_chants.json. Run: python data/song/generate_liverpool_chants.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLUB = "Liverpool FC"

# title, lyrics, description, tags
CHANTS = [
    (
        "You'll Never Walk Alone",
        "When you walk through a storm, hold your head up high,\nAnd don't be afraid of the dark.\nAt the end of a storm, there's a golden sky,\nAnd the sweet silver song of a lark.\nWalk on through the wind, walk on through the rain,\nThough your dreams be tossed and blown.\nWalk on, walk on, with hope in your heart,\nAnd you'll never walk alone.",
        "Liverpool's anthem, sung by the Kop before kickoff. Adapted from Rodgers and Hammerstein's Carousel.",
        ["anthem", "classic", "pre-match"],
    ),
    (
        "Fields of Anfield Road",
        "Outside the Safeway supermarket, I heard a Kopite moan,\nHe said we can't buy players when we're trying to build a home,\nBut I said we play the Liverpool way, we press and never tire,\nAnd when the Reds go marching in, we set the world on fire.",
        "Liverpool fan song sung to the tune of Fields of Athenry, about life around Anfield.",
        ["fan-song", "classic"],
    ),
    (
        "Poor Scouser Tommy",
        "Let me tell you the story of a poor boy,\nWho left his home in the Isle of Dogs,\nTo join a good ship and sail the world wide,\nBut he never returned to the Isle of Dogs.",
        "Traditional Liverpool folk song about a sailor from the Isle of Dogs; often sung on away trips.",
        ["fan-song", "classic", "folk"],
    ),
    (
        "Walk On",
        "Walk on, walk on, with hope in your heart,\nAnd you'll never walk alone.",
        "Refrain from You'll Never Walk Alone; sung throughout matches after the full anthem.",
        ["anthem", "classic"],
    ),
    (
        "In My Liverpool Home",
        "In my Liverpool home, in my Liverpool home,\nWe speak with an accent exceedingly rare,\nWe meet under a statue exceedingly bare,\nIf you want a cathedral, we've got one to spare,\nIn my Liverpool home.",
        "Comic Liverpool folk song celebrating the city's character.",
        ["fan-song", "folk"],
    ),
    (
        "Liverpool Lou",
        "Oh, Liverpool Lou, lovely Liverpool Lou,\nWhy don't you behave, love, like the others do?",
        "Traditional Merseyside folk song associated with Liverpool supporters.",
        ["fan-song", "folk"],
    ),
    (
        "The Leaving of Liverpool",
        "Farewell to Prince's Landing Pier,\nWhere many a pleasant hour I spent,\nI'm bound off for California,\nA place I know right well.",
        "Sea shanty and folk standard sung by Liverpool travelling support.",
        ["fan-song", "folk", "away"],
    ),
    (
        "We All Follow Liverpool",
        "We all follow Liverpool,\nOver land and sea and Leicester,\nWe all follow Liverpool,\nOn to victory.",
        "Core Liverpool call-and-response chant declaring support home and away.",
        ["fan-chant", "classic"],
    ),
    (
        "Oh Liverpool We Love You",
        "Oh Liverpool, we love you,\nWe do, oh Liverpool we love you, we do,\nOh Liverpool we love you, we do,\nAnd we love the Kop as well.",
        "Simple terrace song affirming support for the club and the Kop.",
        ["fan-chant"],
    ),
    (
        "The Liver Bird Upon My Chest",
        "I've got a Liver Bird upon my chest,\nOne nothing else will do,\nI've got a Liver Bird upon my chest,\n'Cause I'm a Liverpudlian through and through.",
        "Terrace song about wearing the Liver Bird crest with pride.",
        ["fan-chant", "classic"],
    ),
    (
        "This Is Anfield",
        "This is Anfield,\nThis is Anfield,\nNo one wants to be here.",
        "Chant referencing the famous This Is Anfield sign in the players' tunnel.",
        ["fan-chant", "anfield"],
    ),
    (
        "Allez Allez Allez",
        "Allez, allez, allez,\nWe are Liverpool, super Liverpool,\nAllez, allez, allez.",
        "Adapted terrace chant popularised during Liverpool's 2018 Champions League run.",
        ["fan-chant", "modern", "european"],
    ),
    (
        "Allez Les Rouges",
        "Allez les Rouges, allez les Rouges,\nAllez les Rouges.",
        "French-style chant for Liverpool's red kit ('the Reds').",
        ["fan-chant"],
    ),
    (
        "We Are Liverpool, Tra La La",
        "We are Liverpool, tra la la la la,\nWe are Liverpool, tra la la la la la la la.",
        "Simple repetitive call chant used on the Kop and around the ground.",
        ["fan-chant"],
    ),
    (
        "One Kiss",
        "One kiss is all it takes,\nFallin' in love with me...",
        "Dua Lipa song adopted by Liverpool fans during the 2018-19 title challenge.",
        ["fan-chant", "modern", "pop"],
    ),
    (
        "Ring of Fire",
        "Love is a burning thing,\nAnd it makes a fiery ring...",
        "Johnny Cash song adopted on the Kop, especially during big European nights.",
        ["fan-song", "terrace"],
    ),
    (
        "Every Other Tuesday",
        "Every other Tuesday, we work and we slouch,\nThe other day's for football, and going to the match...",
        "Humorous Liverpool song about European away nights and matchday routine.",
        ["fan-song", "european"],
    ),
    (
        "Pass and Move (It's the Liverpool Groove)",
        "Pass and move, pass and move, pass and move, pass and move,\nIt's the Liverpool groove, ba da da da da...",
        "1990s terrace song celebrating Liverpool's passing style.",
        ["fan-chant", "classic"],
    ),
    (
        "The Anfield Rap",
        "Anfield rap, we're the Liverpool crew...",
        "1980s novelty song by John Barnes and Craig Johnston; part of club folklore.",
        ["fan-song", "1980s", "novelty"],
    ),
    (
        "Justice for the 96",
        "Justice for the 96,\nJustice for the 96.",
        "Remembrance chant for the 97 victims of the Hillsborough disaster (96 plus later inquest).",
        ["remembrance", "hillsborough"],
    ),
    (
        "Istanbul 2005 Chant",
        "Istanbul, Istanbul, we won it five times,\nIstanbul, Istanbul, we won it five times...",
        "Chant celebrating Liverpool's fifth European Cup, won in Istanbul in 2005.",
        ["fan-chant", "european", "classic"],
    ),
    (
        "We Won It Six Times",
        "We won it six times, we won it six times,\nLiverpool FC, we won it six times.",
        "Chant celebrating Liverpool's sixth European Cup/Champions League title (2019).",
        ["fan-chant", "european", "modern"],
    ),
    (
        "Luis Garcia (Barcelona 2005)",
        "His name is Luis Garcia, he plays for Liverpool,\nHe came from Barcelona to Liverpool,\nHe plays on the left, he plays on the right,\nHe makes the Kop sing every night.",
        "Chant for Luis Garcia, especially remembered for the 'ghost goal' against Chelsea in 2005.",
        ["player-tribute", "european"],
    ),
    (
        "Corner Taken Quickly",
        "Corner taken quickly, ORIGI!",
        "Chant immortalising Divock Origi's goal against Barcelona in the 2019 Champions League semi-final.",
        ["fan-chant", "european", "modern", "origi"],
    ),
    (
        "Origi Against Barcelona",
        "Divock Origi, he scores the winning goal,\nDivock Origi, he scores the winning goal...",
        "Celebration song for Divock Origi's decisive goals in the 2019 Barcelona comeback.",
        ["player-tribute", "european", "origi"],
    ),
    (
        "Steve Gerrard Is His Name",
        "His name is Steven Gerrard, he wears the number eight,\nHis name is Steven Gerrard, he plays for Liverpool great...",
        "Terrace tribute to Steven Gerrard, Liverpool captain and club legend.",
        ["player-tribute", "legend", "gerrard"],
    ),
    (
        "Steven Gerrard Leader of the Kop",
        "Steven Gerrard, leader of the Kop,\nSteven Gerrard, leader of the Kop...",
        "Kop-end chant honouring Gerrard's leadership.",
        ["player-tribute", "legend", "gerrard"],
    ),
    (
        "We All Dream of a Team of Carraghers",
        "We all dream of a team of Carraghers,\nA team of Carraghers, a team of Carraghers...",
        "Jamie Carragher tribute sung to the tune of Just Can't Get Enough.",
        ["player-tribute", "legend", "carragher"],
    ),
    (
        "Jamie Carragher Is His Name",
        "His name is Jamie Carragher, he plays for Liverpool...",
        "Direct terrace tribute to defender Jamie Carragher.",
        ["player-tribute", "legend", "carragher"],
    ),
    (
        "Robbie Fowler God",
        "Worship to Fowler, God almighty Fowler,\nYou are the son of God, Robbie Fowler...",
        "Kop chant for Robbie Fowler, one of Liverpool's greatest natural goalscorers.",
        ["player-tribute", "legend", "fowler"],
    ),
    (
        "Ian Rush Scored 346",
        "Ian Rush scored 346,\nIan Rush scored 346...",
        "Chant celebrating Ian Rush's Liverpool goal-scoring record.",
        ["player-tribute", "legend", "rush"],
    ),
    (
        "King Kenny Dalglish",
        "Kenny Dalglish, King Kenny Dalglish,\nKenny Dalglish, King Kenny Dalglish...",
        "Chant for Kenny Dalglish as player and manager.",
        ["player-tribute", "legend", "dalglish"],
    ),
    (
        "John Barnes",
        "There's only one John Barnes, one John Barnes,\nThere's only one John Barnes...",
        "Tribute to winger John Barnes, key figure in Liverpool's 1980s success.",
        ["player-tribute", "legend", "barnes"],
    ),
    (
        "Michael Owen",
        "Michael Owen, Michael Owen, running down the wing...",
        "1990s/2000s terrace song for striker Michael Owen.",
        ["player-tribute", "owen"],
    ),
    (
        "Luis Suarez",
        "He plays on the left, he plays on the right,\nThat boy Suarez makes Messi look shite...",
        "2010s chant for Luis Suarez during his prolific Liverpool spell.",
        ["player-tribute", "suarez"],
    ),
    (
        "Fernando Torres",
        "His arse offends me, his arse offends me,\nFernando Torres, his arse offends me...",
        "Playful terrace song from Fernando Torres's Liverpool era.",
        ["player-tribute", "torres"],
    ),
    (
        "Dirk Kuyt",
        "Dirk Kuyt, Dirk Kuyt, running down the wing...",
        "Chant for Dutch forward Dirk Kuyt, known for relentless work rate.",
        ["player-tribute", "kuyt"],
    ),
    (
        "Peter Crouch",
        "He's taller than you, he's taller than you,\nPeter Crouch, he's taller than you...",
        "Terrace song for striker Peter Crouch referencing his height.",
        ["player-tribute", "crouch"],
    ),
    (
        "Xabi Alonso",
        "Xabi Alonso, he plays in midfield,\nXabi Alonso, he plays for Liverpool...",
        "Chant for Spanish midfielder Xabi Alonso.",
        ["player-tribute", "alonso"],
    ),
    (
        "Pepe Reina",
        "Pepe Reina, la la la la la la la la la la...",
        "Goalkeeper chant for Pepe Reina during his Anfield years.",
        ["player-tribute", "reina", "goalkeeper"],
    ),
    (
        "Si Senor (Firmino)",
        "Si senor, give the ball to Bobby Firmino,\nSi senor, give the ball to Bobby Firmino...",
        "Brazilian-themed chant for Roberto Firmino.",
        ["player-tribute", "firmino", "modern"],
    ),
    (
        "Si Senor (Henderson)",
        "Si senor, pass the ball to Jordan Henderson...",
        "Variant of Si Senor for captain Jordan Henderson.",
        ["player-tribute", "henderson", "modern"],
    ),
    (
        "Mo Salah (Egyptian King)",
        "Mo Salah, la la la la la la,\nIf he's good enough for you, he's good enough for me,\nIf he scores another few, then I'll be Muslim too...",
        "Iconic Mohamed Salah chant celebrating his goalscoring and global impact.",
        ["player-tribute", "salah", "modern", "legend"],
    ),
    (
        "Running Down the Wing (Salah)",
        "He's running down the wing, Salah la la la la la,\nThe Egyptian King, la la la la la...",
        "Alternative Mohamed Salah terrace melody.",
        ["player-tribute", "salah", "modern"],
    ),
    (
        "Sadio Mane",
        "Sadio Mane, running down the wing,\nSadio Mane, running down the wing...",
        "Chant for Senegalese forward Sadio Mane during the Klopp era.",
        ["player-tribute", "mane", "modern"],
    ),
    (
        "Mane Mane Mane",
        "Mane, Mane, Mane, Mane, Mane, Mane, Mane...",
        "Simple repetitive chant for Sadio Mane.",
        ["player-tribute", "mane", "modern"],
    ),
    (
        "Virgil van Dijk",
        "Oh Virgil van Dijk, oh Virgil van Dijk,\nVirgil van Dijk, he plays for Liverpool...",
        "Chant for centre-back Virgil van Dijk.",
        ["player-tribute", "vandijk", "modern"],
    ),
    (
        "Big Virg",
        "Big Virg, Big Virg, Big Virg...",
        "Nickname chant for Virgil van Dijk.",
        ["player-tribute", "vandijk", "modern"],
    ),
    (
        "Alisson Becker",
        "Alisson Becker, the goalkeeper,\nAlisson Becker, the best in the world...",
        "Chant for Brazilian goalkeeper Alisson Becker.",
        ["player-tribute", "alisson", "modern", "goalkeeper"],
    ),
    (
        "Trent Alexander-Arnold",
        "Trent Alexander-Arnold, he's our right-back,\nTrent Alexander-Arnold, he's our right-back...",
        "Homegrown right-back chant for Trent Alexander-Arnold.",
        ["player-tribute", "trent", "modern"],
    ),
    (
        "Andy Robertson",
        "Andy Robertson, he plays left-back,\nAndy Robertson, he plays for Liverpool...",
        "Chant for Scottish left-back Andy Robertson.",
        ["player-tribute", "robertson", "modern"],
    ),
    (
        "Fabinho",
        "Fabinho, Fabinho, Fabinho...",
        "Midfield destroyer chant for Fabinho.",
        ["player-tribute", "fabinho", "modern"],
    ),
    (
        "Diogo Jota",
        "Diogo Jota, he scores the goals,\nDiogo Jota, he plays for Liverpool...",
        "Tribute to Diogo Jota, tragically killed in 2024.",
        ["player-tribute", "jota", "modern", "remembrance"],
    ),
    (
        "Luis Diaz",
        "Luis Diaz, la la la la la,\nLuis Diaz, la la la la la...",
        "Chant for Colombian winger Luis Diaz.",
        ["player-tribute", "diaz", "modern"],
    ),
    (
        "Darwin Nunez",
        "Darwin Nunez, he plays for Liverpool,\nDarwin Nunez, he scores the goals...",
        "Chant for Uruguayan striker Darwin Nunez.",
        ["player-tribute", "nunez", "modern"],
    ),
    (
        "Alexis Mac Allister",
        "Alexis Mac Allister, he plays for Liverpool,\nWorld Cup winner, Alexis Mac Allister...",
        "Chant for Argentine midfielder Alexis Mac Allister.",
        ["player-tribute", "mac-allister", "modern"],
    ),
    (
        "Wataru Endo",
        "Wataru Endo, he sits in midfield,\nWataru Endo, he plays for Liverpool...",
        "Chant for Japanese midfielder Wataru Endo.",
        ["player-tribute", "endo", "modern"],
    ),
    (
        "Dominik Szoboszlai",
        "Szoboszlai, la la la la la,\nDominik Szoboszlai...",
        "Chant for Hungarian midfielder Dominik Szoboszlai.",
        ["player-tribute", "szoboszlai", "modern"],
    ),
    (
        "Curtis Jones",
        "Curtis Jones, he plays for the team,\nHe wears the number seventeen...",
        "Homegrown midfielder chant for Curtis Jones.",
        ["player-tribute", "curtis-jones", "modern", "academy"],
    ),
    (
        "Harvey Elliott",
        "Harvey Elliott, la la la la la...",
        "Chant for academy graduate Harvey Elliott.",
        ["player-tribute", "elliott", "modern", "academy"],
    ),
    (
        "Cody Gakpo",
        "Cody Gakpo, he plays for Liverpool...",
        "Chant for Dutch forward Cody Gakpo.",
        ["player-tribute", "gakpo", "modern"],
    ),
    (
        "Ibrahima Konate",
        "Ibrahima Konate, he plays at the back...",
        "Chant for French centre-back Ibrahima Konate.",
        ["player-tribute", "konate", "modern"],
    ),
    (
        "I'm So Glad Jurgen Klopp Is a Red",
        "I'm so glad, Jurgen Klopp is a Red,\nI'm so glad, he said fuck off to the Kop...",
        "Celebratory chant for manager Jurgen Klopp during the successful era.",
        ["manager-tribute", "klopp", "modern"],
    ),
    (
        "Jurgen Klopp La La La",
        "Jurgen Klopp, la la la la la la la la,\nJurgen Klopp, la la la la la la la la...",
        "Simple melody chant for Jurgen Klopp.",
        ["manager-tribute", "klopp", "modern"],
    ),
    (
        "The Normal One",
        "I'm the normal one, I'm the normal one...",
        "Reference to Klopp's famous 'I'm the normal one' introductory press conference.",
        ["manager-tribute", "klopp", "modern"],
    ),
    (
        "Arne Slot Chant",
        "Arne Slot, he leads the Reds,\nArne Slot, he leads the Reds...",
        "Chant for manager Arne Slot, Jurgen Klopp's successor.",
        ["manager-tribute", "slot", "modern"],
    ),
    (
        "Bill Shankly Song",
        "Shankly, Shankly, the name on every tongue,\nShankly, Shankly, he made the Kop sing...",
        "Tribute to legendary manager Bill Shankly, architect of modern Liverpool.",
        ["manager-tribute", "legend", "shankly"],
    ),
    (
        "Bob Paisley Song",
        "Bob Paisley, he won it all,\nBob Paisley, he won it all...",
        "Tribute to manager Bob Paisley, who won three European Cups.",
        ["manager-tribute", "legend", "paisley"],
    ),
    (
        "Scouser Tommy (Shankly Gates)",
        "Outside the Shankly Gates, I heard a Kopite moan...",
        "Variant of Poor Scouser Tommy referencing the Shankly Gates at Anfield.",
        ["fan-song", "anfield"],
    ),
    (
        "Let's Talk About Six Baby",
        "Let's talk about six, baby, let's talk about you and me,\nLet's talk about all the good things and the bad things that may be...",
        "Spice Girls parody celebrating Liverpool's sixth European Cup (2019).",
        ["fan-chant", "european", "modern", "parody"],
    ),
    (
        "Song 2 (Woo Hoo)",
        "Woo hoo, woo hoo...",
        "Blur's Song 2 riff frequently sung on the Kop during exciting passages of play.",
        ["fan-chant", "terrace", "pop"],
    ),
    (
        "We Can See You Waving",
        "We can see you waving, we can see you waving,\nYour arms are going mad, your arms are going mad...",
        "Away-end taunt sung by Liverpool fans to home supporters.",
        ["fan-chant", "away"],
    ),
    (
        "Who Are Ya",
        "Who are ya? Who are ya? Who are ya?",
        "Generic terrace taunt used by Liverpool fans toward opposition.",
        ["fan-chant", "away"],
    ),
    (
        "Where Do You Come From",
        "Where do you come from? Where do you come from?\nWhere do you come from, Liverpool?",
        "Call-and-response chant about Liverpool origins and identity.",
        ["fan-chant", "classic"],
    ),
    (
        "Red Men Chant",
        "We are the red men, mighty mighty red men...",
        "Terrace identity chant for Liverpool's red kit.",
        ["fan-chant"],
    ),
    (
        "Liverpool FC (Club Song)",
        "Liverpool FC, Liverpool FC,\nWe are the greatest team in history...",
        "General club pride chant.",
        ["fan-chant"],
    ),
    (
        "Georginio Wijnaldum",
        "Georginio Wijnaldum, he scores the goals...",
        "Chant for Dutch midfielder Georginio Wijnaldum, key in the 2019 Barcelona comeback.",
        ["player-tribute", "wijnaldum", "modern"],
    ),
    (
        "James Milner",
        "James Milner, he runs all day,\nJames Milner, he runs all day...",
        "Chant celebrating James Milner's extraordinary fitness and versatility.",
        ["player-tribute", "milner", "modern"],
    ),
    (
        "Naby Keita",
        "Naby Keita, he plays in midfield...",
        "Chant for Guinean midfielder Naby Keita.",
        ["player-tribute", "keita", "modern"],
    ),
    (
        "Joel Matip",
        "Joel Matip, he plays at the back...",
        "Chant for Cameroonian centre-back Joel Matip.",
        ["player-tribute", "matip", "modern"],
    ),
    (
        "Thiago Alcantara",
        "Thiago, Thiago, Thiago Alcantara...",
        "Chant for Spanish midfielder Thiago Alcantara.",
        ["player-tribute", "thiago", "modern"],
    ),
    (
        "Takumi Minamino",
        "Minamino, Minamino, Minamino...",
        "Chant for Japanese forward Takumi Minamino.",
        ["player-tribute", "minamino", "modern"],
    ),
    (
        "Kostas Tsimikas",
        "Kostas Tsimikas, he plays left-back...",
        "Chant for Greek left-back Kostas Tsimikas.",
        ["player-tribute", "tsimikas", "modern"],
    ),
    (
        "Ryan Gravenberch",
        "Ryan Gravenberch, he plays for Liverpool...",
        "Chant for Dutch midfielder Ryan Gravenberch.",
        ["player-tribute", "gravenberch", "modern"],
    ),
    (
        "Conor Bradley",
        "Conor Bradley, he plays right-back...",
        "Chant for Northern Irish academy graduate Conor Bradley.",
        ["player-tribute", "bradley", "modern", "academy"],
    ),
    (
        "Jarell Quansah",
        "Jarell Quansah, he plays at the back...",
        "Chant for homegrown centre-back Jarell Quansah.",
        ["player-tribute", "quansah", "modern", "academy"],
    ),
    (
        "Emile Heskey",
        "Emile Heskey, he scores the goals...",
        "Chant for striker Emile Heskey during his Liverpool years.",
        ["player-tribute", "heskey"],
    ),
    (
        "Steve McManaman",
        "McManaman, running down the wing...",
        "Chant for winger Steve McManaman, local boy and academy product.",
        ["player-tribute", "mcmanaman", "academy"],
    ),
    (
        "Dietmar Hamann",
        "Hamann, Hamann, Dietmar Hamann...",
        "Chant for German midfielder Dietmar Hamann, Istanbul 2005 hero.",
        ["player-tribute", "hamann", "european"],
    ),
    (
        "Jerzy Dudek",
        "Jerzy Dudek, he saved the day...",
        "Tribute to goalkeeper Jerzy Dudek's penalty shootout heroics in Istanbul 2005.",
        ["player-tribute", "dudek", "european", "goalkeeper"],
    ),
    (
        "Samuel Eto'o Mockery (2005 Final)",
        "Samuel Eto'o, he walks alone...",
        "Taunting chant from the 2005 Champions League final context.",
        ["fan-chant", "european", "banter"],
    ),
    (
        "Steven Gerrard Istanbul",
        "Steven Gerrard, he led the team,\nIn Istanbul, he fulfilled the dream...",
        "Celebrating Gerrard's role in the 2005 Champions League final comeback.",
        ["player-tribute", "gerrard", "european", "legend"],
    ),
    (
        "Champions League Dream",
        "We're Liverpool FC, we're going to win the Champions League...",
        "European campaign chant sung during knockout runs.",
        ["fan-chant", "european"],
    ),
    (
        "Goodison Park Taunt",
        "If you all hate Everton, clap your hands...",
        "Rivalry chant sung toward Everton; part of Merseyside derby culture.",
        ["fan-chant", "derby", "everton"],
    ),
    (
        "Poor Little Everton",
        "Poor little Everton, they haven't won a thing...",
        "Merseyside derby taunt referencing Everton's trophy drought.",
        ["fan-chant", "derby", "everton", "banter"],
    ),
    (
        "Manchester United Taunt",
        "You're not singing anymore, you're not singing anymore...",
        "Generic taunt often directed at Manchester United at Anfield.",
        ["fan-chant", "banter", "rivalry"],
    ),
    (
        "Chelsea Taunt (2005)",
        "Cheer up lads, you'll never walk alone...",
        "Ironic taunt sung to Chelsea after Liverpool's 2005 semi-final victory.",
        ["fan-chant", "banter", "european"],
    ),
    (
        "Fields of Athenry (Away Version)",
        "Low lie the fields of Anfield Road,\nWhere once we watched the great Bill Shankly...",
        "Away-end variant of the Fields of Athenry melody with Liverpool lyrics.",
        ["fan-song", "away", "classic"],
    ),
    (
        "Emre Can",
        "Emre Can, Emre Can, Emre Can...",
        "Chant for German midfielder Emre Can during his Liverpool spell.",
        ["player-tribute", "can"],
    ),
    (
        "Adam Lallana",
        "Adam Lallana, he plays for Liverpool,\nAdam Lallana, he plays for Liverpool...",
        "Chant for midfielder Adam Lallana in the Klopp era.",
        ["player-tribute", "lallana", "modern"],
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
                "tags": ["chant", "liverpool", *tags],
            }
        )

    out = ROOT / "data/song/liverpool_chants.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(songs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(songs)} Liverpool chants to {out}")


if __name__ == "__main__":
    main()
