from flask import Blueprint, render_template, session
from models import Garden, Plant, GrowthLog, Reminder
from .auth import login_required
from datetime import datetime, timedelta

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
@login_required
def index():
    user_id = session['user_id']
    
    gardens_count = Garden.query.filter_by(user_id=user_id).count()
    plants_count = Plant.query.filter_by(user_id=user_id).count()
    
    # Overdue and Pending Reminders
    today = datetime.utcnow().date()
    plants = Plant.query.filter_by(user_id=user_id).all()
   
    plant_ids = [p.plant_id for p in plants]
    
    overdue_reminders = \
        Reminder.query.filter(Reminder.plant_id.in_(plant_ids), Reminder.status == 'pending', Reminder.due_date < today).count() \
        if plant_ids else 0
        
    pending_reminders = \
        Reminder.query.filter(Reminder.plant_id.in_(plant_ids), Reminder.status == 'pending').order_by(Reminder.due_date).limit(5).all() \
        if plant_ids else []
    
    # Activities this week (Growth logs)
    week_ago = datetime.utcnow() - timedelta(days=7)
    recent_logs_count = \
        GrowthLog.query.filter(GrowthLog.plant_id.in_(plant_ids), GrowthLog.recorded_at >= week_ago).count() \
        if plant_ids else 0
    
    return render_template('dashboard/index.html',
                           gardens_count=gardens_count,
                           plants_count=plants_count,
                           overdue_reminders=overdue_reminders,
                           pending_reminders=pending_reminders,
                           recent_logs_count=recent_logs_count)
