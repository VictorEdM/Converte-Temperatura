class Temperatura(object):

    # ------------------------------------------------------------------

    TEMPERATURAS: list = [
        'Celsius',
        'Fahrenheit',
        'Kelvin'
    ]

    # ------------------------------------------------------------------

    def __init__(self) -> None:
        self.temperatura_entrada: float = 0.0
        self.temperatura_saida: float = 0.0
        
    # ------------------------------------------------------------------
    
    def celsius_para_fahrenheit(self) -> None:
        self.temperatura_saida = float(
            f"{self.temperatura_entrada * 1.8 + 32:.2f}"
        )

    # ------------------------------------------------------------------

    def celsius_para_kelvin(self) -> None:
        self.temperatura_saida = float(
            f"{self.temperatura_entrada + 273:.2f}"
        )

    # ------------------------------------------------------------------
    
    def celsius_para_celsius(self) -> None:
        self.temperatura_saida = float(
            f"{self.temperatura_entrada:.2f}"
        )
    
    # ------------------------------------------------------------------

    def fahrenheit_para_celsius(self) -> None:
        self.temperatura_saida = float(
            f"{(self.temperatura_entrada - 32) / 1.8:.2f}"
        )

    # ------------------------------------------------------------------

    def fahrenheit_para_kelvin(self) -> None:
        self.temperatura_saida = float(
            f"{(self.temperatura_entrada - 32) * (5/9) + 273:.2f}"
        )

    # ------------------------------------------------------------------
    
    def fahrenheit_para_fahrenheit(self) -> None:
        self.temperatura_saida = float(
            f"{self.temperatura_entrada:.2f}"
        )
    
    # ------------------------------------------------------------------

    def kelvin_para_celsius(self) -> None:
        self.temperatura_saida = float(
            f"{self.temperatura_entrada - 273:.2f}"
        )

    # ------------------------------------------------------------------

    def kelvin_para_fahrenheit(self) -> None:
        self.temperatura_saida = float(
            f"{(self.temperatura_entrada - 273) * 1.8 + 32:.2f}"
        )

    # ------------------------------------------------------------------
    
    def kelvin_para_kelvin(self) -> None:
        self.temperatura_saida = float(
            f"{self.temperatura_entrada:.2f}"
        )
    
    # ------------------------------------------------------------------
