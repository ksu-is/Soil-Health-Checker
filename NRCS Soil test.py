def main_menu():
    print("\n--- Soil Health Assessment Resource Indicator ---")
    print("1. Compaction Test Battery")
    print("2. Soil Organism Habitat Loss or Degradation Test Battery")
    print("3. Soil Organic Matter Depletion Test Battery")
    print("4. Aggregate Instability Test Battery")
    print("5. Exit")
    return input("Choose an option (1-5): ")

def contact_nrcs():
    print("\nResource Concern Identified! Please contact your local NRCS office for assistance.")
    print("Visit: https://www.nrcs.usda.gov/")

def get_valid_int(prompt, valid_choices):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in valid_choices:
                return user_input
            else:
                print(f"Invalid choice. Please select from {valid_choices}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def compaction_tests():
    print("\n--- Compaction Test Battery ---")

    # Soil Platyness Test
    print("\nSoil Platyness Test:")
    print("Are the soil particles arranged in thin flat layers, like cake layers stacked horizontally?")
    platyness = input("Answer (y/n): ").lower()
    if platyness == 'y':
        contact_nrcs()
        return

    # Ponding/Infiltration Test
    print("\nPonding/Infiltration Test:")
    print("Is the water standing on top of the soil a day after a hard rain?")
    ponding = input("Answer (y/n): ").lower()
    if ponding == 'y':
        contact_nrcs()
        return

    # Penetration Resistance Test
    print("\nPenetration Resistance Test:")
    print("Take a shovel and attempt to insert it into the ground. What happened?")
    print("1. Slides into soil")
    print("2. Takes effort to go into soil")
    print("3. Will not penetrate soil")
    resistance = get_valid_int("Enter your choice (1/2/3): ", [1, 2, 3])
    if resistance == 3:
        contact_nrcs()
        return

    # Water-Stable Aggregates Test
    print("\nWater-Stable Aggregates Test:")
    print("1. Take a clear cup or jar and place a wire mesh on top.")
    print("2. Put a handful of soil on top of the wire mesh.")
    print("3. Pour enough water to cover the soil. Observe how cloudy the water becomes:")
    print("1. Clear")
    print("2. Slightly Cloudy")
    print("3. Dark")
    water_cloudiness = get_valid_int("Enter your choice (1/2/3): ", [1, 2, 3])
    if water_cloudiness == 3:
        contact_nrcs()
        return

    # Soil Structure Test
    print("\nSoil Structure Test:")
    print("1. Cut a square 1 ft deep into the ground and pull it out with a shovel.")
    print("2. Break the soil apart with your hands. What happened?")
    print("1. Breaks into blocks smaller than your hand (sign of good structure)")
    print("2. Won't break apart")
    print("3. Breaks into blocks larger than your hand or looks like bread with a crust and layers beneath")
    structure = get_valid_int("Enter your choice (1/2/3): ", [1, 2, 3])
    if structure in [2, 3]:
        contact_nrcs()
        return

    # Plant Roots Test
    print("\nPlant Roots Test:")
    print("1. Find a grassy area and dig up a handful of plants with roots attached.")
    print("2. Observe the roots:")
    roots_covered = input("Are the roots covered in soil? (y/n): ").lower()
    roots_extended = input("Are the roots fully extended? (y/n): ").lower()
    if roots_covered == 'n' or roots_extended == 'n':
        contact_nrcs()
        return

    print("\nSoil is non-compacted. Compaction Test Battery complete.")

def organism_tests():
    print("\n--- Soil Organism Habitat Loss or Degradation Test Battery ---")

    # Soil Cover Test
    print("\nSoil Cover Test:")
    print("1. Select a few spots in your field where soil cover might vary.")
    print("2. Lay a string or tape measure diagonally across a small area (e.g., 3-4 feet).")
    print("3. Count the number of points along the string where soil is covered by plants or mulch.")
    print("4. Calculate the percentage of soil cover. Example: (15 ÷ 20) × 100 = 75%")
    soil_cover = int(input("What is the soil cover percentage? "))
    if soil_cover < 50:
        contact_nrcs()
        return

    # Surface Crusts Test
    print("\nSurface Crusts Test:")
    print("Use a spade or knife to scrape the top 1 inch of soil. Does the soil break apart in hard, compacted pieces?")
    crusts = input("Answer (y/n): ").lower()
    if crusts == 'y':
        contact_nrcs()
        return

    print("\nSoil Organism Habitat is healthy. Test Battery complete.")

def organic_matter_tests():
    print("\n--- Soil Organic Matter Depletion Test Battery ---")

    # Soil Color Test
    print("\nSoil Color Test:")
    print("1. Dig a small hole about 6 inches deep.")
    print("2. Remove a handful of soil from the mid-depth and spread it thinly on a white surface.")
    print("3. Observe the color. What is the soil color?")
    print("1. Dark brown or black (healthy, high organic matter)")
    print("2. Reddish or yellowish (well-drained but low organic matter)")
    print("3. Gray or bluish (poorly drained, potential waterlogging)")
    soil_color = get_valid_int("Enter your choice (1/2/3): ", [1, 2, 3])
    if soil_color in [2, 3]:
        contact_nrcs()
        return

    print("\nSoil Organic Matter levels are sufficient. Test Battery complete.")

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            compaction_tests()
        elif choice == '2':
            organism_tests()
        elif choice == '3':
            organic_matter_tests()
        elif choice == '4':
            print("Aggregate Instability Tests Coming Soon!")
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
