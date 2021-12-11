from flask import request
from flask_blog import app


@app.route('/')
def show_entries():
    return "全ての記事を表示"


@app.route('/entries', methods=['POST'])
def add_entry():
    return "新しい記事が作成されました"


@app.route('/entries/new', methods=['GET'])
def new_entry():
    return "記事の入力フォームを表示"


@app.route('/entries/<int:id>', methods=['GET'])
def show_entry(id):
    return "記事（{0}）を表示".format(id)


@app.route('/entries/<int:id>/edit', methods=['GET'])
def edit_entry(id):
    return "記事（{0}）の編集".format(id)


@app.route('/entries/<int:id>/update', methods=['POST'])
def update_entry(id):
    return "記事（{0}）を更新".format(id)


@app.route('/entries/<int:id>/delete', methods=['POST'])
def delete_entry(id):
    return "記事（{0}）を削除".format(id)
