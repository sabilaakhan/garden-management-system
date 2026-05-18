from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import Garden
from extensions import db
from .auth import login_required

gardens_bp = Blueprint('gardens', __name__, url_prefix='/gardens')

@gardens_bp.route('/')
@login_required
def index():
    gardens = Garden.query.filter_by(user_id=session['user_id']).all()
    return render_template('gardens/index.html', gardens=gardens)

@gardens_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']

        new_garden = Garden(
            name=name,
            location=location,
            user_id=session['user_id']
        )

        db.session.add(new_garden)
        db.session.commit()

        flash('Garden added successfully!', 'success')
        return redirect(url_for('gardens.index'))

    return render_template('gardens/add.html')


@gardens_bp.route('/<int:garden_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(garden_id):

    garden = Garden.query.filter_by(
        garden_id=garden_id,
        user_id=session['user_id']
    ).first_or_404()

    if request.method == 'POST':
        garden.name = request.form['name']
        garden.location = request.form['location']

        db.session.commit()

        flash('Garden updated successfully!', 'success')
        return redirect(url_for('gardens.index'))

    return render_template('gardens/edit.html', garden=garden)


@gardens_bp.route('/<int:garden_id>/delete', methods=['POST'])
@login_required
def delete(garden_id):

    garden = Garden.query.filter_by(
        garden_id=garden_id,
        user_id=session['user_id']
    ).first_or_404()

    db.session.delete(garden)
    db.session.commit()

    flash('Garden deleted successfully!', 'success')
    return redirect(url_for('gardens.index'))