% Facts: symptoms for diseases
symptom(flu, fever).
symptom(flu, cough).
symptom(cold, cough).
symptom(cold, sneezing).
symptom(malaria, fever).
symptom(malaria, chills).

% Diagnose based on symptoms
diagnose(Disease, Symptom) :- symptom(Disease, Symptom).
