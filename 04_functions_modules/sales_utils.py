# sales_utils.py
from pathlib import Path
from collections import defaultdict
import csv
from typing import Dict, Iterable, Tuple

# ----------Reading-----------------------
def load_sales_text(path: Path) -> Iterable[Tuple[str, int]]:
    """
    Read a simple 'product,quantity' TXT file line by line.
    Yields tuples:(product, quantity).
    Skips invalid lines but does not raise
    """
    with path.open("r", encoding="utf-8") as f:
        for line_num, raw in enumerate(f, start=1):
            line = raw.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                print(f'[WARN] Line {line_num}: wrong format -> {line!r}')
                continue
            product, qty_str = parts[0].strip(), parts[1].strip()
            if not product:
                print(f"[WARN] Line {line_num}: empty product -> {line!r}")
                continue
            try:
                qty = int(qty_str)
            except ValueError:
                print(f"[WARN] Line {line_num}: quantity is not integer -> {qty_str!r}")
                continue
            yield product, qty

def load_sales_csv(path: Path) -> Iterable[Tuple[str, int]]:
    """
    Same idea, but using csv.reader (safer for commas/spaces/quotes).
    """
    with path.open("r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="," , skipinitialspace=True)
        for line_num, row in enumerate(reader, start=1):
            if not row:
                continue
            if len(row) !=2:
                print(f"[WARN] Line {line_num}: wrong format -> {row}")
                continue
            product, qtry_str = row[0].strip(), row[1].strip()
            if not product:
                print(f"[WARN] Line {line_num}: empty product -> {row}")
                continue
            try:
                qty = int(qtry_str)
            except ValueError:
                print(f"[WARN] Line {line_num} quantity is not integer -> {qtry_str}")
                continue
            yield product, qty

# ----------Aggregation-----------------------
def summarize_sales(pairs: Iterable[Tuple[str, int]]) -> Dict[str, int]:
    """
    Aggregate quantities per product.
    """
    totals: Dict[str, int] = defaultdict(int)
    for product, qty in pairs:
        totals[product] += qty
    return dict(totals)

# ----------Writing-----------------------
def save_summary_text(path: Path, summary: Dict[str, int], order: str = "alpha") -> None:
    """
    Save summary to a TXT file as 'Product: total' per line.
    order: 'alpha' (alphabetical) or 'desc' (by total desc).
    """
    if order =="desc":
        items = sorted(summary.items(), key=lambda kv: kv[1], reverse=True)
    else:
        items = sorted(summary.items(), key=lambda kv: kv[0])

    with path.open("w", encoding="utf-8") as f:
        for product, total in items:
            f.write(f"{product}: {total}\n")
