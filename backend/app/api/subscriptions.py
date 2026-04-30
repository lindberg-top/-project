from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from backend.app.db.deps import get_db
from backend.app.models.user import User

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])


#  утилита: продлить подписку
def extend_subscription(user: User, days: int):
    now = datetime.utcnow()

    # если подписка уже есть и активна - продлеваем
    if user.subscription_until and user.subscription_until > now:
        user.subscription_until += timedelta(days=days)
    else:
        # если нет или истекла - начинаем с текущего момента
        user.subscription_until = now + timedelta(days=days)


#  1. пробный период (7 дней)
@router.post("/trial/{telegram_id}")
def start_trial(telegram_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.subscription_until and user.subscription_until > datetime.utcnow():
        raise HTTPException(status_code=400, detail="Subscription already active")

    extend_subscription(user, 7)

    db.commit()
    db.refresh(user)

    return {
        "message": "Trial started",
        "subscription_until": user.subscription_until
    }


# 2. покупка подписки
@router.post("/buy/{telegram_id}")
def buy_subscription(telegram_id: int, months: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # переводим месяцы в дни 
    days = months * 30

    extend_subscription(user, days)

    db.commit()
    db.refresh(user)

    return {
        "message": f"Subscription extended for {months} month(s)",
        "subscription_until": user.subscription_until
    }


#  3. проверить статус подписки
@router.get("/status/{telegram_id}")
def get_subscription_status(telegram_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    now = datetime.utcnow()

    is_active = (
        user.subscription_until is not None and
        user.subscription_until > now
    )

    return {
        "is_active": is_active,
        "subscription_until": user.subscription_until
    }