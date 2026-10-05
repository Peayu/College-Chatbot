# importing libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
vectorizer = TfidfVectorizer()


corpus = [

    # ─────────────────────────────────────
    # COLLEGE TIMINGS & WORKING DAYS
    # ─────────────────────────────────────

    {
        "question": "What are the college timings?",
        "answer": "The college operates from 9:00 AM to 4:00 PM, Monday to Friday."
    },

    {
        "question": "When does college start?",
        "answer": "College starts at 9:00 AM from Monday to Friday."
    },

    {
        "question": "When does college close?",
        "answer": "The regular college day ends at 4:00 PM from Monday to Friday."
    },

    {
        "question": "What are the working days of the college?",
        "answer": "The regular working days are Monday through Friday. Saturday and Sunday are weekly holidays unless special classes or events are scheduled."
    },

    {
        "question": "Is Saturday a working day?",
        "answer": "Saturday is normally a weekly holiday. However, special classes, examinations, workshops, or events may be scheduled on Saturdays."
    },

    {
        "question": "How many hours is the college open?",
        "answer": "The college is open for approximately 7 hours each regular working day, from 9:00 AM to 4:00 PM."
    },


    # ─────────────────────────────────────
    # LIBRARY
    # ─────────────────────────────────────

    {
        "question": "What are the library timings?",
        "answer": "The library is open from 9:00 AM to 7:00 PM, Monday to Friday."
    },

    {
        "question": "When does the library close?",
        "answer": "The library closes at 7:00 PM on regular working days."
    },

    {
        "question": "Is the library open on Saturday?",
        "answer": "The library is normally closed on Saturday and Sunday."
    },


    # ─────────────────────────────────────
    # ATTENDANCE
    # ─────────────────────────────────────

    {
        "question": "What is the minimum attendance requirement?",
        "answer": "Students must maintain at least 75% attendance in their classes."
    },

    {
        "question": "How much attendance do I need?",
        "answer": "A minimum of 75% attendance is required to remain eligible for regular academic activities and examinations."
    },

    {
        "question": "What happens if my attendance is below 75 percent?",
        "answer": "Students with attendance below 75% may be required to provide an explanation and may face restrictions according to college attendance rules."
    },

    {
        "question": "Can I sit for exams with 70 percent attendance?",
        "answer": "Students with 70% attendance are below the standard 75% requirement. Examination eligibility may depend on the college's approved attendance policy and any permitted relaxation."
    },

    {
        "question": "How is attendance calculated?",
        "answer": "Attendance is calculated based on the number of classes attended divided by the total number of classes conducted, multiplied by 100."
    },

    {
        "question": "How can I check my attendance?",
        "answer": "Students can check their attendance through the student portal or by contacting the concerned department."
    },


    # ─────────────────────────────────────
    # EXAMINATIONS
    # ─────────────────────────────────────

    {
        "question": "When are the exams?",
        "answer": "Semester examination dates are announced by the examination department before the examination period."
    },

    {
        "question": "Where can I find the exam timetable?",
        "answer": "The examination timetable is published on the official student portal and through college notices."
    },

    {
        "question": "When is the exam timetable released?",
        "answer": "The exam timetable is normally released at least 2 weeks before the beginning of the examination period."
    },

    {
        "question": "What do I need to bring to the exam?",
        "answer": "Students should bring their valid student ID card and examination admit card. Only permitted stationery and materials should be carried into the examination hall."
    },


    # ─────────────────────────────────────
    # LEAVE
    # ─────────────────────────────────────

    {
        "question": "How do I apply for leave?",
        "answer": "Students can apply for leave through the official leave application process and should submit the request to the concerned department."
    },

    {
        "question": "How many days of leave can I take?",
        "answer": "Leave is subject to approval by the concerned authority. The number of approved days depends on the reason for leave and the applicable college policy."
    },

    {
        "question": "Can I take leave during exams?",
        "answer": "Leave during examinations is generally not permitted unless there is a valid reason and the examination department grants approval."
    },


    # ─────────────────────────────────────
    # FEES
    # ─────────────────────────────────────

    {
        "question": "How can I pay my college fees?",
        "answer": "College fees can be paid through the official online fee payment portal."
    },

    {
        "question": "When is the fee payment deadline?",
        "answer": "The fee payment deadline is specified in the academic schedule or fee notice. Students should complete payment before the stated deadline."
    },

    {
        "question": "What happens if I miss the fee deadline?",
        "answer": "Late payment may result in a late fee or other restrictions depending on the college fee policy."
    },


    # ─────────────────────────────────────
    # STUDENT ID
    # ─────────────────────────────────────

    {
        "question": "How can I get my student ID card?",
        "answer": "Student ID cards are issued by the college administration or student services department after enrollment."
    },

    {
        "question": "What should I do if I lose my ID card?",
        "answer": "Report the lost ID card to the administration immediately and request a replacement. A replacement fee of Rs. 100 may apply."
    },


    # ─────────────────────────────────────
    # COURSES & SUPPORT
    # ─────────────────────────────────────

    {
        "question": "Where can I find information about my courses?",
        "answer": "Course information, including subjects, credits, and schedules, is available through the student portal and the concerned academic department."
    },

    {
        "question": "How can I contact student support?",
        "answer": "Students can contact the student support office during working hours, Monday to Friday from 9:00 AM to 4:00 PM."
    }

]


# create features
questions = [item['question'] for item in corpus]
question_vectors = vectorizer.fit_transform(questions)

# cosine similarity and I/O
def search(user_question):
    user_vector = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_vector, question_vectors)
    best_match = similarities.argmax()
    score = similarities[0][best_match]

    if score >= 0.56:
        answer = corpus[best_match]["answer"]
    else:
        answer = "Sorry, Ask a relevant question."
    return answer 

