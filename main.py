rooms = {
    "Prison Tower": {"South": "Vault", "East": "Shuttle Landing Platform"},
    "Vault": {"North": "Prison Tower", "East": "Grand Training Hall"},
    "Shuttle Landing Platform": {"South": "Grand Training Hall", "West": "Prison Tower"},
    "Grand Training Hall": {
        "North": "Shuttle Landing Platform",
        "South": "Meditation Room",
        "West": "Vault",
        "East": "Sith Lords Chambers"
    },
    "Meditation Room": {"North": "Grand Training Hall", "East":"Ancient Library"},
    "Sith Lords Chambers": {"South": "Ancient Library", "West": "Grand Training Hall", "East": "Throne Room"},
    "Ancient Library": {"North": "Sith Lords Chambers", "West":"Meditation Room"},
    "Throne Room": {"West": "Sith Lords Chambers"}
}
