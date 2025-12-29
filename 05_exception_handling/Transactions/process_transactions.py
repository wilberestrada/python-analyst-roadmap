from pathlib import Path
from datetime import datetime

def main():
    base = Path(__file__).parent
    input_path = base / "dirty_transactions.txt"
    clean_path = base / "clean_transactions.txt"
    log_path = base / "transactions_errors.log"
    summary_path = base / "summary.txt"

    valid_transactions = []
    invalid_count = 0
    balance = 0.0
    valid_types = {"DEPOSIT","WITHDRAW","TRANSFER"}
    subtract_types = {"WITHDRAW","TRANSFER"}
    add_types = {"DEPOSIT"}

    with input_path.open("r", encoding="utf-8") as f, \
        log_path.open("w", encoding="utf-8") as log:

        for num_line, raw_line in enumerate(f, start=1):
            line = raw_line.strip()

            if not line:
                continue

            # 1) Try to separate files: date, type, amount
            try:
                date_str, type_str, amount_str = line.split(",")
            except ValueError:
                log.write(f"Line {num_line}: incorrect format -> {line!r}\n")
                invalid_count += 1
                continue

            # 2) Validate date
            date_clean = date_str.strip()
            try:
                format_date = datetime.strptime(date_clean, "%Y-%m-%d").date()
                format_date_str = format_date.strftime("%Y-%m-%d")

            except ValueError:
                log.write(f"Line {num_line}: incorrect date -> {line!r}\n")
                invalid_count += 1
                continue

            # 3) Validate type
            trx_type = type_str.strip().upper()
            if (trx_type not in valid_types):
                log.write(f"Line {num_line}: invalid transaction type -> {line!r}\n")
                invalid_count += 1
                continue

            # 4) Validate amount
            amount_clear = amount_str.strip()
            try:
                amount = round(float(amount_clear),2)
            except ValueError:
                log.write(f"Line {num_line}: incorrect amount -> {line!r}\n")
                invalid_count += 1
                continue
            # 4.1) Validate negative amount
            if amount <= 0:
                log.write(f"Line {num_line}: negative amount or equal to zero -> {line!r}\n")
                invalid_count += 1
                continue

            # 5) Update balance by type            
            if (trx_type in add_types):
                balance += amount
            if (trx_type in subtract_types):
                balance -= amount

            # 6) add to valid_transactions  as tuple
            valid_transactions.append((format_date_str, trx_type, amount))
            valid_trx_count = len(valid_transactions)
            
    # 7) Write clean_transactions.txt
    with clean_path.open("w", encoding="utf-8") as out:
        for format_date_str, trx_type, amount in sorted(valid_transactions):
            out.write(f"{format_date_str},{trx_type},{amount}\n")    

    # 8) Write summary.txt  
    with summary_path.open("w", encoding="utf-8") as out:
        out.write(f"Total valid transactions: {len(valid_transactions)}\n")
        out.write(f"Total invalid transactions: {invalid_count}\n")
        out.write(f"Total processed lines: {valid_trx_count + invalid_count}\n")
        out.write(f"Final balance: {balance}\n")

    print("Process transactions.")

if __name__ == "__main__":
    main()
