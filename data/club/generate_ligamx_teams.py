"""Generate data/club/ligamx_teams.json with all 18 Liga MX clubs.

Run: python data/club/generate_ligamx_teams.py
Import: python manage.py import_clubs data/club/ligamx_teams.json
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# name, nickname, founded, stadium, location, website, primary_color, secondary_color
TEAMS = [
    (
        "Club America",
        "Las Aguilas",
        1916,
        "Estadio Ciudad de los Deportes",
        "Mexico City, Mexico",
        "https://www.clubamerica.com.mx",
        "#003087",
        "#FBECB2",
    ),
    (
        "Atlas FC",
        "Los Rojinegros",
        1916,
        "Estadio Jalisco",
        "Guadalajara, Jalisco, Mexico",
        "https://www.atlasfc.com.mx",
        "#E4002B",
        "#000000",
    ),
    (
        "Atlético de San Luis",
        "Atlético de San Luis",
        2013,
        "Estadio Alfonso Lastras",
        "San Luis Potosí, San Luis Potosí, Mexico",
        "https://www.atleticodesanluis.mx",
        "#E30613",
        "#002D72",
    ),
    (
        "Cruz Azul",
        "La Maquina",
        1927,
        "Estadio Olímpico Universitario",
        "Mexico City, Mexico",
        "https://www.cruzazulfc.com",
        "#005CB9",
        "#FFFFFF",
    ),
    (
        "Chivas Guadalajara",
        "Chivas",
        1906,
        "Estadio Akron",
        "Zapopan, Jalisco, Mexico",
        "https://www.chivasdecorazon.com.mx",
        "#E40613",
        "#FFFFFF",
    ),
    (
        "FC Juárez",
        "Los Bravos",
        2015,
        "Estadio Olímpico Benito Juárez",
        "Ciudad Juárez, Chihuahua, Mexico",
        "https://www.fcjuarez.com",
        "#E85D04",
        "#000000",
    ),
    (
        "Club León",
        "La Fiera",
        1944,
        "Estadio León",
        "León, Guanajuato, Mexico",
        "https://www.clubleon.mx",
        "#008248",
        "#FFD700",
    ),
    (
        "Mazatlán FC",
        "Los Cañoneros",
        2020,
        "Estadio Mazatlán",
        "Mazatlán, Sinaloa, Mexico",
        "https://www.mazatlanfc.com",
        "#6B2C91",
        "#FFFFFF",
    ),
    (
        "CF Monterrey",
        "Rayados",
        1945,
        "Estadio BBVA",
        "Guadalupe, Nuevo León, Mexico",
        "https://www.rayados.com",
        "#004481",
        "#FFFFFF",
    ),
    (
        "Club Necaxa",
        "Los Rayos",
        1923,
        "Estadio Victoria",
        "Aguascalientes, Aguascalientes, Mexico",
        "https://www.clubnecaxa.com",
        "#E4002B",
        "#FFFFFF",
    ),
    (
        "CF Pachuca",
        "Los Tuzos",
        1901,
        "Estadio Hidalgo",
        "Pachuca, Hidalgo, Mexico",
        "https://www.tuzos.com.mx",
        "#004990",
        "#FFFFFF",
    ),
    (
        "Club Puebla",
        "La Franja",
        1944,
        "Estadio Cuauhtémoc",
        "Puebla, Puebla, Mexico",
        "https://www.clubpuebla.com",
        "#002B7F",
        "#FFFFFF",
    ),
    (
        "Querétaro FC",
        "Gallos Blancos",
        1950,
        "Estadio Corregidora",
        "Querétaro, Querétaro, Mexico",
        "https://www.gallosblancos.com.mx",
        "#003087",
        "#000000",
    ),
    (
        "Santos Laguna",
        "Guerreros",
        1983,
        "Estadio Corona",
        "Torreón, Coahuila, Mexico",
        "https://www.clubsantos.mx",
        "#008542",
        "#FFFFFF",
    ),
    (
        "Club Tijuana",
        "Xolos",
        2007,
        "Estadio Caliente",
        "Tijuana, Baja California, Mexico",
        "https://www.xolos.com.mx",
        "#CE1126",
        "#000000",
    ),
    (
        "Deportivo Toluca FC",
        "Diablos Rojos",
        1917,
        "Estadio Nemesio Díez",
        "Toluca, State of Mexico, Mexico",
        "https://www.deportivotolucafc.com",
        "#E30613",
        "#FFFFFF",
    ),
    (
        "Tigres UANL",
        "Los Tigres",
        1960,
        "Estadio Universitario",
        "San Nicolás de los Garza, Nuevo León, Mexico",
        "https://www.tigres.com.mx",
        "#FFCD00",
        "#006FB4",
    ),
    (
        "Pumas UNAM",
        "Los Pumas",
        1954,
        "Estadio Olímpico Universitario",
        "Mexico City, Mexico",
        "https://www.pumas.mx",
        "#CBA135",
        "#004B87",
    ),
]


def main():
    names = [team[0] for team in TEAMS]
    if len(names) != len(set(names)):
        dupes = {name for name in names if names.count(name) > 1}
        raise SystemExit(f"Duplicate team names: {dupes}")

    clubs = []
    for (
        name,
        nickname,
        founded,
        stadium,
        location,
        website,
        primary_color,
        secondary_color,
    ) in TEAMS:
        clubs.append(
            {
                "name": name,
                "nickname": nickname,
                "founded": founded,
                "stadium": stadium,
                "location": location,
                "website": website,
                "tags": ["ligamx", "mexican", "north-america"],
                "primary_color": primary_color,
                "secondary_color": secondary_color,
            }
        )

    out = ROOT / "data/club/ligamx_teams.json"
    out.write_text(json.dumps(clubs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(clubs)} Liga MX clubs to {out}")


if __name__ == "__main__":
    main()
