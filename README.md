# ISBN

**Definition**: An ISBN (International Standard Book Number) is a unique identifier for books. ISBNs were 10 digits until December 2006, and since January 2007, they consist of 13 digits. They include a check digit for validation.

**Structure**:
- Prefix (3 digits): Currently, only 978 or 979.
- Registration Group (1-5 digits): Identifies country, region, or language.
- Registrant (Up to 7 digits): Identifies the publisher.
- Publication (Up to 6 digits): Identifies edition and format.
- Check Digit (1 digit): Validates the ISBN using a Modulus 10 system.

**Validation**:
1. For a 10-digit ISBN, assign positions, multiply each by its position, and sum the products.
2. Divide the sum by 11; if the remainder is zero, it's valid.

3. For a 13-digit ISBN, assign positions, multiply odd positions by 1 and even positions by 3, sum the products.
4. Divide the sum by 10; if the remainder is zero, it's valid.

---

# UPC (Universal Product Code)

**Definition**: A UPC (Universal Product Code) is a code on retail product packaging to identify an item. It consists of a machine-readable barcode and a unique 12-digit number.

**Structure**:
- Manufacturer ID (First 6 digits)
- Item Number (Next 5 digits)
- Check Digit (Last digit)

**Validation**:
1. Sum odd-positioned digits and multiply by 3.
2. Sum even-positioned digits.
3. Add the results, subtract from the next higher multiple of 10.
4. If the check digit and the result are equal, UPC is valid.

---

# Cards (MasterCard, Visa Card)

## MasterCard

**Definition**: MasterCard is a global payment technology company providing a platform for electronic payments, including credit, debit, commercial, and prepaid cards.

**Structure**:
- Most cards have 16 digits.
- First digit: Major Industry Identifier (MII).
  - 5: Mastercard

**Validation**:
- Luhn's algorithm is used for validation.

## Visa Card

**Definition**: A Visa card uses the Visa network, branded by Visa. It includes credit, debit, prepaid, and gift cards.

**Structure**:
- Most cards have 16 digits.
- First digit: MII.
  - 4: Visa

**Validation**:
- Luhn's algorithm is used for validation.

**Additional Information**:
- The back of the card includes an expiry date and CVV number.
- The first six digits indicate the Issuer Identification number (IIN).
- The following numbers indicate the specific issuing bank.
- The next six numbers indicate the account number assigned to individual customers.

---

**Validation**:
- Luhn's algorithm determines whether a credit card number is valid.
- Double the value of every other digit from right to left.
- Add the digits to the remaining digits.
- If the result mod 10 is 0, the number is valid.
