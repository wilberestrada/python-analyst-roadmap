from pathlib import Path
from email_validator import validate_email, EmailNotValidError

def main():
    base = Path(__file__).parent
    input_path = base / "dirty_customers.txt"
    log_path = base / "customers_errors.log"
    output_path = base / "clear_customers.txt"

    valid_customers = []

    with input_path.open("r", encoding="utf-8") as f, \
        log_path.open("w", encoding="utf-8") as log:

        for num_line, raw in enumerate(f, start=1):
            line = raw.strip()

            # Skip empty lines
            if not line:
                continue

            # Separate values
            try:
                name, age_str, email = line.split(",")
            except ValueError:
                log.write(f"Line {num_line}: incorrect format -> {line!r}\n")
                continue

            # Validate name
            name = name.strip()
            if not name:
                log.write(f"Line {num_line}: empty name -> {line!r}\n")
                continue

            # Validate age
            age_str = age_str.strip()
            try:
                age = int(age_str)
            except ValueError:
                log.write(f"Line {num_line}: invalid age -> {line!r}\n")
                continue

            # Validate negative age
            if age < 0:
                log.write(f"Line {num_line}: invalid age -> {line!r}\n")
                continue

            # Validate email
            email = email.strip()
            try:
                validate = validate_email(email,check_deliverability=False)
                email_validated = validate.email
            except ValueError:
                log.write(f"Line {num_line}: invalid email -> {line!r}\n")
                continue

            # Acumulate
            valid_customers.append((name, age, email_validated))

    with output_path.open("w", encoding="utf-8") as out:
        for name, age, email_validated in sorted(valid_customers):
            out.write(f"{name},{age},{email_validated}\n")
            
    print("Clientes procesados.")

if __name__ == "__main__":
    main()
