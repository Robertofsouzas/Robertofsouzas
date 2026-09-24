"""
Gera o gráfico de acessos (SVG) a partir da API de tráfego do GitHub.

- Busca os últimos 14 dias na API e ACUMULA o histórico em data/traffic.json
  (a API só guarda 14 dias; sem acumular, o histórico se perde).
- Desenha um gráfico de linha em assets/profile-analytics.svg.

Atenção: a API mede visitas ao REPOSITÓRIO Robertofsouzas/Robertofsouzas,
não à página do perfil (github.com/Robertofsouzas).
"""
import json
import math
import os
from datetime import date, timedelta

import requests

OWNER = "Robertofsouzas"
REPO = "Robertofsouzas"

DAYS_SHOWN = 30
HISTORY_FILE = "data/traffic.json"
OUTPUT_SVG = "assets/profile-analytics.svg"
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/traffic/views"

TITLE = "Acessos ao repositório do perfil"


# ---------------------------------------------------------------- dados
def fetch_views(token):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2026-03-10",
    }
    response = requests.get(API_URL, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json().get("views", [])


def load_history():
    """Lê o histórico salvo. Aceita o formato antigo (resposta crua da API)."""
    if not os.path.exists(HISTORY_FILE):
        return {}
    with open(HISTORY_FILE, encoding="utf-8") as f:
        data = json.load(f)
    if "history" in data:
        return data["history"]
    return {
        v["timestamp"][:10]: {"count": v["count"], "uniques": v["uniques"]}
        for v in data.get("views", [])
    }


def merge_history(history, views):
    """Dados novos da API sobrescrevem os antigos do mesmo dia."""
    for v in views:
        history[v["timestamp"][:10]] = {
            "count": v["count"],
            "uniques": v["uniques"],
        }
    return dict(sorted(history.items()))


def save_history(history):
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump({"history": history}, f, indent=2, ensure_ascii=False)


def build_series(history, days):
    """Últimos `days` dias (sem passar do início do histórico); lacunas = 0."""
    dates = sorted(date.fromisoformat(d) for d in history)
    end = dates[-1]
    start = max(dates[0], end - timedelta(days=days - 1))
    series = []
    d = start
    while d <= end:
        item = history.get(d.isoformat(), {})
        series.append(
            {"day": d, "count": item.get("count", 0), "uniques": item.get("uniques", 0)}
        )
        d += timedelta(days=1)
    return series


# -------------------------------------------------------------- desenho
W, H = 720, 260
PAD_L, PAD_R, PAD_T, PAD_B = 44, 24, 64, 40


def nice_max(v):
    if v <= 5:
        return 5
    p = 10 ** math.floor(math.log10(v))
    for m in (1, 2, 5, 10):
        if v <= m * p:
            return m * p
    return 10 * p


def fmt(d):
    return d.strftime("%d/%m")


def render_svg(series):
    n = len(series)
    total = sum(s["count"] for s in series)
    today = series[-1]["count"]
    peak = max(series, key=lambda s: s["count"])
    y_max = nice_max(max(max(s["count"], s["uniques"]) for s in series))

    inner_w = W - PAD_L - PAD_R
    inner_h = H - PAD_T - PAD_B

    def x(i):
        return PAD_L + (inner_w / 2 if n == 1 else i / (n - 1) * inner_w)

    def y(v):
        return PAD_T + inner_h - v / y_max * inner_h

    ticks = 5  # nice_max é sempre divisível por 5 -> rótulos inteiros
    grid = ""
    for t in range(ticks + 1):
        v = y_max / ticks * t
        grid += (
            f'<line class="g" x1="{PAD_L}" y1="{y(v):.1f}" x2="{W - PAD_R}" y2="{y(v):.1f}"/>'
            f'<text class="a" x="{PAD_L - 8}" y="{y(v) + 4:.1f}" text-anchor="end">{int(v)}</text>'
        )

    step = max(1, math.ceil(n / 6))
    xlabels = ""
    for i in range(0, n, step):
        xlabels += f'<text class="a" x="{x(i):.1f}" y="{H - PAD_B + 20}" text-anchor="middle">{fmt(series[i]["day"])}</text>'
    if n > 1 and (n - 1) % step != 0:
        xlabels += f'<text class="a" x="{x(n - 1):.1f}" y="{H - PAD_B + 20}" text-anchor="end">{fmt(series[-1]["day"])}</text>'

    line = "M" + " L".join(f"{x(i):.1f},{y(s['count']):.1f}" for i, s in enumerate(series))
    area = f"{line} L{x(n - 1):.1f},{y(0):.1f} L{x(0):.1f},{y(0):.1f} Z"
    uline = "M" + " L".join(f"{x(i):.1f},{y(s['uniques']):.1f}" for i, s in enumerate(series))

    dots = "".join(
        f'<circle class="d" cx="{x(i):.1f}" cy="{y(s["count"]):.1f}" r="{4.5 if i == n - 1 else 2.5}">'
        f'<title>{fmt(s["day"])}: {s["count"]} acesso(s), {s["uniques"]} único(s)</title></circle>'
        for i, s in enumerate(series)
    )

    peak_txt = f" · pico: {peak['count']} ({fmt(peak['day'])})" if peak["count"] else ""
    sub = f"Últimos {n} {'dia' if n == 1 else 'dias'} · total: {total} · hoje: {today}{peak_txt}"

    lx = W - PAD_R - 170
    legend = (
        f'<line class="l" x1="{lx}" y1="26" x2="{lx + 18}" y2="26"/>'
        f'<text class="s" x="{lx + 24}" y="30">acessos</text>'
        f'<line class="u" x1="{lx + 84}" y1="26" x2="{lx + 102}" y2="26"/>'
        f'<text class="s" x="{lx + 108}" y="30">únicos</text>'
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{TITLE}">
<style>
:root{{--bg:#F8FAFC;--fg:#0F172A;--mu:#64748B;--gr:#E2E8F0;--ln:#342E83;--un:#0E9F9A}}
@media (prefers-color-scheme:dark){{:root{{--bg:#0d1117;--fg:#e6edf3;--mu:#8b949e;--gr:#30363d;--ln:#8B85E8;--un:#2DD4BF}}}}
text{{font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif}}
.bg{{fill:var(--bg)}}.t{{fill:var(--fg);font-size:18px;font-weight:600}}
.s{{fill:var(--mu);font-size:12px}}.a{{fill:var(--mu);font-size:11px}}
.g{{stroke:var(--gr);stroke-width:1}}
.l{{fill:none;stroke:var(--ln);stroke-width:2.5;stroke-linejoin:round;stroke-linecap:round}}
.u{{fill:none;stroke:var(--un);stroke-width:1.8;stroke-dasharray:5 4;stroke-linecap:round}}
.f{{fill:var(--ln);opacity:.12}}.d{{fill:var(--ln)}}
</style>
<rect class="bg" width="{W}" height="{H}" rx="12"/>
<text class="t" x="{PAD_L}" y="30">{TITLE}</text>
<text class="s" x="{PAD_L}" y="49">{sub}</text>
{legend}
{grid}{xlabels}
<path class="f" d="{area}"/>
<path class="u" d="{uline}"/>
<path class="l" d="{line}"/>
{dots}
</svg>
"""


# ----------------------------------------------------------------- main
def main():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN não definido. Confira o secret TRAFFIC_TOKEN no workflow.")

    history = merge_history(load_history(), fetch_views(token))
    if not history:
        raise SystemExit("Nenhum dado de tráfego encontrado.")
    save_history(history)

    svg = render_svg(build_series(history, DAYS_SHOWN))
    os.makedirs(os.path.dirname(OUTPUT_SVG), exist_ok=True)
    with open(OUTPUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Gráfico gerado com sucesso! ({len(history)} dias no histórico)")


if __name__ == "__main__":
    main()
