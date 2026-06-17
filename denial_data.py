"""
Is Health Insurance Stressing Us Out and Making Us Sicker?
IMHIRS Analytics | Dawn Krysa PA-C, MSHIIM, CHDA
Data sources: KFF, CMS, Commonwealth Fund, HHS OIG, AJMC, Ipsos
"""

import pandas as pd

# ── Medicare Advantage Prior Authorization Denial Rates ──────────────────────
# Source: KFF analysis of CMS data (2019-2023); KFF Jan 2026 report for 2024
ma_denial_rates = pd.DataFrame({
    "year": [2019, 2020, 2021, 2022, 2023, 2024],
    "denial_rate_pct": [5.7, 5.6, 5.8, 7.4, 6.4, 5.9],   # KFF / CMS
    "total_requests_millions": [38.0, 40.0, 43.0, 46.0, 50.0, 53.0],  # KFF
    "denials_millions": [2.17, 2.24, 2.49, 3.40, 3.20, 3.13],
})

# ── MA Appeal Rates & Overturn Rates ────────────────────────────────────────
# Source: KFF; Medicare Rights Center; CMS ODAG data
ma_appeals = pd.DataFrame({
    "year":            [2019, 2020, 2021, 2022, 2023, 2024],
    "appeal_rate_pct": [9.0,  9.0,  9.2,  9.5,  10.1, 10.3],   # <10% historically
    "overturn_rate_pct": [75.0, 75.0, 76.0, 82.0, 83.0, 84.0],  # when appealed
})

# ── Insurer-Level Denial & Overturn Rates 2023 ───────────────────────────────
# Source: KFF Jan 2026; Kiplinger Feb 2025
insurer_data_2023 = pd.DataFrame({
    "insurer": ["Centene", "CVS/Aetna", "UnitedHealth", "Humana", "Kaiser", "Elevance"],
    "denial_rate_pct": [14.2, 11.8, 6.1, 5.9, 3.4, 6.7],
    "appeal_overturn_pct": [95.5, 89.7, 78.0, 68.4, 51.0, 72.0],
})

# ── Health Consequences of Denials ───────────────────────────────────────────
# Source: Commonwealth Fund Survey June 2026; Ipsos Patient Experience Survey 2025
health_consequences = pd.DataFrame({
    "consequence": [
        "Care delayed due to prior auth denial",
        "Health problem worsened after denial",
        "Did not fill Rx due to cost/denial",
        "Skipped/delayed care due to cost",
        "Took on medical debt after denial",
        "Avoided follow-up care due to debt fear",
    ],
    "pct_affected": [41, 28, 25, 38, 18, 32],
    "source": [
        "Commonwealth Fund 2026",
        "Commonwealth Fund 2026",
        "Ipsos PES 2025",
        "Commonwealth Fund 2026",
        "Ipsos PES 2025",
        "Commonwealth Fund 2026",
    ]
})

# ── Claim Denial Growth (All Insurance) ──────────────────────────────────────
# Source: AJMC / Komodo Health 2024; Change Healthcare Denials Index
denial_growth = pd.DataFrame({
    "year": [2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "denial_index": [100, 103, 106, 109, 112, 114, 116],  # indexed to 2018=100
    "note": ["Baseline"] + [""] * 6,
})

# ── The "Give Up" Gap: Denials vs Appeals ────────────────────────────────────
# Source: KFF ACA Marketplace 2023; CMS MA ODAG; OIG HHS 2022
give_up_gap = pd.DataFrame({
    "population": ["ACA Marketplace (2023)", "Medicare Advantage (2022)", "Traditional Medicare (2022)"],
    "denials_millions": [73.0, 3.4, 0.072],
    "appeal_rate_pct": [0.1, 9.5, 6.4],
    "overturn_when_appealed_pct": [59.0, 82.0, 28.7],
})

# ── HHS OIG Finding: MA Denials That Met Medicare Coverage Rules ──────────────
# Source: HHS OIG Report April 2022 (sampled 250 PA denials, 2019 data)
oig_finding = {
    "sample_pa_denials": 250,
    "met_medicare_coverage_rules_pct": 13,
    "description": "13% of sampled MA prior auth denials met Medicare coverage rules "
                   "and would have been approved under original Medicare",
    "source": "HHS OIG, April 2022"
}

# ── Mortality Burden Estimate ─────────────────────────────────────────────────
# Source: PNHP analysis; peer-reviewed literature aggregate
mortality_estimate = {
    "annual_excess_deaths_low": 170_000,
    "annual_excess_deaths_mid": 195_000,
    "annual_excess_deaths_high": 220_000,
    "description": "Estimated annual US deaths associated with insurance gaps/access barriers",
    "source": "PNHP synthesis of peer-reviewed literature"
}

if __name__ == "__main__":
    print("MA Denial Rates:\n", ma_denial_rates)
    print("\nHealth Consequences:\n", health_consequences)
    print("\nInsurer 2023:\n", insurer_data_2023)
    print("\nOIG Finding:", oig_finding)
    print("\nMortality Estimate:", mortality_estimate)
