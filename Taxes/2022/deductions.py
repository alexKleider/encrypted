#!/usr/bin/env python3

# File: ~/Encrypted/Taxes/2022/deductions.py

deductions = {
        'real_estate': [
            4865.54,  # Loft 12/12/22
            4779.05,  # Loft 4/9/22
            11442.09, # Bolinas 4/9/22
            11630.66, # Bolinas 12/9/22
            ],
        'personal_property':[
            131,  # 2002 Merz
            249,  # Motor home
            1,    # Jeep
            ],
        }

def main():
    real_estate_total = 0
    personal_property_total = 0
    for tax in deductions['real_estate']:
        real_estate_total += tax
    for tax in deductions['personal_property']:
        personal_property_total += tax
    print(f"Real estate taxes paid: {real_estate_total}")
    print(
    f"Personal Property taxes paid: {personal_property_total}")
    total = real_estate_total + personal_property_total
    print(f"Total deduction: {total}")


if __name__ == '__main__':
    main()
