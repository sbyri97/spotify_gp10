from flask import Blueprint
from app.models import Library


searchSong_routes = Blueprint('search', __name__)


@searchSong_routes.route('/songs/<nameOfSong>')
def searchSong(nameOfSong):
    songs = Library.query.filter(Library.song_title.ilike(f'%{nameOfSong}%'))
    dict_songs = [song.to_dict() for song in songs]
    print("This is name of Song:::", dict_songs)
    return {"songs": dict_songs}
