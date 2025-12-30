from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import sys

def run_quiz():
    question_bank = []

    # OWASP: Manejo seguro de errores
    try:
        for question in question_data:
            # Validación de claves para evitar KeyError si los datos están mal formados
            if "text" not in question or "answer" not in question:
                print(f"Error: Datos de pregunta mal formados. Saltando...")
                continue
                
            new_question = Question(question["text"], question["answer"])
            question_bank.append(new_question)
            
    except Exception as e:
        print(f"Error crítico al cargar el banco de preguntas: {e}")
        sys.exit(1)

    # Iniciar el motor del juego
    if not question_bank:
        print("Error: No hay preguntas cargadas.")
        return

    game = QuizBrain(question_bank)

    while game.still_has_questions():
        game.next_question()

    print("\n" + "="*20)
    print("¡Has completado el quiz!")
    print(f"Tu puntuación final fue: {game.score}/{game.question_number}")
    print("="*20)

if __name__ == "__main__":
    run_quiz()