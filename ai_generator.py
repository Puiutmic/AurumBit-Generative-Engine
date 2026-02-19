import os
import urllib.request
import json

def get_api_key():
    env_key = os.getenv('GEMINI_API_KEY')
    if env_key:
        return env_key

    try:
        with open('.env', 'r') as f:
            for line in f:
                if line.strip().startswith('GEMINI_API_KEY='):
                    return line.strip().split('=')[1]
    except FileNotFoundError:
        pass
    return None

def generate_jewelry_config(user_prompt):
    api_key = get_api_key()
    if not api_key:
        print("Error: GEMINI_API_KEY not found in Environment or .env file.")
        return

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    system_instruction = """
    You are an expert 3D parametric jewelry designer. 
    Transform the user's description into a valid JSON configuration file.
    Structure:
    {
        "radius": 15.0,
        "thickness": 2.5,
        "sides": 32,
        "style": "smooth",
        "twist_angle": 0
    }
    Return ONLY raw JSON. No markdown, no comments.
    """

    payload = {
        "systemInstruction": {"parts": [{"text": system_instruction}]},
        "contents": [{"parts": [{"text": "User request: " + user_prompt}]}],
        "generationConfig": {"responseMimeType": "application/json"}
    }

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})

    print(f"Requesting AI Generation for: '{user_prompt}'...")
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            generated_text = result['candidates'][0]['content']['parts'][0]['text']
            
            with open('config.json', 'w') as f:
                f.write(generated_text)
                
            print("Success. config.json updated via Gemini AI.")
            
    except Exception as e:
        print(f"Execution error: {e}")

if __name__ == "__main__":
    test_prompt = "Thick Mobius twist ring, 17mm radius, high-poly finish."
    generate_jewelry_config(test_prompt)