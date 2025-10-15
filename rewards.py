from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
from random import randint

# List of 100 trending three-word terms

search_terms = [
    # 🎬 Movies & TV
    "Thunderbolts 2025", "Bob Lewis Pullman", "Loki 2.0", "Guardians of the Galaxy Vol. 4", "Dune Part Two",
    "Killers of the Flower Moon", "Barbie 2025", "The Marvels", "Oppenheimer 2", "The Hunger Games: The Ballad of Songbirds and Snakes",

    # 🎮 Video Games
    "Starfield", "Cyberpunk 2077: Phantom Liberty", "The Legend of Zelda: Tears of the Kingdom", "Hogwarts Legacy", "Final Fantasy XVI",
    "Elden Ring DLC", "Resident Evil 9", "Horizon Forbidden West", "God of War: Ragnarok", "Call of Duty: Modern Warfare II",

    # 💃 Dance Styles
    "TikTok Dance Trends 2025", "Hip Hop Dance Battles", "Contemporary Dance Choreography", "Ballet Repertoire", "Salsa Dance Moves",
    "Jazz Funk Dance", "Breakdancing Competitions", "Tango Dance Styles", "Swing Dance Revival", "Modern Dance Techniques",

    # 🍽️ Cuisine & Recipes
    "Plant-Based Recipes", "Air Fryer Dishes", "Vegan Comfort Food", "Fermented Foods", "Global Street Food Recipes",
    "Sustainable Cooking Practices", "Zero-Waste Recipes", "Meal Prep Ideas", "Healthy Smoothie Bowls", "Gourmet Desserts",

    # 🏛️ Architecture & Design
    "Sustainable Architecture", "Smart Homes", "Minimalist Interior Design", "Urban Green Spaces", "Modular Housing",
    "Biophilic Design", "3D-Printed Buildings", "Tiny Homes Movement", "Adaptive Reuse Architecture", "Smart Cities",

    # 🕶️ Eyewear Trends
    "Oversized Sunglasses", "Retro Eyewear Styles", "Smart Glasses", "Eco-Friendly Frames", "Vintage Eyeglasses",
    "Geometric Frame Glasses", "Aviator Sunglasses", "Round Frame Glasses", "Cat-Eye Glasses", "Translucent Eyewear",

    # 🌍 Travel Destinations
    "Lijiang China", "Thessaloniki Greece", "Chongqing China", "Sumba Island Bali", "Tokyo Japan",
    "Paris France", "New York City", "Santorini Greece", "Machu Picchu Peru", "Great Wall of China",

    # 🎭 Celebrities & Pop Culture
    "Tom Hiddleston", "Zendaya", "Timothée Chalamet", "Florence Pugh", "Harry Styles",
    "Beyoncé", "Taylor Swift", "Rihanna", "Chris Hemsworth", "Emma Stone",

    # 🧬 Health & Wellness
    "Mental Health Awareness", "Fitness Trends 2025", "Plant-Based Diet Benefits", "Mindfulness Practices", "Sleep Optimization",
    "Holistic Health Approaches", "Wearable Health Tech", "Personalized Medicine", "Chronic Disease Management", "Telehealth Services",

    # 🤖 Technology & Innovation
    "Artificial Intelligence", "Quantum Computing", "5G Technology", "Blockchain Applications", "Augmented Reality",
    "Virtual Reality", "Internet of Things", "Cybersecurity Innovations", "Robotic Automation", "Sustainable Tech Solutions"
]




def perform_searches_with_selenium():
    """
    Automates performing searches using Microsoft Edge WebDriver.
    """
    edge_driver_path = "C:\\Users\\ASUS\\Downloads\\edgedriver_win64\\msedgedriver.exe"

    # Configure Edge options
    edge_options = Options()
    edge_options.add_argument("--disable-gpu")  # Disable GPU (optional)
    edge_options.add_argument("--no-sandbox")  # Required in some environments

    # Initialize Edge WebDriver
    driver_service = Service(edge_driver_path)
    driver = webdriver.Edge(service=driver_service, options=edge_options)

    try:
        for i, search_term in enumerate(search_terms, start=1):
            # Format the search term for URL encoding
            formatted_term = search_term.replace(" ", "+")
            search_url = f"https://www.bing.com/news/search?q={formatted_term}&form=QBNT"

            # Navigate to the search URL
            driver.get(search_url)
            print(f"Performed search {i}: {search_term}")

            # Wait a few seconds to simulate human behavior
            sleep_time = randint(7, 10)
            print(f"Waiting for {sleep_time} seconds before the next search...")
            time.sleep(sleep_time)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the browser
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    perform_searches_with_selenium()


