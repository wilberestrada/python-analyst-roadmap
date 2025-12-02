# process_sales.py
from pathlib import Path

def main():
    base = Path(__file__).parent
    input_path = base / "dirty_sales_data.txt"
    errors_path = base / "errors.log"
    summary_path = base / "summary.txt"

    totals = {}

    with input_path.open("r", encoding="utf-8") as f, \
    errors_path.open("w", encoding="utf-8") as log:
        
        for num_line, raw in enumerate(f, start=1):
            line = raw.strip()

            # 1) Skip empty lines
            if not line:
                continue

            # 2) Try to separate by product and quantity
            try:
                product, qty_str = line.split(",")
            except ValueError:
                log.write(f"Line {num_line}: incorrect format -> {line!r}\n")
                continue

            # 3) Validate product
            product = product.strip()
            if not product:
                log.write(f"Line {num_line}: empty product -> {line!r}\n")
                continue

            # 4) Validate quantity
            qty_str = qty_str.strip()
            try:
                qty = int(qty_str)
            except ValueError:
                log.write(f"Line {num_line}: invalid amount -> {line!r}\n")
                continue

            # 5) Validate negative amount
            if qty < 0:
                log.write(f"Line {num_line}: negative amount -> {line!r}\n")
                continue

            # 6) Acummulate
            totals[product] = totals.get(product, 0) + qty

    # 7) Save summary
    with summary_path.open("w", encoding="utf-8") as out:
        for product in sorted(totals):
            out.write(f"{product}: {totals[product]}\n")

    print("Processing completed")

if __name__ == "__main__":
    main()
