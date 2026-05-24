from sources import FileTaskSource, GeneratorTaskSource, ApiTaskSource
from contracts import validate_source, TaskSource

def main():
    print("=== Запуск платформы обработки задач ===\n")

    file_source = FileTaskSource("tasks.json")
    gen_source = GeneratorTaskSource(count=3)
    api_source = ApiTaskSource("https://mock-api.com/tasks")


    sources_list = [file_source, gen_source, api_source]

    for source in sources_list:
        print(f"Проверяем источник: {type(source).__name__}")

        try:
            validated_source = validate_source(source)
            
            tasks = validated_source.get_tasks()
            
            print(f" Контракт соблюден. Найдено задач: {len(tasks)}")
            for task in tasks:
                print(f"     - ID: {task['id']}, Payload: {task['payload']}")
                
        except TypeError as e:
            print(f"Ошибка: {e}")

        print("-" * 30)

if __name__ == "__main__":
    main()