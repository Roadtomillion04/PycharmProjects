import settings


def width_prct(percentage: int) -> float:
    return (settings.WIDTH / 100) * percentage

def height_prct(precentage: int) -> float:
    return (settings.HEIGHT / 100) * precentage
