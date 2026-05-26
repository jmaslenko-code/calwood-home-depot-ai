# Dispute Template: Duplicate Deduction

## When to use this template

Use this template when the same deduction — for the same RTV, chargeback, freight charge, or shortage — appears **more than once** in Calwood's remittance records, and Home Depot has taken the money twice (or more).

Common duplicate scenarios:

- The same RTV number appears in two separate remittance periods
- The same chargeback is applied twice against different POs or payment runs
- A freight charge is billed once by the carrier and also deducted separately by Home Depot from remittance
- A shortage deduction appears in two different check runs for the same PO and SKU
- A credit was issued for a dispute but the original deduction was never reversed — the net result is zero recovery

## When NOT to use this template

Do not use this template if:

- The two deductions are for different RTVs, POs, or shipments that happen to be the same dollar amount
- One deduction is a legitimate second charge (e.g., a second RTV for a second shipment of the same product)
- The apparent duplicate is actually a prior-period deduction that was properly carried forward
- You have not yet cross-referenced both deduction IDs against the full remittance history

**Verify before submitting.** A duplicate dispute that turns out to be two distinct valid charges will damage credibility on future disputes.

---

## Required Fields

Fill in every field marked `[FILL]` before submitting.

| Field | Value |
|---|---|
| Deduction / RTV / Chargeback Number | `[FILL]` |
| First Deduction Date | `[FILL]` |
| First Deduction Remittance / Check # | `[FILL]` |
| First Deduction Amount | `[FILL]` |
| Second Deduction Date | `[FILL]` |
| Second Deduction Remittance / Check # | `[FILL]` |
| Second Deduction Amount | `[FILL]` |
| Total Amount Disputed | `[FILL — should equal one of the two deductions]` |
| PO Number | `[FILL]` |
| SKU / Vendor SKU | `[FILL]` |
| Product Description | `[FILL]` |
| Store Number (if applicable) | `[FILL]` |

---

## Evidence Checklist

Gather these before submitting.

- [ ] Remittance detail from first deduction period — showing deduction ID, date, and amount
- [ ] Remittance detail from second deduction period — showing same deduction ID, date, and amount
- [ ] Original RTV notice, chargeback notice, or freight invoice (whichever is being duplicated)
- [ ] Confirmation that the underlying event (return, violation, freight charge) is a single occurrence
- [ ] Any prior dispute correspondence showing the first deduction was already acknowledged or credited

**Strong case:** Same deduction ID appears on two separate remittances with no credit issued in between. Submit immediately.
**Medium case:** Two deductions for the same amount but slightly different reference numbers. Cross-reference both against the original notice before submitting.
**Do not submit:** Until you have confirmed both charges reference the same underlying event.

---

## Subject Line

```
Dispute — Duplicate Deduction — [DEDUCTION/RTV/CHARGEBACK NUMBER] — $[AMOUNT OF DUPLICATE] — Taken Twice — PO [PO NUMBER]
```

---

## Ticket Description (Copy-Paste)

```
Deduction / Reference Number: [FILL]
PO Number: [FILL]
SKU: [FILL]
Total Amount Taken: $[FILL — both deductions combined]
Amount Disputed (duplicate only): $[FILL — one deduction]

First Deduction:
  Date: [FILL]
  Remittance / Check #: [FILL]
  Amount: $[FILL]

Second Deduction:
  Date: [FILL]
  Remittance / Check #: [FILL]
  Amount: $[FILL]

---

Calwood Flooring Supply is disputing a duplicate deduction of $[FILL] taken against [RTV / CHARGEBACK / FREIGHT INVOICE] [FILL].

A review of Calwood's remittance records shows that this deduction was taken twice:

  - First occurrence: $[FILL] deducted from remittance [FILL] on [FILL]
  - Second occurrence: $[FILL] deducted from remittance [FILL] on [FILL]

Both deductions reference the same [RTV number / chargeback number / freight invoice number] and the same PO [FILL] for SKU [FILL]. This is a single event. Only one deduction is valid.

[INCLUDE IF APPLICABLE: Calwood accepted the first deduction on [DATE] / previously disputed the first deduction on [DATE]. In either case, a second deduction for the same charge is not appropriate.]

Calwood requests immediate reversal of the duplicate deduction in the amount of $[FILL], taken from remittance [FILL] on [FILL].

Attachments:
  - Remittance detail — [FILL period] showing first deduction
  - Remittance detail — [FILL period] showing second deduction
  - Original [RTV notice / chargeback notice / freight invoice] for reference

Calwood Contact: [FILL — name, email, phone]
```

---

## Completed Example

**Subject:**
```
Dispute — Duplicate Deduction — RTV 4419037 — $634.80 — Taken Twice — PO 6203712984
```

**Ticket:**
```
Deduction / Reference Number: RTV 4419037
PO Number: 6203712984
SKU: CAL-MP3-TR / HD Internet #: 311029847
Total Amount Taken: $1,269.60 (two deductions of $634.80 each)
Amount Disputed (duplicate only): $634.80

First Deduction:
  Date: February 14, 2025
  Remittance / Check #: HD-REM-20250214-0093
  Amount: $634.80

Second Deduction:
  Date: March 7, 2025
  Remittance / Check #: HD-REM-20250307-0041
  Amount: $634.80

---

Calwood Flooring Supply is disputing a duplicate deduction of $634.80 taken against RTV 4419037.

A review of Calwood's remittance records shows that this deduction was taken twice:

  - First occurrence: $634.80 deducted from remittance HD-REM-20250214-0093 on February 14, 2025
  - Second occurrence: $634.80 deducted from remittance HD-REM-20250307-0041 on March 7, 2025

Both deductions reference the same RTV 4419037 and the same PO 6203712984 for SKU CAL-MP3-TR (Calwood Maple 3 in. Solid Stair Tread). This is a single return event. Only one deduction of $634.80 is valid.

Calwood requests immediate reversal of the duplicate deduction in the amount of $634.80, taken from remittance HD-REM-20250307-0041 on March 7, 2025.

Attachments:
  - Remittance detail — February 14, 2025 (first deduction)
  - Remittance detail — March 7, 2025 (second deduction)
  - RTV 4419037 notice for reference

Calwood Contact: [Name], [email], [phone]
```

---

## Notes

- **Run a duplicate check on every remittance reconciliation.** Sort all deductions by reference number and look for repeated entries. This takes minutes and can catch hundreds or thousands of dollars in overcharges.
- **Credits issued but original deduction not reversed** is the most commonly missed duplicate. If Calwood won a prior dispute and received a credit memo, confirm the credit was actually applied to remittance. If the original deduction was also left standing, the net is zero and the dispute needs to be reopened.
- **Same amount, different reference numbers** requires more investigation. Pull both underlying notices and confirm they are truly the same event before disputing. If they are two distinct events that happen to be the same dollar amount, do not dispute — but document your review.
- When Home Depot responds, they may claim the second deduction was a correction or reissuance of the first. Ask them to explain the distinction in writing and provide documentation showing why two separate charges were appropriate for a single event.
