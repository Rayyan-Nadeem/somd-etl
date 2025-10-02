import json
import os
from collections import Counter

def analyze_unique_roles():
    """
    Analyze the sport.json file to find all unique volunteer roles
    and provide statistics about their usage.
    """
    # Path to the sport.json file
    json_file_path = os.path.join("sports & Events", "sport.json")
    
    try:
        # Read the JSON file
        with open(json_file_path, 'r', encoding='utf-8') as file:
            sports_data = json.load(file)
        
        # Extract all roles from volunteers
        all_roles = []
        sports_with_volunteers = 0
        total_volunteers = 0
        
        for sport in sports_data:
            volunteers = sport.get('volunteers', [])
            if volunteers:
                sports_with_volunteers += 1
                total_volunteers += len(volunteers)
                
                for volunteer in volunteers:
                    role = volunteer.get('role')
                    if role:
                        all_roles.append(role)
        
        # Count unique roles
        role_counts = Counter(all_roles)
        unique_roles = set(all_roles)
        
        # Display results
        print("=" * 60)
        print("UNIQUE VOLUNTEER ROLES ANALYSIS")
        print("=" * 60)
        print(f"Total sports in dataset: {len(sports_data)}")
        print(f"Sports with volunteers: {sports_with_volunteers}")
        print(f"Total volunteers: {total_volunteers}")
        print(f"Total role entries: {len(all_roles)}")
        print(f"Number of unique roles: {len(unique_roles)}")
        
        print("\n" + "=" * 40)
        print("UNIQUE ROLES FOUND:")
        print("=" * 40)
        for i, role in enumerate(sorted(unique_roles), 1):
            print(f"{i}. {role}")
        
        print("\n" + "=" * 40)
        print("ROLE FREQUENCY DISTRIBUTION:")
        print("=" * 40)
        for role, count in role_counts.most_common():
            percentage = (count / len(all_roles)) * 100
            print(f"{role:15} | {count:4} occurrences | {percentage:5.1f}%")
        
        print("\n" + "=" * 40)
        print("SAMPLE SPORTS WITH EACH ROLE:")
        print("=" * 40)
        
        # Find examples of sports for each role
        role_examples = {role: [] for role in unique_roles}
        
        for sport in sports_data:
            sport_name = sport.get('sportName', 'Unknown')
            volunteers = sport.get('volunteers', [])
            
            for volunteer in volunteers:
                role = volunteer.get('role')
                if role and len(role_examples[role]) < 3:  # Limit to 3 examples per role
                    role_examples[role].append(sport_name)
        
        for role in sorted(unique_roles):
            examples = role_examples[role][:3]  # Show up to 3 examples
            examples_str = ", ".join(examples) if examples else "No examples found"
            print(f"{role:15} | Examples: {examples_str}")
        
        return unique_roles, role_counts
        
    except FileNotFoundError:
        print(f"Error: Could not find the file '{json_file_path}'")
        print("Please make sure the file exists in the correct location.")
        return set(), Counter()
    
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{json_file_path}'")
        print(f"JSON Error: {e}")
        return set(), Counter()
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return set(), Counter()

if __name__ == "__main__":
    unique_roles, role_counts = analyze_unique_roles()
