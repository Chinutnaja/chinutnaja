departments = {
    'Sales': {
        'Alice': 85.75,
        'Bob': 75.75,
        'Charlie': 66.75,
    },
    'Engineering': {
        'David': 92.75,
        'Eve': 87.5,
        'Frank': 86.5,
    },
    'HR': {
        'Grace': 73.0,
        'Heidi': 69.0,
        'Ivan': 63.0,
    }
}

average_scores = {department: sum(scores.values()) / len(scores) for department, scores in departments.items()}

top_performers = {department: max(scores.items(), key=lambda x: x[1]) for department, scores in departments.items()}

best_department = max(average_scores.items(), key=lambda x: x[1])

continuous_improvers = {department: [name for name, score in scores.items() if score < average_scores[department]] for department, scores in departments.items()}

print(f"Average Performance Scores: {departments}")
print(f"Top Performers: {top_performers}")
print(f"Best Department: {best_department[0]} with Average Score = {best_department[1]}")
print(f"Continuous Improvers: {continuous_improvers}")
