from typing import Tuple

FOX_PER_BATCH     = 72
GOOSE_PER_BATCH   = 18
BOOZE_PER_BATCH   = 18
COST_TO_MAKE      = 3524
POTIONS_PER_BATCH = 5
PREMIUM_TAXRATE   = 4
MAKER_FEE         = 2.5

def parse_money(x: str) -> float:
    """
    Accepts '4000', '4,000', '  4000  '.
    Blank input => 0.
    """
    x = x.strip()
    if not x:
        return 0.0
    return float(x.replace(',', ''))

def get_inputs() -> Tuple[float, float, float, float]:
    goose = float(input('Goose unit price (silver): '))
    fox   = float(input('Fox unit price (silver): '))
    booze = float(input('Booze unit price (silver): '))
    build_eff = float(input('Build effi. %: '))

    return goose, fox, booze, build_eff

def cost_per_batch(
    goose: float, fox: float, booze: float, COST_TO_MAKE: float
) -> float:
    """
    Total ingredient cost for one batch of 5 potions + flat purchase/crafting fee.
    """
    base = (
        fox   * FOX_PER_BATCH +
        goose * GOOSE_PER_BATCH +
        booze * BOOZE_PER_BATCH
    )
    return base + COST_TO_MAKE


'''
PREMIUM_TAXRATE   = 4
MAKER_FEE         = 2.5
'''
def analyze_profit(
    goose: float, fox: float, booze: float, build_eff: float
    
) -> None:

    ingre_total = FOX_PER_BATCH + GOOSE_PER_BATCH + BOOZE_PER_BATCH
    therotical_build = build_eff * 0.01 # Converts input into decimal
    saved_fox = FOX_PER_BATCH - float(FOX_PER_BATCH * therotical_build)
    saved_goose = GOOSE_PER_BATCH - float(GOOSE_PER_BATCH * therotical_build)
    saved_booze = BOOZE_PER_BATCH - float(BOOZE_PER_BATCH * therotical_build)
    
    est_return = ingre_total * therotical_build # Ingrentigent total with input return rate
    total_saved_est = ingre_total - est_return # Value of estimated total saved mats

    batch_cost     = cost_per_batch(goose, fox, booze, COST_TO_MAKE)  # Cost of ingrentients and build cost
    per_pot_cost   = batch_cost / POTIONS_PER_BATCH # Single potion cost

    batch_cost_wreturn     = saved_goose + saved_fox + saved_booze + COST_TO_MAKE  # Cost of ingrentients and build cost
    per_pot_cost_wreturn   = batch_cost_wreturn / POTIONS_PER_BATCH # Single potion cost
 

    print(f"\n--- Potion Profitability ---")
    print(f"Recipe: {FOX_PER_BATCH} fox, {GOOSE_PER_BATCH} goose, {BOOZE_PER_BATCH} booze → {POTIONS_PER_BATCH} potions")
    print(f"Recipe (wReturn): {saved_fox} fox, {saved_goose} goose, {saved_booze} booze → {POTIONS_PER_BATCH} potions")
    print(f"Ingredient cost (no fees):        {(batch_cost):,.0f} silver")
    print(f"Build Efficeny:                   {(build_eff):,.0f}% ")
    print(f"="*28)
    print(f"Cost per potion (RAW):            {per_pot_cost:,.0f} silver")
    print(f"Cost per potion (wReturn):        {per_pot_cost_wreturn:,.0f} silver")
    print(f"="*28)
    print(f"Cost per potion w/ Tax:           {per_pot_cost_wreturn:,.0f} silver")
    print(f"Cost per potion w/ Tax (wReturn): {per_pot_cost_wreturn:,.0f} silver")
    print(f"="*20)

if __name__ == "__main__":
    goose, fox, booze, build_eff = get_inputs()
    analyze_profit(goose, fox, booze, build_eff)
