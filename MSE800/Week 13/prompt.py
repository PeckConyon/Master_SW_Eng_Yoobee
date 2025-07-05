from openai import OpenAI

from typing import Dict, Any

client = OpenAI(api_key="XXXXXXXXXXXXXXXXXxxxxxxxx")

# Uses OpenAI's GPT model to generate a user-friendly summary of the test results.
def generate_ai_summary(prompt : str) -> str:

    try:
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who summarizes vision game results in a friendly, encouraging, and clear way."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=10000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating AI summary: {e}")
        return "Could not generate an AI summary for this session."
    
def main():
  
  print("Enter following data to generate your itineraries\n")
  name = input("Enter name of tourist : ")
  starting_location = input("Enter starting location : ")
  days = input("Enter no of days : ") 
  age_group = input("Enter age group: ")
  season = input("Enter season: ")
  budget = input("Enter budget: ")
  interests = input("Interests as comma separated: ") #["nature", "wine tasting", "light hiking", "photography", "clubs", "music", "night life", "parties"]
 
  prompt = f"""
  Instructions:
    I need to  create personalized, multi-day travel itineraries for tourists visiting New Zealand.
    Each itinerary should consider preferences of tourists, age, gender, travel duration, budget, interests, and starting location.
    Recommendations should have a logical travel route, time bound  and realistic to achieve.
    I need also start time, travel mode, cost, how long it will take to reach from location A to B like that
    Make sure you cover entire duration do not miss any date.
    
  Context:
    Travel agencies in New Zealand want to automate itinerary planning for clients.
    These agencies handle domestic and international tourists with varying needs such as 
    adventure seekers, nature lovers, families, honeymooners, or elderly travelers. 
    The system should support different trip lengths optimize travel time between destinations,
    and ensure recommendations reflect real-world geography, weather (seasonal), and activity availability.
    The LLM must simulate the reasoning of a human travel agent and generate itineraries with day-by-day plans and optional add-ons.
  
  Input Data:
    
    "travelerName": {name},
    "tripDurationDays": {days},
    "startingLocation": {starting_location},
    "interests":{interests},
    "travelStyle": "relaxed",
    "budgetLevel": {budget},
    "season": {season},
    "ageGroup": {age_group},
    "specialRequests": ["avoid dangerous routes", "avoid very long drives (>4 hrs/day)"]
    
    Output Indicator:
        Return a complete 7-day itinerary formatted in Markdown with:

        Title and short summary

        Daily breakdown including:

            Location

            Key activities with timing estimates

            Meal suggestions

            Estimated travel time between stops

            Optional Tips or Alternative Choices

            Final summary table listing all locations visited, total travel time, and optional tours

            The output should be clear, concise, and usable by both travelers and travel agency staff.
            
            Include thoughtful justifications for major route choices and activity selections
            
  """
  response = generate_ai_summary(prompt)
  print(response)
        
    
if __name__ == '__main__':
     main()