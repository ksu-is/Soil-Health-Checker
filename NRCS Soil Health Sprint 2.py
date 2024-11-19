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
    print("Are the soil particles arranged in thin flat layers, like cake layers stacked horizontally?")
    platyness = input("Answer (y/n): ").lower()
    if platyness == 'y':
        contact_nrcs()
        compaction_status = "Concern Detected"
    
    # Add more compaction test logic here, similar to the previous...

    assessment_results['Compaction Test Battery'] = compaction_status


def generate_report():
    if not assessment_results:
        print("\nNo assessments have been completed yet.")
        
