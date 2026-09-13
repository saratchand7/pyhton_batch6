codegnan = {}

codegnan['course'] = ['PFS', 'JFS', 'DA']
codegnan['students_PFS'] = ['Lahar', 'Asahawi', 'Harshini', 'Vishu', 'Swapana']
codegnan['students_JFS'] = ['Raju', 'Ramu', 'Rani']
codegnan['students_DA'] = ['Balaji', 'Ganesh', 'Janakiram', 'Bhagya', 'Jaykumar']
codegnan.update({'institute_name': 'Codegnan',
    'branch': 'VSP',
    'subjects': {'python', 'mysql', 'aptitude', 'softskills'}})
codegnan.update({'students_PFS_id': ('CGVI0201', 'CGVI0202', 'CGVI0203'),
    'students_DA_id': ('CGVI0204', 'CGVI0205'),
    'students_JFS_id': ('CGVI0206', 'CGVI0207')})
codegnan.update({'daily_exam_time': '7 PM to 11 PM',
    'daily_exam': 'every evening',
    'total_marks': 30})
codegnan['PFS_students_daily_marks'] = [21, 22, 24]
codegnan['DA_students_daily_marks'] = [25, 27]
codegnan['JFS_students_daily_marks'] = [26, 28]
codegnan.update({'weekly_exam_time': '3 PM to 11 PM',
    'weekly_exam': 'every Tuesday',
    'weekly_total_marks': 60})
codegnan['PFS_students_weekly_marks'] = [45, 46, 47]
codegnan['DA_students_weekly_marks'] = [48, 49]
codegnan['JFS_students_weekly_marks'] = [50, 51]
codegnan.update({'ai_mock_interviews_time': '3 days',
    'ai_mock_interviews_day': 'every Sunday',
    'ai_mock_interviews_marks': 10})
codegnan['PFS_students_mock_interview_marks'] = [6, 7, 9]
codegnan['DA_students_mock_interview_marks'] = [6, 8]
codegnan['JFS_students_mock_interview_marks'] = [5, 7]
print(codegnan)
