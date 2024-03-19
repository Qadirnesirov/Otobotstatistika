from os import getenv

API_ID = int(getenv("API_ID", "24066716"))
API_HASH = getenv("API_HASH", "09e30e6e0b1a4c71e43a055979c51b3b")
BOT_TOKEN = getenv("BOT_TOKEN", "7167357324:AAHrkLsFMJ_SV2jDVc5PXWjhOmYD0EfhukU")
OWNER_ID = int(getenv("OWNER_ID", "6184936428"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://nesirovq1997:qadir1997@cluster0.pavador.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
STRING_SESSION = getenv("STRING_SESSION", "AgFvOpwAkqm-9SrYb3Ph_1cDHEm0cCrqU8bU0F8F7yWOr2PI1lulMc_gnE3201tt9t0p-O-1ZsW_AR10dRm7cOklymIGzpv8nnsDZlbjgln6kkrKfRycD-ywZv4CdmybczEImGvO_UXxrtWFQRfFtfQ7Z-JLrUHaksaO4o2fPV9HcuKQE1gQwN7MHgTqSGcZY4rd0NQWu_H9gfU4O81K-xzSzmQGjgQFsVYJpGOci1SHURofEQFnd72iVYOdjY9ZWJhP-HmvJTIslTDzWpkZ5-235Y65z3FUQ5SsL7gyUx84xc3XkH6W6EvMDDU7pSITyKWMG6UUSO_Q2sjURlxKZhJUZGkZOQAAAAFZvEdgAA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6184936428").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/6159b9a38d5da8c92260d.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/Qadirnesirov/Otobotstatistika.git")
BRANCH = getenv("BRANCH", "main")
