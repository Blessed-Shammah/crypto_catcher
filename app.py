#!/usr/bin/env python3
# CryptoBuddy - Your AI Crypto Advisor
# A simple rule-based chatbot for cryptocurrency investment advice

import random
import time

# ASCII art for the bot's greeting
LOGO = """
╔═══════════════════════════════════════════╗
║  ╔═╗╦═╗╦ ╦╔═╗╔╦╗╔═╗╔╗ ╦ ╦╔╦╗╔╦╗╦ ╦  ╔═╗╦ ║
║  ║  ╠╦╝╚╦╝╠═╝ ║ ║ ║╠╩╗║ ║ ║║ ║║╚╦╝  ╠═╣║ ║
║  ╚═╝╩╚═ ╩ ╩   ╩ ╚═╝╚═╝╚═╝═╩╝═╩╝ ╩   ╩ ╩╩ ║
║        Your AI Crypto Advisor!            ║
╚═══════════════════════════════════════════╝
"""

# Predefined cryptocurrency dataset
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10,
        "symbol": "BTC",
        "description": "The original cryptocurrency, known for its first-mover advantage but high energy consumption."
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10,
        "symbol": "ETH",
        "description": "A blockchain platform with smart contract functionality, transitioning to a more energy-efficient consensus mechanism."
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10,
        "symbol": "ADA",
        "description": "A proof-of-stake blockchain platform focused on sustainability and scalability."
    },
    "Solana": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7/10,
        "symbol": "SOL",
        "description": "A high-performance blockchain supporting smart contracts with low transaction costs."
    },
    "Ripple": {
        "price_trend": "falling",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7/10,
        "symbol": "XRP",
        "description": "A digital payment protocol for financial transactions with a focus on banking integration."
    },
    "Polkadot": {
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7.5/10,
        "symbol": "DOT",
        "description": "A multi-chain network enabling different blockchains to transfer messages and value."
    }
}

# Friendly responses with emojis
GREETINGS = [
    "Hey there, crypto explorer! 🚀",
    "Welcome to CryptoBuddy! Ready to dive into crypto? 💰",
    "Hi there! Let's find you some awesome crypto investments! ✨"
]

FAREWELLS = [
    "Happy investing! Remember, to the moon! 🌕",
    "Catch you later, crypto star! 💫",
    "Remember, HODL responsibly! 👋"
]

THINKING = [
    "Analyzing the crypto markets... 📊",
    "Crunching those blockchain numbers... ⛓️",
    "Consulting my crypto crystal ball... 🔮"
]

CONFUSION = [
    "I'm not sure I understand that query. Can you try asking about crypto trends, sustainability, or investment advice?",
    "Hmm, that's outside my programming. Try asking about which cryptos are trending up or which are sustainable!",
    "My circuits are confused! I'm best at answering questions about crypto trends and sustainability."
]

DISCLAIMER = "\n⚠️ DISCLAIMER: This is educational only. Cryptocurrency investments carry high risk. Always do your own research before investing! ⚠️"

# Helper functions for cryptocurrency analysis
def find_trending_cryptos():
    """Find cryptocurrencies with rising price trends"""
    return [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]

def find_sustainable_cryptos():
    """Find the most sustainable cryptocurrencies"""
    sustainable = sorted(crypto_db.items(), key=lambda x: x[1]["sustainability_score"], reverse=True)
    return [name for name, _ in sustainable if crypto_db[name]["sustainability_score"] >= 0.7]

def find_best_overall():
    """Find cryptocurrencies with good balance of profitability and sustainability"""
    good_overall = []
    for name, data in crypto_db.items():
        if data["price_trend"] in ["rising", "stable"] and data["sustainability_score"] >= 0.6:
            good_overall.append(name)
    return good_overall

def get_crypto_details(crypto_name):
    """Get detailed information about a specific cryptocurrency"""
    if crypto_name.lower() in [name.lower() for name in crypto_db]:
        for name in crypto_db:
            if name.lower() == crypto_name.lower():
                crypto = crypto_db[name]
                return f"{name} ({crypto['symbol']}): {crypto['description']}\n" \
                       f"• Price Trend: {crypto['price_trend'].capitalize()}\n" \
                       f"• Market Cap: {crypto['market_cap'].capitalize()}\n" \
                       f"• Energy Use: {crypto['energy_use'].capitalize()}\n" \
                       f"• Sustainability Score: {int(crypto['sustainability_score']*10)}/10"
    return None

def thinking_animation():
    """Display a thinking animation"""
    message = random.choice(THINKING)
    print(message, end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")
    time.sleep(0.5)

# Main chatbot function
def crypto_buddy():
    """Main function to run the CryptoBuddy chatbot"""
    print(LOGO)
    print(random.choice(GREETINGS))
    print("I can help you find the best cryptocurrencies based on profitability and sustainability!")
    print("Ask me things like 'Which crypto is trending up?' or 'What's the most sustainable coin?'")
    print("Type 'exit' when you're done.\n")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in ["exit", "quit", "bye"]:
            print("\nCryptoBuddy: " + random.choice(FAREWELLS))
            break
        
        thinking_animation()
        
        # Process user query
        if not user_input:
            response = "Don't be shy! Ask me about crypto trends or sustainability."
        
        # Questions about trending/profitable cryptocurrencies
        elif any(word in user_input for word in ["trend", "trending", "rise", "rising", "profitable", "profitability", "grow", "growing"]):
            trending = find_trending_cryptos()
            if trending:
                response = f"Based on current trends, {', '.join(trending[:-1]) + ' and ' + trending[-1] if len(trending) > 1 else trending[0]} " \
                          f"{'are' if len(trending) > 1 else 'is'} showing upward price movement! 📈"
            else:
                response = "I don't see any cryptocurrencies with strongly rising trends right now. Maybe consider stable options for now."
        
        # Questions about sustainability/eco-friendly cryptocurrencies
        elif any(word in user_input for word in ["sustainable", "sustainability", "green", "eco", "environmental", "energy"]):
            sustainable = find_sustainable_cryptos()
            if sustainable:
                response = f"For eco-conscious investing, check out {', '.join(sustainable[:-1]) + ' and ' + sustainable[-1] if len(sustainable) > 1 else sustainable[0]}! " \
                          f"{'They all have' if len(sustainable) > 1 else 'It has'} excellent sustainability scores. 🌱"
            else:
                response = "All cryptocurrencies have some environmental impact, but I'm programmed to help you find the least impactful options."
        
        # Questions about specific cryptocurrencies
        elif any(crypto.lower() in user_input for crypto in crypto_db):
            for crypto in crypto_db:
                if crypto.lower() in user_input:
                    details = get_crypto_details(crypto)
                    response = f"Here's what I know about {crypto}:\n\n{details}"
                    break
        
        # General investment advice
        elif any(word in user_input for word in ["invest", "buy", "recommendation", "recommend", "suggest", "best"]):
            best_overall = find_best_overall()
            if best_overall:
                response = f"For a balanced investment considering both growth and sustainability, I'd look at {', '.join(best_overall[:-1]) + ' and ' + best_overall[-1] if len(best_overall) > 1 else best_overall[0]}. " \
                          f"{'These coins show' if len(best_overall) > 1 else 'This coin shows'} good potential while maintaining reasonable energy efficiency. 💰🌿"
            else:
                response = "Currently, it's hard to find options with both strong growth and sustainability. Consider your priorities and maybe split your investment."
        
        # Help or available commands
        elif any(word in user_input for word in ["help", "command", "question", "ask"]):
            response = "Here are some things you can ask me:\n" \
                      "• Which cryptocurrencies are trending up?\n" \
                      "• What are the most sustainable cryptocurrencies?\n" \
                      "• Tell me about [specific crypto name]\n" \
                      "• What's your investment recommendation?\n" \
                      "• Which crypto has the best balance of profit and sustainability?"
        
        # Default response for unrecognized queries
        else:
            response = random.choice(CONFUSION)
        
        print(f"CryptoBuddy: {response}")
        
        # Add disclaimer for investment advice
        if any(word in user_input for word in ["invest", "buy", "recommendation", "recommend", "suggest", "best"]):
            print(DISCLAIMER)

# Run the chatbot
if __name__ == "__main__":
    crypto_buddy()