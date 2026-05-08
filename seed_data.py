import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from datetime import date
from app.models import Driver, Car, Fine  # app — o'zingizning app nomingiz


def run():
    print("🗑️  Eski ma'lumotlar o'chirilmoqda...")
    Fine.objects.all().delete()
    Car.objects.all().delete()
    Driver.objects.all().delete()

    print("👤 Driverlar yaratilmoqda...")

    # ──────────────────────────────
    # Driver 1 — 2 ta mashina, jarimalari bor
    # ──────────────────────────────
    ali = Driver.objects.create(first_name="Ali", last_name="Valiyev")

    nexia = Car.objects.create(
        driver=ali,
        brand="Nexia",
        license_plate="01A111AA"
    )
    Fine.objects.create(car=nexia, amount=150000.00, date=date(2024, 5, 1))
    Fine.objects.create(car=nexia, amount=80000.00,  date=date(2024, 6, 15))

    cobalt = Car.objects.create(
        driver=ali,
        brand="Cobalt",
        license_plate="01B222BB"
    )
    Fine.objects.create(car=cobalt, amount=50000.00, date=date(2024, 7, 20))

    # ──────────────────────────────
    # Driver 2 — 1 ta mashina, jarimasi yo'q
    # ──────────────────────────────
    vali = Driver.objects.create(first_name="Vali", last_name="Karimov")

    Car.objects.create(
        driver=vali,
        brand="Spark",
        license_plate="10C333CC"
    )

    # ──────────────────────────────
    # Driver 3 — mashinasi yo'q
    # ──────────────────────────────
    Driver.objects.create(first_name="Sardor", last_name="Toshmatov")

    # ──────────────────────────────
    # Driver 4 — 3 ta mashina, ko'p jarima
    # ──────────────────────────────
    jasur = Driver.objects.create(first_name="Jasur", last_name="Rahimov")

    malibu = Car.objects.create(
        driver=jasur,
        brand="Malibu",
        license_plate="30D444DD"
    )
    Fine.objects.create(car=malibu, amount=200000.00, date=date(2024, 3, 10))
    Fine.objects.create(car=malibu, amount=120000.00, date=date(2024, 4, 22))
    Fine.objects.create(car=malibu, amount=95000.00,  date=date(2024, 8, 5))

    damas = Car.objects.create(
        driver=jasur,
        brand="Damas",
        license_plate="30E555EE"
    )
    Fine.objects.create(car=damas, amount=30000.00, date=date(2024, 9, 1))

    Car.objects.create(
        driver=jasur,
        brand="Tracker",
        license_plate="30F666FF"
    )  # jarimasi yo'q

    # ──────────────────────────────
    print("\n✅ Ma'lumotlar muvaffaqiyatli yaratildi!")
    print(f"   👤 Driverlar  : {Driver.objects.count()} ta")
    print(f"   🚗 Mashinalar : {Car.objects.count()} ta")
    print(f"   💸 Jarimalar  : {Fine.objects.count()} ta")


if __name__ == '__main__':
    run()