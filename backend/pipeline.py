from backend.generator import generate_content
from backend.validator import validate_content
from database.db import save_campaign

def run_campaign(brand, audience, platform, tone, goal):
    max_retries = 3
    last_error = ""
    
    for attempt in range(max_retries):
        print(f"Generating content (Attempt {attempt+1}/{max_retries})...")
        content = generate_content(brand, audience, platform, tone, goal)
        
        is_valid, errors = validate_content(content, tone, platform)
        
        if is_valid:
            save_campaign(brand, audience, platform, tone, goal, content)
            return {"status": "success", "content": content}
        
        last_error = "; ".join(errors)
        print(f"Validation failed: {last_error}")
    
    return {"status": "error", "message": f"Failed to generate valid content after {max_retries} retries. Last error: {last_error}"}
