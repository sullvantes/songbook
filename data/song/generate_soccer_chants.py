"""Generate data/song/soccer_chants.json. Run: python data/song/generate_soccer_chants.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID_CLUBS = {
    c["name"]
    for c in json.loads((ROOT / "data/club/clubs.json").read_text())
    + json.loads((ROOT / "data/club/world_cup_teams.json").read_text())
}

# title, clubs (list or empty), lyrics, description, extra_tags
CHANTS = [
    ("You'll Never Walk Alone", ["Liverpool FC", "Celtic FC", "Borussia Dortmund", "Feyenoord"], "When you walk through a storm, hold your head up high...", "Anthem adapted from Carousel; sung at Liverpool, Celtic, Dortmund, Feyenoord and others.", ["anthem", "classic"]),
    ("Ole Ole Ole", [], "Ole, ole, ole ole! Ole, ole!", "Universal victory chant heard in stadiums worldwide.", ["global"]),
    ("Seven Nation Army", [], "Oh, oh, oh, oh oh oh oh... (White Stripes riff)", "White Stripes riff adopted by fans globally.", ["global"]),
    ("Allez Allez Allez", ["Liverpool FC", "Chelsea FC"], "Allez, allez, allez...", "Adapted terrace chant used by many clubs including Liverpool and Chelsea.", ["fan-chant"]),
    ("Vamos Vamos", ["Argentina"], "Vamos vamos Argentina...", "Passionate Argentine national team chant.", ["national-team"]),
    ("Guantanamera", [], "Guantanamera, guajira Guantanamera...", "Traditional song sung in many stadiums.", ["global"]),
    ("Fields of Anfield Road", ["Liverpool FC"], "Outside the Safeway supermarket...", "Liverpool fan song set to Fields of Athenry.", ["fan-song"]),
    ("Poor Scouser Tommy", ["Liverpool FC"], "Let me tell you the story of a poor boy...", "Classic Liverpool folk-style terrace song.", ["fan-song", "classic"]),
    ("One Kiss", ["Liverpool FC"], "One kiss is all it takes...", "Dua Lipa song adopted by Liverpool fans.", ["fan-chant", "modern"]),
    ("Steve Gerrard Is His Name", ["Liverpool FC"], "His name is Steven Gerrard...", "Terrace tribute to Steven Gerrard.", ["player-tribute"]),
    ("Si Senor", ["Liverpool FC"], "Si senor, give the ball to Bobby Firmino...", "Liverpool chant for Roberto Firmino.", ["player-tribute"]),
    ("We Are Liverpool, Tra La La", ["Liverpool FC"], "We are Liverpool, tra la la la la...", "Simple Liverpool call-and-response song.", ["fan-chant"]),
    ("Allez Les Rouges", ["Liverpool FC"], "Allez les Rouges...", "Liverpool terrace chant for the Reds.", ["fan-chant"]),
    ("Scouser Tommy (Fields Variant)", ["Liverpool FC"], "Outside the Shankly Gates...", "Variant Liverpool travelling song.", ["fan-song"]),
    ("Glory Glory Man United", ["Manchester United"], "Glory, glory, Man United...", "Manchester United adaptation of Glory Glory.", ["anthem"]),
    ("United Road (Take Me Home)", ["Manchester United"], "Take me home, United Road...", "Man United song to the tune of Country Roads.", ["fan-song"]),
    ("Sit Down, Sit Down", ["Manchester United"], "Sit down, sit down, sit down, sit down...", "Taunt sung by Manchester United fans.", ["fan-chant"]),
    ("Red Army", ["Manchester United"], "United, United, United...", "Manchester United home end chant.", ["fan-chant"]),
    ("Blue Moon", ["Manchester City"], "Blue moon, you saw me standing alone...", "Manchester City anthem.", ["anthem"]),
    ("We Love You City", ["Manchester City"], "We love you City, we do...", "Classic Manchester City terrace song.", ["fan-chant"]),
    ("Manchester City European Nights", ["Manchester City"], "Blue moon, you saw me standing alone...", "City European night atmosphere.", ["fan-chant"]),
    ("Don't Look Back in Anger", ["Manchester City"], "So Sally can wait...", "Oasis anthem adopted by Manchester City fans.", ["fan-chant"]),
    ("Carefree", ["Chelsea FC"], "Carefree, wherever we may be...", "Chelsea fan song.", ["fan-song"]),
    ("Celery", ["Chelsea FC"], "Celery, celery...", "Historic Chelsea terrace chant.", ["fan-chant", "historic"]),
    ("Ten Men Went to Mow", ["Chelsea FC"], "Ten men went to mow, went to mow a meadow...", "Traditional counting song at Chelsea.", ["fan-chant"]),
    ("Jose Mourinho Chant", ["Chelsea FC"], "Jose Mourinho, Jose Mourinho...", "Chelsea tribute to Jose Mourinho.", ["manager-tribute"]),
    ("Good Old Arsenal", ["Arsenal FC"], "Good old Arsenal, good old Arsenal...", "Classic Arsenal fan song.", ["fan-song"]),
    ("1 Nil to the Arsenal", ["Arsenal FC"], "One nil to the Arsenal...", "Arsenal chant for narrow victories.", ["fan-chant"]),
    ("Hot Stuff", ["Arsenal FC"], "Hot stuff, baby this evening...", "Donna Summer track adopted by Arsenal.", ["fan-chant"]),
    ("Gooners Gooners Gooners", ["Arsenal FC"], "Gooners, gooners, gooners...", "Arsenal fan self-identification chant.", ["fan-chant"]),
    ("Marching On Together", ["Leeds United"], "Marching on together, now we're gonna see you through...", "Leeds United anthem.", ["anthem"]),
    ("Leeds! Leeds! Leeds!", ["Leeds United"], "Leeds, Leeds, Leeds...", "Leeds United call chant.", ["fan-chant"]),
    ("Glory Glory (Leeds)", ["Leeds United"], "Glory, glory, Leeds United...", "Leeds adaptation of Glory Glory.", ["fan-chant"]),
    ("I'm Forever Blowing Bubbles", ["West Ham United"], "I'm forever blowing bubbles, pretty bubbles in the air...", "West Ham United anthem since the 1920s.", ["anthem"]),
    ("It's a Grand Old Team", ["Everton FC"], "It's a grand old team to play for...", "Everton fan song to the tune of The Red Flag.", ["fan-song"]),
    ("Z-Cars Theme", ["Everton FC"], "Johnny Todd (instrumental theme)...", "Everton entrance music from Z-Cars.", ["anthem"]),
    ("Blaydon Races", ["Newcastle United"], "Oh, lads, ye shudda seen us gannin'...", "Geordie folk song adopted by Newcastle.", ["fan-song", "classic"]),
    ("Local Hero", ["Newcastle United"], "Instrumental / Mark Knopfler theme...", "Newcastle entrance music from Local Hero.", ["anthem"]),
    ("Glory Glory Tottenham Hotspur", ["Tottenham Hotspur"], "Glory, glory, Tottenham Hotspur...", "Tottenham Glory Glory adaptation.", ["anthem"]),
    ("When the Year Ends in One", ["Tottenham Hotspur"], "Oh when the year ends in one...", "Tottenham chant.", ["fan-chant"]),
    ("Oh When the Spurs", ["Tottenham Hotspur"], "Oh when the Spurs go marching in...", "Tottenham song.", ["fan-chant"]),
    ("Spurs Are on Their Way to Wembley", ["Tottenham Hotspur"], "Spurs are on their way to Wembley...", "Tottenham cup run chant.", ["fan-chant"]),
    ("Blue Army", ["Leicester City"], "Blue army, blue army...", "Leicester City terrace chant.", ["fan-chant"]),
    ("Mull of Kintyre", ["Aston Villa"], "Mull of Kintyre...", "Paul McCartney song associated with Aston Villa.", ["fan-song"]),
    ("Villa Villa Villa", ["Aston Villa"], "Villa, Villa, Villa...", "Aston Villa call chant.", ["fan-chant"]),
    ("Sweet Caroline", ["England"], "Sweet Caroline, ba ba ba...", "Neil Diamond song sung at England matches.", ["national-team", "global"]),
    ("Three Lions", ["England"], "It's coming home, it's coming home...", "England Euro 96 song.", ["national-team", "fan-song"]),
    ("Vindaloo", ["England"], "Me and me dad and me dad's dad...", "England 1998 World Cup song.", ["national-team"]),
    ("Country Roads", ["England"], "Country roads, take me home...", "John Denver song sung by England fans.", ["national-team", "global"]),
    ("Wonderwall", ["England"], "Today is gonna be the day...", "Oasis song on England away trips.", ["national-team"]),
    ("The Celtic Song", ["Celtic FC"], "It's a grand old team to play for...", "Celtic fan song.", ["fan-song"]),
    ("Grace", ["Celtic FC"], "As we draw near the end of the season...", "Celtic title celebration song.", ["fan-song"]),
    ("Just Can't Get Enough", ["Celtic FC"], "Just can't get enough of Celtic...", "Depeche Mode track adopted by Celtic.", ["fan-chant"]),
    ("The Wild Rover", ["Celtic FC"], "I've been a wild rover for many's the year...", "Irish folk song in Scottish football culture.", ["fan-song"]),
    ("Follow Follow", ["Rangers FC"], "Follow, follow, we will follow Rangers...", "Rangers FC terrace song.", ["fan-song"]),
    ("Simply the Best", ["Rangers FC"], "You're simply the best...", "Tina Turner song associated with Rangers.", ["fan-chant"]),
    ("Every Other Saturday", ["Rangers FC"], "Every other Saturday, my heart's in Glasgow...", "Rangers matchday song.", ["fan-song"]),
    ("Come On You Boys in Green", ["Republic of Ireland"], "Come on you boys in green...", "Republic of Ireland chant.", ["national-team"]),
    ("Stern des Sudens", ["Bayern Munich"], "Stern des Sudens, du bist ein Meister...", "Bayern Munich anthem.", ["anthem"]),
    ("Forever Number One", ["Bayern Munich"], "Forever number one...", "Bayern Munich fan song.", ["fan-song"]),
    ("Mia San Mia", ["Bayern Munich"], "Mia san mia...", "Bayern motto chant.", ["fan-chant"]),
    ("Allez Paris-Saint-Germain", ["Paris Saint-Germain"], "Allez Paris-Saint-Germain...", "PSG call chant.", ["fan-chant"]),
    ("Ici C'est Paris", ["Paris Saint-Germain"], "Ici c'est Paris...", "PSG declaration chant.", ["fan-chant"]),
    ("Au Champs-Elysees", ["France"], "Aux Champs-Elysees...", "French song sung by Les Bleus supporters.", ["national-team"]),
    ("Allez Les Bleus", ["France"], "Allez les Bleus!", "France national team chant.", ["national-team"]),
    ("Hala Madrid", ["Real Madrid"], "Hala Madrid, y nada mas...", "Real Madrid anthem.", ["anthem"]),
    ("Vamos Real Madrid", ["Real Madrid"], "Vamos Real, vamos a ganar...", "Real Madrid Spanish terrace chant.", ["fan-chant"]),
    ("Mes Que Un Club", ["FC Barcelona"], "Mes que un club...", "Barcelona motto.", ["fan-chant"]),
    ("Cant del Barca", ["FC Barcelona"], "Tot l'any seguim amb tu...", "Official FC Barcelona anthem.", ["anthem"]),
    ("Ciao Mama", ["SSC Napoli"], "Ciao mama, ciao mama...", "Napoli terrace chant.", ["fan-chant"]),
    ("Un Giorno All'Improvviso", ["SSC Napoli"], "Un giorno all'improvviso...", "Napoli fan song.", ["fan-song"]),
    ("Wij Houden Van Ajax", ["Ajax"], "Wij houden van Ajax...", "Ajax fan chant.", ["fan-chant"]),
    ("Porto Chant (Dragoes Azuis)", ["FC Porto"], "Porto, Porto, Porto...", "FC Porto terrace chant.", ["fan-chant"]),
    ("Benfica Slavia", ["SL Benfica"], "Slavia, Slavia, Benfica...", "Benfica eagle-themed chant.", ["fan-chant"]),
    ("Dale Boca", ["Boca Juniors"], "Dale, dale, dale Boca...", "Boca Juniors call chant.", ["fan-chant"]),
    ("Muchachos Ahora Nos Volvimos a Ilusionar", ["Argentina"], "Muchachos, ahora nos volvimos a ilusionar...", "Argentina World Cup song.", ["national-team", "fan-song"]),
    ("Vai Corinthians", ["Corinthians"], "Vai, Corinthians!", "Corinthians call chant.", ["fan-chant"]),
    ("Flamengo Mengao Chant", ["Flamengo"], "Uma vez Flamengo, Flamengo ate morrer...", "Flamengo anthem line.", ["anthem"]),
    ("Cacique Chant", ["Colo-Colo"], "Colo-Colo, Colo-Colo...", "Colo-Colo terrace chant.", ["fan-chant"]),
    ("Freed from Desire", [], "My love is cheap, you're talking money...", "Gala track adopted by many fan groups.", ["global"]),
    ("We Are the Champions", [], "We are the champions, my friends...", "Queen song sung after cup wins.", ["global"]),
    ("Hi Ho Silver Lining", [], "Hi ho, silver lining...", "Jeff Beck song on terraces.", ["global"]),
    ("On the Ball, City", [], "Kick off, throw in, header, goal...", "Classic English football song.", ["global", "classic"]),
    ("Play Up Pompey", [], "Play up Pompey, Pompey play up...", "Portsmouth chant.", ["global"]),
    ("No One Likes Us", [], "No one likes us, we don't care...", "Millwall anthem.", ["global"]),
    ("We Shall Not Be Moved", [], "We shall not be moved...", "Tradition song sung on terraces.", ["global"]),
    ("Vamos Vamos Mexico", ["Mexico"], "Vamos, vamos Mexico...", "Mexico national team chant.", ["national-team"]),
    ("Sevilla Ole", ["Sevilla FC"], "Ole, ole, ole, Sevilla...", "Sevilla FC call chant.", ["fan-chant"]),
    ("Atleti Chant", ["Atletico Madrid"], "Atleti, Atleti...", "Atletico Madrid terrace chant.", ["fan-chant"]),
    ("Juventus Anthem", ["Juventus"], "Storia di un grande amore...", "Official Juventus anthem.", ["anthem"]),
    ("Forza Milan", ["AC Milan"], "Forza Milan, forza Milan...", "AC Milan call chant.", ["fan-chant"]),
    ("Pazza Inter Amala", ["Inter Milan"], "Pazza Inter amala...", "Inter Milan anthem.", ["anthem"]),
    ("Roma Roma Roma", ["AS Roma"], "Roma, Roma, Roma...", "AS Roma terrace chant.", ["fan-chant"]),
    ("When the Saints Go Marching In", ["Southampton FC"], "Oh when the saints go marching in...", "Southampton FC anthem.", ["anthem"]),
    ("Seagulls Seagulls", ["Brighton & Hove Albion"], "Seagulls, seagulls...", "Brighton & Hove Albion chant.", ["fan-chant"]),
    ("We've Got the Whole World in Our Hands", ["Nottingham Forest"], "We've got the whole world in our hands...", "Nottingham Forest fan song.", ["fan-song"]),
    ("Hi Ho Wolverhampton", ["Wolverhampton Wanderers"], "Hi ho, Wolverhampton...", "Wolverhampton Wanderers chant.", ["fan-chant"]),
    ("E-I-E-I-O", ["Everton FC"], "E-I-E-I-O...", "Everton call-and-response chant.", ["fan-chant"]),
    ("Dortmund Ole", ["Borussia Dortmund"], "Ole, ole, ole, BVB...", "Borussia Dortmund victory chant.", ["fan-chant"]),
    ("Istanbul 2005 Chant", ["Liverpool FC"], "Istanbul, Istanbul, we won it five times...", "Liverpool chant celebrating the 2005 Champions League final.", ["fan-chant", "classic"]),
]


def main():
    if len(CHANTS) != 100:
        raise SystemExit(f"Expected 100 chants, got {len(CHANTS)}")

    titles = [c[0] for c in CHANTS]
    if len(titles) != len(set(titles)):
        dupes = {t for t in titles if titles.count(t) > 1}
        raise SystemExit(f"Duplicate titles: {dupes}")

    songs = []
    for title, clubs, lyrics, description, tags in CHANTS:
        for club in clubs:
            if club not in VALID_CLUBS:
                raise SystemExit(f"{title}: unknown club {club!r}")
        entry = {
            "title": title,
            "lyrics": lyrics,
            "description": description,
            "is_fan_chant": True,
            "accepted": True,
            "tags": ["chant", "soccer", *tags],
        }
        if clubs:
            entry["clubs"] = clubs
        songs.append(entry)

    out = ROOT / "data/song/soccer_chants.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(songs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(songs)} chants to {out}")


if __name__ == "__main__":
    main()
