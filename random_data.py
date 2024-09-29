import names as nm
import numpy as np

# Generate random names and grades for 10 people
def generate_random_data(num_people=10):
    # Create random grades distribution (mean and standard deviation)
    grade_distribution = {
        'Proposal Presentation': (88, 5), 
        'Progress Presentation': (90, 10), 
        'Final Presentation': (87, 7), 
        'Final Report': (90, 5),
        'Homeworks': (80, 15), 
        '3D Games': (78, 10), 
        'Final Exam': (80, 7)
    }

    data = []
    for _ in range(num_people):
        name = nm.get_full_name()
        grades = [np.clip(np.random.normal(*grade_distribution[key]), 0, 100) for key in grade_distribution]
        data.append([name] + [f"{grade:.2f}" for grade in grades])
    
    return data

# Generate 10 random people data
random_data = generate_random_data()

# Save to txt file with headers (comma-separated)
with open('random_students.txt', 'w') as f:
    # Write the header first (comma-separated)
    f.write("Name,Proposal_Presentation,Progress_Presentation,Final_Presentation,Final_Report,Homeworks,3D_Games,Final_Exam\n")
    
    # Write the student data (comma-separated)
    for person in random_data:
        f.write(','.join(person) + '\n')

print("Comma-separated data with headers has been saved to random_students.txt")
