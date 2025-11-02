# systema de biblioteca completo

biblioteca = {
    "libros": {
        "001": {"titulo": "Python Básico", "autor": "Juan Pérez", "prestado": False, "categoria": "programación"},
        "002": {"titulo": "JavaScript Avanzado", "autor": "Ana López", "prestado": True, "categoria": "programación"},
        "003": {"titulo": "Historia del Arte", "autor": "Carlos Ruiz", "prestado": False, "categoria": "arte"},
        "004": {"titulo": "Matemáticas I", "autor": "Diana Torres", "prestado": True, "categoria": "matemáticas"}
    },
    "usuarios": {
        "U001": {"nombre": "Luis", "libros_prestados": ["002"]},
        "U002": {"nombre": "Sofía", "libros_prestados": ["004"]},
        "U003": {"nombre": "Miguel", "libros_prestados": []}
    }
}

# TODO:
# 1. Muestra todos los libros disponibles para préstamo
# 2. Lista libros por categoría
# 3. Encuentra qué usuario tiene qué libro
# 4. Crea función para prestar un libro
# 5. Crea función para devolver un libro
# 6. Muestra estadísticas: libros más prestados, categorías populares
# 7. BONUS: Recomienda libros a usuarios basado en categorías que han leído