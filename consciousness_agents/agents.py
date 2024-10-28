import consciousness_api
import os
import dotenv

dotenv.load_dotenv()

api_key = os.getenv("CONSCIOUSNESS_API_KEY")

api = consciousness_api.ConsciousnessAPI(api_key)

print(api.list_authors())

