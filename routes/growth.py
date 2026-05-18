from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import Plant, GrowthLog
from extensions import db
from .auth import login_required

growth_bp = Blueprint('growth', __name__, url_prefix='/growth')


@growth_bp.route('/')
@login_required
def index():

    plants = Plant.query.filter_by(user_id=session['user_id']).all()

    plant_ids = [p.plant_id for p in plants]

    if plant_ids:
        logs = GrowthLog.query.filter(
            GrowthLog.plant_id.in_(plant_ids)
        ).order_by(
            GrowthLog.recorded_at.desc()
        ).all()
    else:
        logs = []

    return render_template('growth/index.html', logs=logs)


@growth_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():

    plants = Plant.query.filter_by(user_id=session['user_id']).all()

    if not plants:
        flash('You need a plant to add a growth log!', 'warning')
        return redirect(url_for('plants.add'))

    if request.method == 'POST':

        plant_id = request.form['plant_id']
        height = request.form['height']
        leaf_count = request.form['leaf_count']
        notes = request.form['notes']

        height = float(height) if height else None
        leaf_count = int(leaf_count) if leaf_count else None

        new_log = GrowthLog(
            plant_id=plant_id,
            height=height,
            leaf_count=leaf_count,
            notes=notes
        )

        db.session.add(new_log)
        db.session.commit()

        flash('Growth log added successfully!', 'success')

        return redirect(url_for('growth.index'))

    return render_template('growth/add.html', plants=plants)


@growth_bp.route('/<int:log_id>/delete', methods=['POST'])
@login_required
def delete(log_id):

    plants = Plant.query.filter_by(user_id=session['user_id']).all()

    plant_ids = [p.plant_id for p in plants]

    if plant_ids:

        log = GrowthLog.query.filter_by(
            log_id=log_id
        ).filter(
            GrowthLog.plant_id.in_(plant_ids)
        ).first_or_404()

        db.session.delete(log)
        db.session.commit()

        flash('Log deleted successfully!', 'success')

    return redirect(url_for('growth.index'))