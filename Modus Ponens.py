def modus_ponens(p: bool, p_implies_q: bool) -> bool:
    """
    Aplica Modus Ponens: Si (P -> Q) es verdadero y P es verdadero, entonces Q es verdadero.
    """
    if p and p_implies_q:
        return True  # Q es verdadero
    return False  # No podemos concluir que Q es verdadero

# Ejemplo de uso de Modus Ponens
p = True
p_implies_q = True  # P -> Q

print("Modus Ponens:", modus_ponens(p, p_implies_q))  # Debería retornar True