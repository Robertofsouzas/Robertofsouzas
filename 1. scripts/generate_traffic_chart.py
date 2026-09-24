import os
import json
import requests
from datetime import datetime

OWNER = "Robertofsouzas"
REPO = "Robertofsouzas"

TOKEN = os.getenv("GITHUB_TOKEN")

API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/traffic/views"

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2026-03-10"
}

response = requests.get(API_URL, headers=headers)
response.raise_for_status()

data = response.json()

views = data.get("views", [])

# Guarda os dados
os.makedirs("data", exist_ok=True)

with open("data/traffic.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Últimos 7 dias
views = views[-7:]

if not views:
    raise ValueError("Nenhum dado de tráfego encontrado.")

# Dimensões
WIDTH = 900
HEIGHT = 350

LEFT = 70
RIGHT = 30
TOP = 60
BOTTOM = 70

GRAPH_WIDTH = WIDTH - LEFT - RIGHT
GRAPH_HEIGHT = HEIGHT - TOP - BOTTOM

values = [item["count"] for item in views]

max_value = max(values)

if max_value == 0:
    max_value = 1

points = []

for i, item in enumerate(views):

    x = LEFT + (
        i * GRAPH_WIDTH / max(len(views) - 1, 1)
    )

    y = TOP + GRAPH_HEIGHT - (
        item["count"] / max_value * GRAPH_HEIGHT
    )

    points.append((x, y))

# Linha do gráfico
polyline = " ".join(
    f"{x:.1f},{y:.1f}"
    for x, y in points
)

# Pontos
circles = ""

for (x, y), item in zip(points, views):

    circles += f"""
    <circle
        cx="{x:.1f}"
        cy="{y:.1f}"
        r="5"
        fill="#342E83"
    />

    <text
        x="{x:.1f}"
        y="{y - 15:.1f}"
        text-anchor="middle"
        font-size="13"
        fill="#342E83"
        font-family="Arial"
    >
        {item["count"]}
    </text>
    """

# Labels
labels = ""

for (x, _), item in zip(points, views):

    date = datetime.fromisoformat(
        item["timestamp"].replace("Z", "+00:00")
    )

    label = date.strftime("%d/%m")

    labels += f"""
    <text
        x="{x:.1f}"
        y="{HEIGHT - 30}"
        text-anchor="middle"
        font-size="13"
        fill="#64748B"
        font-family="Arial"
    >
        {label}
    </text>
    """

svg = f"""<svg
    xmlns="http://www.w3.org/2000/svg"
    width="{WIDTH}"
    height="{HEIGHT}"
    viewBox="0 0 {WIDTH} {HEIGHT}"
>

<rect
    width="100%"
    height="100%"
    rx="16"
    fill="#F8FAFC"
/>

<text
    x="{LEFT}"
    y="32"
    font-size="20"
    font-weight="bold"
    fill="#0F172A"
    font-family="Arial"
>
    GitHub Traffic — Last 7 Days
</text>

<line
    x1="{LEFT}"
    y1="{TOP + GRAPH_HEIGHT}"
    x2="{WIDTH - RIGHT}"
    y2="{TOP + GRAPH_HEIGHT}"
    stroke="#CBD5E1"
/>

<polyline
    points="{polyline}"
    fill="none"
    stroke="#342E83"
    stroke-width="4"
    stroke-linecap="round"
    stroke-linejoin="round"
/>

{circles}

{labels}

</svg>
"""

os.makedirs("assets", exist_ok=True)

with open(
    "assets/profile-analytics.svg",
    "w",
    encoding="utf-8"
) as f:
    f.write(svg)

print("Gráfico gerado com sucesso!")
