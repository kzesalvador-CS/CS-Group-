# Function to compute grades per quarter

def compute_grades(tentative_q1, tentative_q2, tentative_q3, tentative_q4):
    # First Quarter
    q1 = tentative_q1

    # Second Quarter
    q2 = (q1 + 2 * tentative_q2) / 3

    # Third Quarter
    q3 = (q2 + 2 * tentative_q3) / 3

    # Fourth Quarter (Final Grade)
    q4 = (q3 + 2 * tentative_q4) / 3

    return q1, q2, q3, q4


# --- Input section ---
t1 = float(input("Enter Tentative Grade for Q1: "))
t2 = float(input("Enter Tentative Grade for Q2: "))
t3 = float(input("Enter Tentative Grade for Q3: "))
t4 = float(input("Enter Tentative Grade for Q4: "))

# --- Compute ---
q1, q2, q3, q4 = compute_grades(t1, t2, t3, t4)

# --- Output ---
print("\nFinal Grades:")
print(f"Q1: {q1:.2f}")
print(f"Q2: {q2:.2f}")
print(f"Q3: {q3:.2f}")
print(f"Q4 (Final Grade): {q4:.2f}")