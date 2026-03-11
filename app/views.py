import json
from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import JsonUploadForm
from .models import Record

DATE_FORMAT = "%Y-%m-%d_%H:%M"


def upload_json_view(request):
    if request.method == 'POST':
        form = JsonUploadForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = request.FILES['file']

            try:
                data = json.load(uploaded_file)
            except json.JSONDecodeError:
                messages.error(request, 'Файл не является корректным JSON.')
                return render(request, 'app/upload.html', {'form': form})

            if not isinstance(data, list):
                messages.error(request, 'JSON должен содержать список объектов.')
                return render(request, 'app/upload.html', {'form': form})

            records_to_create = []
            errors = []

            for index, item in enumerate(data, start=1):
                if not isinstance(item, dict):
                    errors.append(f'Элемент #{index} должен быть объектом.')
                    continue

                if 'name' not in item:
                    errors.append(f'Элемент #{index}: отсутствует ключ "name".')
                    continue

                if 'date' not in item:
                    errors.append(f'Элемент #{index}: отсутствует ключ "date".')
                    continue

                name = item.get('name')
                date_str = item.get('date')

                if not isinstance(name, str):
                    errors.append(f'Элемент #{index}: поле "name" должно быть строкой.')
                    continue

                if len(name) >= 50:
                    errors.append(f'Элемент #{index}: длина поля "name" должна быть меньше 50 символов.')
                    continue

                if not isinstance(date_str, str):
                    errors.append(f'Элемент #{index}: поле "date" должно быть строкой.')
                    continue

                try:
                    parsed_date = datetime.strptime(date_str, DATE_FORMAT)
                except ValueError:
                    errors.append(f'Элемент #{index}: поле "date" должно быть в формате YYYY-MM-DD_HH:mm.')
                    continue

                records_to_create.append(Record(name=name, date=parsed_date))

            if errors:
                for error in errors:
                    messages.error(request, error)
                return render(request, 'app/upload.html', {'form': form})

            Record.objects.bulk_create(records_to_create)
            messages.success(request, 'Данные успешно загружены.')
            return redirect('records_list')
    else:
        form = JsonUploadForm()

    return render(request, 'app/upload.html', {'form': form})


def records_list_view(request):
    records = Record.objects.all().order_by('id')
    return render(request, 'app/records_list.html', {'records': records})