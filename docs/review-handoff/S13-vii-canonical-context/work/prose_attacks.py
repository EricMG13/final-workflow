from deploy_vii.prose import bare_figures, check
cases = [
    "Covenant headroom was breached in 3 of 4 quarters.",            # issuer fact as 'coverage' label
    "Leverage rose to seven times EBITDA and revenue halved.",        # spelled numbers
    "Liquidity covers 18 months of interest.",                        # control: should flag
    "Revenue grew in 2025 to 2030 levels.",                           # year label, fine
    "Net leverage of 12.5% senior notes due 2031 is unsustainable.",  # coupon via instrument label
    "Leverage of 6x.",                                                # control
    "EBITDA margin fell by 2024 basis points.",                       # year-shaped figure
]
for c in cases:
    print(repr(c), "->", bare_figures(c), check(c, refs=(), gaps=()))
