"""Scores new-project ideas for the X2D venture. Edit SCORES/WEIGHTS, run `python3 opportunities.py`.
Criteria: demand (local, from your experience), X2D fit, margin, supply gap (parts lost by the market), effort, synergy (brands and network you know), safety. Each criterion is 1-5, where 5 is best (for effort: 5 = least effort; for risk: 5 = safest).
Writes opportunities.csv ranked by weighted score."""
import csv

WEIGHTS = dict(demand=.20, fit=.20, margin=.20, gap=.15, effort=.10, synergy=.10, safety=.05)

# name, material, tier, then scores in WEIGHTS order
IDEAS = [
 ("Alfa Romeo 33/145/155/164/916: interior trim, vents, handles", "ASA/ABS",   "B/C", 5,5,5,5,3,5,4),
 ("BMW E30/E36/E34: interior clips, trim, regulator clips",       "ASA/PETG",  "A/B", 5,5,4,4,4,5,4),
 ("Honda Civic/Integra/Accord/CRX: interior plastics",            "ASA/PETG",  "A/B", 5,5,4,4,4,5,4),
 ("General clip & retainer kits (any pre-2000 car)",              "ASA/PETG",  "A",   4,5,3,4,5,4,5),
 ("E36 hardware kits: skirt brackets, molding clips, end caps",   "ASA/PETG+PA6-CF","B",3,5,4,4,4,5,4),
 ("General non-pressure brackets and mounts",                     "PA6-CF/ASA","B/C", 3,5,5,4,3,4,3),
 ("Aux-light brackets / mate mount",                              "PA6-CF",    "C",   3,5,5,4,3,4,3),
 ("Camera car-mount accessories (Rawspeed)",                      "PA6-CF/PETG","B/C",3,5,5,3,4,5,3),
 ("Track-day mounts (camera, logger, dash)",                      "PA6-CF",    "C",   3,5,4,3,4,5,3),
 ("Patterns for casting rare bodies and panels",                  "PLA/PETG+finish","C",3,4,4,4,2,4,4),
 ("UTN / SGS tooling, jigs, prototypes",                          "PETG/PA6-CF","B/C",3,5,4,4,3,3,5),
 ("Model-specific console/cupholder inserts",                     "ASA",       "B",   3,5,4,3,4,4,5),
 ("Model-specific phone mounts",                                  "ASA",       "B",   4,5,3,2,5,4,5),
 ("Custom badges/emblems (own designs)",                          "ASA/PETG",  "A/B", 4,4,4,3,4,4,2),
 ("Gauge pods / aux gauge housings",                              "ASA",       "B",   3,4,4,3,3,4,4),
 ("STL licensing (Printables/Cults)",                             "digital",   "-",   2,5,3,2,3,4,5),
 ("M-style side moldings in segments",                            "TPU/ASA",   "B",   3,3,3,3,2,5,4),
 ("Full E36 side skirts, segmented FDM",                          "ASA",       "C",   3,1,2,3,1,5,3),
]

def score(row):
    return sum(w * s for w, s in zip(WEIGHTS.values(), row[3:]))

if __name__ == "__main__":
    ranked = sorted(IDEAS, key=score, reverse=True)
    with open("opportunities.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["rank", "idea", "material", "tier", *WEIGHTS, "score"])
        for i, r in enumerate(ranked, 1): w.writerow([i, r[0], r[1], r[2], *r[3:], round(score(r), 2)])
    print("| # | Idea | Material | Tier | Score |\n|--|--|--|--|--|")
    for i, r in enumerate(ranked, 1): print(f"| {i} | {r[0]} | {r[1]} | {r[2]} | {score(r):.2f} |")
