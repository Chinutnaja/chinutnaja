
survey_results = [
    ["Python", "JavaScript", "C++"],  
    ["Python", "JavaScript", "C#"],   
    ["Python", "Java"],               
    ["Python", "C++", "JavaScript"], 
    ["Python", "JavaScript", "C++", "Java"] 
]

all_languages = set(survey_results[0])
for result in survey_results[1:]:
    all_languages.intersection_update(result)

from collections import Counter

language_counts = Counter(language for result in survey_results for language in result)
unique_languages = {language for language, count in language_counts.items() if count == 1}

unique_language_count = len(language_counts)


languages_chosen_by_two = {language for language, count in language_counts.items() if count == 2}


from itertools import combinations

identical_participants = []
for i, j in combinations(range(len(survey_results)), 2):
    if set(survey_results[i]) == set(survey_results[j]):
        identical_participants.append((i + 1, j + 1))  

print(f"Languages chosen by all participants: {all_languages}")
print(f"Languages chosen by only one participant: {unique_languages}")
print(f"Number of unique languages: {unique_language_count}")
print(f"Languages chosen by exactly two participants: {languages_chosen_by_two}")
print(f"Participants with identical choices: {identical_participants}")
