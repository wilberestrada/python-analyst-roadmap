from pathlib import Path
from sales_utils import load_sales_csv, summarize_sales, save_summary_text

def main():
    base = Path(__file__).parent
    in_path = base / "sales.txt"
    out_path = base / "resumen.txt"

    # 1)
    pairs = load_sales_csv(in_path)

    # 2)
    totals = summarize_sales(pairs)

    # 3)
    save_summary_text(out_path, totals, order="alpha")

    print("Done! Wrote:", out_path)

if __name__ == "__main__":
    main()
