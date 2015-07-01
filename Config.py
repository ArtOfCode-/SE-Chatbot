class Config:
    
    General = {
        "owner_name": "ArtOfCode", # Required
        "owners": [ { "stackexchange.com": 121520 }, { "stackexchange.com": 146754 }, { "stackexchange.com": 138766 } ], # you can add multiple owners
        "chatbot_name": "KarmaBot", # Required
    }
    
    Configurations = { # Optional, add configurations here
        "dev": {
            "site": "stackexchange.com",
            "room": 25323
        },
        "os": {
            "site": "stackexchange.com",
            "room": 25118
        }
    }

    