import os 
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()
APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")

# Initialize the ApifyClient with your API token

client = ApifyClient(APIFY_API_TOKEN)

# Fetch LinkedIn jobs based on search query and location
def fetch_linkedin_jobs(search_query,location='india',rows=60):

    # Prepare the Actor input
    run_input = {
            "title": search_query,
            "location": location,
            "rows": rows,
            "proxy": {
                "useApifyProxy": True,
                "apifyProxyGroups": ["RESIDENTIAL"],
            }
        }

    # Run the Actor and wait for it to finish
    run = client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    jobs = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    
    return jobs

# Fetch Naukri jobs based on search query and location
def fetch_naukri_jobs(search_query,location='india',rows=60):

    # Prepare the Actor input
    run_input = {
        "keyword": search_query,
        "fetchDetails": False,
        "maxJobs": 60,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
    }

    # Run the Actor and wait for it to finish
    run = client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    jobs = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs
        