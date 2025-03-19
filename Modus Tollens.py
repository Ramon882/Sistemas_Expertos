def modus_tollens(q: bool, p_implies_q: bool) -> bool:
    """
    Aplica Modus Tollens: Si (P -> Q) es verdadero y Q es falso, entonces P es falso.
    """
    if not q and p_implies_q:
        return False  # P es falso
    return True  # No podemos concluir que P es falso

# Ejemplo de uso de Modus Tollens
q = False
p_implies_q = True  # P -> Q

print("Modus Tollens:", modus_tollens(q, p_implies_q))  # Debería retornar False