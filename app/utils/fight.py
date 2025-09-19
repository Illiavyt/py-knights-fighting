from app.knights.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> dict:
    knight1.take_damage(knight2.power - knight1.protection)
    knight2.take_damage(knight1.power - knight2.protection)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }
