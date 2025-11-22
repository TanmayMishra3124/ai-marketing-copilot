from backend.pipeline import run_campaign
from database.db import init_db, get_campaigns
import os
from dotenv import load_dotenv

load_dotenv()

def test_backend():
    # Ensure DB is init
    init_db()

    print("🧪 Testing Backend Pipeline...")
    
    if not os.getenv("GROQ_API_KEY"):
        print("⚠️  WARNING: GROQ_API_KEY not found in env. Please ensure it is set in .env file.")

    print("Generating campaign for 'TestBrand'...")
    result = run_campaign(
        brand="TestBrand",
        audience="Developers",
        platform="Twitter",
        tone="Witty",
        goal="Test the system"
    )

    print("\nResult Status:", result['status'])

    if result['status'] == 'success':
        print("✅ Campaign generated and saved.")
        campaigns = get_campaigns()
        print(f"📊 Total campaigns in DB: {len(campaigns)}")
        if campaigns:
            print("📝 Latest content snippet:\n", campaigns[0]['content'][:200] + "...")
    else:
        print("❌ Failed:", result.get('message'))

if __name__ == "__main__":
    test_backend()
