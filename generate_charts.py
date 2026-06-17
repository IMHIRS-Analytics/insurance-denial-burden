"""
Generate all charts for the IMHIRS denial/health project.
"""

import sys
sys.path.insert(0, "/home/claude/denial-health-project")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from data.denial_data import (
    ma_denial_rates, ma_appeals, insurer_data_2023,
    health_consequences, give_up_gap, oig_finding, mortality_estimate
)

BRAND_DARK   = "#1a2e44"   # deep navy
BRAND_RED    = "#c0392b"   # alert red
BRAND_AMBER  = "#e67e22"   # warning amber
BRAND_TEAL   = "#16a085"   # IMHIRS teal
BRAND_LIGHT  = "#ecf0f1"   # background
GRID_COLOR   = "#dfe6e9"
FONT         = "DejaVu Sans"

plt.rcParams.update({
    "font.family": FONT,
    "axes.facecolor": "white",
    "figure.facecolor": BRAND_LIGHT,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": GRID_COLOR,
    "grid.linewidth": 0.7,
    "text.color": BRAND_DARK,
    "axes.labelcolor": BRAND_DARK,
    "xtick.color": BRAND_DARK,
    "ytick.color": BRAND_DARK,
})

OUT = "/home/claude/denial-health-project/charts"

# ── Chart 1: MA Denial Rate Trend ────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5))
ax.fill_between(ma_denial_rates["year"], ma_denial_rates["denial_rate_pct"],
                alpha=0.18, color=BRAND_RED)
ax.plot(ma_denial_rates["year"], ma_denial_rates["denial_rate_pct"],
        color=BRAND_RED, linewidth=2.8, marker="o", markersize=8, zorder=5)
for _, row in ma_denial_rates.iterrows():
    ax.annotate(f'{row["denial_rate_pct"]}%',
                xy=(row["year"], row["denial_rate_pct"]),
                xytext=(0, 12), textcoords="offset points",
                ha="center", fontsize=10, fontweight="bold", color=BRAND_RED)
ax.axhspan(7.0, 8.0, alpha=0.07, color=BRAND_RED)
ax.set_xlabel("Year", fontsize=11)
ax.set_ylabel("Prior Auth Denial Rate (%)", fontsize=11)
ax.set_title("Medicare Advantage Prior Authorization Denial Rate (2019–2024)",
             fontsize=13, fontweight="bold", pad=15)
ax.set_ylim(4, 9)
ax.set_xticks(ma_denial_rates["year"])
ax.annotate("Peak: 7.4%\n2022", xy=(2022, 7.4), xytext=(2022.2, 8.2),
            fontsize=9, color=BRAND_RED,
            arrowprops=dict(arrowstyle="->", color=BRAND_RED, lw=1.3))
fig.text(0.99, 0.01, "Source: KFF analysis of CMS data | IMHIRS Analytics",
         ha="right", fontsize=7.5, color="gray")
plt.tight_layout()
plt.savefig(f"{OUT}/01_ma_denial_trend.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 1 done")

# ── Chart 2: The Give-Up Gap ─────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5))
populations = give_up_gap["population"]
x = np.arange(len(populations))
width = 0.35
bars1 = ax.bar(x - width/2, give_up_gap["appeal_rate_pct"],
               width, label="% Who Actually Appeal", color=BRAND_TEAL, alpha=0.9, zorder=3)
bars2 = ax.bar(x + width/2, give_up_gap["overturn_when_appealed_pct"],
               width, label="% Overturned When Appealed", color=BRAND_AMBER, alpha=0.9, zorder=3)

for bar in bars1:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 0.8,
            f'{h:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold', color=BRAND_TEAL)
for bar in bars2:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 0.8,
            f'{h:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold', color=BRAND_AMBER)

ax.set_xticks(x)
ax.set_xticklabels(populations, fontsize=9.5)
ax.set_ylabel("Percent (%)", fontsize=11)
ax.set_title("The Give-Up Gap: Few Appeal, Most Who Do — Win",
             fontsize=13, fontweight="bold", pad=15)
ax.legend(fontsize=10)
ax.set_ylim(0, 105)
# Annotation callout
ax.annotate("Most denials go\nunchallenged.\nMost challenges\nsucceed.",
            xy=(0 - width/2, give_up_gap["appeal_rate_pct"].iloc[0]),
            xytext=(-0.05, 55), fontsize=9, color=BRAND_DARK,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor=BRAND_TEAL, alpha=0.85))
fig.text(0.99, 0.01, "Source: KFF, CMS ODAG, Medicare Rights Center | IMHIRS Analytics",
         ha="right", fontsize=7.5, color="gray")
plt.tight_layout()
plt.savefig(f"{OUT}/02_give_up_gap.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 2 done")

# ── Chart 3: Health Consequences of Denials ──────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
consequences = health_consequences["consequence"]
pcts = health_consequences["pct_affected"]
colors = [BRAND_RED if p >= 35 else BRAND_AMBER if p >= 25 else BRAND_TEAL for p in pcts]
bars = ax.barh(consequences, pcts, color=colors, alpha=0.88, zorder=3, height=0.6)
for bar, pct in zip(bars, pcts):
    ax.text(pct + 0.5, bar.get_y() + bar.get_height()/2,
            f'{pct}%', va='center', fontsize=11, fontweight='bold',
            color=BRAND_DARK)
ax.set_xlabel("% of Adults Who Experienced a Denial", fontsize=11)
ax.set_title("When Insurance Says No: Real Health Consequences",
             fontsize=13, fontweight="bold", pad=15)
ax.set_xlim(0, 55)
legend_patches = [
    mpatches.Patch(color=BRAND_RED, alpha=0.88, label="High impact (≥35%)"),
    mpatches.Patch(color=BRAND_AMBER, alpha=0.88, label="Moderate impact (25-34%)"),
    mpatches.Patch(color=BRAND_TEAL, alpha=0.88, label="Lower impact (<25%)"),
]
ax.legend(handles=legend_patches, fontsize=9, loc="lower right")
fig.text(0.99, 0.01, "Source: Commonwealth Fund Survey 2026; Ipsos PES 2025 | IMHIRS Analytics",
         ha="right", fontsize=7.5, color="gray")
plt.tight_layout()
plt.savefig(f"{OUT}/03_health_consequences.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 3 done")

# ── Chart 4: Insurer Denial Rate vs Overturn Rate (2023) ─────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(insurer_data_2023))
width = 0.38
b1 = ax.bar(x - width/2, insurer_data_2023["denial_rate_pct"],
            width, label="Denial Rate (%)", color=BRAND_RED, alpha=0.85, zorder=3)
b2 = ax.bar(x + width/2, insurer_data_2023["appeal_overturn_pct"],
            width, label="Appeal Overturn Rate (%)", color=BRAND_TEAL, alpha=0.85, zorder=3)
for bar in b1:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 0.3,
            f'{h}%', ha='center', fontsize=9, fontweight='bold', color=BRAND_RED)
for bar in b2:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 0.3,
            f'{h}%', ha='center', fontsize=9, fontweight='bold', color=BRAND_TEAL)
ax.set_xticks(x)
ax.set_xticklabels(insurer_data_2023["insurer"], fontsize=10)
ax.set_ylabel("Percent (%)", fontsize=11)
ax.set_title("Medicare Advantage 2023: Who Denies Most — and Gets Reversed Most?",
             fontsize=12.5, fontweight="bold", pad=15)
ax.legend(fontsize=10)
ax.set_ylim(0, 110)
# Callout: Centene paradox
ax.annotate("Highest denial rate\nAND highest overturn.\nSomething's wrong upstream.",
            xy=(0, 14.2), xytext=(0.6, 75),
            fontsize=8.5, color=BRAND_DARK,
            arrowprops=dict(arrowstyle="->", color=BRAND_RED, lw=1.2),
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                      edgecolor=BRAND_RED, alpha=0.85))
fig.text(0.99, 0.01, "Source: KFF Jan 2026; Kiplinger Feb 2025 | IMHIRS Analytics",
         ha="right", fontsize=7.5, color="gray")
plt.tight_layout()
plt.savefig(f"{OUT}/04_insurer_comparison.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 4 done")

# ── Chart 5: The Human Cost Summary ──────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis("off")

stats = [
    ("1 in 5", "privately insured adults\ndenied recommended care\nin the past year", BRAND_RED),
    ("13%", "of MA prior auth denials\nmeet Medicare coverage rules\n(OIG, 2022)", BRAND_AMBER),
    ("~195,000", "estimated annual US deaths\nlinked to insurance\naccess barriers", BRAND_DARK),
    ("<1%", "of ACA marketplace denials\never appealed — yet\n59% would be overturned", BRAND_TEAL),
]

for i, (number, label, color) in enumerate(stats):
    x_pos = 0.12 + i * 0.24
    ax.text(x_pos, 0.72, number, transform=ax.transAxes,
            fontsize=26, fontweight="bold", color=color,
            ha="center", va="center")
    ax.text(x_pos, 0.35, label, transform=ax.transAxes,
            fontsize=9.5, color=BRAND_DARK, ha="center", va="center",
            linespacing=1.6)
    if i < 3:
        fig.add_artist(plt.Line2D(
            [0.12 + i * 0.24 + 0.12, 0.12 + i * 0.24 + 0.12], [0.12, 0.88],
            transform=fig.transFigure, color=GRID_COLOR, linewidth=1.2))

ax.set_title("Is Health Insurance Making Us Sicker? The Numbers Say Yes.",
             fontsize=14, fontweight="bold", pad=20, color=BRAND_DARK)
fig.text(0.99, 0.01,
         "Sources: Commonwealth Fund 2026, HHS OIG 2022, PNHP, KFF | IMHIRS Analytics",
         ha="right", fontsize=7.5, color="gray")
plt.tight_layout()
plt.savefig(f"{OUT}/05_human_cost_summary.png", dpi=150, bbox_inches="tight")
plt.close()
print("Chart 5 done")

print("\nAll charts saved to", OUT)
