# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto corregido y listo para compilar.

---

```
Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:
from typing import List, Dict, Any, Optional

class Transaction:
    def __init__(self, id: str, description: str, amount: float, date: str):
        self.id = id
        self.description = description
        self.amount = amount
        self.date = date

    def __repr__(self):
        return f'Transaction(id={self.id}, description={self.description}, amount={self.amount}, date={self.date}')

class TransactionManager:
    def __init__(self):
        self.transactions: Dict[str, Transaction] = {}
        self.transactions_list: List[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        if transaction.id in self.transactions:
            raise ValueError('Transaction with this ID already exists.')
        self.transactions[transaction.id] = transaction
        self.transactions_list.append(transaction)

    def remove_transaction(self, transaction_id: str):
        if transaction_id not in self.transactions:
            raise ValueError('Transaction with this ID does not exist.')
        del self.transactions[transaction_id]
        self.transactions_list = [t for t in self.transactions_list if t.id!= transaction_id]

    def get_transaction(self, transaction_id: str) -> Optional[Transaction]:
        return self.transactions.get(transaction_id)

    def get_all_transactions(self) -> List[Transaction]:
        return self.transactions_list


# === ARCHIVO: tests/test_transaction_manager.py ===
import pytest
from src.transaction_manager import Transaction, TransactionManager

def test_add_transaction():
    manager = TransactionManager()
    transaction = Transaction('1', 'Test transaction', 100.0, '2024-07-24')
    manager.add_transaction(transaction)
    assert manager.get_transaction('1') == transaction

def test_remove_transaction():
    manager = TransactionManager()
    transaction = Transaction('1', 'Test transaction', 100.0, '2024-07-24')
    manager.add_transaction(transaction)
    manager.remove_transaction('1')
    assert manager.get_transaction('1') is None

def test_get_transaction():
    manager = TransactionManager()
    transaction = Transaction('1', 'Test transaction', 100.0, '2024-07-24')
    manager.add_transaction(transaction)
    assert manager.get_transaction('1') == transaction

def test_get_all_transactions():
    manager = TransactionManager()
    transaction1 = Transaction('1', 'Test transaction 1', 100.0, '2024-07-24')
    transaction2 = Transaction('2', 'Test transaction 2', 200.0, '2024-07-25')
    manager.add_transaction(transaction1)
    manager.add_transaction(transaction2)
    assert manager.get_all_transactions() == [transaction1, transaction2]

def test_add_duplicate_transaction():
    manager = TransactionManager()
    transaction = Transaction('1', 'Test transaction', 100.0, '2024-07-24')
    manager.add_transaction(transaction)
    with pytest.raises(ValueError):
        manager.add_transaction(transaction)

def test_remove_non_existent_transaction():
    manager = TransactionManager()
    with pytest.raises(ValueError):
        manager.remove_transaction('1')
```
