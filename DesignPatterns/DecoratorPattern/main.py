from VanillaIceCream import VanillaIceCream
from ToppingDecorator import ChocolateSyrup, Sprinkles, Nuts

if __name__ == "__main__":
    # Create a simple vanilla ice cream
    ice_cream = VanillaIceCream()
    print(f"Description: {ice_cream.description()}")
    print(f"Cost: {ice_cream.cost()}")

    # Add chocolate syrup to the vanilla ice cream
    ice_cream_with_syrup = ChocolateSyrup(ice_cream)
    print(f"Description: {ice_cream_with_syrup.description()}")
    print(f"Cost: {ice_cream_with_syrup.cost()}")

    # Add sprinkles on top of chocolate syrup
    ice_cream_with_syrup_and_sprinkles = Sprinkles(ice_cream_with_syrup)
    print(f"Description: {ice_cream_with_syrup_and_sprinkles.description()}")
    print(f"Cost: {ice_cream_with_syrup_and_sprinkles.cost()}")

    # Add nuts on top of everything
    fully_loaded_ice_cream = Nuts(ice_cream_with_syrup_and_sprinkles)
    print(f"Description: {fully_loaded_ice_cream.description()}")
    print(f"Cost: {fully_loaded_ice_cream.cost()}")
