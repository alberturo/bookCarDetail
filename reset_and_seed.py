from app import create_app
from app.models import db
from app.seeds.books import seed_books

app = create_app()
app.app_context().push()

with app.app_context():
    db.drop_all()
    db.create_all()
    seed_books()
