import os
import json
import xlsxwriter
from django.shortcuts import render, redirect
from django.conf import settings

results_dir = os.path.join(settings.MEDIA_ROOT, 'results')
# Create media directory if it doesn't exist
if not os.path.exists(settings.MEDIA_ROOT):
    os.mkdir(settings.MEDIA_ROOT)
# Create reulsts directory within media directory if it doesn't exist
if not os.path.exists(results_dir):
    os.mkdir(results_dir)

with open(os.path.join(settings.BASE_DIR, 'questions.json'), 'r', encoding='utf-8') as question_data:
    questions = json.load(question_data)


def show_questions(request):
    return render(request, 'questions.html',
                  context={
                      'title': 'Questions_test',
                      'questions': questions
                  })


def generate_file(request):
    # Form is submitted via post method:
    if request.method == 'POST':
        file_path = os.path.join(results_dir, '{}-results.xlsx'.format(request.POST['username']))

        answers = []
        for foo in range(len(questions)):
            answers.append([
                int(request.POST.get('q_{}_{}'.format(foo, bar)))
                for bar in range(len(questions[foo].get('quiz_questions')))
            ])

        # Define worksheet and workbook:
        workbook = xlsxwriter.Workbook(file_path)
        worksheet = workbook.add_worksheet()
        col = 0
        for i in range(len(questions)):
            worksheet.write(0, col + i, 'Question')
            worksheet.write(0, col + i + 1, 'Answer')
            for j in range(len(answers[i])):
                worksheet.write(j + 1, col + i, questions[i].get('quiz_questions')[j])
                worksheet.write_number(j + 1, col + i + 1, answers[i][j])
            col += 1

        workbook.close()

        return render(request, 'results.html',
                      context={
                          'title': 'Quiz results',
                          'file': file_path
                      })
    # If url is accessed without post data, redirect to questions page:
    return redirect('questions')


def show_files(request):
    return render(request, 'files.html', context={'files': os.listdir(results_dir)})
