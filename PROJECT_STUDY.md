# New-Project Study — what to print next, and where it already sells
*Market study for the X2D Print Venture. Ranks 16 ideas by fit with the X2D, margin, local gap and your network. Includes the E36 side-skirt and M-style molding idea from your friend.*

> **How reliable this is.** Case evidence comes from a quick web search (sources linked). I did not find any 3D-printed E36 skirt or molding business, and I found no local Argentine price data. Everything marked **(VERIFY)** needs a 30-minute check on Mercado Libre, Instagram or a car-club group before you spend filament. The ranking is a scoring model (`opportunities.py`), not a forecast.

---

## 1. What the market abroad already does

| Case | What it shows | Source |
|---|---|---|
| **Porsche Classic** | Prints rare parts for out-of-production cars (plastic parts in SLS, metal in SLM). About 9 printed parts inside a range of ~52,000, e.g. the 959 clutch release lever. Proves *discontinued parts* is a real category, even for OEMs. | [Porsche Newsroom](https://newsroom.porsche.com/en/company/porsche-classic-3d-printer-spare-parts-sls-printer-production-cars-innovative-14816.html) |
| **Mercedes-Benz Classic** | Printed inside-mirror base for the 300 SL Coupé, sold through a service partner. | [VoxelMatters](https://www.voxelmatters.com/mercedes-3d-printed-spare-parts/) |
| **Etsy sellers** | Small shops sell printed reproductions: Chevy C10 AC vent bezels (1964–66), Audi A4 B6/B7 rear cup holders and ashtray replacements, trim for cars like the BMW E30. | [Etsy: 3D-printed car parts](https://www.etsy.com/market/car_part_3d_printed) |
| **Freshmade 3D** | Newer company making hard-to-find parts for classic cars and trucks, partnered with a restoration shop (Hahn-Vorbach, Pennsylvania). Model: *partner with a restorer*. | [Wilson Auto](https://wilsonauto.com/cant-find-a-classic-car-part-no-problem-make-it-with-a-3d-printer/) |
| **HV3DWorks** | Another small reproduction-parts shop. | [hv3dworks.com](https://hv3dworks.com/) |
| **E36 skirts & moldings (conventional)** | Sold as injection-molded ABS, polypropylene or fiberglass by ECS Tuning, Turner Motorsport and many eBay sellers. No printed version found. | [ECS Tuning](https://www.ecstuning.com/BMW-E36-M3-S52_3.2L/Exterior/Body/Molding_-and-_Trim/), [Turner](https://www.turnermotorsport.com/BMW-E36-M3-Parts/c-684-bmw-side-skirts) |

**Pattern across all of them:** printing wins on *small, fit-critical, discontinued or low-volume* parts. It loses on large body panels that are cheap to mold. A blog I found claims 7-figure revenue and USD 4,000/month side hustles in this niche; it's marketing content, so I did not use those numbers.

**Why Argentina may be better than the US for this:** imported aftermarket parts take longer, cost more and may not exist at all for local models (Fiat 128/147/Uno, Renault 12/18/Fuego, Ford Falcon/Sierra, Peugeot 504/205/206, VW Gol, Chevrolet Corsa). A part that is a USD 15 click away abroad can be a real gap here. **(VERIFY: current import rules and ML prices.)**

---

## 2. The E36 skirts and M-style moldings idea

### 2.1 Why full side skirts are a poor fit for one X2D
- Build volume is 256×256×260 mm. An E36 skirt is roughly 1.6–1.9 m long **(VERIFY)**, so each side needs **7–8 segments** with joints, bonding, filling and sanding.
- Rough capacity math (estimates, not measured): ~8–14 h per segment → **~120–200 print-hours per pair**. Your realistic capacity is ~200 h/month, so one pair can take 60–100% of the month.
- Machine-time floor: the cuota is 395,000/month over ~200 h, so the machine must earn **≥ ARS 2,000 per print-hour** just to cover itself. Aim for ARS 4,000+. A pair at 160 h needs a price of roughly **ARS 650k+** before paint and your labor. Check that against what a customer pays for an imported ABS or fiberglass pair **(VERIFY)**. If the import price is lower, printing loses.
- Finish is the real cost: filler primer, sanding and paint add many hours that the printer cannot do for you.

### 2.2 Where printing does help your friend
1. **Hardware kits (score 3rd of 16):** mounting brackets, clips, end caps and alignment jigs for skirts and moldings. Small, fit-critical, ARS 6–15k each, and the parts that are usually missing or broken on old cars.
2. **Plugs and patterns:** print the master shape, finish it, then cast silicone molds and pour or laminate copies. One plug serves many copies, so the machine hours are paid once. This is how a printed design becomes a repeatable product.
3. **Local classics with no aftermarket:** for models that have no ABS or fiberglass skirts at all (many older local cars), a segmented printed set can be a custom, higher-priced product. Quote per job, not per catalog.
4. **M-style moldings:** a long strip is mostly a finish and joint problem. Try TPU or ASA segments with hidden joints only after a single test strip.

### 2.3 Suggested way to work with your friend
- You print and finish hardware and patterns; they sell, install and handle paint.
- Test on **one car** first and photograph it for Rawspeed content.
- Agree the split in writing before the first job: who owns the designs, who buys material, who carries warranty claims.

---

## 3. Ranked project ideas
Scores 1–5 on demand, X2D fit, margin, local competition gap, effort, network synergy and safety/legal risk (`opportunities.py`). Weights: 20/20/20/15/10/10/5.

| # | Idea | Material | Tier | Score |
|--|--|--|--|--|
| 1 | Discontinued interior bezels, knobs, vent caps (local classics) | ASA/ABS | B/C | **4.55** |
| 2 | Interior trim clip & retainer kits by model | ASA/PETG | A/B | 4.15 |
| 3 | E36 hardware kits: skirt brackets, clips, end caps | ASA/PETG + PA6-CF | B | 4.10 |
| 4 | Camera car-mount accessories (Rawspeed) | PA6-CF/PETG | B/C | 4.10 |
| 5 | Aux-light brackets / mate mount | PA6-CF | C | 4.05 |
| 6 | Track-day mounts (camera, logger, dash) | PA6-CF | C | 3.90 |
| 7 | Model-specific console/cupholder inserts | ASA | B | 3.90 |
| 8 | UTN / SGS tooling, jigs, prototypes | PETG/PA6-CF | B/C | 3.85 |
| 9 | Model-specific phone mounts | ASA | B | 3.85 |
| 10 | Custom badges/emblems (own designs) | ASA/PETG | A/B | 3.75 |
| 11 | Plugs & patterns for fiberglass/silicone casting | PLA/PETG + finish | C | 3.70 |
| 12 | Engine-bay cable management | PAHT-CF | C | 3.70 |
| 13 | Gauge pods / aux gauge housings | ASA | B | 3.55 |
| 14 | STL licensing (Printables/Cults) | digital | – | 3.25 |
| 15 | M-style side moldings in segments | TPU/ASA | B | 3.15 |
| 16 | Full E36 side skirts, segmented FDM | ASA | C | **2.40** |

**Reading the ranking**
- **Top 5 share a profile:** small parts, ASA or PA6-CF, high local gap, and content you can film on a real car. They also fit your tiers B and C, so they raise your average ticket.
- **Your weights may differ.** Change `WEIGHTS` or any score in `opportunities.py` and rerun it.
- **Safety:** items 4, 6 and 7 hold cameras, lights or tools on a moving car. Design for a safety tether and state limits, and never print brake, steering or seatbelt parts.

---

## 4. Material-to-project map (X2D range)
| Material | Good for | Projects above | Watch out |
|---|---|---|---|
| PLA/PLA+ | Plugs, prototypes, desk items | 11, 14 | Softens near 55 °C: never inside a hot car |
| PETG | General functional, jigs | 2, 8, 11 | Moderate heat only |
| ASA/ABS | Interior and exterior trim, UV and heat | 1, 3, 7, 9, 10, 13, 15, 16 | Needs the enclosure and ventilation |
| TPU 95A | Seals, flexible moldings, bumpers | 15 | Slow; test AMS compatibility |
| PA6-CF / PAHT-CF | Brackets, mounts, under-hood | 3, 4, 5, 6, 12 | Dry filament, hardened nozzle |
| Support for PA/PET or ABS | Undercuts in engineering parts | 4, 5, 6 | Never PLA as support |
| PC, PC-CF, PPS-CF | Out of X2D range | – | Skip parts that need them |

If your own "FDM Materials Engineering Reference" differs from this table, paste it in a new chat and I will align the map.

---

## 5. How to validate before you buy filament (2 weeks, no printer needed)
| Step | What to do | Pass if |
|---|---|---|
| 1 | Search Mercado Libre and Instagram for each of your top 5 ideas. Note prices, sellers, review counts. | At least 3 sellers with sales, or none with clear demand |
| 2 | Post a poll and question box ("¿qué pieza no conseguís para tu auto?") | 20+ replies naming specific parts |
| 3 | Ask 3 car-club admins what parts members cannot find | 5+ concrete part requests |
| 4 | Quote 3 requested parts: material + hours × ARS 2,000 + finishing | Price ≥ 2× material cost and under the import price |
| 5 | Pre-sell 3 of them with a discount | 3 deposits |

Log each lead in the dashboard (Log data tab) with source and tier so the numbers feed the plan.

---

## 6. Risks specific to these projects
| Risk | Mitigation |
|---|---|
| Brand marks (BMW roundel, M stripes) | Do not copy logos or the M tricolor mark; sell "compatible with" shapes and your own badge designs |
| Design rights on body parts | Check whether any local registration covers E36-style skirts **(VERIFY)** before selling a copy of a branded design |
| Fit variation between car years/trims | Measure the actual car; sell by model-year with a fit guide |
| Finishing time eats the margin | Sell raw/primed parts and let the painter finish |
| Heat and UV failure | ASA or PA6-CF only on exterior or hot interior parts; test one sample in the sun and photograph it |
| Friend's business depends on you | Keep a written split, a backlog queue and a fixed turnaround |

---

## 7. Next steps
1. Run steps 1–3 of the validation table this week.
2. Pick the top 3 survivors and add them to the catalog (tiers, price, hours).
3. Ask your friend for the exact E36 model years and the 3 parts customers ask for most.
4. After the printer arrives, print one hardware kit and one plug sample and film both.

*Files: `opportunities.py` (scoring model) and `opportunities.csv` (ranked output).*
