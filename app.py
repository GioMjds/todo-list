from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append({'id': len(tasks) + 1, 'task': task, 'done': False})
        return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks)

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['done'] = not task['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    tasks[:] = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)