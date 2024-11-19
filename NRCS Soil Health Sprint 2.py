# Dictionary to store test results
assessment_results = {}

def main_menu():
    print("\n--- Soil Health Assessment Resource Indicator ---")
    print("1. Compaction Test Battery")
    print("2. Soil Organism Habitat Loss or Degradation Test Battery")
    print("3. Soil Organic Matter Depletion Test Battery")
    print("4. Aggregate Instability Test Battery")
    print("5. Generate Report")
    print("6. Exit")
    return input("Choose an option (1-6): ")

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
    compaction_status = "Healthy"

    # Soil Platyness Test
    print("\nSoil Platyness Test:")
    platyness = input("Are the soil particles arranged in thin flat layers? (y/n): ").lower()
    if platyness == 'y':
        contact_nrcs()
        compaction_status = "Concern Detected"

    # Additional compaction tests...
    print("\nPenetration Resistance Test:")
    print("Take a shovel and attempt to insert it into the ground. What happened?")
    print("1. Slides into soil")
    print("2. Takes effort to go into soil")
    print("3. Will not penetrate soil")
    resistance = get_valid_int("Enter your choice (1/2/3): ", [1, 2, 3])
    if resistance == 3:
        contact_nrcs()
        compaction_status = "Concern Detected"

    assessment_results['Compaction Test Battery'] = compaction_status
    print("\nCompaction Test Battery complete.")

def organism_tests():
    print("\n--- Soil Organism Habitat Loss or Degradation Test Battery ---")
    organism_status = "Healthy"

    print("\nSoil Cover Test:")
    soil_cover = int(input("What is the soil cover percentage? "))
    if soil_cover < 50:
        contact_nrcs()
        organism_status = "Concern Detected"

    assessment_results['Soil Organism Habitat Loss Test Battery'] = organism_status
    print("\nSoil Organism Habitat Loss Test Battery complete.")

def organic_matter_tests():
    print("\n--- Soil Organic Matter Depletion Test Battery ---")
    organic_matter_status = "Healthy"

    print("\nSoil Color Test:")
    print("1. Dark brown or black (healthy, high organic matter)")
    print("2. Reddish or yellowish (well-drained but low organic matter)")
    print("3. Gray or bluish (poorly drained, potential waterlogging)")
    soil_color = get_valid_int("Enter your choice (1/2/3): ", [1, 2, 3])
    if soil_color in [2, 3]:
        contact_nrcs()
        organic_matter_status = "Concern Detected"

    assessment_results['Soil Organic Matter Depletion Test Battery'] = organic_matter_status
    print("\nSoil Organic Matter Depletion Test Battery complete.")

def aggregate_instability_tests():
    print("\n--- Aggregate Instability Test Battery ---")
    aggregate_status = "Healthy"

    print("\nSoil Breaks Apart Test:")
    breaks_apart = input("Does the soil break apart easily? (y/n): ").lower()
    if breaks_apart == 'n':
        contact_nrcs()
        aggregate_status = "Concern Detected"

    assessment_results['Aggregate Instability Test Battery'] = aggregate_status
    print("\nAggregate Instability Test Battery complete.")

def generate_report():
    if not assessment_results:
        print("\nNo assessments have been completed yet.")
        return
    
    print("\n--- Soil Health Assessment Report ---")
    for test, result in assessment_results.items():
        print(f"{test}: {result}")
    
    if "Concern Detected" in assessment_results.values():
        print("\nAction Required: One or more resource concerns were detected. Contact your local NRCS office for assistance.")
    else:
        print("\nAll tests indicate healthy soil. No immediate action required.")

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
            aggregate_instability_tests()
        elif choice == '5':
            generate_report()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
