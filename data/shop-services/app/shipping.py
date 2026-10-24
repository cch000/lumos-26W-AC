"""ZIP -> NorthStar Parcel zone -> shipping rate. Rates = our negotiated NorthStar Parcel rates for 2022/23."""
import csv
from pathlib import Path

ZONES_FILE = Path(__file__).resolve().parent.parent / "config" / "shipping_zones.csv"

GROUND_RATES = {2: 5.10, 3: 5.55, 4: 6.10, 5: 6.80, 6: 7.45, 7: 8.60, 8: 9.40}
GROUND_EXTRA_UNIT = 0.55

EXPRESS_AIR = "Express Air"
EXPRESS_AIR_RATE = 16.40
EXPRESS_EXTRA_UNIT = 0.85


def load_zones(path=ZONES_FILE):
    zones = []
    with open(path, newline="") as f:
        lines = [line for line in f if line.strip() and not line.startswith("#")]
    for row in csv.DictReader(lines):
        zones.append((int(row["dest_zip3_from"]), int(row["dest_zip3_to"]), int(row["zone"])))
    return zones


ZONES = load_zones()


def zone_for_zip(zip_code):
    zip3 = int(str(zip_code).strip()[:3])
    for lo, hi, zone in ZONES:
        if lo <= zip3 <= hi:
            return zone
    return None


def rate_for_zip(zip_code, units=1):
    """Returns {"service", "zone", "cost"} for one parcel with `units` items."""
    units = max(int(units), 1)
    zone = zone_for_zip(zip_code)
    if zone is None:
        # unknown zone -> ship express so we never miss SLA
        cost = EXPRESS_AIR_RATE + EXPRESS_EXTRA_UNIT * (units - 1)
        return {"service": EXPRESS_AIR, "zone": None, "cost": round(cost, 2)}
    cost = GROUND_RATES[zone] + GROUND_EXTRA_UNIT * (units - 1)
    return {"service": "Ground", "zone": zone, "cost": round(cost, 2)}
