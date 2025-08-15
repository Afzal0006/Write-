# words_generator.py

# List of (word, hint) tuples
words = [
    ("python", "A popular programming language"),
    ("telegram", "A messaging app"),
    ("banana", "A yellow fruit"),
    ("computer", "An electronic device"),
    ("hangman", "A word guessing game"),
    ("internet", "Global network connecting computers"),
    ("keyboard", "Input device with keys"),
    ("monitor", "Screen for displaying visuals"),
    ("mouse", "Handheld pointing device"),
    ("notebook", "Portable personal computer"),
    ("chocolate", "Sweet treat made from cocoa"),
    ("pizza", "Italian dish with cheese and tomato"),
    ("guitar", "String musical instrument"),
    ("piano", "Keyboard musical instrument"),
    ("river", "Large natural stream of water"),
    ("mountain", "Large natural elevation of land"),
    ("forest", "Large area covered with trees"),
    ("desert", "Dry, barren area of land"),
    ("ocean", "Large body of saltwater"),
    ("island", "Land surrounded by water"),
    ("book", "Collection of written pages"),
    ("library", "Place to borrow books"),
    ("school", "Place for learning"),
    ("teacher", "Person who educates students"),
    ("student", "Person who learns"),
    ("doctor", "Person who treats sick people"),
    ("nurse", "Person assisting in medical care"),
    ("hospital", "Place for medical treatment"),
    ("car", "Four-wheeled motor vehicle"),
    ("bicycle", "Two-wheeled pedal vehicle"),
    ("train", "Rail transport vehicle"),
    ("airplane", "Aircraft for air travel"),
    ("rocket", "Space travel vehicle"),
    ("earth", "Our home planet"),
    ("moon", "Natural satellite of Earth"),
    ("sun", "Star at the center of our solar system"),
    ("galaxy", "System of stars and planets"),
    ("universe", "All of space and everything in it"),
    ("flower", "Blooming plant"),
    ("tree", "Large plant with trunk and branches"),
    ("grass", "Green ground plant"),
    ("dog", "Domesticated canine animal"),
    ("cat", "Domesticated feline animal"),
    ("bird", "Animal with feathers and wings"),
    ("fish", "Aquatic animal with gills"),
    ("elephant", "Largest land animal"),
    ("tiger", "Big striped wild cat"),
    ("lion", "King of the jungle"),
    ("monkey", "Playful primate"),
    ("butterfly", "Insect with colorful wings"),
    ("bee", "Insect that makes honey"),
]

# Save words.txt
with open("words.txt", "w", encoding="utf-8") as f:
    for word, hint in words:
        f.write(f"{word}|{hint}\n")

print("✅ words.txt file created successfully!")
