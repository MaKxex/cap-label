from Cheetah.Template import Template
import csv

# Ваш шаблон Cheetah
template_str = """
<!DOCTYPE html>
<html>
<head>
    <title>Закругленный текст внутри окружности</title>
    <style>
        /* Стиль для SVG-контейнера */
        body {
            margin: 0;
        }
        /* Стиль для окружностей */
        .circle {
            fill: none;
            stroke-width: 2;
        }

        /* Стиль для текста */
        text {
            font-family: Arial, sans-serif;
            font-size: 15px;
            font-weight: 700;
            text-anchor: middle; /* Выравнивание текста по центру по горизонтали */
            dominant-baseline: middle; /* Выравнивание текста по центру по вертикали */
            fill: #333; /* Черный цвет */
        }

        .circle-container {
            display: flex;
            margin: 10px;
            gap: 1mm;
            flex-wrap: wrap;
        }
    </style>
</head>
<body>
    <div class="circle-container">
        #for $num in $numbers
            <svg width="100" height="100" viewBox="0 0 50 50" preserveAspectRatio="xMidYMid meet">
                <!-- Окружность с радиусом 23мм -->
                <circle class="circle" cx="25" cy="25" r="23" stroke="#007bff" />

                <!-- Окружность с радиусом 6.8мм и отступом 10 пикселей -->
                <circle class="circle" cx="25" cy="25" r="6.8" stroke="#007bff" />
        
                <!-- Путь, по которому будет следовать текст (закругленный путь) с отступом 10 пикселей-->
                <path id="textPath"       d="M12,25 A 12,13 0 1,1 38,25" fill="none" />
                <path id="textPathBottom" d="M12,28 A 13,14 0 1,0 38,27" fill="none" />

                <!-- Текст, следующий по закругленному пути -->
                <!-- Текст сверху окружности -->
                <text>
                    <textPath xlink:href="#textPath" startOffset="50%">
                        $num
                    </textPath>
                </text>

                <!-- Текст снизу окружности -->
                <text>
                    <textPath xlink:href="#textPathBottom" startOffset="50%">
                        $num
                    </textPath>
                </text>
            </svg>
        #end for
    </div>
</body>
</html>
"""


def extract_thread_numbers(filename):
    ids_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            ids_list.append(row['id'].split(" ")[1][1:])
    return ids_list
        



# Создаем экземпляр шаблона
template = Template(template_str, searchList=[{"numbers": extract_thread_numbers("marathonVol3.csv")}])
html_output = str(template)

# Ваш список чисел

# Заполняем шаблон значениями

# Сохраняем в файл
file_path = "output.html"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_output)

print(f"HTML-код сохранен в файл {file_path}")
