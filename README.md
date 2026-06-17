# insurance-denial-burden
Analyzing the public health impact of health insurance claim denials in the United States. Federal data visualization and analysis by IMHIRS Analytics
# Insurance Denial Burden: Are Health Insurance Denials Making Americans Sicker?

**IMHIRS Analytics | Dawn Krysa PA-C, MSHIIM, CHDA**  
**github.com/IMHIRS-Analytics**

---

## Project Overview

Health insurance denials aren't just a billing problem. They're a public health problem.

This project analyzes federal data to answer a simple but underexplored question: **Does the American health insurance denial system contribute to worse health outcomes?**

Using publicly available data from CMS, KFF, the Commonwealth Fund, HHS OIG, and peer-reviewed literature, this analysis traces the path from denial → avoidance → delayed care → worsened outcomes → increased cost.

---

## Key Findings

- **1 in 5** privately insured U.S. adults were denied recommended care in the past year *(Commonwealth Fund, 2026)*
- **7.4%** of Medicare Advantage prior authorization requests were denied at peak in 2022 -- up from 5.7% in 2019 *(KFF/CMS)*
- **<1%** of ACA Marketplace denials are ever appealed -- yet **59%** would be overturned *(KFF, 2023)*
- **82%** of appealed Medicare Advantage denials are overturned *(CMS ODAG)*
- **13%** of sampled MA prior auth denials met Medicare coverage rules and would have been approved under Original Medicare *(HHS OIG, 2022)*
- **~195,000** estimated annual U.S. deaths linked to insurance access barriers *(PNHP synthesis)*
- Claim denials increased **16%** from 2018 to 2024 *(AJMC/Komodo Health)*

---

## Visualizations

| Chart | Description |
|---|---|
| `01_ma_denial_trend.png` | Medicare Advantage prior auth denial rate 2019-2024 |
| `02_give_up_gap.png` | Appeal rates vs. overturn rates -- the Give-Up Gap |
| `03_health_consequences.png` | Real health consequences when insurance says no |
| `04_insurer_comparison.png` | Denial rate vs. appeal overturn rate by insurer (2023) |
| `05_human_cost_summary.png` | Summary stat card -- the burden in four numbers |

---

## Data Sources

| Source | Data Used |
|---|---|
| KFF / CMS | MA prior authorization denial rates 2019-2024 |
| KFF (Jan 2026) | Insurer-level denial and overturn rates 2023 |
| CMS ODAG | Medicare Advantage appeals data |
| HHS OIG (April 2022) | Sampled MA denial review -- coverage rule analysis |
| Commonwealth Fund (June 2026) | Patient-reported health consequences of denials |
| Ipsos Patient Experience Survey (2025) | Medication non-adherence, medical debt |
| AJMC / Komodo Health (2024) | Claim denial growth 2018-2024 |
| PNHP (peer-reviewed synthesis) | Mortality burden estimate |
| Medicare Rights Center | Appeal behavior and beneficiary experience |

---

## Repository Structure

```
insurance-denial-burden/
├── README.md
├── data/
│   └── denial_data.py        # All sourced datasets as pandas DataFrames
├── generate_charts.py         # Reproducible chart generation script
└── charts/
    ├── 01_ma_denial_trend.png
    ├── 02_give_up_gap.png
    ├── 03_health_consequences.png
    ├── 04_insurer_comparison.png
    └── 05_human_cost_summary.png
```

---

## How to Run

```bash
git clone https://github.com/IMHIRS-Analytics/insurance-denial-burden
cd insurance-denial-burden
pip install pandas matplotlib seaborn
python generate_charts.py
```

---

## Clinical Context

This project was developed alongside active Medicare Advantage CDI/clinical validation work in Kentucky long-term care facilities. The patterns identified in federal data mirror what is observed at the patient level: documentation gaps, delayed care, and clinical findings that go unaddressed -- often in facilities already flagged by CMS for poor performance.

The gap between what AI tools surface and what clinical judgment catches is real. This project is part of a broader IMHIRS Analytics portfolio examining where data, clinical expertise, and policy intersect in American healthcare.

---

## About IMHIRS Analytics

IMHIRS Analytics is an independent healthcare analytics consultancy founded by Dawn Krysa PA-C, MSHIIM, CHDA. Specializing in risk adjustment, program integrity, and clinical documentation intelligence.

- **Portfolio:** [imhirs-analytics.github.io](https://imhirs-analytics.github.io)
- **GitHub:** [github.com/IMHIRS-Analytics](https://github.com/IMHIRS-Analytics)
- **LinkedIn:** [linkedin.com/in/dawn-krysa-b00160388](https://linkedin.com/in/dawn-krysa-b00160388)

---

*All data sourced from publicly available federal datasets and peer-reviewed literature. Analysis reflects data available as of June 2026.*
