import re

def assess_password(password):
    score = 0
    feedback = []

    #Criteria 1
    if len(password) >= 12:
        score += 2
        feedback.append("Password length is excellent.")
    elif 8 <= len(password) < 12:
        score += 1
        feedback.append("Password length is moderate")
    else: 
        feedback.append("Password length is short. Aim for atleast 12 charecters.")
    
    #Criteria 2: Uppercase letters
    if re.search(r'[A-Z]',password):
        score += 1
    else:
        feedback.append("Add atleast one uppercase")
    
    #Criteria 3: Lowercase letters
    if re.search(r'[a-z]',password):
        score += 1
    else:
        feedback.append("Add atleast one lowercase")

    #Criteria 4: Number
    if re.search(r'\d',password):
        score += 1
    else:
        feedback.append("Add atleast one number")  

    #Criteria 5: Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        score += 1
    else:
        feedback.append("Add atleast one special character (like @,#,$..)")

    
    #Strength Checker
    if score == 6:
        category = "Very strong"
    elif score >= 4:
        category = "Strong"
    elif score >= 2:
        category ="Weak"
    else:
        category = "Very Weak"
    
    #Construct the result
    result = {
        "score": score,
        "category": category,
        "feedback": feedback
    }

    return result

print('*** PASSWORD COMPLIXITY CHECKER ***\n')

password = input("Enter your password to assess: ")
assessment = assess_password(password)

print("\nPassword strength assessment")
print(f"Score: {assessment['score']}/6")
print(f"Category: {assessment['category']}")
print("Feedback: ")
for item in assessment['feedback']:
    print(f"- {item}")

