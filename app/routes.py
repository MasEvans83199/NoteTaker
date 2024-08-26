from flask import request, jsonify, Blueprint, render_template, redirect, url_for
from .models import Note
from .database import db

bp = Blueprint('note', __name__)

@bp.route('/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    return render_template('notes.html', notes=notes)

@bp.route('/notes', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    note = Note(title=title, content=content)
    db.session.add(note)
    db.session.commit()
    return redirect(url_for('note.get_notes'))

@bp.route('/notes/<int:id>', methods=['GET'])
def get_note(id):
    note = Note.query.get_or_404(id)
    return jsonify({'id': note.id, 'title': note.title, 'content': note.content})

@bp.route('/notes/<int:id>/update', methods=['POST'])
def update_note(id):
    note = Note.query.get_or_404(id)
    note.title = request.form['title']
    note.content = request.form['content']
    db.session.commit()
    return redirect(url_for('note.get_notes'))