"""Scores new-project ideas for the X2D venture. Edit SCORES/WEIGHTS, run `python3 opportunities.py`.
Each criterion is 1-5, where 5 is best (for effort: 5 = least effort; for risk: 5 = safest).
Writes opportunities.csv ranked by weighted score."""
import csv

WEIGHTS = dict(demand=.20, fit=.20, margin=.20, gap=.15, effort=.10, synergy=.10, safety=.05)

# name, material, tier, then scores in WEIGHTS order
IDEAS = [
 ("Discontinued interior bezels/knobs/vent caps (local classics)", "ASA/ABS",   "B/C", 4,5,5,5,3,5,4),
 ("E36 hardware kits: skirt brackets, clips, end caps",           "ASA/PETG+PA6-CF", "B", 3,5,4,4,4,5,4),
 ("Interior trim clip & retainer kits by model",                  "ASA/PETG",   "A/B", 4,5,3,4,5,4,5),
 ("Aux-light brackets / mate mount",                              "PA6-CF",     "C",   3,5,5,4,3,4,3),
 ("UTN / SGS tooling, jigs, prototypes",                          "PETG/PA6-CF","B/C", 3,5,4,4,3,3,5),
 ("Plugs & patterns for fiberglass/silicone casting",             "PLA/PETG+finish","C",3,4,4,4,2,5,4),
 ("Track-day mounts (camera, logger, dash)",                      "PA6-CF",     "C",   3,5,4,3,4,5,3),
 ("Camera car-mount accessories (Rawspeed)",                      "PA6-CF/PETG","B/C", 3,5,5,3,4,5,3),
 ("Model-specific console/cupholder inserts",                     "ASA",        "B",   3,5,4,3,4,4,5),
 ("Engine-bay cable management",                                  "PAHT-CF",    "C",   3,4,4,4,4,3,4),
 ("Gauge pods / aux gauge housings",                              "ASA",        "B",   3,4,4,3,3,4,4),
 ("Custom badges/emblems (own designs)",                          "ASA/PETG",   "A/B", 4,4,4,3,4,4,2),
 ("Model-specific phone mounts",                                  "ASA",        "B",   4,5,3,2,5,4,5),
 ("M-style side moldings in segments",                            "TPU/ASA",    "B",   3,3,3,3,2,5,4),
 ("STL licensing (Printables/Cults)",                             "digital",    "-",   2,5,3,2,3,4,5),
 ("Full E36 side skirts, segmented FDM",                          "ASA",        "C",   3,1,2,3,1,5,3),
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
