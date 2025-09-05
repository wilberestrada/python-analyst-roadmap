from pathlib import Path
from collections import defaultdict
import csv


def main():
    base = Path(__file__).parent
    in_path = base / "sales.txt"
    out_path = base / "summary.txt"

    totals = defaultdict(int)

    with in_path.open("r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",", skipinitialspace=True)
        for lineno, row in enumerate(reader, start=1): # index control
            if not row :
                continue
            if len(row) != 2:
                print(f"[WARN] Line {lineno}: wrong format -> {row}")
                continue
            product, qty_str = row[0].strip(), row[1].strip() 
            if not product: # Check if the product comes empty
                print(f"[WARN] Line {lineno}: empty product -> {row}")
                continue
            try:
                qty = int(qty_str)
            except ValueError: # Check if amount is empty or different to 0.
                print(f"[WARN] Line {lineno}: quantity is not integer -> {qty_str!r}")
                continue
            totals[product] += qty
    
    # Write sorted alphabetically
    with out_path.open("w", encoding="utf-8") as f:
        for product in sorted(totals.keys()):
            f.write(f"{product}: {totals[product]}\n")

    print("Done! Wrote:", out_path)

if __name__ == "__main__":
    main()

