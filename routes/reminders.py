from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import Plant, Reminder
from extensions import db
from .auth import login_required
from datetime import datetime

reminders_bp = Blueprint('reminders', __name__, url_prefix='/reminders')


@reminders_bp.route('/')
@login_required
def index():

    plants = Plant.query.filter_by(
        user_id=session['user_id']
    ).all()

    plant_ids = [p.plant_id for p in plants]

    if plant_ids:
        reminders = Reminder.query.filter(
            Reminder.plant_id.in_(plant_ids)
        ).order_by(
            Reminder.due_date
        ).all()
    else:
        reminders = []

    today = datetime.utcnow().date()

    return render_template(
        'reminders/index.html',
        reminders=reminders,
        today=today
    )


@reminders_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():

    plants = Plant.query.filter_by(
        user_id=session['user_id']
    ).all()

    if not plants:
        flash('You need a plant to add a reminder!', 'warning')
        return redirect(url_for('plants.add'))

    if request.method == 'POST':

        plant_id = request.form['plant_id']
        reminder_type = request.form['reminder_type']
        due_date_str = request.form['due_date']

        due_date = datetime.strptime(
            due_date_str,
            '%Y-%m-%d'
        ).date()

        new_reminder = Reminder(
            plant_id=plant_id,
            reminder_type=reminder_type,
            due_date=due_date
        )

        db.session.add(new_reminder)
        db.session.commit()

        flash('Reminder added successfully!', 'success')

        return redirect(url_for('reminders.index'))

    return render_template(
        'reminders/add.html',
        plants=plants
    )


@reminders_bp.route('/<int:reminder_id>/done', methods=['POST'])
@login_required
def mark_done(reminder_id):

    plants = Plant.query.filter_by(
        user_id=session['user_id']
    ).all()

    plant_ids = [p.plant_id for p in plants]

    if plant_ids:

        reminder = Reminder.query.filter_by(
            reminder_id=reminder_id
        ).filter(
            Reminder.plant_id.in_(plant_ids)
        ).first_or_404()

        reminder.status = 'done'

        db.session.commit()

        flash('Reminder marked as done!', 'success')

    return redirect(
        request.referrer or url_for('reminders.index')
    )


@reminders_bp.route('/<int:reminder_id>/delete', methods=['POST'])
@login_required
def delete(reminder_id):

    plants = Plant.query.filter_by(
        user_id=session['user_id']
    ).all()

    plant_ids = [p.plant_id for p in plants]

    if plant_ids:

        reminder = Reminder.query.filter_by(
            reminder_id=reminder_id
        ).filter(
            Reminder.plant_id.in_(plant_ids)
        ).first_or_404()

        db.session.delete(reminder)

        db.session.commit()

        flash('Reminder deleted successfully!', 'success')

    return redirect(url_for('reminders.index'))