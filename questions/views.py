import os
import xlsxwriter
from django.shortcuts import render, redirect
from psych_test_demo.settings import BASE_DIR

questions = [
    'I like python',
    '',
    'I like Java'
]


def show_questions(request):
    return render(request, 'questions.html',
                  context={
                      'title': 'Questions_test',
                      'questions': questions
                  })


def generate_file(request):
    def get_answer(x):
        answer = request.POST.get('question_{}'.format(x))
        # Return value of answer if such question exists, otherwise return 0
        return int(answer) if answer else 0

    # Form is submitted via post method:
    if request.method == 'POST':

        results_dir = os.path.join(BASE_DIR, 'results')
        if not os.path.exists(results_dir):
            os.mkdir(results_dir)
        file_path = os.path.join(results_dir, '{}-results.xlsx'.format(request.POST['username']))

        answers = [get_answer(i) for i in range(len(questions))]
        results = list(zip(questions, answers))

        # Define worksheet and workbook:
        workbook = xlsxwriter.Workbook(file_path)
        worksheet = workbook.add_worksheet()
        # Define header:
        worksheet.write(0, 0, 'Question')
        worksheet.write(0, 1, 'Answer')
        # Write data to columns:
        for i in range(len(results)):
            # If answer is greater than 0 (which means it exists)
            if results[i][1] > 0:
                worksheet.write(i + 1, 0, results[i][0])
                worksheet.write_number(i + 1, 1, results[i][1])
        workbook.close()

        return render(request, 'results.html',
                      context={
                          'title': 'Quiz results',
                          'file': file_path
                      })
    # If url is accessed without post data, redirect to questions page:
    return redirect('questions')
