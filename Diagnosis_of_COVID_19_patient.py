'''
----- Covid-19 Questionnaire -----


Patient name: sid
Patient age: 34

Some possible Covid-19 symptoms. Answer 'Yes' or 'No' for each symptom for yourself:
Fever? (Yes/No): yes
Cough? (Yes/No): yes
Shortness of breath or difficulty breathing? (Yes/No): yes
Fatigue? (Yes/No): yes
Muscle or body aches? (Yes/No): no
Headache? (Yes/No): no
Sore throat? (Yes/No): no
Loss of taste or smell? (Yes/No): yes
Congestion or runny nose? (Yes/No): no
Gastrointestinal symptoms (nausea, vomiting, diarrhea, abdominal pain)? (Yes/No): no

Duration of symptoms (in days): 6

Have you done the following tests?
PCR Test? (Yes/No): no
Rapid Antigen Test? (Yes/No): yes
- 4. Ginger tea
- 5. Chamomile tea
- 6. Green tea
- 7. Honey and warm milk
Possibility of being Covid-19 affected : 70%
PS D:\all codes>  d:; cd 'd:\all codes'; & 'C:\Users\HP\AppData\Local\Programs\Python\Python311\python.exe' 'c:\Users\HP\.vscode\extensions\ms-python.python-2023.10.1\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher' '10859' '--' 'd:\all codes\covid-2.py'

----- Covid-19 Questionnaire -----


Patient name: sid
Patient age: 35

Some possible Covid-19 symptoms. Answer 'Yes' or 'No' for each symptom for yourself:
Fever? (Yes/No): yes
Cough? (Yes/No): yes
Shortness of breath or difficulty breathing? (Yes/No): yes
Fatigue? (Yes/No): yes
Muscle or body aches? (Yes/No): no
Headache? (Yes/No): yes
Sore throat? (Yes/No): no
Loss of taste or smell? (Yes/No): no
Congestion or runny nose? (Yes/No): yes
Gastrointestinal symptoms (nausea, vomiting, diarrhea, abdominal pain)? (Yes/No): no

Duration of symptoms (in days): 6

Have you done the following tests?
PCR Test? (Yes/No): no
Rapid Antigen Test? (Yes/No): yes
Report for Rapid Antigen Test: positive/negative: positive
Antibody Test? (Yes/No): no

Do you have any pre-existing diseases? (Yes/No): yes

Answer 'Yes' or 'No' for each pre-existing disease:
Chronic obstructive pulmonary disease (COPD)? (Yes/No): no
Asthma? (Yes/No): yes
Pulmonary fibrosis? (Yes/No): no
Heart failure? (Yes/No): no
Coronary artery disease? (Yes/No): no
Hypertension (high blood pressure)? (Yes/No): yes
--- Result ---

High possibility of Covid 19.


Suggested Home remedies:
- 1. Take Lemon tea
- 2. Gargling with warm saltwater
- 3. Steam inhalation
- 4. Ginger tea
- 5. Chamomile tea
- 6. Green tea
- 7. Honey and warm milk
- 8. Deep breathing exercises
- 9. Nutritious foods
- 10.Adequate hydration
- 11.Rest and relaxation

Possibility of being Covid-19 affected : 70%

'''


print("\n----- Covid-19 Questionnaire -----\n")

# Patient Information

patient_name = input("\nPatient name: ")

patient_age = input("Patient age: ")

# Covid 19 symptoms

symptoms = [
    "Fever",
    "Cough",
    "Shortness of breath or difficulty breathing",
    "Fatigue",
    "Muscle or body aches",
    "Headache",
    "Sore throat",
    "Loss of taste or smell",
    "Congestion or runny nose",
    "Gastrointestinal symptoms (nausea, vomiting, diarrhea, abdominal pain)"
]

symptom_answers = {}

print("\nSome possible Covid-19 symptoms. Answer 'Yes' or 'No' for each symptom for yourself:")

for symptom in symptoms:
    answer = input(f"{symptom}? (Yes/No): ")
    symptom_answers[symptom] = answer.lower()


# Duration of symptoms

symptoms_duration = int(input("\nDuration of symptoms (in days): "))


# Tests

print("\nHave you done the following tests?")

tests = {
    "PCR Test": None,
    "Rapid Antigen Test": None,
    "Antibody Test": None
}

for test, _ in tests.items():
    result = input(f"{test}? (Yes/No): ")
    if result.lower() == "yes":
        report = input(f"Report for {test}: positive/negative: ")
        tests[test] = report.lower()


# Pre-existing diseases

existing_diseases = input("\nDo you have any pre-existing diseases? (Yes/No): ")

disease_count = 0

if existing_diseases.lower() == "yes":
    diseases = [
        "Chronic obstructive pulmonary disease (COPD)",
        "Asthma",
        "Pulmonary fibrosis",
        "Heart failure",
        "Coronary artery disease",
        "Hypertension (high blood pressure)",
        "Diabetes type 1",
        "Diabetes type 2",
        "Obesity (a body mass index (BMI) of 30 or higher)",
        "Chronic kidney disease",
        "Cirrhosis",
        "Undergoing cancer treatment",
        "Organ transplantation",
        "Stroke",
        "Rheumatoid arthritis or lupus",
        "Pregnancy"
    ]

    disease_answers = {}

    print("\nAnswer 'Yes' or 'No' for each pre-existing disease:")

    for disease in diseases:
        answer = input(f"{disease}? (Yes/No): ")
        disease_answers[disease] = answer.lower()
        if answer.lower() == "yes":
            disease_count += 1


# Covid history and vaccination

covid_history = input("\nHave you been affected by Covid-19 before? (Yes/No): ")

vaccination_history = input("\nHave you been vaccinated previously? (Yes/No): ")


# Calculate the probability percentage

probability_percentage = 0

if symptom_answers.get("Fever") == "yes":
    probability_percentage += 10

if symptom_answers.get("Cough") == "yes":
    probability_percentage += 10

if symptom_answers.get("Shortness of breath or difficulty breathing") == "yes":
    probability_percentage += 10

if symptom_answers.get("Loss of taste or smell") == "yes":
    probability_percentage += 10

if symptoms_duration >= 5:
    probability_percentage += 10

if tests["PCR Test"] == "positive":
    probability_percentage += 30

if tests["Rapid Antigen Test"] == "positive":
    probability_percentage += 20
    if disease_count > 3:
        probability_percentage += 10

# Home remedies

home_remedies = [
    "1. Take Lemon tea",
    "2. Gargling with warm saltwater",
    "3. Steam inhalation",
    "4. Ginger tea",
    "5. Chamomile tea",
    "6. Green tea",
    "7. Honey and warm milk",
    "8. Deep breathing exercises",
    "9. Nutritious foods",
    "10.Adequate hydration",
    "11.Rest and relaxation"
]


# Result

if probability_percentage >= 50:
    print("\n--- Result ---\n\nHigh possibility of Covid 19.")
    print("\n\nSuggested Home remedies:")
    for remedy in home_remedies:
        print("- " + remedy)
else:
    print("\n--- Result ---\n\nUnlikely to have Covid 19.")

print(f"\nPossibility of being Covid-19 affected : {probability_percentage}%")

