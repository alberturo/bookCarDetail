import os
from app.models import db, environment, SCHEMA, Book
from datetime import datetime
from sqlalchemy.sql import text


def seed_books():
#   BUCKET_NAME = os.environ.get("S3_BUCKET")
#   S3_LOCATION = f"http://{BUCKET_NAME}.s3.us-east-2.amazonaws.com"

  books_data = [
        #English Books
        {
            "id": 1,
            "name": "Frankenstein",
            "lang": "English",
            "summary": "IThe story is about Victor Frankenstein, a scientist who creates a monster from body parts and brings it to life. The monster initially seeks affection, but everyone who meets it is repelled. ",
            "publisher": "Harper & Brothers",
            "publishDate": datetime(1797, 10, 15),
            "author": "Shelley, Mary Wollstonecraft",
            "genre": ["Novel", "Fiction"],
            "difficulty": "Beginner",
            "imgUrl": "https://www.gutenberg.org/cache/epub/84/pg84.cover.medium.jpg",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "id": 2,
            "name": "A Christmas Carol in Prose",
            "lang": "English",
            "summary": "A Christmas Carol in Prose is a classic novella by Charles Dickens, telling the story of Ebenezer Scrooge, a miserly old man who is visited by ghosts on Christmas Eve, forcing him to confront his past and present behavior, ultimately leading to a transformation into a generous and compassionate individual, embracing the true spirit of Christmas.",
            "publisher": "J.B. Lippincott & Co.",
            "publishDate": datetime(1960, 7, 11),
            "author": "Dickens, Charles",
            "genre": ["Thriller", "Novel", "Fiction"],
            "difficulty": "Intermediate",
            "imgUrl": "https://www.gutenberg.org/ebooks/46.kf8.images",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "id": 3,
            "name": "Moby Dick",
            "lang": "English",
            "summary": "The story is told from the perspective of Ishmael, a young narrator who joins the Pequod after traveling from Manhattan to Nantucket",
            "publisher": "Secker & Warburg",
            "publishDate": datetime(1949, 6, 8),
            "author": "Melville, Herman",
            "genre": ["Adventure", "Fiction"],
            "difficulty": "Conversational",
            "imgUrl": "https://www.gutenberg.org/cache/epub/2701/pg2701.cover.medium.jpg",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "id": 4,
            "name": "Romeo and Juliet",
            "lang": "English",
            "summary": "Ulysses by James Joyce is a modernist novel that follows the experiences of three characters, Leopold Bloom, Stephen Dedalus, and Molly Bloom, over the course of a single day (June 16, 1904) in Dublin, Ireland, drawing parallels between their lives and the characters in Homer's 'Odyssey' - with Bloom representing Odysseus, Molly as Penelope, and Stephen as Telemachus; the book explores themes of identity, consciousness, and the complexities of everyday life through a stream-of-consciousness narrative style, showcasing the rich tapestry of Dublin society and its cultural nuances while using intricate literary devices and allusions to various historical and literary figures.",
            "publisher": "Sylvia Beach",
            "publishDate": datetime(1564, 2, 2),
            "author": "Shakespeare, William",
            "genre": ["Drama", "Fiction"],
            "difficulty": "Native",
            "imgUrl": "https://www.gutenberg.org/cache/epub/1513/pg1513.cover.medium.jpg",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },

        #Japanese Books
        {
            "id": 5,
            "name": "どんぐりと山猫 (Donguri to Yamaneko)",
            "lang": "Japanese",
            "summary": "The story begins with Ichiro, a curious and imaginative boy, who receives a mysterious postcard in the mail. The sender is Yamaneko (the Wildcat), an enigmatic figure who asks Ichiro to come to a 'court' in the forest. Intrigued, Ichiro follows the instructions on the postcard and ventures deep into the woods. When Ichiro arrives at the appointed place, he discovers a peculiar trial in progress. The participants in the trial are acorns (donguri), which are squabbling over who among them is the most important and deserving of special recognition. Each acorn claims superiority, citing its size, shape, or uniqueness. Their incessant bickering creates a chaotic scene. Presiding over the trial is Yamaneko, who is both whimsical and wise. Yamaneko seeks Ichiro's help in resolving the dispute. However, Ichiro finds himself puzzled by the quarrels of the acorns and struggles to find a solution.",
            "publisher": "Kindaibungeisha",
            "publishDate": datetime(1914, 1, 1),
            "author": "Kenji Miyazawa",
            "genre": ["Fiction", "Drama"],
            "difficulty": "Beginner",
            "imgUrl": "https://www.gutenberg.org/cache/epub/1342/pg1342.cover.medium.jpg",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "id": 6,
            "name": "君の名は。 (Your Name.)",
            "lang": "Japanese",
            "summary": "One day, Mitsuha and Taki begin to mysteriously swap bodies while they sleep. When they wake up, they find themselves living each other's lives. At first, they are confused and frustrated by the strange phenomenon, but over time, they adapt by leaving notes and messages for each other to explain what happened during their swapped days. Through this bizarre connection, Mitsuha and Taki begin to develop a strong bond. They come to understand each other's struggles and help each other navigate their respective lives. Taki helps Mitsuha become more confident and assertive, while Mitsuha introduces Taki to a slower, more heartfelt way of living.",
            "publisher": "Kadokawa Shoten",
            "publishDate": datetime(2016, 6, 18),
            "author": "Makoto Shinkai",
            "genre": ["Romance", "Fiction"],
            "difficulty": "Intermediate",
            "imgUrl": "https://www.gutenberg.org/cache/epub/1342/pg1342.cover.medium.jpg",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "id": 7,
            "name": "ノルウェイの森 (Norwegian Wood)",
            "lang": "Japanese",
            "summary": "Norwegian Wood is a poignant coming-of-age novel by Haruki Murakami that explores themes of love, loss, mental illness, and the complexities of human relationships. The story is set in 1960s Japan and is narrated by Toru Watanabe, a man in his thirties looking back on his college days.",
            "publisher": "Kodansha",
            "publishDate": datetime(1987, 9, 4),
            "author": "Haruki Murakami",
            "genre": ["Novel", "Drama", "Fiction"],
            "difficulty": "Conversational",
            "imgUrl": "https://www.gutenberg.org/cache/epub/1342/pg1342.cover.medium.jpg",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "id": 8,
            "name": "源氏物語 (The Tale of Genji)",
            "lang": "Japanese",
            "summary": "The Tale of Genji revolves around Hikaru Genji, the son of a Japanese emperor and a low-ranking consort, which leaves him politically marginalized despite his beauty, talent, and charm. Stripped of royal rank, Genji becomes a commoner and dedicates his life to the pursuit of art, love, and pleasure. Genji's romantic entanglements are a central focus of the story. He has numerous affairs, often with women of vastly different social standings and temperaments. One of his most complicated relationships is with Fujitsubo, his father's wife, with whom he has a secret child. Another is with Murasaki, a young girl he essentially raises to become his ideal companion.",
            "publisher": "Various publishers",
            "publishDate": datetime(1008, 1, 1),
            "author": "Murasaki Shikibu",
            "genre": ["Novel", "Fiction"],
            "difficulty": "Native",
            "imgUrl": "https://www.gutenberg.org/cache/epub/1342/pg1342.cover.medium.jpg",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },

        #Spanish Books
        {
            "id": 9,
            "name": "El Principito (The Little Prince)",
            "lang": "Spanish",
            "summary": "The Little Prince by Antoine de Saint-Exupéry is a poignant and philosophical tale about a pilot stranded in the Sahara Desert who encounters a young prince from a tiny asteroid. Through the Prince's whimsical journey across various planets and encounters with eccentric adults, the story explores themes of love, responsibility, and the importance of childhood wonder. The pilot's friendship with the Prince reminds him of the beauty and fragility of human connection, leaving a lasting impact on his perspective on life.",
            "publisher": "Editorial Sudamericana",
            "publishDate": datetime(1951, 1, 1),
            "author": "Antoine de Saint-Exupéry",
            "genre": ["Fiction"],
            "difficulty": "Beginner",
            "imgUrl": "https://www.gutenberg.org/cache/epub/1342/pg1342.cover.medium.jpg",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "id": 10,
            "name": "Cien años de soledad (One Hundred Years of Solitude)",
            "lang": "Spanish",
            "summary": "One Hundred Years of Solitude, a masterpiece of magical realism, chronicles the tumultuous history of the Buendía family in the mythical Colombian town of Macondo. Through seven generations, the Buendías grapple with love, loneliness, solitude, and the cyclical nature of time. The novel is a richly imaginative and poetic exploration of themes like memory, fate, and the disintegration of the human spirit, interwoven with fantastical elements like rain that falls for four years and a character who can levitate.",
            "publisher": "Editorial Sudamericana",
            "publishDate": datetime(1967, 5, 30),
            "author": "Gabriel García Márquez",
            "genre": ["Fantasy", "Novel", "Fiction"],
            "difficulty": "Intermediate",
            "imgUrl": "https://www.gutenberg.org/cache/epub/1342/pg1342.cover.medium.jpg",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "id": 11,
            "name": "Don Quijote de la Mancha (Don Quixote)",
            "lang": "Spanish",
            "summary": "Don Quixote is a satirical masterpiece of Spanish literature that follows the misadventures of a delusional nobleman who sets out on a quixotic quest to revive the age of chivalry. Driven by the reading of too many romances, Don Quixote, accompanied by his loyal squire Sancho Panza, embarks on a series of comical and tragic encounters, mistaking windmills for giants, inns for castles, and ordinary people for knights and princesses. Cervantes masterfully satirizes the ideals of chivalry, the power of imagination, and the human condition with a blend of humor, pathos, and social commentary.",
            "publisher": "Francisco de Robles",
            "publishDate": datetime(1605, 1, 16),
            "author": "Miguel de Cervantes",
            "genre": ["Novel", "Fiction", "Satire"],
            "difficulty": "Conversational",
            "imgUrl": "https://www.gutenberg.org/cache/epub/1342/pg1342.cover.medium.jpg",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        },
        {
            "id": 12,
            "name": "Rayuela (Hopscotch)",
            "lang": "Spanish",
            "summary": "Rayuela is an experimental novel that defies traditional narrative structures, offering readers multiple ways to experience the story. The novel is divided into two parts: 'Heaven' and 'Hell.' Readers are encouraged to read 'Heaven sequentially, while 'Hell' can be read in a non-linear fashion, allowing for a unique and personalized reading experience. The story follows Horacio Oliveira, an Argentine expatriate in Paris, as he navigates love, loss, and the search for meaning in a fragmented and ever-changing world.",
            "publisher": "Editorial Sudamericana",
            "publishDate": datetime(1963, 1, 1),
            "author": " Julio Cortázar",
            "genre": ["Novel", "Fiction"],
            "difficulty": "Native",
            "imgUrl": "https://www.gutenberg.org/cache/epub/1342/pg1342.cover.medium.jpg",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
    ]
  db.session.bulk_insert_mappings(Book, books_data)
  db.session.commit()


def undo_books():
    if environment == "production":
        db.session.execute(f"TRUNCATE TABLE {SCHEMA}.books RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM books"))
    db.session.commit()
