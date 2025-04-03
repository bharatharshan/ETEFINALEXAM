import pandas as pd
import numpy as np
from datetime import timedelta, date

def generate_data():
    # Define parameters
    num_participants = 350
    num_days = 3
    hackathon_domains = ['AI', 'Web Development', 'Data Science', 'Cybersecurity', 'Blockchain']
    colleges = ['College A', 'College B', 'College C']
    states = ['State X', 'State Y', 'State Z']
    
    # Generate participant IDs
    participant_ids = [f"Participant {i}" for i in range(1, num_participants + 1)]
    
    # Generate random scores
    scores = np.random.randint(0, 100, size=num_participants)
    
    # Generate random feedback
    feedback_options = ["Good", "Average", "Poor"]
    feedback = np.random.choice(feedback_options, size=num_participants)
    
    # Generate random dates
    start_date = date.today()
    dates = [(start_date + timedelta(days=np.random.randint(0, num_days))).strftime("%Y-%m-%d") for _ in range(num_participants)]
    
    # Assign random domains
    domains = np.random.choice(hackathon_domains, size=num_participants)
    
    # Additional columns
    colleges_assigned = np.random.choice(colleges, size=num_participants)
    states_assigned = np.random.choice(states, size=num_participants)
    ages = np.random.randint(18, 30, size=num_participants)
    genders = np.random.choice(['Male', 'Female'], size=num_participants)
    team_names = [f"Team {i}" for i in range(1, num_participants + 1)]
    project_titles = [f"Project {i}" for i in range(1, num_participants + 1)]
    contact_info = [f"participant{i}@example.com" for i in range(1, num_participants + 1)]
    
    # Create DataFrame
    data = {
        "Participant ID": participant_ids,
        "Score": scores,
        "Feedback": feedback,
        "Date": dates,
        "Domain": domains,
        "College": colleges_assigned,
        "State": states_assigned,
        "Age": ages,
        "Gender": genders,
        "Team Name": team_names,
        "Project Title": project_titles,
        "Contact Information": contact_info
    }
    df = pd.DataFrame(data)
    return df
