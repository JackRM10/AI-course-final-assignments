import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'api-key' # API key to be inserted

def get_response(prompt):
    """Fetch a response from OpenAI's API based on the user's input."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can use 'gpt-3.5-turbo' if available
            prompt=prompt,
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error fetching response: {e}")
        return None

def word_association_game():
    print("Welcome to the Word Association Game!")
    print("Type a word and see how the AI responds. Type 'quit' to end the game.\n")

    user_input = input("You: ")
    
    while user_input.lower() != 'quit':
        prompt = f"Respond with an associated word for '{user_input}':"
        response = get_response(prompt)
        
        if response:
            print(f"AI: {response}")
        else:
            print("AI failed to respond. Please try again.")
        
        user_input = input("\nYou: ")

    print("Thanks for playing!")

if __name__ == "__main__":
    word_association_game()
