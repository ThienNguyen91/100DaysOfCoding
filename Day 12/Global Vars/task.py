# Modifying Global Scope

enemies = 1


def increase_enemies(enemy):
    enemy += 1
    return enemy


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


