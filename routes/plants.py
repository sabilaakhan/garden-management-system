from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import Plant, Garden
from extensions import db
from .auth import login_required
from datetime import datetime

plants_bp = Blueprint('plants', __name__, url_prefix='/plants')


@plants_bp.route('/')
@login_required
def index():

    plants = Plant.query.filter_by(
        user_id=session['user_id']
    ).all()

    return render_template(
        'plants/index.html',
        plants=plants
    )


@plants_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():

    gardens = Garden.query.filter_by(
        user_id=session['user_id']
    ).all()

    if not gardens:
        flash('You need a garden to add a plant!', 'warning')
        return redirect(url_for('gardens.add'))

    if request.method == 'POST':

        name = request.form['name']
        species = request.form['species']
        garden_id = request.form['garden_id']
        planted_date_str = request.form['planted_date']
        notes = request.form['notes']

        planted_date = (
            datetime.strptime(planted_date_str, '%Y-%m-%d').date()
            if planted_date_str else None
        )

        new_plant = Plant(
            name=name,
            species=species,
            garden_id=garden_id,
            planted_date=planted_date,
            notes=notes,
            user_id=session['user_id']
        )

        db.session.add(new_plant)
        db.session.commit()

        flash('Plant added successfully!', 'success')

        return redirect(url_for('plants.index'))

    return render_template(
        'plants/add.html',
        gardens=gardens
    )


@plants_bp.route('/<int:plant_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(plant_id):

    plant = Plant.query.filter_by(
        plant_id=plant_id,
        user_id=session['user_id']
    ).first_or_404()

    gardens = Garden.query.filter_by(
        user_id=session['user_id']
    ).all()

    if request.method == 'POST':

        plant.name = request.form['name']
        plant.species = request.form['species']
        plant.garden_id = request.form['garden_id']

        planted_date_str = request.form['planted_date']

        plant.planted_date = (
            datetime.strptime(planted_date_str, '%Y-%m-%d').date()
            if planted_date_str else None
        )

        plant.notes = request.form['notes']

        db.session.commit()

        flash('Plant updated successfully!', 'success')

        return redirect(url_for('plants.index'))

    return render_template(
        'plants/edit.html',
        plant=plant,
        gardens=gardens
    )


@plants_bp.route('/<int:plant_id>/delete', methods=['POST'])
@login_required
def delete(plant_id):

    plant = Plant.query.filter_by(
        plant_id=plant_id,
        user_id=session['user_id']
    ).first_or_404()

    db.session.delete(plant)
    db.session.commit()

    flash('Plant deleted successfully!', 'success')

    return redirect(url_for('plants.index'))