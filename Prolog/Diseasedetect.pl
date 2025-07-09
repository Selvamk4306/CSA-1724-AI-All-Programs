% --- Facts: disease_diet(Disease, Diet) ---

disease_diet(diabetes, 'Low sugar diet with high fiber, whole grains, and vegetables.').
disease_diet(hypertension, 'Low salt diet with fruits, vegetables, and low-fat dairy.').
disease_diet(obesity, 'Calorie-controlled diet rich in vegetables, fruits, and lean proteins.').
disease_diet(anemia, 'Iron-rich foods like leafy greens, beans, and red meat.').
disease_diet(gastritis, 'Soft, non-spicy foods; avoid acidic drinks.').
disease_diet(constipation, 'High fiber diet with lots of fruits, vegetables, and water.').

% --- Rule: suggest_diet(Disease, Diet) ---

suggest_diet(Disease, Diet) :-
    disease_diet(Disease, Diet).

% --- Optional: Rule to handle unknown diseases
suggest_diet(Disease, 'No specific diet found. Please consult your doctor.') :-
    \+ disease_diet(Disease, _).
