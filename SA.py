def get_pshs_grade(percent):
    """
    Returns the PSHS grade equivalent and adjectival rating 
    based on a percentage score.
    """
    if percent >= 96:
        return {"equivalent": 1.00, "description": "EXCELLENT"}
    elif percent >= 90:
        return {"equivalent": 1.25, "description": "VERY GOOD"}
    elif percent >= 84:
        return {"equivalent": 1.50, "description": "VERY GOOD"}
    elif percent >= 78:
        # Note: Image shows 1.75 and 2.00 both falling under 'GOOD'
        return {"equivalent": 1.75, "description": "GOOD"}
    elif percent >= 72:
        return {"equivalent": 2.00, "description": "GOOD"}
    elif percent >= 66:
        return {"equivalent": 2.25, "description": "SATISFACTORY"}
    elif percent >= 60:
        return {"equivalent": 2.50, "description": "SATISFACTORY"}
    elif percent >= 55:
        return {"equivalent": 2.75, "description": "FAIR"}
    elif percent >= 50:
        return {"equivalent": 3.00, "description": "FAIR"}
    elif percent >= 40:
        return {"equivalent": 4.00, "description": "FAILED ON CONDITION"}
    else:
        return {"equivalent": 5.00, "description": "FAILED"}

# --- Sample Usage ---
score = 88.5
result = get_pshs_grade(score)

print(f"Score: {score}%")
print(f"Grade Equivalent: {result['equivalent']}")
print(f"Rating: {result['description']}")
